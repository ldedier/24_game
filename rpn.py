# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    rpn.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ldedier <ldedier@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/12/07 08:28:03 by ldedier           #+#    #+#              #
#    Updated: 2019/12/07 08:28:03 by ldedier          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import re;

def isNumber(s):
    try:
        float(s);
        return True;
    except ValueError:
        return False;

def isOperator(token):
    return (token == '+' or token == '*' or
        token == '/' or token == '-');

def getPrecedence(token):
    if (token == '+' or token == '-'):
		return 1;
    elif (token == '*' or token == '/'):
		return 2;
    else:
		raise Exception("token :" + token  + " undefined");

def shouldPopOperators(operatorStack, token):
    if len(operatorStack) == 0:
        return False;
    else:
        operator = operatorStack[0];
        return operator != '(' and getPrecedence(operator) >= getPrecedence(token);

def computeRPNQueue(tokens):
    queue = [];
    operatorStack = [];
    while (len(tokens) > 0):
        token = tokens.pop(0);
        if isNumber(token):
            queue.append(token);
        elif isOperator(token):
            while shouldPopOperators(operatorStack, token):
                operator = operatorStack.pop(0);
                queue.append(operator);
            operatorStack.insert(0, token);
        elif token == '(':
            operatorStack.insert(0, token);
        elif token == ')':
            operator = None;
            while (len(operatorStack) != 0):
				operator = operatorStack.pop(0);
				if (operator != '('):
					queue.append(operator);
				else:
					break
            if operator != '(':
				raise Exception("mismatched parenthesis");
    while len(operatorStack):
        operator = operatorStack.pop(0);
        if (operator == ')' or operator == '('):
            raise Exception("mismatched parenthesis");
        queue.append(operator);
    return queue;

def getResult(leftOperand, rightOperand, token):
    if (token == '+'):
		return leftOperand + rightOperand;
    elif (token == '-'):
        return leftOperand - rightOperand;
    elif (token == '*'):
        return leftOperand * rightOperand;
    elif (token == '/'):
        return leftOperand / rightOperand;
    else:
        return Exception(token + " : unknown operator");

def calulateFromRPNQueue(queue):
    operandStack = [];
    while (len(queue)):
        token = queue.pop(0);
        if (isNumber(token)):
            operandStack.insert(0, token);
        else:
            if (len(operandStack) < 2):
                raise Exception("syntax error");
            else:
                leftOperand = float(operandStack.pop(0));
                rightOperand = float(operandStack.pop(0));
                ret = getResult(leftOperand, rightOperand, token);
                operandStack.insert(0, ret);
    if (len(operandStack) != 1):
        raise Exception("syntax error");
    return operandStack.pop(0);

def rpn(string):
    tokens = re.findall('[+-/*//()]|[0-9]+', string);
    rpnQueue = computeRPNQueue(tokens);
    return calulateFromRPNQueue(rpnQueue);
