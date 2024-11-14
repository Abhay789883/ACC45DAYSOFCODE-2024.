T = int(input())
for _ in range(T):
    N, X, P = map(int, input().split())
    score = 3 * X - (N - X)
    print("PASS" if score >= P else "FAIL")
