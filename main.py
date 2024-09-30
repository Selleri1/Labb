from add import add 
from div import div
from mult import mult

def rakn(t1, t2, op):
    if op == '+':
        return add(t1, t2)

    if op == '-':
        return t1 - t2

    if op == '/':
        return div(t1, t2) 

    if op == '*':
        return mult(t1, t2)


t1 = int(input('Tal 1: '))
op = input('Operator: ').strip()
t2 = int(input('Tal 2:'))


print(rakn(t1, t2, op))
