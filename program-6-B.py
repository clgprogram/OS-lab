from queue import Queue 

# Function to find page faults using FIFO
def pageFaults(pages, n, capacity): 
	
	# To represent set of current pages
	s = set() 

	# To store the pages in FIFO manner
	indexes = Queue() 

	# Start from initial page
	page_faults = 0
	
	for i in range(n): 
		
		# Check if the set can hold more pages
		if len(s) < capacity: 
			
			# If the page is not already in set, add it
			if pages[i] not in s: 
				s.add(pages[i]) 

				# Increment page fault
				page_faults += 1

				# Push the current page into the queue
				indexes.put(pages[i]) 
		
		# If the page is not in set and the set is full
		else:
			if pages[i] not in s: 
				
				# Get the first page from the queue (FIFO) and remove it from the set
				val = indexes.queue[0]
				indexes.get() 

				# Remove the first page from the set
				s.remove(val) 

				# Insert the current page
				s.add(pages[i]) 

				# Push the current page into the queue
				indexes.put(pages[i]) 

				# Increment page faults
				page_faults += 1

	return page_faults 

# Driver code 
if __name__ == '__main__': 
	pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2] 
	n = len(pages) 
	capacity = 4
	print("Page Faults: ", pageFaults(pages, n, capacity))
