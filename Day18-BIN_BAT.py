def calculate_total_time(N, A, B):
    rounds = N.bit_length() - 1
    total_time = rounds * A 
    if rounds > 1:
        total_time += (rounds - 1) * B  
    return total_time

def main():
    T = int(input())
    results = []
    for _ in range(T):
        N, A, B = map(int, input().split())
        total_time = calculate_total_time(N, A, B)
        results.append(total_time)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
