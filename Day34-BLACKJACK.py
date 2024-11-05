T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    third_number = 21 - (A + B)
    if 1 <= third_number <= 10:
        print(third_number)
    else:
        print(-1)
