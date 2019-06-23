'''
QUESTION:
Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.



Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]

'''


class Solution(object):
    def transpose(self, A):

        r, c = len(A), len(A[0])
        answer = [[None] * r for _ in range(c)]
        for row_index, row in enumerate(A):
            for col_index, value in enumerate(row):
                answer[col_index][row_index] = value
        return answer


'''
ideas/thoughts:

create a  answer new list with None , row len len(A) , col len len(A's one element)
iterate throught the lst and again
iterate through the lst
 save in the new list each value.

'''