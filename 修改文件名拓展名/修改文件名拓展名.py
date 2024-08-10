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

def modify_file_names(folder_path):
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(full_path):
            # 分离文件名和后缀
            name, ext = os.path.splitext(filename)
            # 将文件名改为大写
            new_name = name.upper()
            # 更改新的后缀
            new_ext = '.m'
            # 创建新的文件名，后缀保持不变
            new_filename = f"{new_name}{new_ext}"
            new_full_path = os.path.join(folder_path, new_filename)
            # 重命名文件
            os.rename(full_path, new_full_path)
            print(f"Renamed: {filename} -> {new_filename}")

# 使用示例
folder_path = 'D:/MyGitRepository/Math-Modeling/(1) 优化函数工具箱/线性规划Matlab文本文件'  # 替换为你的文件夹路径
modify_file_names(folder_path)