def tennis_ball_decision(test_cases):
    results = []
    for referees in test_cases:
        if all(r == 0 for r in referees):
            results.append("IN")
        else:
            results.append("OUT")
    return results

if __name__ == "__main__":
    import sys

    input = sys.stdin.read  
    data = input().strip().splitlines()
    
    T = int(data[0]) 
    test_cases = []
    
    for i in range(1, T + 1):
        referees = list(map(int, data[i].split())) 
        test_cases.append(referees)
    
    results = tennis_ball_decision(test_cases)
    
    for result in results:
        print(result)

