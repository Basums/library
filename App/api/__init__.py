from flask_restful import Api

from App.api.api_book import BookResource, BookSearchResource
from App.api.api_bookSort import BookSortResource
from App.api.api_borrow import BorrowResource
from App.api.api_manager import ManagerResource
from App.api.api_returnBook import ReturnResource
from App.api.api_student import StudentResource

api = Api()


def init_api(app):
    api.init_app(app)


api.add_resource(StudentResource, '/api/student')
api.add_resource(BookResource, '/api/book')
api.add_resource(BookSearchResource, '/api/book/search')
api.add_resource(BorrowResource, '/api/borrow')
api.add_resource(BookSortResource, '/api/bookSort')
api.add_resource(ManagerResource, '/api/manager')
api.add_resource(ReturnResource, '/api/return')
