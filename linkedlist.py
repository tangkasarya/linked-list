class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.isEmpty():
            print("Antrean kosong")
            return
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data

    def displayQueue(self):
        if self.isEmpty():
            print("Antrean kosong")
            return
        temp = self.front
        print("Isi antrean: ", end="")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# Contoh penggunaan
if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.displayQueue()
    q.dequeue()
    q.displayQueue()
