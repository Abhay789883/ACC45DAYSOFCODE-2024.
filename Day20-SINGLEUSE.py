def minimum_attacks(T, test_cases):
    results = []
    
    for case in test_cases:
        H, X, Y = case
        
        health_after_special = H - Y
        if health_after_special <= 0:
            min_attacks_with_special = 1
        else:
            normal_attacks_needed = (health_after_special + X - 1) // X  
            min_attacks_with_special = 1 + normal_attacks_needed  

        normal_attacks_only = (H + X - 1) // X  

        results.append(min(min_attacks_with_special, normal_attacks_only))
    
    return results

T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]
results = minimum_attacks(T, test_cases)

for res in results:
    print(res)
