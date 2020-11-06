import uuid
from datetime import time

from flask import request
from flask_restful import Resource, marshal, fields, marshal_with

from App.api.code import massage_203, massage_405, massage_400, massage_500, massage_402, massage_205, massage_406, \
    massage_202, massage_204
from App.ext import db
from App.models import Book


def _custom_format(dt, fmt):
    if isinstance(dt, str):
        return dt
    return dt.strftime(fmt)


class CustomDate(fields.DateTime):
    '''
    自定义CustomDate,原有的fileds.DateTime序列化后
    只支持 rfc822,ios8601 格式，新增 strftime 格式
    strftime格式下支持 format 参数，默认为 '%Y-%m-%d %H:%M:%S'
    '''

    def __init__(self, dt_format='rfc822', format=None, **kwargs):
        super(fields.DateTime, self).__init__(**kwargs)
        self.dt_format = dt_format
        self.fmt = format if format else '%Y-%m-%d %H:%M:%S'

    def format(self, value):
        if self.dt_format in ('rfc822', 'iso8601'):
            return super(fields.DateTime.format(value))
        elif self.dt_format == 'strftime':
            return _custom_format(value, self.fmt)
        else:
            raise Exception('Unsupported date format %s' % self.dt_format)


book_fields = {
    'book_id': fields.Integer,
    'book_name': fields.String,
    'book_author': fields.String,
    'book_pub': fields.String,
    'book_num': fields.Integer,
    'book_sort': fields.String,
    'book_record': CustomDate(dt_format='strftime')
}

multi_book_field = {
    'code': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(book_fields)),
    'error': fields.String,
}


class BookResource(Resource):
    # 增改查
    @staticmethod
    def post():
        try:
            data = eval(request.data.decode())
            try:
                book = Book()
                book.book_id = data['book_id']
                book.book_name = data['book_name']
                book.book_author = data['book_author']
                book.book_pub = data['book_pub']
                book.book_num = data['book_num']
                book.book_sort = data['book_sort']
                if book.save():
                    return {'code': 203, 'msg': massage_203, 'data': marshal(book, book_fields),
                            'error': 'success'}
                else:
                    return {'code': 405, 'msg': massage_405, 'error': 'error'}
            except KeyError:  # 缺少关键信息
                return {'code': 400, 'msg': massage_400, 'error': 'error'}
        except SyntaxError:
            return {'code': 500, 'msg': massage_500, 'error': 'error'}

    @staticmethod
    @marshal_with(multi_book_field)
    def get():
        try:
            data = eval(request.data.decode())
            try:
                books = Book.query.filter(Book.book_name == data['book_name']).all()
                if len(books) == 0:
                    return {'code': 402, 'msg': massage_402, 'error': 'error'}
                else:
                    return {'code': 205, 'msg': massage_205, 'data': books, 'error': 'success'}
            except KeyError:  # 缺少关键信息
                return {'code': 400, 'msg': massage_400, 'error': 'error'}
        except SyntaxError:
            return {'code': 500, 'msg': massage_500, 'error': 'error'}

    @staticmethod
    def put():
        try:
            data = eval(request.data.decode())
            try:
                books = Book.query.filter(Book.book_id == data['book_id']).all()
                if len(books) == 0:
                    return {'code': 406, 'msg': massage_406, 'error': 'error'}
                else:
                    for book in books:
                        book.book_name = data['book_name']
                        book.book_author = data['book_author']
                        book.book_pub = data['book_pub']
                        book.book_num = data['book_num']
                        book.book_sort = data['book_sort']
                        db.session.commit()
                        return {'code': 204, 'msg': massage_204, 'data': marshal(book, book_fields)}
            except KeyError:  # 缺少关键信息
                return {'code': 400, 'msg': massage_400, 'error': 'error'}
        except SyntaxError:
            return {'code': 500, 'msg': massage_500, 'error': 'error'}


class BookSearchResource(Resource):
    @staticmethod
    @marshal_with(multi_book_field)
    def get():
        try:
            data = eval(request.data.decode())
            _book_id = data['book_id']
            _book_name = data['book_name']
            _book_author = data['book_author']
            books = Book.query
            if len(_book_id) != 0:
                books = books.filter(Book.book_id == _book_id)
            if len(_book_name) != 0:
                books = books.filter(Book.book_name == _book_name)
            if len(_book_author) != 0:
                books = books.filter(Book.book_author == _book_author)
            books = books.all()
            return {'code': 205, 'msg': massage_205, 'data': books, 'error': 'success'}
        except SyntaxError:
            return {'code': 500, 'msg': massage_500, 'error': 'error'}
        except NameError:
            return {'code': 500, 'msg': "name 'null' is not defined", 'error': 'error'}
