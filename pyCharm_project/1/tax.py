file1 = r'C:\Users\Administrator\Desktop\深圳-赵永福-20181217\file1.txt'
file2 = r'C:\Users\Administrator\Desktop\深圳-赵永福-20181217\file2.txt'
with open(file1,'r') as beforeTax, open(file2, 'w') as afterTax:
    beforeTaxList = beforeTax.readlines()#用列表按行保存原始信息
    for Str in beforeTaxList:
        name_salary_info = Str.split(';')#用列表把姓名收入分开保存
        name_info = name_salary_info[0].replace(' ', '')#去除姓名字符串可能包含的空格
        name = name_info[5:]#提取姓名
        salary_info = name_salary_info[1].replace(' ', '').replace('\n', '')#去除salary字符串可能包含的空格和换行符
        salary = int(salary_info[7:])#提取工资
        afterTax.write('name: {};\tsalary:{};\ttax:{};\tincome:{}\n'.format(name,salary,int(salary*0.1),int(salary*0.9)))
with open(file2,'r') as afterTax:
    print(afterTax.read())