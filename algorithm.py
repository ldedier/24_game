# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    algorithm.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ldedier <ldedier@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/12/07 05:54:08 by ldedier           #+#    #+#              #
#    Updated: 2019/12/07 05:54:08 by ldedier          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from rpn import rpn

def F(a1, a2, a3, a4):
    """returns a list of combinations of operators/operands producing the result 24 """
    print rpn("("+ str(a1) + "* (" + str(a2) + " + " + str(a3) + ") + " + str(a4) + ")");
    exec("res = 4 + 5");
    print res;
