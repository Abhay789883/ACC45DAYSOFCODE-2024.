def find_polynomial_degree(test_cases):
    results = []
    
    for n, coefficients in test_cases:
        degree = -1
        for i in range(n - 1, -1, -1):
            if coefficients[i] != 0:
                degree = i
                break
        results.append(degree)
    
    return results

T = int(input())
test_cases = []

for _ in range(T):
    N = int(input())
    coefficients = list(map(int, input().split()))
    test_cases.append((N, coefficients))

degrees = find_polynomial_degree(test_cases)

for degree in degrees:
    print(degree)
