from sys import stdin

def push(heap, value):
    i = len(heap)
    heap.append(value)

    while i != 1 and value < heap[i//2]:
        heap[i] = heap[i // 2]
        i //= 2

    heap[i] = value

def pop(heap):
    i = len(heap)

    if i == 1:
        print(0)
    else:
        print(heap[1])
        last = heap[i - 1]
        i -= 2
        parent, child = 1, 2

        while child <= i:
            if child < i and heap[child] > heap[child + 1]:
                child += 1
            if last <= heap[child]:
                break

            heap[parent] = heap[child] 
            parent = child
            child *= 2

        heap[parent] = last
        heap.pop()


n = int(stdin.readline().rstrip())
heap = [0]

for _ in range(n):
    cmd = int(stdin.readline().rstrip())
    if cmd:
        push(heap, cmd)
    else:
        pop(heap)
