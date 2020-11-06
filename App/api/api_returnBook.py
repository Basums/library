import uuid
from datetime import time, datetime, timedelta

from flask import request
from flask_restful import Resource, marshal, fields, marshal_with

from App.api.api_book import CustomDate
from App.api.code import massage_500, massage_400, massage_407, massage_206, massage_409, massage_207, massage_208, \
    massage_212
from App.ext import db
from App.models import Book, Borrow, ReturnTable

return_fields = {
    'student_id': fields.String,
    'book_id': fields.String,
    'borrow_date': CustomDate(dt_format='strftime'),
    'return_date': CustomDate(dt_format='strftime')
}

multi_return_field = {
    'code': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(return_fields)),
    'error': fields.String,
}


class ReturnResource(Resource):
    # 增改查
    @staticmethod
    def post():
        try:
            data = eval(request.data.decode())
            try:
                returnBook = ReturnTable()
                returnBook.student_id = data['student_id']
                returnBook.book_id = data['book_id']
                returnBook.borrow_date = data['borrow_date']
                returnBook.return_date = datetime.now()
                if returnBook.save():
                    return {'code': 212, 'msg': massage_212, 'data': marshal(returnBook, multi_return_field),
                            'error': 'success'}
                else:
                    return {'code': 407, 'msg': massage_407, 'error': 'error'}
            except KeyError:  # 缺少关键信息
                return {'code': 400, 'msg': massage_400, 'error': 'error'}
        except SyntaxError:
            return {'code': 500, 'msg': massage_500, 'error': 'error'}

    @staticmethod
    @marshal_with(multi_return_field)
    def get():
        try:
            data = eval(request.data.decode())
            try:  # student_id 学生查询自己的借阅信息
                returnBooks = ReturnTable.query.filter(ReturnTable.student_id == data['student_id']).all()
                if len(returnBooks) == 0:
                    return {'code': 409, 'msg': massage_409, 'error': 'error'}
                else:
                    return {'code': 207, 'msg': massage_207, 'data': returnBooks, 'error': 'success'}
            except KeyError:  # # book_id 管理员查询某本书的借阅信息
                returnBooks = ReturnTable.query.filter(ReturnTable.book_id == data['book_id']).all()
                if len(returnBooks) == 0:
                    return {'code': 409, 'msg': massage_409, 'error': 'error'}
                else:
                    return {'code': 207, 'msg': massage_207, 'data': returnBooks, 'error': 'success'}
        except SyntaxError:
            return {'code': 500, 'msg': massage_500, 'error': 'error'}
