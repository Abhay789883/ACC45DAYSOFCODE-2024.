t = int(input())
for _ in range(t):
    x, a, b = map(int, input().split())
    score = a + 2 * b
    print("Qualify" if score >= x else "NotQualify")
