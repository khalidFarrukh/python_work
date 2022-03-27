import random
import threading
 
def list_append(count, id, out_list):
    """
    Creates an empty list and then appends a 
    random number to the list 'count' number
    of times. A CPU-heavy operation!
    """
    for i in range(count):
        out_list.append(random.random())
gcounter=0
def number_addition(loop_size,id):
    global gcounter
    for i in range(loop_size):  
        gcounter+=1
def number_subtraction(loop_size,id):
    global gcounter
    for i in range(loop_size):
        gcounter-=1

def main():
    
    size = 10000000   # Number of random numbers to add
    threads = 2   # Number of threads to create
    # Create a list of jobs and then iterate through
    # the number of threads appending each thread to
    # the job list 
    global gcounter
    gcounter=0
    thread = threading.Thread(target=number_addition(size, 0))
    thread.start()
    thread.join()
    print("counter = ",gcounter)
    thread = threading.Thread(target=number_subtraction(size, 1))
    thread.start()
    thread.join()
    print("counter = ",gcounter)

    print("counter processing complete.")

main()
