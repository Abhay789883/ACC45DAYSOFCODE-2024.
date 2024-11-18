T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    print("YES" if X % N == 0 else "NO")
