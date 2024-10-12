def calculate_bags_needed(N, K, M):
    total_capacity = K * M
    bags_needed = (N + total_capacity - 1) // total_capacity 
    return bags_needed

def main():
    T = int(input())  
    results = []
    
    for _ in range(T):
        N, K, M = map(int, input().split())
        result = calculate_bags_needed(N, K, M)
        results.append(result)

    for res in results:
        print(res)

if __name__ == "__main__":
    main()
