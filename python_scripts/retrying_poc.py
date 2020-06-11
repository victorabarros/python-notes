import random
from retrying import retry
from datetime import datetime


# @retry(stop_max_attempt_number=3, wait_random_min=200, wait_random_max=500)
# def do_something_unreliable():
#     print(datetime.utcnow())
#     ii = random.randint(0, 10)
#     print(ii)
#     if ii > 2:
#         print('broke')
#         raise IOError("Broken sauce, everything is hosed!!!111one")
#     else:
#         return "Awesome sauce!"


# print(do_something_unreliable())


@retry(stop_max_attempt_number=7)
def stop_after_7_attempts():
    print("Stopping after 7 attempts")
    raise Exception()

stop_after_7_attempts()