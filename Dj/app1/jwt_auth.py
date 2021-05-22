import jwt
import datetime
from rest_framework.authentication import BaseAuthentication
from project import settings

JWT_SALT = settings.SECRET_KEY

# 生成token
def create_token(payload, timeout=7):
    headers = {
        'typ': 'jwt',
        'alg': 'HS256'
    }
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(days=timeout)
    result = jwt.encode(payload=payload, key=JWT_SALT, algorithm="HS256", headers=headers).decode('utf-8')
    return result


# 验证token
def parse_payload(token):
    result = {'data': None, 'error': None}
    try:
        result['data'] = jwt.decode(token, JWT_SALT, True)
    except:
        result['error'] = '认证失败'
    return result


# 用户验证
class JwtAuthentication(BaseAuthentication):
    def authenticate(self, request):
        result = {'data': None, 'error': None}
        try:
            token = request.data['token']
            result = parse_payload(token)
            if result['error'] is None:
                result['data'].pop('exp')
        except:
            result['error'] = '格式错误'
        return (result['data'], result['error'])

        