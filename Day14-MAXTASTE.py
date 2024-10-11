def maximize_tastiness(test_cases):
    results = []
    for case in test_cases:
        a, b, c, d = case
        tastiness_A_C = a + c
        tastiness_A_D = a + d
        tastiness_B_C = b + c
        tastiness_B_D = b + d
        
        max_tastiness = max(tastiness_A_C, tastiness_A_D, tastiness_B_C, tastiness_B_D)
        results.append(max_tastiness)
    
    return results

T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

results = maximize_tastiness(test_cases)

for result in results:
    print(result)
