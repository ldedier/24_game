# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    permutations.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ldedier <ldedier@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/12/07 13:57:37 by ldedier           #+#    #+#              #
#    Updated: 2019/12/07 13:57:37 by ldedier          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def computePermutationsNoRepetitions(permutations, toCompute, depth, n):
	if (depth == n):
		permutations.append(toCompute[:]);
		return ;
	potentialValues = set([i for i in range(n)]) ^ (set(toCompute[:depth]));
	for value in potentialValues:
		toCompute[depth] = value;
		computePermutationsNoRepetitions(permutations, toCompute, depth + 1, n);

def computePermutations(permutations, toCompute, depth, n, r):
	if (depth == n):
		permutations.append(toCompute[:]);
		return ;
	for i in range(r):
		toCompute[depth] = i;
		computePermutations(permutations, toCompute, depth + 1, n, r);

def intersectParenthesis(start, end, parenthesisPermutations):
	for perm in parenthesisPermutations:
		if ((start != perm[0] and end != perm[1])) and\
			((end > perm[1] and start <= perm[1]) or (end >= perm[0] and start < perm[1])):
			return True;
	return False;

def computeParenthesisPermutations(permutations, toCompute, i, j, nbOperands):
	while (j < nbOperands):
		if ((i, j) != (0, nbOperands - 1) and not intersectParenthesis(i, j, toCompute)):
			toCompute.append((i, j));
			computeParenthesisPermutations(permutations, toCompute, j + 1, j + 2, nbOperands);
			computeParenthesisPermutations(permutations, toCompute, i, j + 1, nbOperands);
			if (i + 1 < nbOperands and j > i + 1):
				computeParenthesisPermutations(permutations, toCompute, i + 1, j, nbOperands);
			permutations.append(toCompute[:]);
			toCompute.remove((i, j));
		j = j + 1;

def getPermutationsNoRepetitions(n):
	"""returns the array of permutations index of n objects without repetitions"""
	permutations = [];
	computePermutationsNoRepetitions(permutations, [None] * n, 0, n);
	return permutations;


def getPermutations(n, r):
	"""returns the array of n^r permutations index of n objects of r possible states"""
	permutations = [];
	computePermutations(permutations, [None] * n, 0, n, r);
	return permutations;

def getParenthesisPermutations(nbOperands):
	""" returns the list of parenthesis permutations in the format:
	(first operand index, second operand index)"""

	permutations = [];
	i = 0;
	while (i < nbOperands):
		toCompute = [];
		computeParenthesisPermutations(permutations, toCompute, i, i + 1, nbOperands);
		i = i + 1;
	permutations.append([]); # no parenthesis
	return permutations;
