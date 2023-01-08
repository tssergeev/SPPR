import numpy as np

matrix = np.array([[2, 10, 1, 3, 7],
                   [11, 7, 0, 10, 5],
                   [3, 10, 11, 10, 12],
                   [9, 10, 5, 2, 9],
                   [5, 6, 9, 12, 5]])
q = [0.0, 0.0, 0.0, 0.5, 0.5]
p = [0.53, 0.0, 0.37, 0.07, 0.03]
answer = {}

lower_price = max([min(x) for x in matrix])
upper_price = min([max(x) for x in np.rot90(matrix)])
if lower_price == upper_price:
    print("седловая точка есть", f"ответ v={lower_price}")
else:
    buff = 0
    for i, pin in zip(matrix, p):
        buff += pin * sum([x * y for x, y in zip(i, q)])
    answer["H(P,Q)"] = buff
    for k, i in enumerate(np.rot90(matrix), 1):
        answer["H(P,B{})".format(k)] = sum([x * y for x, y in zip(i, p)])
for i in [(x, y) for x, y in answer.items()]:
    print("Ответ выйгрыш игрока А в ситуации {0[0]} = {0[1]}".format(i))
