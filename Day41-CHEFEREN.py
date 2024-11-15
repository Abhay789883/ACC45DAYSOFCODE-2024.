def calculate_total_duration(T, test_cases):
    results = []
    for case in test_cases:
        N, A, B = case
        odd_count = (N + 1) // 2
        even_count = N // 2
        total_duration = odd_count * B + even_count * A
        results.append(total_duration)
    return results

T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]
results = calculate_total_duration(T, test_cases)
for result in results:
    print(result)
