# Import the 'Process' class from the 'multiprocessing' module.
from multiprocessing import Process

# Import the 'os' module for interacting with the operating system.
import os

# Define a function 'info' to print process-related information.
def info(title):
    print(title)
    print('module name:', __name__)  # Correct use of __name__ to get the module name
    print('parent process:', os.getppid())  # Parent process ID
    print('process id:', os.getpid())  # Current process ID

# Define a function 'f' that takes a name as an argument.
def f(name):
    # Call the 'info' function to print process-related information.
    info('function f')
    # Print a greeting using the provided name.
    print(f'hello {name}')

# Check if the script is being run as the main program.
if __name__ == '__main__':
    # Call the 'info' function to print process-related information for the main process.
    info('Main line')

    # Create a new 'Process' object, specifying the target function 'f' and its arguments.
    p = Process(target=f, args=('Bob',))

    # Start the new process.
    p.start()

    # Wait for the child process to complete before continuing.
    p.join()
    print(f"child process:{p.name}")
    print(f"child process:{p.pid}")
