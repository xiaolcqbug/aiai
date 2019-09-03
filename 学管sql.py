import pymysql
connect = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='19960120', db='pythonclass')
cursor = connect.cursor()
def pymysql_hui():
    try:
        cursor.execute("create table students(id varchar(10) unique ,name varchar(10),sex varchar(5),age varchar(10),phone varchar(20))")
        connect.commit()
    except:
        print("*"*10,'已拥有此表',"*"*10)
def show_students():        # 查询
    print('ID','\t' '  ','姓名',' ','性别','  ' ,'年龄','  ','电话')
    print('*'*50)
    cursor.execute('select * from students;')
    row = cursor.fetchall()
    for i in row:
        print(i)
    connect.commit()
def add_students():      # 添加
    id = input('新学生学号:')
    name = input('新学生姓名:')
    sex = input('新学生性别：')
    age = input('新学生年龄：')
    phone = input('新学生电话:')
    try:
        eow = "INSERT INTO students VALUES ('%s','%s','%s','%s','%s')"%(id,name,sex,age,phone);
        print('添加成功：',eow)
        cursor.execute(eow)
        connect.commit()
    except:
        print("*"*10,'该ID已存在',"*"*10)
def update_students():      # 改
    new_xh = input('请输入要修改的学生ID：')
    cursor.execute('select * from students;')
    row = cursor.fetchall()
    try:
        for a in row:
            if new_xh == a[0]:
                new_id = input('新学生学号:')
                new_ne = input('新学生姓名:')
                new_sex = input('新学生性别：')
                new_age = input('新学生年龄：')
                new_phone = input('新学生电话:')
                cursor.execute("""update students set id=%s,name=%s,sex=%s,age=%s,phone=%s where id =%s""",(new_id,new_ne, new_sex, new_age, new_phone,new_xh,))
                connect.commit()
                print("*"*10,'修改成功',"*"*10)
    except:
        print("*"*10,'该ID已存在',"*"*10)
def delete_students():
    new_xh = input('请输入要删除的学生ID：')
    cursor.execute('select * from students;')
    row = cursor.fetchall()
    try:
        for a in row:
            if new_xh == a[0]:
                cursor.execute("""delete from students where id=%s""",(new_xh))
                connect.commit()
                print("*"*10,'删除成功',"*"*10)
    except:
        print('操作异常，请从新操作')
def main():     # 主函数，程序入口
    while True:
        print("""
            欢迎使用学生管理系统
            1-创建数据库表
            2-查看学员信息
            3-添加学员信息
            4-修改学员信息
            5-删除学员信息
            0-退出程序
            """)
        num = int(input('请输入操作编号：'))
        if num == 1:
            pymysql_hui()
        elif num == 2:
            show_students()
        elif num == 3:
            add_students()
        elif num == 4:
            update_students()
        elif num == 5:
            delete_students()
        elif num == 0:
            break
if __name__ == '__main__':
    main()
    cursor.close()
    connect.close()
