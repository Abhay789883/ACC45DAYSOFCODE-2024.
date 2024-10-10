T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())
    
    if 2 * Y >= X:
        print("YES")
    else:
        print("NO")
