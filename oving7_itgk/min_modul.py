
def foo():
    print("Miserere mei, Deus")

def bar():
    print("Cousino")

def greeting():
    print("Hello from module!")

class Stack:
    def __init__(self, *args):
        self.items = [arg for arg in args]
    
    def push(self, item):
        self.items = [item] + self.items
    
    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return None
    
    def peek(self):
        if self.items:
            return self.items[0]
        else:
            return None

    def is_empty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __repr__(self):
        return str(self.items)
    
    def __iter__(self):
        return iter(self.items)
    
    def __next__(self):
        return next(self.items)
