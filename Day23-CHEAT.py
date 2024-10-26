def count_tuesdays(n):
    if n < 2:
        return 0
    return (n - 2) // 7 + 1

T = int(input())

results = []
for _ in range(T):
    N = int(input())
    results.append(count_tuesdays(N))

for result in results:
    print(result)
