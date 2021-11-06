# 3, 2, 4, 1, 5

long_dict = {
    'json' : 'a standard text-based format for representing structured data based on JavaScript object syntax', 
    'python' : 'an interpreted high-level general-purpose programming language',
    'ruby' : 'a front- and back-end web development, as well as other similar applications',
    'C++' : 'a very popular language for performance-critical applications that rely on speed and efficient memory management',
    'SQL' : 'which is a programming language used to communicate with relational databases'
}

print(long_dict.get(2, 'ruby'))
print(long_dict['ruby'])

print(long_dict.get(1, 'python'))
print(long_dict['python'])

print(long_dict.get(3, 'C++'))
print(long_dict['C++'])

print(long_dict.get(0, 'json'))
print(long_dict['json'])

print(long_dict.get(4, 'SQL'))
print(long_dict['SQL'])