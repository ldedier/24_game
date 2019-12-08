#!/usr/local/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ldedier <ldedier@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/12/07 05:49:35 by ldedier           #+#    #+#              #
#    Updated: 2019/12/07 05:49:35 by ldedier          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Solver import Solver

import sys

try:
	solver = Solver(sys.argv);
	res = solver.solve();
	solver.printSolutions(res);
	exit(0);
except Exception as e:
	print (e);
	exit(1);
