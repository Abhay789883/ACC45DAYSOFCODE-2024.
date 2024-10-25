def count_problems(test_cases):
    results = []
    for _ in range(test_cases):
        N = int(input().strip())
        codes = input().strip().split()
        
        count_start38 = codes.count("START38")
        count_ltime108 = codes.count("LTIME108")
        
        results.append(f"{count_start38} {count_ltime108}")
    
    return results

T = int(input().strip())
output = count_problems(T)

for result in output:
    print(result)
