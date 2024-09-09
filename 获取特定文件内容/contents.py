# This project is created by aFei-CQUT
# ------------------------------------------------------------------------------------------------------------------------------------
#   About aFei-CQUT
# - Interests&Hobbies: Programing,  ChatGPT,  Reading serious books,  Studying academical papers.
# - CurrentlyLearning: Mathmodeling，Python and Mathmatica (preparing for National College Mathematical Contest in Modeling).
# - Email:2039787966@qq.com
# - Pronouns: Chemical Engineering, Computer Science, Enterprising, Diligent, Hard-working, Sophomore,Chongqing Institute of Technology,
# - Looking forward to collaborating on experimental data processing of chemical engineering principle
# ------------------------------------------------------------------------------------------------------------------------------------
from pathlib import Path
import os

IGNORE_EXTENSIONS = [
    '.pyc',
    '.md',
    '.png',
    '.idx',
    '.pack',
    '.rev',
    '.sample',
    'jpg',
    '.xmind'
]

IGNORE_FILES = [
    '.gitattributes',
    '.ignore',
    'LICENSE'
]

def generate_directory_structure(startpath, indent=''):
    """
    递归生成从 `startpath` 开始的目录结构，并返回目录结构字符串。

    参数：
        startpath (str): 要开始生成的根目录路径。
        indent (str): 当前的缩进级别，用于嵌套目录和文件。
    
    返回：
        str: 目录结构的字符串表示。
    """
    structure = ""
    path = Path(startpath)
    if not any(path.iterdir()):
        structure += f"{indent}|-- (空目录)\n"
    else:
        for item in path.iterdir():
            if item.is_dir():
                structure += f"{indent}|-- 文件夹: {item.name}\n"
                structure += generate_directory_structure(item, indent + '|   ')
            else:
                structure += f"{indent}|-- 文件: {item.name}\n"
    return structure

def write_directory_contents_to_file(input_dir, output_file_name):
    """
    将指定目录中的文件内容和目录结构写入输出文件。

    参数：
        input_dir (str): 输入目录的路径。
        output_file_name (str): 输出文件的名称。
    """
    # 构建输出文件路径
    output_dir = os.path.dirname(__file__)
    os.makedirs(output_dir, exist_ok=True)
    output_file_path = os.path.join(output_dir, output_file_name)

    # 以写模式打开输出文件
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        # 在文件开头写入目录结构
        directory_structure = generate_directory_structure(input_dir)
        output_file.write("目录结构：\n")
        output_file.write(directory_structure)
        output_file.write("\n\n")  # 在文件内容之前添加间隔

        # 遍历输入目录
        for root, dirs, files in os.walk(input_dir):
            # 修改 dirs 列表以跳过 .git 目录
            dirs[:] = [d for d in dirs if d != '.git']
            # 忽略特定的文件和扩展名
            files = [f for f in files if not (
                any(f.endswith(ext) for ext in IGNORE_EXTENSIONS) or
                f in IGNORE_FILES
            )]
            for file in files:
                file_path = os.path.join(root, file)
                # 尝试以不同的编码读取每个文件的内容
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                except (UnicodeDecodeError, IsADirectoryError):
                    try:
                        with open(file_path, 'r', encoding='latin1') as f:
                            content = f.read()
                    except (UnicodeDecodeError, IsADirectoryError):
                        # 跳过无法解码的文件
                        continue
                
                # 在每个文件内容前写入明显的标记
                marker = "=" * 80  # 示例标记
                output_file.write(f"{marker}\n")
                output_file.write(f"{file_path} 的内容:\n")
                output_file.write(f"{marker}\n")
                output_file.write(content)
                output_file.write("\n\n")  # 在文件之间添加一些间隔

if __name__ == "__main__":
    input_directory = r'D:\EdgeDownloads\MathematicalModelingEssayTemplate-master'
    output_file_name = f"{os.path.basename(input_directory)}.txt"
    write_directory_contents_to_file(input_directory, output_file_name)
