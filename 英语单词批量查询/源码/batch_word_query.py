# This project is created by aFei-CQUT
# ------------------------------------------------------------------------------------------------------------------------------------
#   About aFei-CQUT
# - Interests&Hobbies: Programing,  ChatGPT,  Reading serious books,  Studying academical papers.
# - CurrentlyLearning: Mathmodeling，Python and Mathmatica (preparing for National College Mathematical Contest in Modeling).
# - Email:2039787966@qq.com
# - Pronouns: Chemical Engineering, Computer Science, Enterprising, Diligent, Hard-working, Sophomore,Chongqing Institute of Technology,
# - Looking forward to collaborating on experimental data processing of chemical engineering principle
# ------------------------------------------------------------------------------------------------------------------------------------
import pandas as pd
import re
import eng_to_ipa as ipa

def read_and_query_unknown_words(excel_file, txt_file, output_file):
    """
    读取Excel文件和文本文件，查询生词信息，并保存到CSV文件中。

    Parameters:
    excel_file (str): Excel文件路径。
    txt_file (str): 文本文件路径。
    output_file (str): 输出CSV文件路径。
    """
    df = pd.read_excel(excel_file)
    with open(txt_file, 'r', encoding='utf-8') as file:
        content = file.read()

    unknown_words = list(set([word.strip().lower() for word in content.split(',')]))
    df['单词'] = df['单词'].str.strip().str.lower()
    unknown_words_info = df[df['单词'].isin(unknown_words)]
    save_query_results(unknown_words_info, output_file)

def read_and_query_handwritten_words(excel_file, txt_file, output_file):
    """
    读取Excel文件和手录生词文本文件，查询生词信息，并保存到CSV文件中。

    Parameters:
    excel_file (str): Excel文件路径。
    txt_file (str): 手录生词文件路径。
    output_file (str): 输出CSV文件路径。
    """
    with open(txt_file, 'r', encoding='utf-8') as file:
        content = file.read()

    handwritten_words = list(set([word.strip().lower() for word in content.split(',')]))
    df = pd.read_excel(excel_file)
    df['单词'] = df['单词'].str.strip().str.lower()
    handwritten_words_info = df[df['单词'].isin(handwritten_words)]
    save_query_results(handwritten_words_info, output_file)

def save_query_results(dataframe, output_file):
    """
    保存查询结果到CSV文件。

    Parameters:
    dataframe (pandas.DataFrame): 要保存的数据。
    output_file (str): 输出文件路径。
    """
    dataframe.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f"查询结果已保存到 {output_file}")

def convert_csv_to_markdown_list(input_file, output_file):
    """
    从CSV文件中读取数据并将其转换为Markdown格式的列表，然后写入MD文件。

    Parameters:
    input_file (str): 输入CSV文件路径。
    output_file (str): 输出MD文件路径。
    """
    df = pd.read_csv(input_file)
    with open(output_file, 'w', encoding='utf-8') as md_file:
        md_file.write("| 序列 | 单词 | 词义 |\n")
        md_file.write("|-----|-----|-----|\n")
        for index, row in df.iterrows():
            md_file.write(f"| {row['序列']} | {row['单词']} | {row['词义']} |\n")
    print(f"Markdown表格已写入 {output_file}")

def convert_format(input_file, output_file):
    """
    转换高亮文本格式。

    Parameters:
    input_file (str): 输入文件路径。
    output_file (str): 输出文件路径。
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    highlighted_words = re.findall(r'高亮文本：(.+)', content)
    with open(output_file, 'w', encoding='utf-8') as f:
        for word in highlighted_words:
            f.write(f"{word.strip()},\n")
    print(f"转换完成。结果已保存到 {output_file}")

def read_and_query_pronunciations(input_file, output_file):
    """
    读取文件并查询单词音标。

    Parameters:
    input_file (str): 输入文件路径。
    output_file (str): 输出文件路径。
    """
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    word_pronunciations = set()
    for line in lines:
        words = line.strip().split(',')
        for word in words:
            word = word.strip()
            if word:
                pronunciation = ipa.convert(word)
                word_pronunciations.add((word, pronunciation))
    save_pronunciation_results(list(word_pronunciations), output_file)

def save_pronunciation_results(pronunciations, output_file):
    """
    将单词音标查询结果保存到CSV文件。

    Parameters:
    pronunciations (list): 单词和音标的列表。
    output_file (str): 输出文件路径。
    """
    df = pd.DataFrame(pronunciations, columns=['Word', 'Pronunciation'])
    df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"查询结果已保存到 {output_file}")

def convert_pronunciations_csv_to_md(input_file, output_file):
    """
    将单词音标查询结果从CSV转换为Markdown格式。

    Parameters:
    input_file (str): 输入CSV文件路径。
    output_file (str): 输出MD文件路径。
    """
    df = pd.read_csv(input_file)
    with open(output_file, 'w', encoding='utf-8') as md_file:
        md_file.write("| Word | Pronunciation |\n")
        md_file.write("|------|---------------|\n")
        for index, row in df.iterrows():
            md_file.write(f"| {row['Word']} | {row['Pronunciation']} |\n")
    print(f"Markdown表格已写入 {output_file}")

if __name__ == "__main__":
    # 文件路径
    excel_file_path = '../数据/20000词频查询资料.xlsx'

    # 手录生词处理
    handwritten_txt_file_path = '../数据/手录生词记录/手录生词记录.txt'
    output_csv_path_handwritten = '../结果/手录生词查询结果/手录单词信息.csv'
    output_md_path_handwritten = '../结果/手录生词查询结果/手录单词信息.md'
    pronunciation_csv_path_handwritten = '../结果/手录生词查询结果/手录单词音标.csv'
    pronunciation_md_path_handwritten = '../结果/手录生词查询结果/手录单词音标.md'

    read_and_query_handwritten_words(excel_file_path, handwritten_txt_file_path, output_csv_path_handwritten)
    convert_csv_to_markdown_list(output_csv_path_handwritten, output_md_path_handwritten)
    read_and_query_pronunciations(handwritten_txt_file_path, pronunciation_csv_path_handwritten)
    convert_pronunciations_csv_to_md(pronunciation_csv_path_handwritten, pronunciation_md_path_handwritten)
    
    # NeatReader高亮生词处理
    highlighted_txt_file = '../数据/NeatReader高亮生词/NeatReader高亮生词.txt'
    converted_highlighted_txt_file = '../数据/NeatReader高亮生词/NeatReader高亮生词txt文件转换格式后的生词记录.txt'
    output_csv_path_highlighted = '../结果/NeatReader高亮生词查询结果/NeatReader高亮单词信息.csv'
    output_md_path_highlighted = '../结果/NeatReader高亮生词查询结果/NeatReader高亮单词信息.md'
    pronunciation_csv_path_highlighted = '../结果/NeatReader高亮生词查询结果/NeatReader高亮单词音标.csv'
    pronunciation_md_path_highlighted = '../结果/NeatReader高亮生词查询结果/NeatReader高亮单词音标.md'
    
    convert_format(highlighted_txt_file, converted_highlighted_txt_file)
    read_and_query_unknown_words(excel_file_path, converted_highlighted_txt_file, output_csv_path_highlighted)
    convert_csv_to_markdown_list(output_csv_path_highlighted, output_md_path_highlighted)
    read_and_query_pronunciations(converted_highlighted_txt_file, pronunciation_csv_path_highlighted)
    convert_pronunciations_csv_to_md(pronunciation_csv_path_highlighted, pronunciation_md_path_highlighted)
