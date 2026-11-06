# Assessment 3.2: Stack Implementation (LIFO) for SANCHEZ

def main():
    stack = []
    print("--- PUSH ---")
    letters = ['S', 'A', 'N', 'C', 'H', 'E', 'Z']
    for letter in letters:
        stack.append(letter)
        print(f"Push {letter}")
        
    top_to_bottom = stack[::-1]
    print(f"\nStack before popping (top to bottom): {', '.join(top_to_bottom)}")
    
    print("\n--- POP ---")
    pop_order = []
    while len(stack) > 0:
        popped = stack.pop()
        pop_order.append(popped)
        print(f"Pop {popped}")
        
    print(f"\nPop order: {', '.join(pop_order)}")
    print("After popping: EMPTY")

if __name__ == "__main__":
    main()
