def s(a,b): return a+b
def u(a,b): return a-b
def m(a,b): return a*b
def d(a,b): return a/b
o,x,y=input('op:'),float(input()),float(input())
if o=='+':print(s(x,y))
elif o=='-':print(u(x,y))
elif o=='*':print(m(x,y))
elif o=='/':print(d(x,y))
#insira qual operação depois insira os 2 numeros