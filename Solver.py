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
from algorithm import G
from algorithm import F

class Solver:

	upperLimit = 13;
	lowerLimit = 1;
	goal = 24;
	
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
		self.quiet = False;
	
		if (len(argv) < 2):
			raise Exception(self.getUsage());
		elif (len(argv) > 6):
			raise Exception("up to 5 operands can be taken (received %d)" % (len(argv) - 1));
		params = argv[1:];
		self.operands = list(map(Solver.parseParam, params));

	@classmethod
	def solve(self):
		if (len(self.operands) == 4):
			return F(self.operands[0], self.operands[1], self.operands[2], self.operands[3]);
		else:
			return G(self.operands, Solver.goal);

	@classmethod
	def getUsage(self):
		return "usage: python " + self.progname + " operands..."

	@staticmethod
	def printSolutions(solutions):
		if (len(solutions) == 0):
			print("No solutions were found !");
		elif (len(solutions) == 1):
			print(solutions[0]);
		else:
			print("Solutions:\n");
			for solution in solutions:
				print(solution);
			print("\nfound %d distincts solutions" % len(solutions));
