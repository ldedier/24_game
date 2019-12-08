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
from algorithm import F, G

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
	def parseOptions(self, argv):
		i = 1;
		while (i < len(argv)):
			if (argv[i] == "--"):
				return (i + 1);
			elif (argv[i] == "-q"):
				self.quiet = True;
			else:
				return (i);
			i = i + 1;
		return (i);
	
	@classmethod
	def __init__(self, argv):
		self.progname = argv[0];
		self.quiet = False;
		argv = argv[self.parseOptions(argv):];

		if (len(argv) < 1):
			raise Exception(self.getUsage());
		elif (len(argv) > 5):
			raise Exception("up to 5 operands can be taken (received %d)" % (len(argv)));
		params = argv[:];
		self.operands = list(map(Solver.parseParam, params));

	@classmethod
	def solve(self):
		if (len(self.operands) == 4):
			return F(self.operands[0], self.operands[1], self.operands[2], self.operands[3]);
		else:
			return G(self.operands, Solver.goal);

	@classmethod
	def getUsage(self):
		return "usage: python " + self.progname + " [-q] operands..."

	@classmethod
	def printSolutions(self, solutions):
		if (self.quiet):
			for solution in solutions:
				solution.printTokens();
		else:
			if (len(solutions) == 0):
				print("No solutions were found !");
			elif (len(solutions) == 1):
				print(solutions[0]);
				print("\nfound a single solution")
			else:
				print("Solutions:\n");
				for solution in solutions:
					print(solution);
				print("\nfound %d distincts solutions" % len(solutions));
