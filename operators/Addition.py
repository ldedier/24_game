# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Addition.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ldedier <ldedier@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/12/08 07:02:32 by ldedier           #+#    #+#              #
#    Updated: 2019/12/08 07:02:32 by ldedier          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Addition:
	def __init__(self):
		self.precedence = 1;
	
	@classmethod
	def calculate(self, op1, op2):
		return op1 + op2;
