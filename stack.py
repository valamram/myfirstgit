operators=set(['+','-','*','/','(',')','^'])
priority={'+':1,'-':1,'*':2,'/':2,'^':3}
def infixToPostfix(expression):
    stack=[]
    output=''
    for character in expression:
        if character not in operators:
            output+=character
        elif character=='(':
            stack.append('(')
        elif character==')':
            while stack and stack[-1]!='(':
                output+=stack.pop()
            stack.pop()
        else:
            while stack and stack[-1]!='('and priority[character]<=priority[stack[-1]]:
                output+=stack.pop()
                stack.apppend(character)
    while stack:
        output+=stack.pop()
        return output
expression=input('enter infix expression')
print('infix notation:',expression)
print('postfix notation:',infixToPostfix(expression))
