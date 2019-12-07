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

from rpn import rpn
from permutations import getPermutations, getPermutationsNoRepetitions, getParenthesisPermutations

def addPermutationsSolutions(orderedOperands, operatorPermutations, parenthesisPermutations, solutions):
	operators = ['+', '-', '/', '*'];
	tokens = [];
	for operatorPerm in operatorPermutations:
		orderedOperators = list(map(lambda args : operators[operatorPerm[args[0]]], enumerate(range(3)))); #nb_operands - 1 ( = nb operators)
		for parenthesisPerm in parenthesisPermutations:
			tokens = generateTokens(orderedOperands, orderedPermutations, parenthesisPermutations);
			try:
				res = rnp_tokens(tokens);
				if (rnp_tokens == 24):
					print("OK!");
			except Exception as e:
				print(e);

def F(a1, a2, a3, a4):
	"""returns a list of combinations of operators/operands producing the result 24 """
	solutions = [];
	operands = [a1, a2, a3, a4];
	operatorPermutations = getPermutations(3, 4);
	operandPermutations = getPermutationsNoRepetitions(4);
	parenthesisPermutations = getParenthesisPermutations(4);
	print(parenthesisPermutations);
	for perm in operandPermutations:
		orderedOperands = list(map(lambda args : operands[perm[args[0]]], enumerate(operands[:])));
		addPermutationsSolutions(orderedOperands, operatorPermutations, parenthesisPermutations, solutions);
	return solutions;
