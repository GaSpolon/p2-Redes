import asyncio
from time import time

def ou():
    ou()
    return 2

ou()

# class tst:
#     def __init__(self):
#         self.timer = None

#     def f_time(self):
#         self.call_time()


#     def call_time(self):
#         self.timer = asyncio.get_event_loop().call_later(0, self.f_time)

# a = tst()
# a.call_time()