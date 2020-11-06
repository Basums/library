import uuid
from datetime import time, datetime, timedelta

from flask import request
from flask_restful import Resource, marshal, fields, marshal_with

from App.api.api_book import CustomDate
from App.api.code import massage_500, massage_400, massage_407, massage_206, massage_409, massage_207, massage_208
from App.ext import db
from App.models import Book, Borrow

borrow_fields = {
    'student_id': fields.String,
    'book_id': fields.String,
    'borrow_date': CustomDate(dt_format='strftime'),
    'expect_return_date': CustomDate(dt_format='strftime')
}

multi_borrow_field = {
    'code': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(borrow_fields)),
    'error': fields.String,
}


class BorrowResource(Resource):
    # 增改查
    @staticmethod
    def post():
        try:
            data = eval(request.data.decode())
            try:
                borrow = Borrow()
                borrow.student_id = data['student_id']
                borrow.book_id = data['book_id']
                borrow.expect_return_date = datetime.now() + timedelta(days=30)
                if borrow.save():
                    return {'code': 206, 'msg': massage_206, 'data': marshal(borrow, borrow_fields),
                            'error': 'success'}
                else:
                    return {'code': 407, 'msg': massage_407, 'error': 'error'}
            except KeyError:  # 缺少关键信息
                return {'code': 400, 'msg': massage_400, 'error': 'error'}
        except SyntaxError:
            return {'code': 500, 'msg': massage_500, 'error': 'error'}

    @staticmethod
    @marshal_with(multi_borrow_field)
    def get():
        try:
            data = eval(request.data.decode())
            try:  # student_id 学生查询自己的借阅信息
                borrows = Borrow.query.filter(Borrow.student_id == data['student_id']).all()
                if len(borrows) == 0:
                    return {'code': 409, 'msg': massage_409, 'error': 'error'}
                else:
                    return {'code': 207, 'msg': massage_207, 'data': borrows, 'error': 'success'}
            except KeyError:  # # book_id 管理员查询某本书的借阅信息
                borrows = Borrow.query.filter(Borrow.book_id == data['book_id']).all()
                if len(borrows) == 0:
                    return {'code': 409, 'msg': massage_409, 'error': 'error'}
                else:
                    return {'code': 207, 'msg': massage_207, 'data': borrows, 'error': 'success'}
        except SyntaxError:
            return {'code': 500, 'msg': massage_500, 'error': 'error'}

    @staticmethod
    def put():
        try:
            data = eval(request.data.decode())
            try:
                borrows = Borrow.query.filter(Borrow.book_id == data['book_id'],
                                              Borrow.student_id == data['student_id']).all()
                if len(borrows) == 0:
                    return {'code': 409, 'msg': massage_409, 'error': 'error'}
                else:
                    for borrow in borrows:
                        db.session.delete(borrow)
                        db.session.commit()
                        return {'code': 208, 'msg': massage_208, 'error': 'error'}
            except KeyError:  # 缺少关键信息
                return {'code': 400, 'msg': massage_400, 'error': 'error'}
        except SyntaxError:
            return {'code': 500, 'msg': massage_500, 'error': 'error'}
