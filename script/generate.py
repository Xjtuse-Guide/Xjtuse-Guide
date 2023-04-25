import os
import os.path as osp

dct = {
    "大一上": [
        "高等数学上",
        "线性代数",
        "大学计算机基础",
        "国防教育",
        "思修",
    ],
    "大一下": [
        "高等数学下",
        "大学物理上",
        "程序设计基础",
        "工程制图",
        "大学化学",
        "生命科学基础",
        "中国近现代史纲要"
    ],
    "大二上": [
        "面向对象程序设计方法",
        "电路与电子学",
        "数据结构与算法",
        "离散数学基础",
        "毛概&习中特",
        "大学物理下",
        "软件工程导论"
    ],
    "大二下": [
        "数字逻辑设计专题实验",
        "数学建模",
        "概率论与数理统计",
        "图论与代数系统",
        "马原",
        "数据库系统",
    ],
    "大三上": [
        "计算机组成与结构",
        "操作系统",
        "软件质量保证",
        "软件项目管理",
        "软件系统分析与设计",
        "计算机图形学-选修",
        "算法分析与设计-选修",
        "软件体系结构基础-选修",
    ],
    "大三下": [
        "计算机网络",
        "编译原理",
        "软件工程经济学",
        "专业实习",
        "网络信息安全-选修",
        "机器学习导论-选修",
        "大数据技术-选修",
        "自然语言处理技术-选修",
        "图像处理与机器视觉-选修"
    ],
    "大四上": [
        "表达与交流"
    ],
    "实训&实验": [
        "第一次实训",
        "第二次实训",
        "专业实习-大三下",
        "数据结构与算法设计综合训练",
        "数字逻辑设计专题实验",
        "计算机组成与结构专题实验",
        "数据库系统设计综合训练",
        "机器学习技术综合训练",
        "编译系统设计综合训练",
        "计算机网络专题实验",
        "软件项目管理综合训练",
        "面向对象程序设计综合训练",
        "计算机图形学课程综合训练",
        "软件系统分析与设计综合训练",
        "Linux操作系统应用开发训练",
        "Python程序设计综合训练"
    ]
}

base_path = osp.join(".", "docs", "课内笔记")
for semester, courses in dct.items():
    for course in courses:
        print(semester, course)
        path = osp.join(base_path, semester, course)
        # 生成课程目录
        if not osp.exists(path):
            os.makedirs(path)
        else:
            continue

        # 生成笔记目录
        os.mkdir(osp.join(path, "笔记"))

        # 生成README
        with open(osp.join(path, "README.md"), 'w', encoding='UTF-8') as f:
            f.write("# " + course)

        dir_path = f"docs/课内笔记/{semester}/{course}"
        readme_path = f"{dir_path}/README.md"

        # 生成_siderbar, .nojekyll, 考试经验帖
        open(osp.join(path, ".nojekyll"), 'w').close()
        with open(osp.join(path, "考试经验帖.md"), 'w', encoding='UTF-8') as f:
            f.write(f"# {course}考试经验帖")
        with open(osp.join(path, "_sidebar.md"), 'w', encoding='utf-8') as f:
            f.write(f"- [课程介绍]({readme_path})\n")
            f.write(f"- [考试经验帖]({dir_path}/考试经验帖.md)\n")
            f.write(f"- 笔记")

        # 更新目录
        with open(osp.join(base_path, semester, 'README.md'), 'a', encoding='utf-8') as f:
            f.write(f"- [{course}]({readme_path})\n")
