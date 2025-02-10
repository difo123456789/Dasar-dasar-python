class Deque:
  def __init__(self):
    self.items = []

  def add_front(self, item):
    self.items.append(item)

  def add_rear(self, item):
    self.items.insert(0, item)

  def remove_front(self):
    if self.items:
      return self.items.pop()
    return None

  def remove_rear(self):
    if self.items:
      return self.items.pop(0)
    return None

  def is_empty(self):
    return self.items == []

  def size(self):
    return len(self.items)

  def __str__(self):
    return str(self.items)
  
dq = Deque();

dq.add_front(17)
dq.add_front(6)
dq.add_front(41)

dq.add_rear(19)
dq.add_rear(35)
dq.add_rear(10)

dq.remove_front()

dq.remove_rear()
dq.remove_rear()
dq.remove_rear()

print(f"Size dari deque adalah {dq.size()} dan isinya adalah {dq.items}")

