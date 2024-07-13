import json

import jwt
import requests
from flask import request
from jwt import get_unverified_header, decode


class UserNameInjectorFilter:

    def __init__(self):
        self.public_keys = {}
        self.jwk_endpoint = "http://localhost:3000/jwks"
        jwks = requests.get(self.jwk_endpoint).json()
        for jwk in jwks['keys']:
            kid = jwk['kid']
            print(f"process kid: {kid}")
            self.public_keys[kid] = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk))

    def filter(self, user_name_claim="user_name"):
        token = str(request.headers.get("authorization"))
        print(f"token: {token}")
        decoded_token = decode(jwt=token, key=self.public_keys['123'], algorithms=['RS256'], audience="http://localhost:5000")
        print(f"decoded token: {decoded_token}")

        return None

    def decode(self, token):
        kid = get_unverified_header(token)['kid']
        key = self.public_keys[kid]

        return decode(token, key=key, algorithms=['RS256'])
