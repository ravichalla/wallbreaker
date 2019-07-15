'''
QUESTION:
56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.



'''

class Solution(object):
    def merge(self, intervals):
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, key=lambda x: x[0])
        ans = []
        ans.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] > ans[-1][1]:
                ans.append(intervals[i])
            else:
                ans[-1][1] = max(intervals[i][1], ans[-1][1])
        return ans

'''
Ideas/thoughts:
Initially sort the intervals based on the start point.
For just sanity check , return 0 , if the interval len is zero.
Just add the first interval to ans and iterate through from 1 to n intervals,(no need to compare first one)
and in each interval check  next interval start point is greater than last result end point.
if yes, then add the interval to the ans list.
if not , then choose max of ans last ele last value and current interval last value as the updation value of ans last value end value.
'''

