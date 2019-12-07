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

def computeParenthesisPermutations(permutations, toCompute, i, nbOperands):
	j = i + 1;
	while (j < nbOperands):
		toCompute.append((i, j));
		permutations.append(toCompute[:]);
		computeParenthesisPermutations(permutations, toCompute, i + j + 1, nbOperands);
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
	permutations.append([]); # no parenthesis
	i = 0;
	while (i < nbOperands):
		toCompute = [];
		computeParenthesisPermutations(permutations, toCompute, i, nbOperands);
		i = i + 1;
	permutations.remove([(0, nbOperands - 1)]); # removing the all parenthesed expression
	return permutations;
