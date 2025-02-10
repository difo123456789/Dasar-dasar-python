# write class stak below

class Stack:
  def __init__(self):
    self.stack = []

  def push(self, value):
    self.stack.append(value)

  def pop(self):
    if not self.is_empty():
      return self.stack.pop()
    else:
      return None

  def peek(self):
    if not self.is_empty():
      return self.stack[-1]
    else:
      return None

  def is_empty(self):
    return len(self.stack) == 0

  def size(self):
    return len(self.stack)

  def __str__(self):
    return str(self.stack)

  def __len__(self):
    return len(self.stack)

  def __getitem__(self, index):
    return self.stack[index]

  def __setitem__(self, index, value):
    self.stack[index] = value

# Contoh penggunaan
stack = Stack()

stack.push('ular')
stack.push('ayam')
stack.push('burung')
stack.push('harimau')

stack.pop()
stack.pop()
stack.pop()

stack.push("bebek")
stack.push("kepiting")
stack.push("ubur-ubur")
stack.push("siput")
stack.push("kupu-kupu") 
stack.push("kelelawar")
stack.push("ikan")
stack.push("lebah")
stack.push("singa")

print("hasil dari stack ",stack)

