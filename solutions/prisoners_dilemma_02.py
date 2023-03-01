# The payoff matrix needs to be adjusted to solve the prisoners
# dilemma using nashpy. different approaches are possible. The
# simplest one is just to negate the matrix.

t = -np.array([[1, 10], [0, 5]])
l = t.transpose()

prisoners_dilemma = nash.Game(t, l)

prisoners_dilemma_eqs = list(prisoners_dilemma.support_enumeration())
sigma_t, sigma_l = prisoners_dilemma_eqs[0]
payoff_t, payoff_l = prisoners_dilemma[sigma_t, sigma_l]


print(f"Thelma's strategy: {sigma_t} - Louise's strategy {sigma_l}")
print(f"Thelma's payoff: {payoff_t} - Louise's payoff: {payoff_l}")
