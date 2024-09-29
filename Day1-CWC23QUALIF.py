def check_qualification(score):
    if score >= 12:
        return "Yes"
    else:
        return "No"

score = int(input())
result = check_qualification(score)
print(result)