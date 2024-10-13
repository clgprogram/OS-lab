import multiprocessing

def sender(queue):
    messages = ['Hello', 'World', 'This', 'Is', 'IPC', 'in', 'Python']
    for msg in messages:
        print(f"Sending message: {msg}")
        queue.put(msg)
    queue.put('END')  # Signal to the receiver to stop

def receiver(queue):
    while True:
        msg = queue.get()
        if msg == 'END':
            break
        print(f"Received message: {msg}")

if __name__ == "__main__":
    # Creating a queue for communication between processes
    queue = multiprocessing.Queue()

    # Creating sender and receiver processes
    sender_process = multiprocessing.Process(target=sender, args=(queue,))
    receiver_process = multiprocessing.Process(target=receiver, args=(queue,))

    # Starting both processes
    sender_process.start()
    receiver_process.start()

    # Waiting for the sender process to finish
    sender_process.join()
    
    # Waiting for the receiver process to finish
    receiver_process.join()

    print("Inter-process communication completed.")
