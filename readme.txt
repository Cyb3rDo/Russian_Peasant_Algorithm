The Russian Peasant's Algorithm

Author: Sukhvinder Singh | karramsos@gmail.com | @karramsos

The way most people learn to multiply large numbers looks something like this:

        86
      x 57
     ------
       602
    + 4300
     ------
      4902

If you know your multiplication facts, this "long multiplication" is quick and relatively simple. However, there are many other ways to multiply. One of these methods is often called the Russian peasant algorithm. You don't need multiplication facts to use the Russian peasant algorithm; you only need to double numbers, cut them in half, and add them up. Here are the rules:

    Write each number at the head of a column.
    Double the number in the first column, and halve the number in the second column.
       If the number in the second column is odd, divide it by two and drop the remainder.
    If the number in the second column is even, cross out that entire row.
    Keep doubling, halving, and crossing out until the number in the second column is 1.
    Add up the remaining numbers in the first column. The total is the product of your original numbers. 



Real Russian peasants may have tracked their doublings with bowls of pebbles, instead of columns of numbers. (They probably weren't interested in problems as large as our example, though; four thousand pebbles would be hard to work with!) Russian peasants weren't the only ones to use this method of multiplication. The ancient Egyptians invented a similar process thousands of years earlier, and computers are still using related methods today.

AKA = Meiation and Duplication Method

##: Pseudocode
##: Developing an algorithm
##: They are really useful
##: They are really clever
##: They make the world faster
##: They are problems that solves problems

Example: pseudocode

def algorithm_development(problems_specs):
	correct = False
	while not correct or not fast_enough(running_time):
		algorithm = devise_algorithm(problem_specs)
		correct = analyze_correctness(algorithm)
		running_time = analyse_efficiency(algorithm)
	return algorithm

Input: two numbers
Output: the solution to those two numbers multiplied together using the Russian Peasant Algorithm