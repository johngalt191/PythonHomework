import argparse
from math import pi,e,cos,sin,acos,asin,tan,atan,log,log10,sqrt,exp,factorial

ap = argparse.ArgumentParser(description = 'Pure-Python comand line calculator.')
ap.add_argument('EXPRESSION', type=str, help='expression string to evalute')
ap.add_argument('-p', '--PRINT', default='n', choices=['y', 'n'], type =str, help = 'print evaluation process')
ap.add_argument('-m', '--MODULE', type=str, help='use modules MODULE [MODULE...] additional modules to use')
args = ap.parse_args()
argsexpr = args.EXPRESSION
argsprint = args.PRINT

numbers = ('1','2','3','4','5','6','7','8','9','0','.')
oper = ('!','^','/','//','*','%','-','+','(',')','==','<=','>=','<','>','!=','=')
trfunc = ('cos','sin','acos','asin','tan','atan','log','log10','sqrt','exp','abs','round')
string = ''
word = ''
operator = ''
gather = []


#parsing a string into list items
def parse(string):
    word=''
    #correcting the wrong character
    string = string.replace(' ','')
    string = string.replace(',','.')
    string = string.replace('--','+')
    string = string.replace('++','+')
    string = string.replace('+-','-')
    string = string.replace('-+','-')
    string = string.replace('<+','<')
    string = string.replace('>+','>')
    string = string.replace('=<','<=')
    string = string.replace('=>','>=')
    string = string.replace('==+','+')
    if string[0] == '+':
        string=string[1:]

#string parsing
    for i,sym in enumerate(string + ' '): #add extra space
        if sym in oper or i == len(string):
            if word == 'pi':
                gather.append(pi)
            elif word == 'e':
                gather.append(e)
            elif word.replace('.','').isdigit() and word.count('.')<2:
                gather.append(float(word))
            elif word in trfunc:
                gather.append(word)
            elif word != '':
                print('ERROR: unknown function "',word,sym,'"')
                exit(0)
            gather.append(sym)
            word = ''
        else:
            word = word + sym
    gather.pop() #delete extra space

    for i,item in enumerate(gather):
        if gather[i] == '/' and gather[i + 1] == '/':
            gather[i] = '//'
            gather.pop(i + 1)
        if gather[i] == '=' and gather[i + 1] == '=' or gather[i] == '=':
            gather[i] = '=='
            gather.pop(i + 1)
        if gather[i] == '!' and gather[i + 1] == '=':
            gather[i] = '!='
            gather.pop(i + 1)
        if gather[i] == '-' and gather[i - 1] in oper and type(gather[i + 1]) == float:
            gather[i + 1] = gather[i + 1]* - 1
            gather.pop(i)
        if (gather[i] == '-' and i == 0) or(gather[i] == '-' and gather[i - 1] in('*','^','+','-','(','<','>','=') ):
            gather[i] = -1
            gather.insert(i + 1,'*')
        if gather[i] == '-' and gather[i - 1] == '/':
            gather[i - 1] = '*'
            gather[i] = -1
            gather.insert(i + 1,'/')
        if gather[i] == '>' and gather[i + 1] == '=':
            gather[i] = '>='
            gather.pop(i + 1)
        if gather[i] == '<' and gather[i + 1] == '=':
            gather[i] = '<='
            gather.pop(i + 1)

    return(gather)

def operate(operator,a,b):
    if operator == "+":
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "//":
        if b != 0:
            result = a // b
        else:
            print('ERROR: division by zero')
            exit(0)
    elif operator == "/":
        if b != 0:
            result = a / b
        else:
            print('ERROR: division by zero')
            exit(0)
    elif operator == "<=":
        result = a <= b
    elif operator == ">=":
        result = a >= b
    elif operator == "<":
        result = a < b
    elif operator == ">":
        result = a > b
    elif operator == "==":
        result = a == b
    elif operator == "!=":
        result = a != b
    elif operator == "%":
       result = a % b
    elif operator == "^":
       result = a**b
    elif operator == "abs":
        result = abs(a)
    elif operator == "round":
        result = round(a)
    elif operator == "cos":
        result = cos(a)
    elif operator == "acos":
        result = acos(a)
    elif operator == "sin":
        result = sin(a)
    elif opeator == "asin":
        result = asin(a)
    elif operator == "tan":
        result = tan(a)
    elif operator == "atan":
        result = atan(a)
    elif operator == "log":
        result = log(a)
    elif operator == "log10":
        result = log10(a)
    elif operator == "sqrt":
        result = sqrt(a)
    elif operator == "exp":
        result = exp(a)
    elif operator == "!":
        result = factorial(a)
    else:
        print('ERROR: unknown math operator',operator)
        result = 0
    if argsprint == 'y':
        if operator in oper:
            print('Operate:',a,operator,b,'=',result)
        elif operator in trfunc:
            print('Operate:',operator,a,'=',result)
    return result

#calculation without brackets
def calculate(gather):
    if argsprint == 'y':
        print('Calculate:',gather)
    #search through the list of functions
    for f in trfunc:
        for i in range(gather.count(f)):
            s = gather.index(f)
            gather[s] = (operate(f,gather[s + 1],0))
            gather[s + 1] = ''
            wipe(gather)
    #сomputation of exponentiation with reverse list
    if '^' in gather:
        gather.reverse()
        while '^' in gather:
            i = gather.index('^')
            gather[i] = gather[i + 1]**gather[i - 1]
            gather[i - 1] = ''
            gather[i + 1] = ''
            wipe(gather)
        gather.reverse()

    #enumeration of the list of mathematical operations
    for j in oper:
        i = 1
        while i < len(gather):
            if gather[i] == j:
                gather[i] = operate(gather[i],gather[i - 1],gather[i + 1])
                gather[i - 1] = ''
                gather[i + 1] = ''
                wipe(gather)
                i = i - 1
            i = i + 1
    wipe(gather)
    result = gather[0]
    if len(gather) > 1:
        print('ERROR: missed operator')
        exit(0)
    return(result)

#wipe list of emty values
def wipe(gather):
    while '' in gather:
        i = gather.index('')
        gather.pop(i)
    return(gather)

#search for the beginning and end of an expression in parentheses
def brktindx(gather):
    bl = gather.index('(')
    br = gather.index(')')
    s = gather[bl + 1:br]
    while '(' in s:
        if s.count('(') == s.count(')'):
            bl = gather.index('(',bl + 1)
            br = gather.index(')',bl + 1)
            s = gather[bl + 1:br]
        else:
            br = gather.index(')',br + 1)
            s = gather[bl:br + 1]
    return(bl + 1,br)

#start of the main program

#checking brackets in a string
if argsexpr.count('(') != argsexpr.count(')'):
    print('ERROR: brackets are not balanced')
    exit(0)
#parsing a string into a list
gather = parse(argsexpr)
#search for brackets and calculate in brackets
while '(' in gather:
    a,b = brktindx(gather)
    gather[a - 1] = calculate(gather[a:b])
    while a < b + 1:
        gather[a] = ''
        a = a + 1
    wipe(gather)
#calculate without brackets
result = calculate(gather)

print(result)
