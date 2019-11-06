from flask import Flask, request, render_template, redirect, url_for
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo
from show_all import load_all_from_mysql
from show_id import load_one_from_mysql
from lianjie import *
import pymysql

connect = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123456',
    db='pythonclass',
    charset='utf8'
)
cursor = connect.cursor()
# cursor.execute('CREATE TABLE usern( name varchar(25) primary_key ,password varchar() )')
app = Flask(__name__)
app.secret_key = 'dklsdfjsdjgklgjkdjglkf'


class MyForm(Form):  # 定义了表单的样子
    name = StringField('user-name:', validators=[DataRequired()])
    pwd = PasswordField('pwd:', validators=[DataRequired()])
    pwd2 = PasswordField('pwd2', validators=[DataRequired(), EqualTo('pwd')])
    submit = SubmitField('提交')


@app.route('/', methods=["GET", "POST"])
def shouye():
    tuple = load_all_from_mysql()
    return render_template('0.html', content=tuple)


@app.route('/blog/<int:id>')
def blog(id):
    print(id)
    tuple1 = load_one_from_mysql(id)
    # print(tuple1)
    return render_template('03.html', row=tuple1)


@app.route('/newblog', methods=['GET', 'POST'])
def newblog():
    flag = 1
    if request.method == 'GET':
        return render_template('new.html',flag=flag)
    else:
        title = request.form['title']
        username = request.form['username']
        content = request.form['content']
        try:
            cursor.execute('insert into xxxx (title,author,content) values(%s,%s,%s)', (title, username, content))
            connect.commit()
        except Exception as e:
            print(e)
            connect.rollback()
            print('添加失败')
            flag = 'defeat'
        else:
            print('添加成功')
            flag = 'ok'
        return render_template('new.html',flag = flag)

@app.route('/editblog/<int:id>',methods=['GET','POST'])
def editblog(id):
    tuple3 = load_one_from_mysql(id)
    # print('----------------00')
    if request.method == 'GET':
        return render_template('editblog.html',row = tuple3)
    else:
        # print('-------------0')
        try:
            id = request.form.get('id')
            rec = request.form.get('content')
            # print('-------------1')
            cursor.execute("update xxxx set content=%s where id= %s", (rec, id))
            connect.commit()
            # print('-------------2')
            # return render_template('editblog.html',row = tuple3)
        except Exception as e:
            # print('------------- 3')
            connect.rollback()
            print(e)
        else:
            return redirect(url_for('shouye'))




@app.route('/delblog/<int:id>',methods=['GET','POST'])
def delblog(id):
    print('1-------------------------------------->')
    tuple4 = load_one_from_mysql(id)
    if request.method == 'GET':
        print('2----------------------------->')
        return render_template('delblog.html',row = tuple4)
    else:
        print('3----------------------------------->')
        try:
            id = request.form.get('id')
            cursor.execute('delete from xxxx where id= %s'%id)
            connect.commit()

        except Exception as e:
            print(e)
            connect.rollback()
        else:
            return redirect(url_for('shouye'))






@app.errorhandler(404)
def not_found(e):
    return '页面没找到', 404


if __name__ == '__main__':
    app.run()
