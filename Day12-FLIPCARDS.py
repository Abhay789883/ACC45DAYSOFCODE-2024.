def min_flips(test_cases):
    results = []
    for N, X in test_cases:
        face_down = N - X
        min_flips = min(X, face_down)
        results.append(min_flips)
    return results

T = int(input())
test_cases = []
for _ in range(T):
    N, X = map(int, input().split())
    test_cases.append((N, X))

results = min_flips(test_cases)
for result in results:
    print(result)
