from flask import request
from flask_restful import Resource, marshal, fields

from App.api.code import massage_500, massage_400, massage_401, massage_200, massage_402, massage_201, massage_403, \
    massage_202
from App.ext import db
from App.models import Student

student_fields = {
    'stu_id': fields.Integer,
    'stu_name': fields.String,
    'stu_sex': fields.String,
    'stu_pro': fields.String
}


class StudentResource(Resource):
    # 注册
    @staticmethod
    def post():
        try:
            data = eval(request.data.decode())
            try:
                student = Student()
                student.stu_id = data['stu_id']
                student.stu_name = data['stu_name']
                student.stu_sex = data['stu_sex']
                student.stu_pro = data['stu_pro']
                student.password = data['password']
                if student.save():
                    return {'code': 200, 'msg': massage_200, 'data': marshal(student, student_fields),
                            'error': 'success'}
                else:
                    return {'code': 401, 'msg': massage_401, 'error': 'error'}
            except KeyError:
                return {'code': 400, 'msg': massage_400, 'error': 'error'}
        except SyntaxError:
            return {'code': 500, 'msg': massage_500, 'error': 'error'}

    # 查询
    @staticmethod
    def get():
        try:
            data = eval(request.data.decode())
            try:
                students = Student.query.filter(Student.stu_id == data['stu_id']).all()
                if len(students) == 0:
                    return {'code': 402, 'msg': massage_402, 'error': 'error'}
                else:
                    for student in students:
                        if student.check_password(data['password']) is True:
                            return {'code': 201, 'msg': massage_201, 'data': marshal(student, student_fields),
                                    'error': 'success'}
                        else:
                            return {'code': 403, 'msg': massage_403, 'error': 'error'}
            except KeyError:  # 缺少关键信息
                return {'code': 400, 'msg': massage_400, 'error': 'error'}
        except SyntaxError:
            return {'code': 500, 'msg': massage_500, 'error': 'error'}

    # put方式修改个人密码
    @staticmethod
    def put():
        try:
            data = eval(request.data.decode())
            try:
                students = Student.query.filter(Student.stu_id == data['stu_id']).all()
                if len(students) == 0:
                    return {'code': 402, 'msg': massage_402, 'error': 'error'}
                else:
                    for student in students:
                        student.password = data['re_password']
                        student.stu_name = data['stu_name']
                        student.stu_sex = data['stu_sex']
                        student.stu_pro = data['stu_pro']
                        db.session.commit()
                        return {'code': 202, 'msg': massage_202, 'data': marshal(student, student_fields)}
                    else:
                        return {'code': 403, 'msg': massage_403, 'error': 'error'}
            except KeyError:  # 缺少关键信息
                return {'code': 400, 'msg': massage_400, 'error': 'error'}
        except SyntaxError:
            return {'code': 500, 'msg': massage_500, 'error': 'error'}
