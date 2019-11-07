from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'dfdsfdfsdfdsfsdfsadf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/pythonclass'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////text.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'student_table'
    student_name = db.Column(db.String(10),index=True,primary_key=True)
    studebt_age = db.Column(db.String(2), nullable=True)
    xueli = db.Column(db.String(20), nullable=True)
    shengfen_id = db.Column(db.String(18), nullable=True)
    benren_dianhua = db.Column(db.String(11), nullable=True)
    hujidi = db.Column(db.String(30), nullable=True)
    bishi = db.Column(db.String(10), nullable=True)
    jishi = db.Column(db.String(10), nullable=True)

    def __init__(self, student_name, studebt_age,shengfen_id,xueli,benren_dianhua,hujidi,bishi,jishi):
        self.student_name = student_name
        self.studebt_age = studebt_age
        self.shengfen_id = shengfen_id
        self.benren_dianhua = benren_dianhua
        self.hujidi = hujidi
        self.bishi = bishi
        self.jishi = jishi
        self.xueli = xueli

    def __repr__(self):
        return '<User %r >' % self.student_name

db.create_all()# 创建数据库表结构
@app.route('/')
def shouye():
    return render_template('首页.html')
@app.route('/add',methods=['GET','POST'])
def add():
    if request.method == 'GET':
        return render_template('add.html')
    else:
        student_name = request.form.get('student_name')
        studebt_age = request.form.get('studebt_age')
        xueli = request.form.get('xueli')
        shengfen_id = request.form.get('shengfen_id')
        benren_dianhua = request.form.get('benren_dianhua')
        hujidi = request.form.get('hujidi')
        bishi = request.form.get('bishi')
        jishi = request.form.get('jishi')
        blog = User(student_name,studebt_age,xueli,shengfen_id,benren_dianhua,hujidi,bishi,jishi)
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('shouye'))
@app.route('/search',methods=['POST','GET'])
def search():
    if request.method == 'GET':
        return render_template('search.html')
    else:
        name = request.form.get('name')
        user = db.session.query(User).filter_by(student_name=name).all()
        return render_template('xianshi.html',user=user)






if __name__ == '__main__':
    app.run()
