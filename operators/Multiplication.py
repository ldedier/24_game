# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Multiplication.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ldedier <ldedier@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/12/08 07:05:29 by ldedier           #+#    #+#              #
#    Updated: 2019/12/08 07:05:29 by ldedier          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Multiplication:
	def __init__(self):
		self.precedence = 2;

	def calculate(self, op1, op2):
		return op1 * op2;
