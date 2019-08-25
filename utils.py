import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

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
    
def evaluate(a,b,operator,imflag=False):
    if operator == '+':
        return a+b
    elif operator == '-':
        return a-b
    elif operator == '/':
        if imflag:
            cv2.imwrite('./temp.jpg',a/b)
            im=cv2.imread('./temp.jpg')
            os.remove('./temp.jpg')
            return im
        else : return a/b
    elif operator == '*':
        return a*b
        
def toPostfix(infix):
    stack = []
    infix=Wrap(infix)
    postfix = ''
    operator=''
    opflag=False
    for c in infix:
        if isOperand(c):
            if opflag == False:
                postfix+='@'
            postfix += c
            opflag=True
            
        else:
            if opflag == True :
                postfix+='@'
                opflag=False

            if c == '(' or len(stack)==0:
                stack.append(c)
            elif c == ')':
                operator = stack.pop()
                while not operator == '(':
                    postfix += operator
                    operator = stack.pop()              
            else:
                while stack and not hasLessOrEqualPriority(c,peek(stack)):
                    postfix += stack.pop()
                stack.append(c)
    
    while (not (len(stack)==0)):
        postfix += stack.pop()
    return postfix

def Wrap(exp):
    if exp[0] == '(' and exp[len(exp)-1] == ')' :
        return exp
    else :
        return '('+ exp + ')'     

def transform_Image(Image,transform,pixelrange=[]):
    transform = toPostfix(transform)
    stack = []
    opflag = False
    dig_holder = ''
    for c in transform:
        print(stack)
        if isOperand(c):
            if c == '@' :
                opflag= not opflag
                if opflag == False:
                    stack.append(dig_holder)
                    dig_holder=''
            if opflag == True:
                if c != '@':
                    dig_holder += c
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            if (op1 == 'X' or op1 == 'x') and (op2 == 'x' or op2 == 'X'):
                op1 = Image
                op2 = Image
                Image=evaluate(op2,op1,c,True)
                stack.append('x')
            elif op1 == 'x' or op1 == 'X':
                op1 = Image
                op2 = int(op2)
                Image=evaluate(op2,op1,c,True)
                stack.append('x')
            elif op2 == 'x' or op2 == 'X':
                op2 = Image
                op1 = int(op1)
                Image=evaluate(op2,op1,c,True)
                stack.append('x')    
            else:
                op1 = int(op1)
                op2 = int(op2)
                stack.append(evaluate(op2,op1,c))

    return Image
    
# transform='x/20'
# Image=cv2.imread('./Test.jpg')
# Image=transform_Image(Image,transform)
# cv2.imshow('lol',Image)
# cv2.waitKey(0)


    


