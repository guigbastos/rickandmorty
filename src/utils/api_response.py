from flask import jsonify
from typing import Any


class ApiResponse:
    @staticmethod
    def success(message: str, data: Any=None, status_code: int=200):
        response = {
            'success': True,
            'message': message,
            'data': data if data is not None else {}
        }
        return jsonify(response), status_code
    
    def error(message: str, errors: Any = None, status_code: int=400):
        response = {
            'success': False,
            'message': message,
            'errors': errors if errors is not None else {}
        }
        return jsonify(response), status_code
