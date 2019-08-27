#task1.1
import string
a=["hello", "world", "python", ]
b=set(a[0])
c=set(a[1])
d=set(a[2])
result=b&c&d
result2=b|c|d
one=b&c
two=c&d
three=b&d
result3=one|two|three
k=set(string.ascii_lowercase)
result4=k-b-c-d
print(result)
print(result2)
print(result3)
print(result4)


#task1.2
def generate_squares(x):
    dict={}
    for i in range(1,x+1):

        dict[i]=i**2
    return dict

print(generate_squares(9))

#task1.3
def count_letters(x):
    dict={}
    for i in x:
        dict[i]=x.count(i)
    return dict

print(count_letters("stringsample"))

#task1.4
from collections import Counter
def combine_dicts(*args):
    dict={}

    for arg in args:
        m=Counter(arg)
        n=m+Counter(dict)
        dict.update(n)
    return dict
dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}
print(combine_dicts(dict_1, dict_2))
print(combine_dicts(dict_1, dict_2, dict_3))

#task1.5
