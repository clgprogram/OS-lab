q = []

# Adds elements {0, 1, 2, 3, 4} to the queue
for i in range(5):
    q.append(i)

# Display the contents of the queue
print("Elements of the queue:", q)

# Remove the head of the queue (the oldest element)
removed_ele = q.pop(0)
print("Removed element:", removed_ele)

# Display the queue after removal
print("Queue after removal:", q)

# View the head of the queue
head = q[0]
print("Head of queue:", head)

# Display the size of the queue
size = len(q)
print("Size of queue:", size)
