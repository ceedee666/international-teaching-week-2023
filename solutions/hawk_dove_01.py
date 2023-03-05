china = np.array([[10, 4], [12, 0]])
us = np.array([[10, 12], [4, 0]])

hawk_dove_game = nash.Game(china, us)
hawk_dove_game_eqs = list(hawk_dove_game.support_enumeration())

print(f"In this version of the crop game {len(hawk_dove_game_eqs)} equilibria exist:")
for eqs in hawk_dove_game_eqs:
    sigma_china, sigma_us = eqs
    print(f"{eqs} with a payoff of {hawk_dove_game[sigma_china, sigma_us]}.")
