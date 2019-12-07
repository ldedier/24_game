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

def computePermutations(computations, toCompute, depth, n):
	if (depth == n):
		computations.append(toCompute[:]);
		return ;
	index = toCompute.index(-1);
	potentialValues = set([i for i in range(n)])^(set(toCompute));
	potentialValues.remove(-1);
	for value in potentialValues:
			toCompute[index] = value;
			computePermutations(computations, toCompute, depth + 1, n);
	toCompute[index] = -1;

def getPermutations(n):
	permutations = [];
	computePermutations(permutations, [-1 for i in range(n)], 0, n);
	return permutations;

def naiveF(a1, a2, a3, a4):
	solutions = [];
	operators = ['+', '-', '/', '*'];
	operands = [a1, a2, a3, a4];
	permutations = getPermutations(4);
	for perm in permutations:
		#orderedOperands = operands[perm[i]], enumerate(operands[:]));
		print orderedOperands;
	#	addPermutation( ,);

def F(a1, a2, a3, a4):
	"""returns a list of combinations of operators/operands producing the result 24 """
	return naiveF(a1, a2, a3, a4);
