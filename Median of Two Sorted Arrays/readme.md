This problem requires you to merge two separate arrays and find the exact median value, handling the complex math of both odd and even combined lengths.
Here is the logic I used for my initial working solution:
  ➕ List Concatenation to quickly merge the arrays
  🔄 Python's built-in .sort() method to organize the data
  🧮 Modulo operators (%) and integer division (//) to dynamically locate the median index without floating-point errors.
  Getting that green "Accepted" screen after passing all 2,098 test cases is an incredible feeling!
  My next goal is to refactor this code to use Binary Search to optimize the time complexity down to $O(\log(m+n))$.
