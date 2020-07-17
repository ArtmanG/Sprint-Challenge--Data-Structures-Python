#### Task 1. Implement a Ring Buffer Data Structure

# A ring buffer is a non-growable buffer with a fixed size. When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element. This kind of data structure is very useful for use cases such as storing logs and history information, where you typically want to store information up until it reaches a certain age, after which you don't care about it anymore and don't mind seeing it overwritten by newer data.

# Implement this behavior in the RingBuffer class. RingBuffer has two methods, `append` and `get`. The `append` method adds the given element to the buffer. The `get` method returns all of the elements in the buffer in a list in their given order. It should not return any `None` values in the list even if they are present in the ring buffer.

# For example:

# ```python
# buffer = RingBuffer(3)

# buffer.get()   # should return []

# buffer.append('a')
# buffer.append('b')
# buffer.append('c')

# buffer.get()   # should return ['a', 'b', 'c']

# # 'd' overwrites the oldest value in the ring buffer, which is 'a'
# buffer.append('d')

# buffer.get()   # should return ['d', 'b', 'c']

# buffer.append('e')
# buffer.append('f')

# buffer.get()   # should return ['d', 'e', 'f']
# ```

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
        self.index = 0
        

    def append(self, item):
        # if the queue is not full, we just need to append the item.
        if len(self.queue) < self.capacity:
            self.queue.append(item)
        else:  # if the queue is full, append the new item to the item at current index, which is the oldest item in the queue
            self.queue[self.index] = item

        # current position will not exceed capacity
        if self.index + 1 == self.capacity:
            self.index = 0
        else: 
            self.index += 1
        
    def get(self):
        return self.queue