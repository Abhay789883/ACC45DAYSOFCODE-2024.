def water_filling_time(B1, B2, B3):
    empty_bottles = (B1 == 0) + (B2 == 0) + (B3 == 0)
    if empty_bottles >= 2:
        return "Water filling time"
    else:
        return "Not now"

T = int(input().strip())

for _ in range(T):
    B1, B2, B3 = map(int, input().strip().split())
    result = water_filling_time(B1, B2, B3)
    print(result)
