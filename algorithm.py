# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    algorithm.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ldedier <ldedier@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/12/07 05:54:08 by ldedier           #+#    #+#              #
#    Updated: 2019/12/07 05:54:08 by ldedier          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from rpn import rpnFromTokensNoDoubles
from permutations import getPermutations, getPermutationsNoRepetitions, getParenthesisPermutations

def generateTokens(orderedOperands, orderedOperators, parenthesisPermutations):
	tokens = [];
	i = 0;
	parenthesisPermutationsDup = parenthesisPermutations[:];
	while (i < 4):
		while (len(parenthesisPermutations) > 0):
			if (parenthesisPermutations[0][0] == i):
				parenthesisPermutations.pop(0);
				tokens.append('(');
			else:
				break;
		tokens.append(orderedOperands[i]);
		while (len(parenthesisPermutationsDup) > 0):
			if (parenthesisPermutationsDup[0][1] == i):
				parenthesisPermutationsDup.pop(0);
				tokens.append(')');
			else:
				break;
		if (i < 3):
			tokens.append(orderedOperators[i]);
		i = i + 1;
	return tokens;

def addPermutationsSolutions(orderedOperands, operatorPermutations,
		parenthesisPermutations, processedRPN, solutions):
	operators = ['+', '-', '/', '*'];
	for operatorPerm in operatorPermutations:
		orderedOperators = list(map(lambda args : operators[operatorPerm[args[0]]], enumerate(range(3)))); #nb_operands - 1 ( = nb operators)
		for parenthesisPerm in parenthesisPermutations:
			tokens = generateTokens(orderedOperands, orderedOperators, parenthesisPerm[:]);
			try:
				res = rpnFromTokensNoDoubles(tokens[:], processedRPN);
				if (res == 24.0):
					solutions.append(tokens[:]);
			except ZeroDivisionError as e:
				pass;

def F(a1, a2, a3, a4):
	"""returns a list of combinations of operators/operands producing the result 24 """

	solutions = [];
	operands = [a1, a2, a3, a4];

	operatorPermutations = getPermutations(3, 4);
	operandPermutations = getPermutationsNoRepetitions(4);
	parenthesisPermutations = getParenthesisPermutations(4);

	processedOperandPermutations = {};
	processedRPN = {};

	for perm in operandPermutations:
		orderedOperands = list(map(lambda args : operands[perm[args[0]]], enumerate(operands[:])));
		if (not tuple(orderedOperands) in processedOperandPermutations):
			addPermutationsSolutions(orderedOperands, operatorPermutations,\
				parenthesisPermutations, processedRPN, solutions);
			processedOperandPermutations[tuple(orderedOperands)] = 1;
	return solutions;
