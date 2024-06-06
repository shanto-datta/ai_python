from math import comb

expected_value_jackpot = 11826941 / comb(59, 6)
expected_value_match_5_bonus = 1054214 / (comb(6, 5) * comb(53, 1))
expected_value_match_5 = 5795 / (comb(6, 5) * comb(53, 0))
expected_value_match_4 = 214 / (comb(6, 4) * comb(53, 2))
expected_value_match_3 = 66 / (comb(6, 3) * comb(53, 3))
expected_value_match_2 = 5 / (comb(6, 2) * comb(53, 4))

expected_value_per_ticket = (expected_value_jackpot + expected_value_match_5_bonus + expected_value_match_5 + expected_value_match_4 + expected_value_match_3 + expected_value_match_2) - 2

minimum_tickets_to_profit = int(1 / expected_value_per_ticket)

print(f"Expected value per ticket: {expected_value_per_ticket:.2f}")
print(f"Minimum number of tickets needed to make a profit: {minimum_tickets_to_profit}")
