t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        print(-1)
    else:
        positive_count = arr.count(1)
        negative_count = n - positive_count
        diff = abs(positive_count - negative_count) // 2
        print(diff)
