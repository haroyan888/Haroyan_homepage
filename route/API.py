from flask import jsonify, request, Blueprint, redirect
from database import Test, engine, create_session

api = Blueprint('db_get', __name__, url_prefix='/api')

@api.route('/get')
def get_test():
    try:
        session = create_session()
        test_datum = session.query(Test).all()
        return jsonify([test.to_dict() for test in test_datum]), 200
    except Exception as e:
        print(e)
        return jsonify([]), 500

@api.route('/create')
def create_test():
    try:
        session = create_session()
        session.add(Test(sentence = 'Hello'))
        session.commit()
        return redirect('/api/get')
    except Exception as e:
        print(e)
        return jsonify([]), 500