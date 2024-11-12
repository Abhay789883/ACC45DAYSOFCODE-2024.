T = int(input())
results = []

for _ in range(T):
    X, Y = map(int, input().split())
    water_per_person = 2 * Y
    max_people = X // water_per_person
    results.append(max_people)

for result in results:
    print(result)
