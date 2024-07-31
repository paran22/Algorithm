import heapq

def solution(operations):
    heap = []
    for operation in operations:
        if operation.startswith("I"):
            str_num = operation.split()[1]
            heapq.heappush(heap, int(str_num))
            continue
        if heap and operation == "D -1":
            heapq.heappop(heap)
            continue
        if heap and operation == "D 1":
            max_value = max(heap)
            heap.remove(max_value)

    if len(heap) == 0:
        return [0, 0]
    return [max(heap), heapq.heappop(heap)]