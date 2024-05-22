"""

Stack (Stapel) und Queue

"""

# Stapel (Stack). LAST IN, FIRST OUT (LIFO)
# Pop und push

stack = []
stack.append(3)
stack.append(4)
print(stack)
stack.pop() # der letzte im Stapel darf raus
print(stack)


# Queue: FIRST IN, FIRST OUT (FIFO)
# Enequeue und dequeue
queue = []
queue.append(3)
queue.append(4)
print(queue)
queue.pop(0) # der erste in der Warteschlange darf raus
print(queue)



