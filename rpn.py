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
from operators.Addition import Addition;
from operators.Division import Division;
from operators.Multiplication import Multiplication;
from operators.Substraction import Substraction;

operators = {
	"+": Addition(),
	"*": Multiplication(),
	"/": Division(),
	"-": Substraction(),
}

def isOperator(token):
	global operators;
	return token in operators;

def getPrecedence(token):
	global operators;
	return operators[token].precedence;

def shouldPopOperators(operatorStack, token):
    if len(operatorStack) == 0:
        return False;
    else:
        operator = operatorStack[0];
        return operator != '(' and getPrecedence(operator) >= getPrecedence(token);

def computeRPNQueue(tokens):
    """compute the RPN queue given an expression lexed as a token list"""
    queue = [];
    operatorStack = [];
    while (len(tokens) > 0):
        token = tokens.pop(0);
        if isinstance(token, int):
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
	global operators;
	return operators[token].calculate(leftOperand, rightOperand);

def calulateFromRPNQueue(queue):
    """return the float result given a RPN queue as input"""
    operandStack = [];
    while (len(queue)):
        token = queue.pop(0);
        if (isinstance(token, int)):
            operandStack.insert(0, token);
        else:
            if (len(operandStack) < 2):
                raise Exception("syntax error");
            else:
                rightOperand = float(operandStack.pop(0));
                leftOperand = float(operandStack.pop(0));
                ret = getResult(leftOperand, rightOperand, token);
                operandStack.insert(0, ret);
    if (len(operandStack) != 1):
        raise Exception("syntax error");
    return operandStack.pop(0);

def rpnFromTokens(tokens):
    rpnQueue = computeRPNQueue(tokens);
    return calulateFromRPNQueue(rpnQueue);

def rpnFromTokensNoDoubles(tokens, processedRPN):
    rpnQueue = computeRPNQueue(tokens);
    rpnTuple = tuple(rpnQueue);
    if (not rpnTuple in processedRPN):
        processedRPN[rpnTuple] = 1;
        return calulateFromRPNQueue(rpnQueue);
    else:
        return None;

def rpn(string):
    tokens = re.findall('[+-/*//()]|[0-9]+', string);
    return rpnFromTokens(tokens);
