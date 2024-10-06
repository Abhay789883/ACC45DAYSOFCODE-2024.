def max_rent_months(T, test_cases):
    results = []
    for X, Y in test_cases:
        if X >= Y:
            results.append(0)
        else:
            max_months = (Y - 1) // X
            results.append(max_months)
    return results

T = int(input())
test_cases = []

for _ in range(T):
    X, Y = map(int, input().split())
    test_cases.append((X, Y))

results = max_rent_months(T, test_cases)

for result in results:
    print(result)

