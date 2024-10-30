def min_steps_to_reach(T, test_cases):
    results = []
    for i in range(T):
        A, B, K = test_cases[i]
        distance = abs(A - B)
        steps = (distance + K - 1) // K  
        results.append(steps)
    return results

T = int(input())
test_cases = []

for _ in range(T):
    A, B, K = map(int, input().split())
    test_cases.append((A, B, K))

results = min_steps_to_reach(T, test_cases)

for result in results:
    print(result)
