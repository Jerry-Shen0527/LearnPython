print(int('123456'))
print(int('123456',base=8))

import functools

int8=functools.partial(int,base=8)

print(int8('123456'))

max10=functools.partial(max,10)

print(max10(1,3,5))
print(max10(5,7,9,11))
print(max)