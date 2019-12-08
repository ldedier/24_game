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
from Solution import Solution
from rpn import operators
from permutations import getPermutations, getPermutationsNoRepetitions, getParenthesisPermutations

def generateTokens(nbOperands, orderedOperands, orderedOperators, parenthesisPermutations):
	tokens = [];
	i = 0;
	parenthesisPermutationsDup = parenthesisPermutations[:];
	while (i < nbOperands):
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
		if (i < nbOperands - 1):
			tokens.append(orderedOperators[i]);
		i = i + 1;
	return tokens;

def F(a1, a2, a3, a4):
	return G([a1, a2, a3, a4], 24.0);

def G(operands, goal):
	"""returns a list of combinations of operators/operands producing the result goal
	from the list of operands"""
	global operators;

	operatorKeys = list(operators.keys());
	nbOperands = len(operands);
	solutions = [];
	operatorPermutations = getPermutations(nbOperands - 1, len(operatorKeys));
	operandPermutations = getPermutationsNoRepetitions(nbOperands);
	parenthesisPermutations = getParenthesisPermutations(nbOperands);
	processedOperandPermutations = {};
	processedRPN = {};
	for perm in operandPermutations:
		orderedOperands = list(map(lambda args : operands[perm[args[0]]], enumerate(operands[:])));
		if (not tuple(orderedOperands) in processedOperandPermutations):
			for operatorPerm in operatorPermutations:
				orderedOperators = list(map(lambda args : operatorKeys[operatorPerm[args[0]]], enumerate(range(nbOperands - 1))));
				for parenthesisPerm in parenthesisPermutations:
					tokens = generateTokens(nbOperands, orderedOperands, orderedOperators, parenthesisPerm[:]);
					try:
						res = rpnFromTokensNoDoubles(tokens[:], processedRPN);
						if (res == goal):
							solutions.append(Solution(tokens[:], goal));
					except ZeroDivisionError as e:
						pass;
			processedOperandPermutations[tuple(orderedOperands)] = 1;
	return solutions;
