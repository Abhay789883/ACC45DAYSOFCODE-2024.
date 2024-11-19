def minimum_apps_to_delete(T, test_cases):
    results = []
    for case in test_cases:
        S, X, Y, Z = case
        unused_memory = S - (X + Y)
        if unused_memory >= Z:
            results.append(0)
        elif unused_memory + max(X, Y) >= Z:
            results.append(1)
        else:
            results.append(2)
    return results

def main():
    T = int(input())
    test_cases = [tuple(map(int, input().split())) for _ in range(T)]
    results = minimum_apps_to_delete(T, test_cases)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()