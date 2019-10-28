# 24game
given 4 random numbers, ranging from 1-13 (based on card numbers), use only BEDMAS functions to achieve a total of 24. 
The hard part of this question is how to handle different locations for the brackets - that is why I was only able to solve this 
problem using a brute force method. 
Right now, I am still missing some stuff and there are test cases this code will fail. 
EXAMPLE: trying 5,5,2,4 passes but the code misses one possibility: 2(5+5) + 4 
Working on fixing. 
This is similar to a leetcode hard question https://leetcode.com/problems/expression-add-operators/description/
The biggest difference is in the leetcode question, the order is preset. Whereas in my case, the numbers can be reordered to reach the 
target number. 
