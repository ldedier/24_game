# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Solver.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ldedier <ldedier@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/12/07 05:52:12 by ldedier           #+#    #+#              #
#    Updated: 2019/12/07 05:52:12 by ldedier          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

from algorithm import F

class Solver:

	upperLimit = 13;
	lowerLimit = 1;
	
	@staticmethod
	def parseParam(param):
		try:
			res = int(param);
		except:
			raise Exception(param + " is not a valid integer parameter");
		if res < Solver.lowerLimit or res > Solver.upperLimit:
			raise Exception(param + " is not a valid integer for this game,"\
			" integers shall be contained between " + str(Solver.lowerLimit) + " and " + str(Solver.upperLimit));
		return res;

	@classmethod
	def __init__(self, argv):
		self.progname = argv[0];
		if (len(argv) != 5):
			raise Exception(self.getUsage());
		params = argv[1:];
		self.a1, self.a2, self.a3, self.a4 = tuple(map(Solver.parseParam, params));

	@classmethod
	def solve(self):
		return F(self.a1, self.a2, self.a3, self.a4);

	@classmethod
	def getUsage(self):
		return "usage: python " + self.progname + " a1 a2 a3 a4"

	@staticmethod
	def printSolutions(solutions):
		if (len(solutions) == 0):
			print("No solutions were found !");
		elif (len(solutions) == 1):
			print(" ".join(map(str, solutions[0])) + " = 24");
		else:
			print("Solutions:\n");
			for solution in solutions:
				print(" ".join(map(str, solution)) + " = 24");
			print("\nfound %d distincts solutions" % len(solutions));
