def openreadtxt(file_name):
    # data = []
    file = open(file_name, 'r')  # 打开文件
    file_data = file.readlines()  # 读取所有行
    for row in file_data:
        data = row.strip('\n') #去掉列表中每一个元素的换行符

        # tmp_list = row.split(' ')  # 按‘，’切分每行的数据
        # tmp_list[-1] = tmp_list[-1].replace('\n',',') #去掉换行符
        # data.append(tmp_list)  # 将每行数据插入data中
    return data


if __name__ == "__main__":
    data = openreadtxt('G:\电话.txt')
    print(data)