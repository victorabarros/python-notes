from jwcrypto import jwt, jwk
import json

key = jwk.JWK(generate='oct', size=256)
print(key.export())

Token = jwt.JWT(header={"alg": "HS256"},
                claims={"info": "I'm a signed token"})
Token.make_signed_token(key)
print(Token.serialize())

# Etoken = jwt.JWT(header={"alg": "A256KW", "enc": "A256CBC-HS512"},
#                  claims=Token.serialize())
# Etoken.make_encrypted_token(key)
# print(Etoken.serialize())

# k = json.loads(key.export())
# key = jwk.JWK(**k)

# e = Etoken.serialize()
# print(e)

# ET = jwt.JWT(key=key, jwt=e)
# ST = jwt.JWT(key=key, jwt=ET.claims)

ST = jwt.JWT(key=key, jwt=Token.serialize())
print(ST.claims)
