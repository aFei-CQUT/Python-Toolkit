def reformat_markdown(input_file, output_file):
    # 打开输入文件进行读取
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 初始化标题编号变量
    sec2_num = 0  # 二级标题编号
    sec3_num = 0  # 三级标题编号
    sec4_num = 0  # 四级标题编号

    # 初始化列表以存储重新格式化的行
    reformatted_lines = []

    # 处理每一行
    for line in lines:
        if line.startswith('## '):
            # 处理二级标题
            sec2_num += 1
            sec3_num = 0  # 重置三级标题计数器
            sec4_num = 0  # 重置四级标题计数器
            if '<center>' in line:
                line = f'## <center>{sec2_num} {line.lstrip("## <center>").lstrip().rstrip()}'
            else:
                line = f'## {sec2_num} {line.lstrip("## ").lstrip().rstrip()}'
        elif line.startswith('### '):
            # 处理三级标题
            sec3_num += 1
            sec4_num = 0  # 重置四级标题计数器
            line = f'### {sec2_num}.{sec3_num} {line.lstrip("### ").lstrip().rstrip()}'
        elif line.startswith('#### '):
            # 处理四级标题
            sec4_num += 1
            line = f'#### {sec2_num}.{sec3_num}.{sec4_num} {line.lstrip("#### ").lstrip().rstrip()}'

        # 将重新格式化的行添加到列表中
        reformatted_lines.append(line)

    # 将重新格式化的行写入输出文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(reformatted_lines)

# 示例用法:
input_file = r'D:\20397\Documents\重庆理工大学网络生态圈计划书.md'  # 替换为你的输入文件路径
output_file = r'D:\20397\Documents\重庆理工大学网络生态圈计划书[添加序列].md'  # 替换为期望的输出文件路径
reformat_markdown(input_file, output_file)
