# Assessment 3.2: Linked List Implementation for SANCHEZ

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"Insert {data}")

    def delete_from_head(self):
        if not self.head:
            return None
        removed_data = self.head.data
        self.head = self.head.next
        print(f"Delete {removed_data}")
        return removed_data

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        if not elements:
            print("DISPLAY: EMPTY")
        else:
            print("DISPLAY:", " -> ".join(elements) + " -> NULL")

def main():
    ll = LinkedList()
    print("--- INSERT AT TAIL ---")
    letters = ['S', 'A', 'N', 'C', 'H', 'E', 'Z']
    for letter in letters:
        ll.insert_at_tail(letter)
    
    print("\nBefore deletion:")
    ll.display()
    
    print("\n--- DELETE FROM HEAD ---")
    while ll.head:
        ll.delete_from_head()
        
    print("\nAfter deletion:")
    ll.display()

if __name__ == "__main__":
    main()
