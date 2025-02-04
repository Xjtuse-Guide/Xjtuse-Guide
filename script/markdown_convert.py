# 读取 markdown 文件的全部图片，然后检查这些图片是否在泉佬图床中存在
# 如果存在直接链接到对应图床，如果不存在则上传到 telegraph 图床
# 最后，生成修改后的 markdown 文件
# 此脚本适用于在泉佬的笔记上二次修改，而且喜欢将笔记引用的图片下载到本地的同学
# 使用此脚本后，笔记中的所有本地图片如果在泉佬图床中存在同名内容，将改为引用已存在的图床内容
# 如果不存在，则直接上传这些图片到 telegraph 图床中，并改为引用新图床的内容。

import re
import requests
import os
import sys


COMMON_PREFIX = "https://raw.githubusercontent.com/yijunquan-afk/img-bed-1/main/"
all_prefix =["img/", "img1/", "", "images/", "img12/", "img13/", "img14/", "img2/", "img3/",
              "img4/", "img5/", "img6/", "imge/", "imge3/", "imges3/", "imgethe/"]
use_frequency = {prefix: 0 for prefix in all_prefix}

# 用于屏蔽输出
devnull = open(os.devnull, "w")
dst = sys.stdout

# 访问 GitHub 显然需要一些魔法助力
proxies = {}
if os.getenv("http_proxy"):
    proxies["http"] = os.environ.get("http_proxy")
elif os.getenv("https_proxy"):
    proxies["https"] = os.environ.get("https_proxy")
else:
    proxies = None


def try_ignore_ssl_exception(func):
    """
    不断尝试调用函数 func 直到不发生异常并成功，忽略其中发生的任何 SSLError 和 ConnectionAbortError, 但在出现其他错误时传递错误。
    这是因为墙非常喜欢隔三差五中断一下 GitHub 连接，导致时不时出现异常然后让整个程序挂掉
    """
    while True:
        try:
            return func()
        except requests.exceptions.SSLError:
            print("已忽略 SSL 连接被刻意阻断而引发的错误。", file=dst)
        except requests.exceptions.ConnectionError as e:
            if "Connection aborted" in str(e):
                print("已忽略连接被刻意中断而引发的错误。", file=dst)
            else:
                raise e


def upload_image(url):
    """
    上传图片到 telegraph 图床
    :params url: 本地图片的地址，不能为网络图片地址。
    """
    print("正在上传图片到图床...", file=dst)
    f = open(url, "rb")
    # post 直接上传
    # 如果你有其他的 telegraph 图床，可以对应替换下一行的链接和 new_url = "https://telegraph-image-5ms.pages.dev" + response.json()[0]["src"] 这行的链接
    response = requests.post("https://telegraph-image-5ms.pages.dev/upload", headers={
        "Accept": "application/json, text/plain, */*"
    }, files={"file": f})
    f.close()
    if not response.ok:
        print("Failed to upload image.", file=dst)
        return url

    # 读取返回的图床 url
    new_url = "https://telegraph-image-5ms.pages.dev" + response.json()[0]["src"]
    print(f"上传图片成功，新链接为 {new_url}", file=dst)

    return new_url


def modify_image_links_in_markdown(file_path, img_bed_prefix, ignore_prefix=None, check_exist=False):
    """
    读取 markdown 文件，解析所有图片类内容，上传本地图片到图床中。
    如果 check_exist 为 True，尝试替换其中的本地图片为泉佬图床的同名图片；如果图片不存在于泉佬的图床中，再上传到 telegraph 图床，可以减少图床占用。
    如果 check_exist 为 True 且 ignore_prefix 不为 None 、图片的开头位于 ignore_prefix 列表中，跳过重复检查并直接上传这些图片。这可以减少访问 GitHub 的次数，加快运行速度。
    :params file_path: 要处理的 markdown 文件的路径
    :params check_exist: 为 True 时检查本地图片是否在泉佬图床中存在，如果存在则不上传
    :params img_bed_prefix: 默认为 COMMON_PREFIX, 指向泉佬图床的主路径
    :params ignore_prefix: 一个列表，如果图片的开头位于这个列表中，直接上传到 telegraph 图床，跳过检查，仅在 check_exist 为 True 时有效
    """
    with open(file_path, "r", encoding="utf-8") as file:
        markdown_text = file.read()
    
    # 匹配 Markdown 图片语法
    pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
    html_pattern = r'<img\s+[^>]*src="([^"]+\.(?:jpg|jpeg|png|gif))"[^>]*alt="([^"]+)"[^>]*>'
    # 图片别名在前还是链接在前
    # 这点在 markdown 语法和 html 语法中不同。
    alt_first = True
    
    def replace_link(match):
        if alt_first:
            alt_text = match.group(1)
            url = match.group(2)
        else:
            url = match.group(1)
            alt_text = match.group(2)

        # 如果图片是本地图片，对其进行检查
        if not url.startswith("http"):
            if not os.path.exists(url):
                # 如果文件不存在，可能是因为它以相对路径存储，而我们不在 markdown 文件目录下。
                # 我们可以更改文件路径为完整的，即在前方添加 markdown 文件的目录，用于处理那些以相对路径存在的文件
                url = os.path.join(os.path.dirname(file_path), url)
            # 检查图片是否存在
            print(f"找到了本地图片路径: {url}, 此文件{'存在' if os.path.exists(url) else '不存在'}", file=dst)
            if not os.path.exists(url):
                print(f"警告: 未能在磁盘上找到图片 {url}, 因此跳过上传, markdown 中的路径将会保持不变...", file=dst)
                return f'![{alt_text}]({url})'
            
            if check_exist:
                if ignore_prefix is not None:
                    # 如果在 ignore_prefix 目录下，直接上传
                    for prefix in ignore_prefix:
                        if url.split("/")[-1].startswith(prefix):
                            new_url = upload_image(url)
                            return f'![{alt_text}]({new_url})'
                # 按照频率从高到低检查图床
                all_prefix.sort(key=lambda x: use_frequency[x], reverse=True)
                # 搜索图片是否在已有的图床下
                for prefix in all_prefix:
                    # 拼接图床 url
                    new_url = f"{img_bed_prefix}{prefix}{url.split('/')[-1]}"
                    if proxies is not None:
                        response = try_ignore_ssl_exception(lambda: requests.head(new_url, proxies=proxies))
                    else:
                        response = try_ignore_ssl_exception(lambda: requests.head(new_url))
                    # 如果存在，不需要上传
                    if response.ok:
                        print(f"找到本地图片路径对应的网络图片为 {new_url}，此图片存在，因此不会被上传。", file=dst)
                        # 更新使用频率
                        use_frequency[prefix] += 1
                        break
                else:
                    # 如果文件不存在于网络图床，则上传文件。
                    new_url = upload_image(url)
            else:
                # 不检查图床重复时，直接上传图片
                new_url = upload_image(url)
        else:
            # 如果图片本身就是链接，检查其是否可以访问
            if proxies is not None:
                response = try_ignore_ssl_exception(lambda: requests.head(url, proxies=proxies))
            else:
                response = try_ignore_ssl_exception(lambda: requests.head(url))
            if response.ok:
                print(f"找到引用的网络图片，网址为: {url}，此文件存在，因此不会被上传。", file=dst)
            else:
                print(f"警告：引用的图片 {url} 是一个网址，但无法访问，因此跳过上传, markdown 中的路径将会保持不变...", file=dst)
            new_url = url
        
        # 重新拼装图片语法
        return f'![{alt_text}]({new_url})'
    
    # 替换所有匹配项
    alt_first = True
    new_markdown_text = re.sub(pattern, replace_link, markdown_text)
    # html 的图片语法和 markdown 的图片语法不同，图片路径在前而非别名在前
    alt_first = False
    new_markdown_text = re.sub(html_pattern, replace_link, new_markdown_text)
    
    # 写回 Markdown 文件
    with open(file_path.strip(".md") + "_backup.md", "w", encoding="utf-8") as file:
        file.write(markdown_text)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(new_markdown_text)
    print("图片链接更新完成", file=dst)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="检查 markdown 文件中的图片，将本地图片上传到图床中。")
    parser.add_argument("file", help="待转换的 markdown 文件路径")
    parser.add_argument("--skip-prefix", nargs="+", help="认为以特定前缀开头的图片一定不在图床中，可用于减少搜索时间。")
    parser.add_argument("--silent", action="store_true", help="屏蔽输出")
    parser.add_argument("--check-exist", action="store_true", help="检查图片是否在泉佬的图床中存在，如果存在则更改链接为已有图床地址，而不再次上传", default=False)
    args = parser.parse_args()

    if args.silent:
        dst = devnull

    modify_image_links_in_markdown(args.file, COMMON_PREFIX, args.skip_prefix, args.check_exist)
