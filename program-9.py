def first_fit(block_sizes, process_sizes):
    allocation = [-1] * len(process_sizes)
    
    for i in range(len(process_sizes)):
        for j in range(len(block_sizes)):
            if block_sizes[j] >= process_sizes[i]:
                allocation[i] = j
                block_sizes[j] -= process_sizes[i]
                break

    print("First Fit Allocation:")
    print_allocation(allocation, process_sizes)


def best_fit(block_sizes, process_sizes):
    allocation = [-1] * len(process_sizes)
    
    for i in range(len(process_sizes)):
        best_index = -1
        for j in range(len(block_sizes)):
            if block_sizes[j] >= process_sizes[i]:
                if best_index == -1 or block_sizes[j] < block_sizes[best_index]:
                    best_index = j
        if best_index != -1:
            allocation[i] = best_index
            block_sizes[best_index] -= process_sizes[i]

    print("Best Fit Allocation:")
    print_allocation(allocation, process_sizes)


def worst_fit(block_sizes, process_sizes):
    allocation = [-1] * len(process_sizes)

    for i in range(len(process_sizes)):
        worst_index = -1
        for j in range(len(block_sizes)):
            if block_sizes[j] >= process_sizes[i]:
                if worst_index == -1 or block_sizes[j] > block_sizes[worst_index]:
                    worst_index = j
        if worst_index != -1:
            allocation[i] = worst_index
            block_sizes[worst_index] -= process_sizes[i]

    print("Worst Fit Allocation:")
    print_allocation(allocation, process_sizes)


def print_allocation(allocation, process_sizes):
    print(f"{'Process No.':<12} {'Process Size':<15} {'Block No.':<10}")
    for i in range(len(process_sizes)):
        print(f"{i+1:<12} {process_sizes[i]:<15} {allocation[i] + 1 if allocation[i] != -1 else 'Not Allocated':<10}")


# Test example
block_sizes = [100, 500, 200, 300, 600]
process_sizes = [212, 417, 112, 426]

# First Fit
first_fit(block_sizes.copy(), process_sizes)
print()

# Best Fit
best_fit(block_sizes.copy(), process_sizes)
print()

# Worst Fit
worst_fit(block_sizes.copy(), process_sizes)
