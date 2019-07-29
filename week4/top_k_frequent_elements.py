from collections import Counter
import heapq


def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    d, h = [(freq, num) for num, freq in Counter(nums).items()], []
    print("d", d)
    for i in range(k):
        heapq.heappush(h, d[i]) #heappush(heap, ele)
    for i in range(k, len(d)): # range([start], stop[, step])
        if d[i][0] > h[0][0]:
            heapq.heappop(h) # remove and return smallest ele from heap
            heapq.heappush(h, d[i])
    print([heapq.heappop(h)[1] for _ in range(k)][::])
    return [heapq.heappop(h)[1] for _ in range(k)][::-1]

print(topKFrequent([1,1,1,2,2,3],2))