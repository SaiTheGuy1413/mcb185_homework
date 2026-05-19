import math

def char_to_prob(a):
    qv = ord(a) - 33
    prob = 10 ** (-qv / 10)
    return prob

def prob_to_char(a):
    if a == 0:
        return None
    else:
        qv = -10 * math.log10(a)
        char = chr(int(round(qv + 33)))
        return char

print(char_to_prob('A'))
print(prob_to_char(0.001))