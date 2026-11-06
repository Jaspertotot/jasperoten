# Assessment 3.2: Queue Implementation (FIFO) for SANCHEZ
from collections import deque

def main():
    queue = deque()
    print("--- ENQUEUE ---")
    letters = ['S', 'A', 'N', 'C', 'H', 'E', 'Z']
    for letter in letters:
        queue.append(letter)
        print(f"Enqueue {letter}")
        
    print(f"\nQueue before dequeuing: FRONT -> {' -> '.join(queue)} <- REAR")
    
    print("\n--- DEQUEUE ---")
    dequeue_order = []
    while len(queue) > 0:
        dequeued = queue.popleft()
        dequeue_order.append(dequeued)
        print(f"Dequeue {dequeued}")
        
    print(f"\nDequeue order: {', '.join(dequeue_order)}")
    print("After dequeuing: EMPTY")

if __name__ == "__main__":
    main()
