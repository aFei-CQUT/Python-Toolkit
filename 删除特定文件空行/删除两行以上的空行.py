# This project is created by aFei-CQUT
# ------------------------------------------------------------------------------------------------------------------------------------
#   About aFei-CQUT
# - Interests&Hobbies: Programing,  ChatGPT,  Reading serious books,  Studying academical papers.
# - CurrentlyLearning: Mathmodeling，Python and Mathmatica (preparing for National College Mathematical Contest in Modeling).
# - Email:2039787966@qq.com
# - Pronouns: Chemical Engineering, Computer Science, Enterprising, Diligent, Hard-working, Sophomore,Chongqing Institute of Technology,
# - Looking forward to collaborating on experimental data processing of chemical engineering principle
# ------------------------------------------------------------------------------------------------------------------------------------
import os

def remove_extra_blank_lines(file_path):
    """
    删除文件中的多余空行，只保留两个空行的情况。

    参数：
        file_path (str): 要处理的文件路径。
    """
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 处理文件内容，删除多余的空行
    new_lines = []
    blank_line_count = 0

    for line in lines:
        if line.strip() == "":
            blank_line_count += 1
            if blank_line_count <= 2:
                new_lines.append(line)
        else:
            new_lines.append(line)
            blank_line_count = 0

    # 写回处理后的内容
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

def traverse_and_process_directory(directory, extension):
    """
    遍历指定目录及其子目录中的所有指定扩展名的文件，并删除多余空行。

    参数：
        directory (str): 要遍历的根目录路径。
        extension (str): 要处理的文件扩展名（包括点，如 '.py'）。
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):  # 只处理指定扩展名的文件
                file_path = os.path.join(root, file)
                print(f"Processing file: {file_path}")
                remove_extra_blank_lines(file_path)

if __name__ == "__main__":
    # 指定要遍历的根目录路径和文件扩展名
    root_directory = 'D:/gitNow/Path-Planning'
    file_extension = '.py'
    traverse_and_process_directory(root_directory, file_extension)
