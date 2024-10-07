# DAA-Mini_Project
Write a program to implement matrix multiplication. Also implement multithreaded matrix
multiplication with either one thread per row or one thread per cell. Analyze and compare their
performance.



Matrix Multiplication Program

This program implements basic matrix multiplication, which is a fundamental operation in linear algebra. The multiplication of two matrices, A and B, is only possible if the number of columns in A is equal to the number of rows in B.

Matrix Multiplication Concept:
Given two matrices A of size m x n and B of size n x p, the result is a matrix C of size m x p where each element C[i][j] is computed as:

css
Copy code
C[i][j] = Σ (A[i][k] * B[k][j]) for k = 0 to n
How to Use the Program:
The program accepts two input matrices from the user.
It checks if matrix multiplication is possible by verifying the dimensions of the matrices.
If valid, the program computes the product of the two matrices and outputs the result.
Example:
For two matrices A (2x3) and B (3x2):

css
Copy code
A = | 1 2 3 |       B = | 1 4 |
    | 4 5 6 |           | 2 5 |
                        | 3 6 |
The product C (2x2) is:

makefile
Copy code
C = | 14 32 |
    | 32 77 |
Code Structure:
Matrix Multiplication Function: Implements the logic for standard matrix multiplication.
Input/Output Handling: Accepts user input for the matrices and outputs the result.





