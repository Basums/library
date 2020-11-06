from datetime import datetime

from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

from App.ext import db


class BaseModel(db.Model):
    __abstract__ = True

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except IntegrityError:
            return False


class Student(BaseModel):
    __tablename__ = 'Student'
    # 学号
    stu_id = db.Column(db.String(32), nullable=False, primary_key=True, unique=True)
    # 姓名
    stu_name = db.Column(db.String(32), nullable=False)
    # 性别
    stu_sex = db.Column(db.String(32), nullable=False)
    # 专业
    stu_pro = db.Column(db.String(32), nullable=False)
    # 密码
    _password = db.Column(db.String(256))

    # 设置访问密码的方法,并用装饰器@property设置为属性,调用时不用加括号
    @property
    def password(self):
        return self._password

    # 设置加密的方法,传入密码,对类属性进行操作
    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)

    # 设置验证密码的方法
    def check_password(self, user_pwd):
        return check_password_hash(self._password, user_pwd)


class Book(BaseModel):
    __tablename__ = 'Book'
    # 书籍序列
    book_id = db.Column(db.String(32), nullable=False, primary_key=True, unique=True)
    # 名称
    book_name = db.Column(db.String(256), nullable=False)
    # 作者
    book_author = db.Column(db.String(256), nullable=False)
    # 出版社
    book_pub = db.Column(db.String(256), nullable=False)
    # 数量
    book_num = db.Column(db.Integer(), nullable=False)
    # 分类
    book_sort = db.Column(db.String(256), nullable=False)
    # 登记日期
    book_record = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


class BookSort(BaseModel):
    __tablename__ = 'BookSort'
    # 类型编号
    sort_id = db.Column(db.String(256), nullable=False, primary_key=True, unique=True)
    # 类型名称
    sort_name = db.Column(db.String(256), nullable=False)


class Borrow(BaseModel):
    __tablename__ = 'Borrow'
    # 学生编号
    student_id = db.Column(db.String(256), nullable=False, primary_key=True)
    # 书籍编号
    book_id = db.Column(db.String(256), nullable=False, primary_key=True)
    # 借书时间
    borrow_date = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    # 预期归还日期 
    expect_return_date = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


class ReturnTable(BaseModel):
    __tablename__ = 'ReturnTable'
    # 学生编号
    student_id = db.Column(db.String(256), nullable=False, primary_key=True)
    # 书籍编号
    book_id = db.Column(db.String(256), nullable=False, primary_key=True)
    # 借书时间
    borrow_date = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, primary_key=True)
    # 预期归还日期 
    return_date = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


class Manager(BaseModel):
    __tablename__ = 'Manager'
    # 学号
    manager_id = db.Column(db.String(32), nullable=False, primary_key=True, unique=True)
    # 姓名
    manager_name = db.Column(db.String(32), nullable=False)
    # 密码
    _password = db.Column(db.String(256))

    # 设置访问密码的方法,并用装饰器@property设置为属性,调用时不用加括号
    @property
    def password(self):
        return self._password

    # 设置加密的方法,传入密码,对类属性进行操作
    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)

    # 设置验证密码的方法
    def check_password(self, user_pwd):
        return check_password_hash(self._password, user_pwd)
