from flask import request
from flask_restful import Resource, marshal, fields

from App.api.code import massage_500, massage_400, massage_401, massage_200, massage_402, massage_201, massage_403, \
    massage_202, massage_209, massage_210, massage_211
from App.ext import db
from App.models import Student, Manager

manager_fields = {
    'manager_id': fields.Integer,
    'manager_name': fields.String,
}


class ManagerResource(Resource):
    # 注册
    @staticmethod
    def post():
        try:
            data = eval(request.data.decode())
            try:
                manager = Manager()
                manager.manager_id = data['manager_id']
                manager.manager_name = data['manager_name']
                manager.password = data['password']
                if manager.save():
                    return {'code': 209, 'msg': massage_209, 'data': marshal(manager, manager_fields),
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
            print(data)
            try:
                managers = Manager.query.filter(Manager.manager_id == data['manager_id']).all()
                if len(managers) == 0:
                    return {'code': 402, 'msg': massage_402, 'error': 'error'}
                else:
                    for manager in managers:
                        if manager.check_password(data['password']) is True:
                            return {'code': 211, 'msg': massage_211, 'data': marshal(manager, manager_fields),
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
                managers = Manager.query.filter(Manager.manager_id == data['manager_id']).all()
                if len(managers) == 0:
                    return {'code': 402, 'msg': massage_402, 'error': 'error'}
                else:
                    for manager in managers:
                        if manager.check_password(data['password']) is True:
                            manager.password = data['re-password']
                            manager.stu_name = data['manager_name']
                            db.session.commit()
                            return {'code': 210, 'msg': massage_210, 'data': marshal(manager, manager_fields)}
                        else:
                            return {'code': 403, 'msg': massage_403, 'error': 'error'}
            except KeyError:  # 缺少关键信息
                return {'code': 400, 'msg': massage_400, 'error': 'error'}
        except SyntaxError:
            return {'code': 500, 'msg': massage_500, 'error': 'error'}
