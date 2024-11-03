n = int(input())
player1_score = player2_score = max_lead = winner = 0

for _ in range(n):
    s1, s2 = map(int, input().split())
    player1_score += s1
    player2_score += s2
    lead = abs(player1_score - player2_score)
    if lead > max_lead:
        max_lead = lead
        winner = 1 if player1_score > player2_score else 2

print(winner, max_lead)

