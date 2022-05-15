import os
# 获取指定格式的excel文件名
def get_all_cp_mapping_files(dir):
    file_list = []
    for root_dir, sub_dir, files in os.walk(r'' + dir):
        for file in files:
            # 此处可以按照要查找的文件名要求修改
            # 大概就是以什么为结尾，以什么为开头这样的判定条件，当然也可以用正则表达式。
            if file.endswith('.xlsx') and not file.startswith('~$'):
                file_name = os.path.join(root_dir, file)
                # 把拼接好的文件目录信息添加到列表中
                file_list.append(file_name)
    return file_list


dir = 'C:\\Users\\Wenyuan Xu\\Desktop\\excel-process'
res = get_all_cp_mapping_files(dir)
print(res)