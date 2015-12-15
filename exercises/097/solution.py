def love_meet(bob, alice):
    A = set(alice) & set(bob)
    return(A)


def affair_meet(bob, alice, silvester):
    A = set(alice) & set(silvester)
    B = set(bob)
    C = A - B
    return(C)
