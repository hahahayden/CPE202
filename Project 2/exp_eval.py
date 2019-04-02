from stack_array import *

#Design Recipe: Create a class to address index Error
#Attributes none
class PostfixFormatException(Exception):

    pass


#Purpose: create a function to check if expression is postfix expression
#Signature: str-> bool
def postfix_valid(string):
    operandList=["+","-","*","/","^"]
    stringList=string.split()
  

    if (type(string)==str and (stringList[0]).isnumeric()==True and (stringList[-1] == "+" or stringList[-1] == "-"or stringList[-1] == "*" or stringList[-1] == "/"or stringList[-1] == "^")):
        
        return True
    elif (type(string)==str and len(string)==1 and stringList[0].isnumeric() and stringList[-1].isnumeric()):
        return True
    else:
        if (type(string)==str and stringList[-1].isnumeric() and stringList[0].isnumeric()):
            raise PostfixFormatException("Too many operands")
        
        elif (type(string)==str and stringList[0] in operandList and stringList[-1].isnumeric()):
            raise PostfixFormatException("Not valid postfix")
        elif (type(string)==str and len(string)==1 and (stringList[0] in operandList) and (stringList[0] in operandList) ):
            raise PostfixFormatException("Insufficient operands")
        elif (type(string)==str and stringList[-1] in operandList and stringList[0] in operandList):
            raise PostfixFormatException("Insufficient Operands")
        else:
            return False
        

#Purpose: to evaluate a postfix expression
# Evaluates a postfix expression"""

"""
Input argument:  a string containing a postfix expression where tokens 
are space separated.  Tokens are either operators + - * / ^ or numbers
Returns the result of the expression evaluation. 
Raises an PostfixFormatException if the input is not well-formed
"""
#Signature: str-> int
def postfix_eval(expression):
   
    if type((expression))!=str:
        raise PostfixFormatException('Not string formatted')    
    if (len(expression)==0):
        raise PostfixFormatException("Invalid token")
    postfix_valid(expression)
    expression=expression.strip()
    xlist = expression.split()
    stack = StackArray(30)
    if expression.isalpha() == True:
        raise PostfixFormatException("Invalid token")
    
        
    

    for items in range(len(xlist)):
        operator = None
        if (xlist[items] == ")" or xlist[items] == "+" or xlist[items] == "-"or xlist[items] == "*" or xlist[items] == "/"or xlist[items] == "^"or xlist[items] == "("):
            try:
                var1 = stack.pop()
                # try:
                var2 = stack.pop()
            except:
                raise PostfixFormatException("Insufficient operands")
            # except:
            #   raise PostfixFormatException("Insufficient operands")

            operator = xlist[items]
            if operator == "+":
                
                result = var1+var2

                stack.push(result)
               
                stack.itemList[stack.head]

            elif operator == "-":
                result = var2-var1

                stack.push(result)
            elif operator == "*":
                result = var2*var1

                stack.push(result)
            elif operator == "/":
                if var1==0 or var1==0.0:
                    raise ValueError

                result = var2/var1

                stack.push(result)
            elif operator == "^":

                result = var2**var1
                stack.push(result)
        elif(xlist[items].isalpha() == True):
            raise PostfixFormatException("Invalid token")
        else:

                #raise PostfixFormatException("Too many operands")
            try: 
                item2=float(xlist[items])
            except:
                item2=int(xlist[items])

            #stack.push((int(xlist[items])))
            stack.push(item2)
    if (stack.num_items > 1):
        raise PostfixFormatException("Too many operands")
        
    return(stack.pop())
#print(postfix_eval("+ 9"))
#print(postfix_eval("1 2 3 +"))


# postfix_eval("blah")
#print(postfix_eval("8 2 +"))
#print(postfix_eval("2 9 + 7 -"))
# print(postfix_eval("abc"))
#print(postfix_eval("5 1 2 + 4 ^ + 3 -"))
#print(postfix_eval("12 2 - 2 ^"))


"""Converts an infix expression to an equivalent postfix expression"""

"""Input argument:  a string containing an infix expression where tokens are 
space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
Returns a String containing a postfix expression """
#Signature: string->string
def infix_to_postfix(infix_expr):
    infix_expr=infix_expr.strip()
    xlist = infix_expr.split()
    stack = StackArray(10)
    output = ""
   
    operatorHierarchy = {"(": 0, "^": 1, "*": 2,
                         "/": 2, "+": 3, "-": 3}
    # if input is "1"
    if len(xlist) == 1:
        if xlist[0] in operatorHierarchy:
            raise IndexError
        else:

            output += xlist[0]
            return output

    for items in range(len(xlist)):

        if(xlist[items] == "("):

            stack.push("(")

            # print(stack.itemList[0])
        elif(xlist[items] == ")"):  # deletes from stack until open (

            while (stack.peek() != "("):

                output += stack.pop()
                output += " "

            stack.pop()

        elif xlist[items] in operatorHierarchy:

            if stack.num_items == 0:

                stack.push(xlist[items])

            # o2, o1<= o2
            elif stack.peek() == xlist[items] and (xlist[items]=="-" or xlist[items]=="+" or xlist[items]=="*" or xlist[items]=="/"):
                output+=stack.pop()
                output+=" "
                stack.push(xlist[items])

            elif stack.peek() == xlist[items] and (xlist[items]=="^"):
                stack.push(xlist[items])

            elif (operatorHierarchy.get(stack.peek()) <= operatorHierarchy.get(xlist[items])):
                count = True
                while ((operatorHierarchy.get(stack.peek()) <= operatorHierarchy.get(xlist[items]) and stack.peek() != xlist[items]) ):
                  
                    if(stack.num_items == 0):
                        count = False
                        break
                    elif (stack.peek() != "(" and stack.num_items > 0):
                        # print('here')
                     
                        output += stack.pop()
                       
                        output += " "
                    if stack.num_items == 0 or stack.peek() == "(":
                        count = False
                        break

                stack.push(xlist[items])
            # lower element so push  (+ is greater than *) so push xlist
            # or "*"
            elif (operatorHierarchy.get(stack.peek()) > operatorHierarchy.get(xlist[items]) or stack.peek() == '('):
               
                stack.push(xlist[items])
            #elif (operatorHierarchy.get(stack.peek()== operatorHierarchy.get(xlist[items]) and stack.peek()=="^")):
             #   stack.push(xlist[items])
          # insert regular numbers in
        elif xlist[items] != "(" or xlist[items] != ")" :
            # print("175")

            output += (xlist[items])

            output += " "

     
    for i in range(stack.num_items):
    
        if (stack.peek() != "("):
            


            output += stack.pop()
            output += " "
        else:
            stack.pop()

  
    newString = ""
    output = output.strip()
  
    return output


#print(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3"))
# infix_to_postfix("3 / 4 ^ 6 - 10")  # 346^/10-
#infix_to_postfix("3 * 6 + ( 9 ^ 3 )")
#print(infix_to_postfix("3.7 * 6 + ( 9 ^ 3 )"))
#print(infix_to_postfix("( A + B ) * C * D"))
#print(infix_to_postfix("( 3 + 5 ) + 6"))




"""Converts a prefix expression to an equivalent postfix expression"""

"""Input argument: a string containing a prefix expression where tokens are 
space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
Returns a String containing a postfix expression(tokens are space separated)"""
#Signature: str-> str
def prefix_to_postfix(prefix_expression):
    
    xlist = prefix_expression.split()
    stack = StackArray(30)     #using a stack array of size 30
    string = ""
  
    operatorHierarchy = {"(": 0, "^": 1, "*": 2,
                         "/": 2, "+": 3, "-": 3}
    # if input is "1"
    for items in range(len(xlist)-1, -1, -1):
        if xlist[items] not in operatorHierarchy:
            if(xlist[items] != ")"):
                stack.push(str(xlist[items]))

        elif xlist[items] in operatorHierarchy:
           
            if(xlist[items] != ")" and xlist[items] != ")"):
                output = ""
                op1 = stack.pop()
                op2 = stack.pop()

                if(xlist[items] == "^"):
                    output += str(xlist[items])
                    output += str(op2)
                    output += str(op1)

                else:
                    output += (str(xlist[items]))
                    output += str(op2)
                    output += str(op1)
                stack.push(output)

    newStr = (stack.pop())
    newStr = newStr[::-1]
    newerStr = ""
    count = 0
    for i in newStr:
        newerStr += i
        newerStr += " "
        count += 1
    newerStr = newerStr.strip()

    return(newerStr)


#print(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"))
