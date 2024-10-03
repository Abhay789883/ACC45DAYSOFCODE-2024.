def maximum_points(test_cases):
    results = []
    
    for X, Y in test_cases:
        points_A_first = (500 - 2 * X) + (1000 - 4 * (X + Y))
        
        points_B_first = (1000 - 4 * Y) + (500 - 2 * (X + Y))
        
        max_points = max(points_A_first, points_B_first)
        results.append(max_points)
    
    return results


T = int(input())
test_cases = []

for _ in range(T):
    X, Y = map(int, input().split())
    test_cases.append((X, Y))

results = maximum_points(test_cases)

for result in results:
    print(result)
