def minimum_coins(T, cases):
    results = []
    for N in cases:
        results.append(N - N // 5)
    return results

T = int(input())
cases = [int(input()) for _ in range(T)]
for result in minimum_coins(T, cases):
    print(result)
