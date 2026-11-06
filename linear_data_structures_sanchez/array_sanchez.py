# Assessment 3.2: Array Implementation for SANCHEZ

def main():
    arr = []
    print("--- INSERTION ---")
    letters = ['S', 'A', 'N', 'C', 'H', 'E', 'Z']
    for letter in letters:
        arr.append(letter)
        print(f"Append {letter}")
        
    print(f"\nBefore deletion: {arr}")
    
    print("\n--- DELETION ---")
    while len(arr) > 0:
        removed = arr.pop(0)
        print(f"Remove {removed}")
        
    print(f"After deletion: {arr} (empty array)")

if __name__ == "__main__":
    main()
