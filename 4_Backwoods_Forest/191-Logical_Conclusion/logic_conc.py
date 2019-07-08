def goTo(logic, x, y):
    hero.moveXY(x, y)
    hero.say(logic)

hero.moveXY(24, 16);
a = hero.findNearestFriend().getSecretA()
b = hero.findNearestFriend().getSecretB()
c = hero.findNearestFriend().getSecretC()

goTo(a and b or c, 19, 26)
goTo((a or b) and c, 26, 36)
goTo((a or c) and (b or c), 37, 34)
goTo((a and b) or (not c and b), 40, 22)
