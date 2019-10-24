from collections import Counter
import heapq


def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    heap = []
    result = []
    myDict = Counter(nums)
    for key in myDict:
        temp = (myDict[key] , key)
        if len(heap) >= k:
            heapq.heappushpop(heap, temp)
        else:
            heapq.heappush(heap, temp)
        print(heap)
    for i in range(len(heap)):
        result.append(heapq.heappop(heap)[1])
    #print(heapq.heappop(heap))
    print(result,"result")
    return result[::-1]


print(topKFrequent([1,1,1,1,2,2,3,3],2))