#确定代码目录 listdir
#批量读取代码文件，非代码文件略过
# 注释（分#注释和"""多行注释）-空行-代码行

import os

def list_code():#确定代码文件.py，剔除非代码文件.csv.ico
    dirs = os.listdir("D:/zhuomian/我的文件夹/学习/python")
    dirs_code= [dirs[i] for i in range(0,len(dirs)) if dirs[i][-3:] == ".py"]#如果后缀是.py
    #保留在列表中
    dirs_code.pop()#删除练习0007.py
    return dirs_code
def code_to_list(list):
    code_count=0
    for i in range(0,len(list)/2):
        code_count += list[i+1]- list[i]

def handle_file(file):
    file_to_open = "D:/zhuomian/我的文件夹/学习/python" +"/" + file
    f =open(file_to_open,"r",encoding='utf-8')   #打开代码
    codes = f.readlines()     #把代码保存为文本.readlines()
                  #codes 的长度len()就是代码行数 \n的个数就是空代码行数
    one_comment_code=sum(map(lambda x : '#' in x , codes))#单行注释代码行数
    many_comment_code = 0
    #多行注释代码行数
    #for i in code_list0:

    #code_list0 = [i for i in range(0, len(codes)) if "\"\"\"" in codes[i] ]
    #a = code_list0[1]-code_list0[0]
    #b=  code_list0[3]-code_list0[2]

    #for i in range(0,len(code_list0))

    #code_list1 = [i for i in range(0, len(codes)) if "\'\'\'" in codes[i]]


    #print(many_comment_code)
    comment_code = one_comment_code + many_comment_code #多行代码单行代码数目合并
    return codes.count('\n'),comment_code,len(codes)
if __name__ == '__main__':
    code_files = list_code()
    print(handle_file("练习0001.py"))
    empty_code=0
    comment_code=0
    common_code=0
    for file in code_files:
        coude_num_tuple=handle_file(file)
        empty_code+=coude_num_tuple[0]
        comment_code+=coude_num_tuple[1]
        common_code+=coude_num_tuple[2]
    print("目录下所有程序的空代码总数：",empty_code)
    print("目录下所有程序的注释代码总数(仅单行注释)：",comment_code)
    print("目录下所有程序的代码总数：",common_code)
