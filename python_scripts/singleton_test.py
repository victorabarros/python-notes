import os
from singleton import Singleton
import json

class Configuration(metaclass=Singleton):
    def __init__(self):
        try:
            self.health_timeout = os.getenv("HEALTH_CHECK_TIMEOUT", 2)
        except Exception:
            raise Exception
    
    def get_credentials(self):
        try:
            env = os.environ
            credential = json.loads(env["CLIENT_CREDENTIALS"])
            return {"credentials": credential}
        except Exception:
            raise Exception

if __name__ == "__main__":
    cred = Configuration().get_credentials()
    _c = Configuration()
    print(_c.health_timeout)
    print(cred)
    import pdb; pdb.set_trace()
