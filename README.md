# making_change
Inspired by the mathologer video "Explaining the bizarre pattern in making change for a googol dollars (infinite generating functions)", this code answers the question "How many ways are there to make change for X cents given a fixed set of coin denominations?" In this case the coin denominations are [1, 5, 10, 25, 50, 100] and the goal was to find the answer for the largest X possible. 

Youtube link: https://www.youtube.com/watch?v=VLbePGBOVeg&t=1s

My solution uses dynamic programming based on the well known "Unbounded knapsack problem" https://en.wikipedia.org/wiki/Knapsack_problem. This allows us to calculate the number of ways to calculate change for X cents with K coins in O(XK) time. The space used is also O(KL) where L is the largest coin denomination. 

"coins.py" contains the code used to generate solutions. 
"results.txt" contains solutions. The first column is the number of cents for which to make change. The second column is the number of ways to make change for that amount. The third column is the time it took in seconds to calculate solutions from the previous row up to the current row. 