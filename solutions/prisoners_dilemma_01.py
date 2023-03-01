t = np.array([[1, 10], [0, 5]])
l = np.array([[1, 0], [10, 5]])

prisoners_dilemma = nash.Game(t, l)
prisoners_dilemma_eqs = list(prisoners_dilemma.support_enumeration())
print(prisoners_dilemma_eqs)

sigma_t, sigma_l = prisoners_dilemma_eqs[0]
payoff_t, payoff_l = prisoners_dilemma[sigma_t, sigma_l]


print(f"Thelma's strategy: {sigma_t} - Louise's strategy {sigma_l}")
print(f"Thelma's payoff: {payoff_t} - Louise's payoff: {payoff_l}")
