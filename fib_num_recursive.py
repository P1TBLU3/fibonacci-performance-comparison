import numpy as np

def fib_num_loop(n):
    """Calculates the full fibonnacci sequence and stores it in a list,
    and returns the last element"""
    sequence = [1,1]

    for i in range(n-2):   
        sequence.append(sequence[i] + sequence[i+1])
    
    return sequence[n-1]


def fib_num_loop_speff(n):
    """Same approach as fib_num_loop(), but only keeps stored the last 2 
    elements of the sequence"""
    sequence = [1,1]

    for i in range(n-2):   
        sequence[i%2] = sequence[0] + sequence[1]
    
    return sequence[(n-1)%2]

def fib_num_recursive(n):
    """Recursive approach"""
    if(n<3):
        return 1
    
    return fib_num_recursive(n-2) + fib_num_recursive(n-1)

def fib_num_matrix(n):
    """Approach using fibbonaci """
    result = np.array([1],
                    [1])
    fib_matrix = np.array([0,1],
                    [1,1])
    
    for i in range(n-2):
        result = fib_matrix @ result
    
    return result[1][0]


print(fib_num_loop_speff(30))
print(fib_num_loop(30))
print(fib_num_recursive(30))
print(fib_num_matrix(30))