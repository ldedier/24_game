# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Substraction.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ldedier <ldedier@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/12/08 07:04:57 by ldedier           #+#    #+#              #
#    Updated: 2019/12/08 07:04:57 by ldedier          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Substraction:
	def __init__(self):
		self.precedence = 1;
	
	@classmethod
	def calculate(self, op1, op2):
		return op1 - op2;
