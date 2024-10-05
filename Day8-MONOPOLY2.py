def check_monopoly(test_cases):
    results = []
    for profits in test_cases:
        P, Q, R, S = profits
        total_other_profits = Q + R + S 
        if P > total_other_profits or Q > (P + R + S) or R > (P + Q + S) or S > (P + Q + R):
            results.append("YES")
        else:
            results.append("NO")
    return results

T = int(input())
test_cases = []

for _ in range(T):
    profits = list(map(int, input().split()))
    test_cases.append(profits)

results = check_monopoly(test_cases)

for result in results:
    print(result)

