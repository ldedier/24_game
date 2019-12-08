#!/bin/zsh

NB_ITERS=5
MAX_ARGS=4
GOAL=24

green="\033[32m"
red="\033[91m"
eoc="\033[39m"

function randint()
{
	seed=$(head -1 /dev/urandom | od -N 1 | awk '{ print $2 }')
	RANDOM=$seed;
	val=$RANDOM
	val=$((($val % 12) + 1))
	echo $val
}

nbTests=0;
passedTests=0;

i=0
while [ $i -le $NB_ITERS ];
do
	array=(`randint 1 13` `randint 1 13` `randint 1 13` `randint 1 13`)
	j=1
	while [ $j -le $MAX_ARGS ];
	do
		python3 main.py -q $array | while read line || [[ -n $line ]];
		do
			res=$(echo $(printf "%.2f" $(echo "${line}"| bc -l)) " == ${GOAL}" | bc -l)
			if [ $res -eq 0 ];
			then
				echo "${red}Error !${eoc}";
				exit 1;
			else
				echo "${green}$line = ${GOAL} OK !${eoc}";
				passedTests=$(($passedTests + 1))
			fi
			nbTests=$(($nbTests + 1))
		done
		array[$j]="";
		j=$((j + 1))
	done
	i=$((i + 1))
done

echo

if [ $nbTests -eq $passedTests ];
then
	echo "${green}all ${nbTests} tests passed !${eoc}"
else
	echo "${red}only ${passedTests} out of ${nbTests}${eoc}"
fi
