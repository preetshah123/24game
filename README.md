# 24game
given 4 random numbers, ranging from 1-13 (based on card numbers), use only BEDMAS functions to achieve a total of 24. 
The hard part of this question is how to handle different locations for the brackets - that is why I was only able to solve this 
problem using a brute force method but by appplying it smartly so time and code is conserved. 
The program works for all test cases and now I am just working on small details, such as a more detailed output than the current one. 
 
This is similar to a leetcode hard question https://leetcode.com/problems/expression-add-operators/description/
The biggest difference is in the leetcode question, the order is preset. Whereas in my case, the numbers can be reordered to reach the 
target number. 

This is based on a card game I was taught where you split the deck between four people. No one looks at their cards and each player has to flip the first card from their deck. Based on these four numbers, each player must try to reach 24 using only BEDMAS functions and whoever gets it first wins. 
If no one can get it, you can pass the round. My friends and I were always curious about if it was possible when we pass a round
and we just happen to miss it. Thus, I rose to the challenge and decided to code the program for fun. 
