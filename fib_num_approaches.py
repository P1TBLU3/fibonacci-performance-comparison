import numpy as np
import time
import matplotlib.pyplot as plt



def fib_num_loop(n):
    """Calculates the full Fibonacci sequence and stores it in a list,
    and returns the last element"""
    sequence = [1,1]

    for i in range(n-2):   
        sequence.append(sequence[i] + sequence[i+1])
    
    return sequence[n-1]

def fib_num_bottom_up_list(n):
    """Same approach as fib_num_loop(), but only keeps stored the last 2 
    elements of the sequence"""
    sequence = [1,1]

    for i in range(n-2):   
        sequence[i%2] = sequence[0] + sequence[1]
    
    return sequence[(n-1)%2]

def fib_num_bottom_up_vars(n):
    """Efficient bottom-up approach using two variables instead of a list."""
    if n < 3:
        return 1 

    prev, curr = 1, 1 

    for _ in range(n - 2):  
        prev, curr = curr, prev + curr  

    return curr  

def fib_num_recursive(n, memo={}):
    """Recursive approach with a cache"""
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fib_num_recursive(n-1, memo) + fib_num_recursive(n-2, memo)
    
    return memo[n]

def fib_num_matrix(n):
    """Approach using matrix multiplication """
    result = np.array([[1],
                    [1]],dtype=object)
    fib_matrix = np.array([[0,1],
                    [1,1]],dtype=object)
    
    for i in range(n-2):
        result = fib_matrix @ result

    return result[1][0]


def fib_num_matrix_exponentiation(n):
    """Approach using matrix exponentiation, which is supposed to be faster than
    simple matrix multiplication """
    if(n<2):
        return n
    
    result = np.array([[1],
                    [1]],dtype=object)
    
    fib_matrix = np.array([[0,1],
                    [1,1]],dtype=object)

    n -= 2

    while((n)>0):
        if(n%2 == 1):
            result = fib_matrix @ result
        
        fib_matrix = fib_matrix @ fib_matrix
        n = n//2

    return result[1][0]



def fib_num_binary(n):
    """Computes the nth Fibonacci number using the fast doubling method."""
    if(n<2):
        return n
    
    def fib_helper(k):
        """Returns (F(k), F(k+1)) using fast doubling."""
        if k == 0:
            return (0, 1)

        f_k, f_k1 = fib_helper(k // 2)

        # Apply fast doubling formulas
        f_2k = f_k * (2 * f_k1 - f_k)
        f_2k1 = f_k1 * f_k1 + f_k * f_k

        if k % 2 == 0:
            return (f_2k, f_2k1)
        else:
            return (f_2k1, f_2k + f_2k1)

    return fib_helper(n)[0] 






fibonacci_number = int(input("Input the nth number of the fibonacci sequence you want to calculate:") )

times = {}
results = {}

# Loop-based Fibonacci
start_time = time.time()
results["Loop"] = fib_num_loop(fibonacci_number)
times["Loop"] = time.time() - start_time
print(f"Loop method result: {results['Loop']}, Execution time: {times['Loop']} seconds")


# Bottom-up List
start_time = time.time()
results["Bottom-Up List"] = fib_num_bottom_up_list(fibonacci_number)
times["Bottom-Up List"] = time.time() - start_time
print(f"Bottom-Up List method result: {results['Bottom-Up List']}, Execution time: {times['Bottom-Up List']} seconds")


# Bottom-up using variables
start_time = time.time()
results["Bottom-Up Vars"] = fib_num_bottom_up_vars(fibonacci_number)
times["Bottom-Up Vars"] = time.time() - start_time
print(f"Bottom-Up Vars method result: {results['Bottom-Up Vars']}, Execution time: {times['Bottom-Up Vars']} seconds")


# Recursive (limited to small numbers)
if fibonacci_number < 200:
    start_time = time.time()
    results["Recursive"] = fib_num_recursive(fibonacci_number)
    times["Recursive"] = time.time() - start_time
    print(f"Recursive method result: {results['Recursive']}, Execution time: {times['Recursive']} seconds")


# Matrix Multiplication
start_time = time.time()
results["Matrix"] = fib_num_matrix(fibonacci_number)
times["Matrix"] = time.time() - start_time
print(f"Matrix method result: {results['Matrix']}, Execution time: {times['Matrix']} seconds")


# Matrix Exponentiation
start_time = time.time()
results["Matrix Exponentiation"] = fib_num_matrix_exponentiation(fibonacci_number)
times["Matrix Exponentiation"] = time.time() - start_time
print(f"Matrix Exponentiation method result: {results['Matrix Exponentiation']}, Execution time: {times['Matrix Exponentiation']} seconds")


# Binary Fibonacci (Fast Doubling)
start_time = time.time()
results["Binary (Fast Doubling)"] = fib_num_binary(fibonacci_number)
times["Binary (Fast Doubling)"] = time.time() - start_time
print(f"Binary (Fast Doubling) method result: {results['Binary (Fast Doubling)']}, Execution time: {times['Binary (Fast Doubling)']} seconds")



# Creating a histogram of execution times
plt.figure(figsize=(10, 6))
plt.bar(times.keys(), times.values(), color=['blue', 'green', 'red', 'purple', 'orange', 'cyan', 'brown'])
plt.ylabel("Execution Time (seconds)")
plt.xlabel("Fibonacci calculation methods")
plt.title("Performance comparison of different Fibonacci calculation approaches")
plt.xticks(rotation=30)
plt.show()
