
from functools import wraps
import jwt
from flask import request, jsonify


def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return jsonify({'message': 'Токен отсутствует'}), 403

        try:
            data = jwt.decode(token, 'ваш_секретный_ключ', algorithms=['HS256'])

        except:
            return jsonify({'message': 'Недействительный токен'}), 403

        return func(*args, **kwargs)

    return decorated
