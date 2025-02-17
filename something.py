import time

obj = time.localtime()
print(obj)
new_obj = time.mktime(obj)
print(new_obj)
another = time.gmtime(0)
print(another)