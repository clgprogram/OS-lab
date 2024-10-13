def page_faults(pages, capacity):
    # Set to store the current pages in memory
    s = set()
    
    # Dictionary to store the indexes of the pages
    indexes = {}
    
    # Initialize the count of page faults
    page_faults = 0

    n = len(pages)  # Get the number of pages

    for i in range(n):  # Use n here
        # If the page is not in the set
        if len(s) < capacity:
            if pages[i] not in s:
                s.add(pages[i])  # Add page to the set
                page_faults += 1  # Increment page fault count
                indexes[pages[i]] = i  # Store the index of the page
        else:
            # If the page is not already in memory
            if pages[i] not in s:
                # Find the least recently used page
                lru_page = min(indexes, key=indexes.get)
                
                # Remove the LRU page
                s.remove(lru_page)
                del indexes[lru_page]
                
                # Add the new page
                s.add(pages[i])
                page_faults += 1  # Increment page fault count
                indexes[pages[i]] = i  # Update the index of the new page

            # Update the index of the page being accessed
            indexes[pages[i]] = i

    return page_faults

# Driver code
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
capacity = 4
print(f"Page faults: {page_faults(pages, capacity)}")
