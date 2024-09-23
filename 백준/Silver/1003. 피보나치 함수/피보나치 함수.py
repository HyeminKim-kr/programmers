# Precomputing the number of times 0 and 1 are printed for all N from 0 to 40
def fibonacci_count():
    # Initialize lists to store counts of 0 and 1
    count_0 = [0] * 41
    count_1 = [0] * 41
    
    # Base cases
    count_0[0], count_1[0] = 1, 0  # For fibonacci(0)
    count_0[1], count_1[1] = 0, 1  # For fibonacci(1)
    
    # Fill in the counts using bottom-up dynamic programming
    for i in range(2, 41):
        count_0[i] = count_0[i - 1] + count_0[i - 2]
        count_1[i] = count_1[i - 1] + count_1[i - 2]
    
    return count_0, count_1

# Function to handle multiple test cases
def solve_fibonacci_problem():
    # Precompute results for all N from 0 to 40
    count_0, count_1 = fibonacci_count()
    
    # Get number of test cases
    T = int(input())  # Read the number of test cases
    
    for _ in range(T):
        N = int(input())  # Read each test case
        print(count_0[N], count_1[N])

# Example input handling for the given inputs
solve_fibonacci_problem()
