def maximize_tastiness(test_cases):
    results = []
    for a, b, c, d in test_cases:
        combination1 = a + c
        combination2 = a + d
        combination3 = b + c
        combination4 = b + d
        max_tastiness = max(combination1, combination2, combination3, combination4)
        results.append(max_tastiness)
    
    return results

T = int(input())
test_cases = []
for _ in range(T):
    a, b, c, d = map(int, input().split())
    test_cases.append((a, b, c, d))

results = maximize_tastiness(test_cases)

for result in results:
    print(result)

