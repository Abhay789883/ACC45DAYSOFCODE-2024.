def can_achieve_marks(T, test_cases):
    results = []
    for n, x, y in test_cases:
        if y % x == 0 and y // x <= n:
            results.append("YES")
        else:
            results.append("NO")
    return results

T = int(input())
test_cases = []
for _ in range(T):
    n, x, y = map(int, input().split())
    test_cases.append((n, x, y))

results = can_achieve_marks(T, test_cases)

for result in results:
    print(result)
