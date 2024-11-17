def max_plates(T, test_cases):
    results = []
    for X, Y, R in test_cases:
        extra_sticks = R // 30
        total_sticks = X + extra_sticks
        plates = (total_sticks + Y - 1) // Y
        results.append(plates)
    return results

T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]
results = max_plates(T, test_cases)
print(*results, sep='\n')
