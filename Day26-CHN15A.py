def count_wolverine_like_minions(test_cases):
    results = []
    for N, K, initial_values in test_cases:
        wolverine_count = sum(1 for value in initial_values if (value + K) % 7 == 0)
        results.append(wolverine_count)
    return results

def main():
    import sys
    
    input = sys.stdin.read
    data = input().splitlines()
    
    T = int(data[0])
    test_cases = []
    
    index = 1
    for _ in range(T):
        N, K = map(int, data[index].split())
        initial_values = list(map(int, data[index + 1].split()))
        test_cases.append((N, K, initial_values))
        index += 2
    
    results = count_wolverine_like_minions(test_cases)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()

