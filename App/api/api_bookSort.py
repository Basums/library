import uuid
from datetime import time

from flask import request
from flask_restful import Resource, marshal, fields, marshal_with

from App.api.code import massage_203, massage_405, massage_400, massage_500, massage_402, massage_205, massage_406, \
    massage_202, massage_204, massage_409, massage_208
from App.ext import db
from App.models import Book, BookSort

bookSort_fields = {
    'sort_id': fields.String,
    'sort_name': fields.String,
}

multi_bookSort_field = {
    'code': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(bookSort_fields)),
    'error': fields.String,
}


class BookSortResource(Resource):
    # 增改查
    @staticmethod
    def post():
        try:
            data = eval(request.data.decode())
            try:
                bookSort = BookSort()
                bookSort.sort_id = data['sort_id']
                bookSort.sort_name = data['sort_name']
                if bookSort.save():
                    return {'code': 203, 'msg': massage_203, 'data': marshal(bookSort, bookSort_fields),
                            'error': 'success'}
                else:
                    return {'code': 405, 'msg': massage_405, 'error': 'error'}
            except KeyError:  # 缺少关键信息
                return {'code': 400, 'msg': massage_400, 'error': 'error'}
        except SyntaxError:
            return {'code': 500, 'msg': massage_500, 'error': 'error'}

    @staticmethod
    @marshal_with(multi_bookSort_field)
    def get():
        try:
            data = eval(request.data.decode())
            try:
                bookSorts = BookSort.query.filter(BookSort.sort_id == data['sort_id']).all()
                if len(bookSorts) == 0:
                    return {'code': 402, 'msg': massage_402, 'error': 'error'}
                else:
                    return {'code': 205, 'msg': massage_205, 'data': bookSorts, 'error': 'success'}
            except KeyError:  # 缺少关键信息
                return {'code': 400, 'msg': massage_400, 'error': 'error'}
        except SyntaxError:
            return {'code': 500, 'msg': massage_500, 'error': 'error'}

    @staticmethod
    def put():
        try:
            data = eval(request.data.decode())
            try:
                bookSorts = BookSort.query.filter(BookSort.sort_id == data['sort_id'],
                                                  BookSort.sort_name == data['sort_name']).all()
                if len(bookSorts) == 0:
                    return {'code': 409, 'msg': massage_409, 'error': 'error'}
                else:
                    for bookSort in bookSorts:
                        db.session.delete(bookSort)
                        db.session.commit()
                        return {'code': 208, 'msg': massage_208, 'error': 'error'}
            except KeyError:  # 缺少关键信息
                return {'code': 400, 'msg': massage_400, 'error': 'error'}
        except SyntaxError:
            return {'code': 500, 'msg': massage_500, 'error': 'error'}
