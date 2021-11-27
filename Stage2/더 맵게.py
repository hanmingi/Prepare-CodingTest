import heapq
def solution(scoville, K):
    answer = 0

    heap = []
    for i in scoville:
        heapq.heappush(heap, i)

    while True:
        if len(heap) >= 2:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        else:
            if heap[0] < K:
                return -1
        answer += 1

        if heap[0] >= K:
            break
    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))