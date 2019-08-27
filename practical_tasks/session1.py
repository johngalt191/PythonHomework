#task1.1
def replace_quotes(input_string):
    return input_string.translate(
        input_string.maketrans({"'":'"', '"': "'"})
    )

str = input('write text with \" or \' and press enter: ')
print(replace_quotes(str))

#task1.2
def palindrome(pl):
    if pl == pl[::-1]:
        print('This is palindrome')
    else:
        print('This is not palindrome')
word = input('write your word: ')
print(palindrome(word))

#task1.3

def splitNEW(x):
    a = []
    for symbol in x:
        a.append(symbol)
    return a

x=input()

print(splitNEW(x))

#task1.4

index=[]
def splitindex (stroka, index):
    spisok=[]
    slovo=""
    print(stroka, index)
    j=0
    i=0
    while i < len(stroka):
            slovo=slovo+stroka[i]
            if i+1 == index[j]:
                spisok.insert(j,slovo)
                slovo=""
                if j+1 < len(index):
                    j=j+1
            i=i+1
    if slovo !="":
        spisok.insert(j+1,slovo)
    return spisok

print ("\n Task 1.4 split by index")
print (splitindex("12345678901234567",[4,6,10,15]))
print (splitindex("pythoniscool",[6,8]))

#task1.5
def get_digits(num):
    print(num)
    spisok=list(str(num))
    i=0
    while i<len(spisok):
        spisok[i]=int(spisok[i])
        i=i+1
    tup=tuple(spisok)
    return tup

print (get_digits(394692))

#task1.6
def get_shortest_word (stroka):
    return max(stroka.split(' '), key=len)

print (get_shortest_word("why Python is simple and effective!!!"))

#task1.7
def foo (spisok):
    product=1
    print (spisok)
    for i in spisok:
        product=product*i
    i=0
    while i<len(spisok):
        spisok[i]=int(product/spisok[i])
        i=i+1
    return spisok

print (foo([1,2,3,4,5]))
print (foo([3,2,1]))

#task1.8

def get_pairs(string):
    a=[]
    i=0
    while i<len(string)-1:
        a.insert(i,(string[i],string[i+1]))
        i=i+1
    return a
string=(1,2,3,4,5,6,7,8)
print (string)
print (get_pairs(string))
