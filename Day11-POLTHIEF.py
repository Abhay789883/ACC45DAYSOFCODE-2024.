def min_time_to_catch(T, test_cases):
    results = []
    for i in range(T):
        X, Y = test_cases[i]
        time_to_catch = abs(Y - X)
        results.append(time_to_catch)
    return results

T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

results = min_time_to_catch(T, test_cases)
for result in results:
    print(result)
