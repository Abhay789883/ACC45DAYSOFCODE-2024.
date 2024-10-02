input_line = input().strip()
A, B, C, X = map(int, input_line.split())

if X == A or X == B or X == C:
    print("Yes")
else:
    print("No")
