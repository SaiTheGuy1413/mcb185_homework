def tm(a, t, g, c):
    if a + t + g + c <= 13:
        return None
    if a + t + g + c <= 13:
        return ((a + t) * 2) + ((c + g) * 4)
    else:
        return 64.9 + (41 * (g + c - 16.4) / (a + t + c + g))
    
print(tm(5, 7, 3, 4))