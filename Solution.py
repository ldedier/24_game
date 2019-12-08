# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ldedier <ldedier@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/12/08 11:23:35 by ldedier           #+#    #+#              #
#    Updated: 2019/12/08 11:23:35 by ldedier          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Solution:

	def __init__(self, tokens, result):
		self.tokens = tokens;
		self.result = result;

	def __repr__(self):
		return (" ".join(map(str, self.tokens)) + " = " + repr(int(self.result)));

	def printTokens(self):
		print (" ".join(map(str, self.tokens)));
