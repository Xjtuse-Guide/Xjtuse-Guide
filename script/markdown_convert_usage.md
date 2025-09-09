# 图床上传工具用法

在使用前，需要在电脑上下载 Python 3（任何版本都可以），然后使用 pip 安装 requests 库：
```shell
pip install requests
```

## 功能

使用 md 格式的同学应该都知道，markdown 文件中是不能嵌入图片的，只能插入指向图片的链接，然后把图片存储在本地的某个位置或者网站上。但上传到 guide 时，md 文件中的图片必须都上传到网络上，否则无法正常显示。这种存储 md 文件中图片的网站就是图床。

为了快速上传本地图片到图床，编写了这个 [脚本](https://github.com/Xjtuse-Guide/Xjtuse-Guide/blob/main/script/markdown_convert.py)。

此脚本的主要功能是：搜索 markdown 文件中的所有图片，将其中的本地图片上传到图床，然后更改文件中的图片链接，使其指向图床。

> 请不要在图床中存放与 xjtuse-guide 不相关的图片

如果你的 markdown 笔记是在易俊泉学长的笔记基础上改进来的，但笔记中的图片被你下载到了本地，那么此脚本还有高级功能：尝试匹配本地图片和易学长图床中的图片，如果成功找到，就不需要上传本地图片到图床中了，直接更改本地图片的链接就可以。

## 输入参数

此脚本需要在命令行（Windows 下的 cmd，powershell，macOS 下的终端）中使用，并且添加部分参数。可以使用的参数如下：

`--check-exist`：添加此参数后，可以解锁高级功能：检查图片是否在易学长的图床中存在，如果存在则更改链接为已有图床地址，而不再次上传。

`--skip-prefix`：认为以特定前缀开头的图片一定不在图床中，直接上传这些图片，可用于减少搜索时间。此参数仅在填写了 `--check-exist` 时有效。

`--silent`：不输出任何信息。

`--website-blacklist`：输入此参数后，对于位于名单中的网站，强制上传这些网站中的图片到图床中。适用于笔记中包含 csdn 等不允许外链访问的网站上的图片的情况。默认情况下，将强制上传 `img-blog.csdnimg.cn` 域名下的图片。

此外，还需要输入待转换的 markdown 文件的位置。

输出文件和输入文件在同一目录下，名称为输入文件的名称再加上“_changed"后缀。

### 设置代理

如果你无法连接到 GitHub，可以在终端设置代理。Windows 的 cmd 下，输入：

```cmd
set http_proxy=http://127.0.0.1:7890
set https_proxy=http://127.0.0.1:7890
```

Powershell 下，输入：

```powershell
$env:HTTP_PROXY="http://127.0.0.1:7890"
$env:HTTPS_PROXY="https://127.0.0.1:7890"
```

macOS 和 Linux 发行版的终端下，输入：

```bash
export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890
```

请将上方命令中的端口换成你所使用软件的实际端口。

脚本会自动读取命令行中的环境变量，并使用代理。

## 使用示范

> 以下内容只是例子，你需要更改命令中的文件名为实际的路径

```shell
python3 markdown_convert.py ~/desktop/README.md
```

上传 `桌面/README.md` 中的所有图片到图床中，生成修改后的文件 `桌面/README_changed.md`

```shell
python3 markdown_convert.py ~/desktop/README.md --silent
```

上传 `桌面/README.md` 中的所有图片到图床中，生成修改后的文件 `桌面/README_changed.md`，且在处理过程中不要输出任何信息。

```shell
python3 markdown_convert.py ~/desktop/README.md --check-exist
```

上传 `桌面/README.md` 中不存在于易学长图床的图片到图床中，对于已存在的图片，直接更改链接为已有图床的链接。生成修改后的文件 `桌面/README_changed.md`。

判断本地图片是否和易学长图床中的图片相同的依据是图片的文件名。

```shell
python3 markdown_convert.py ~/desktop/README.md --check-exist --skip-prefix 'image-2024'
```

上传 `桌面/README.md` 中不存在于易学长图床的图片到图床中，但一定会上传所有以 'image-2024' 开头的图片。对于已存在的图片，直接更改链接为已有图床的链接。生成修改后的文件 `桌面/README_changed.md`。

```shell
python3 markdown_convert.py ~/desktop/README.md --check-exist --skip-prefix 'image-2024' 'IMG'
```

上传 `桌面/README.md` 中不存在于易学长图床的图片到图床中，但一定会上传所有以 'image-2024' 或者 'IMG' 开头的图片。对于已存在的图片，直接更改链接为已有图床的链接。生成修改后的文件 `桌面/README_changed.md`。

