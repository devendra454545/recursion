# Recursion Programs in Python

This repository contains basic recursion programs implemented in Python.
These programs are created to understand the fundamentals of recursion, base cases, and recursive calls.

## Programs Included
## 1️⃣ 1_to_n.py

Description:
Prints numbers from 1 to N using recursion.

Concept Used:

Base case when n == 0

Recursive call before printing

Example Output (n = 5):

1 2 3 4 5

## 2️⃣ n_to_1.py

Description:
Prints numbers from N to 1 using recursion.

Concept Used:

Print first

Then recursive call

Example Output (n = 5):

5 4 3 2 1

## 3️⃣ print_name_n_times.py

Description:
Prints a given name N times using recursion.

Concept Used:

Counter-based recursion

Base case to stop recursion

Example Output (n = 3):

Devendra
Devendra
Devendra

## 4️⃣ print_something_n_times.py

Description:
Prints a custom message N times using recursion.

Concept Used:

Recursive repetition

Decreasing problem size

## 5️⃣ sum_of_first_n_numbers.py

Description:
Calculates the sum of first N natural numbers using recursion.

Formula Used Recursively:

sum(n) = n + sum(n-1)

Example:

Input: 5
Output: 15

## 6️⃣ factorial_of_n.py

Description:
Finds the factorial of a number using recursion.

Formula:

n! = n * (n-1)!

Example:

Input: 5
Output: 120

## 7️⃣ array_rev.py

Description:
Reverses an array using recursion (swapping elements).

Concept Used:

Two pointers (left & right)

Swap elements

Recursive call with updated indices

Example:

Input:  [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]

## 8️⃣ palindrome_number.py

Description:
Checks whether a number is a palindrome using recursion (without converting to string).

Concept Used:

Digit extraction using % and //

Recursive number reversal

Base case (n == 0)

Comparison of original and reversed number

Example:

Input: 121
Output: True

Input: 123
Output: False

## 🧠 Concepts Covered

Base Case

Recursive Case

Stack memory usage

Function call stack behavior

Backtracking in recursion

Two-pointer technique in recursion

To check if number is Palindrome or not

## 🚀 How to Run

Make sure Python is installed.

python filename.py

Example:

python factorial_of_n.py
📌 Purpose of This Repository

This repository is created for:

Practicing recursion fundamentals

Strengthening DSA basics

Preparing for coding interviews

Understanding stack flow visually

👨‍💻 Author

Devendra Singh Thakur
Python & DSA Learner