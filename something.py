import time

obj = time.localtime()
str_time = time.strftime("%c",obj) # has to have a format before
print(str_time)
print(obj)
new_obj = time.mktime(obj)
print(new_obj)
another = time.gmtime(0)
print(another)