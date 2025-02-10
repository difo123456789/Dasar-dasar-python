class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# Contoh penggunaan
queue = Queue()
queue.enqueue('bayam')
queue.enqueue('brokoli')
queue.enqueue('sawi')
queue.enqueue('cabai')
queue.enqueue('kangkung')

queue.dequeue()
queue.dequeue()



queue.enqueue("kol")
queue.enqueue("Kacang Panjang")
queue.enqueue("pare")
queue.enqueue("timun")
queue.enqueue("pokcoy")
queue.enqueue("daun bawang")
queue.enqueue("kemangi")
queue.enqueue("kale")
queue.enqueue("bucis")



print("hasil dari enque adalah: ", queue.items)