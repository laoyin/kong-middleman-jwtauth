#coding=utf-8
import jwt
import time

class JwtHelper(object):

    @classmethod
    def validate(cls, token):
        # raise "error"
        try:
            payload = jwt.decode(token, '123456', audience='www.aegis.com', algorithms=['HS256'])
        except:
            return False, token
        if payload:
            return True, token
        else:
            return True, token


    @classmethod
    def generate_token(cls):
        payload = {
            "iss":"aegis.com",
            "iat":int(time.time()),
            "exp":int(time.time())+3600*7,
            "aud":"www.aegis.com",
            "sub":"yin",
            "user":"yin",
            "role":"admin"
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        return True, {'access_token':token}