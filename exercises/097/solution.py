def love_meet(bob, alice):
    for i in set(alice) & set(bob):
        print(i)


def affair_meet(bob, alice, silvester):
    for i in set(alice) & set(silvester):
        if i not in set(bob):
            print(i)
