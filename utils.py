import cv2
import numpy as np
import matplotlib.pyplot as plt

operators=['+','-','/','*','^','(',')']

def isOperand(c):
    if c not in operators:
        return True
    return False

def hasLessOrEqualPriority(a,b):
    if a == '(':
        return False
    if a == '^':
        if b in ['(','^']:
            return True
    if a in ['/','*']:
        if b in ['(','/','*']:
            return True 
    if a in ['+','-']: 
            return True
    if b in ['emp',')']:
        return True
    return False
    
def peek(stack):
    if len(stack) == 0:
        return 'emp'
    return stack[len(stack)-1]    
    
def evaluate(a,b,operator):
    if operator == '+':
        return a+b
    elif operator == '-':
        return a-b
    elif operator == '/':
        return a/b
    elif operator == '*':
        return a*b
        
def toPostfix(infix):
    stack = []
    postfix = ''

    for c in infix:
        if isOperand(c):
            postfix += c
        else:
            if c == '(' or len(stack)==0:
                stack.append(c)
            elif c == ')':
                operator = stack.pop()
                while not operator == '(':
                    postfix += operator
                    operator = stack.pop()              
            else:
                while stack and hasLessOrEqualPriority(c,peek(stack)):
                    postfix += stack.pop()
                stack.append(c)

    while (not (len(stack)==0)):
        postfix += stack.pop()
    return postfix

def transform_Image(Image,transform):
    transform=toPostfix(transform)
    stack=[]
    for c in transform:
        if isOperand(c):
            stack.append(c)
        else:
            op1=stack.pop()
            op2=stack.pop()
            if op1 == 'x':
                op1=Image
                op2=int(op2)
                Image=evaluate(op2,op1,c)
                stack.append('x')
            elif op2 == 'x':
                op2=Image
                op1=int(op1)
                Image=evaluate(op2,op1,c)
                stack.append('x')
            else:
                op1=int(op1)
                op2=int(op2)
                stack.append(evaluate(op2,op1,c))
            
    return Image
    
#transform='50+x*2+33-128'
#Image=cv2.imread('./Test.jpg',cv2.IMREAD_GRAYSCALE)
#
#Image=transform_Image(Image,transform)
#plt.imshow(Image)


    


