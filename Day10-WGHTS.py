def can_measure_weight(W, X, Y, Z):
    possible_sums = {0, X, Y, Z, X + Y, X + Z, Y + Z, X + Y + Z}
    return W in possible_sums

def main():
    T = int(input())
    results = []
    
    for _ in range(T):
        W, X, Y, Z = map(int, input().split())
        if can_measure_weight(W, X, Y, Z):
            results.append("YES")
        else:
            results.append("NO")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()

