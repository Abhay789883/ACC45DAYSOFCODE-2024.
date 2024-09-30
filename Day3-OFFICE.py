def total_working_hours(T, test_cases):
    results = []
    for i in range(T):
        X, Y = test_cases[i]
        total_hours = (4 * X) + Y
        results.append(total_hours)
    return results

T = int(input())
test_cases = []

for _ in range(T):
    X, Y = map(int, input().split())
    test_cases.append((X, Y))

results = total_working_hours(T, test_cases)

for result in results:
    print(result)
