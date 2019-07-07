hero.cast("haste", hero)
hero.moveXY(12, 34)
hero.say("Wake up, wolf!")

while True:
    item = hero.findNearestItem()
    if hero.distanceTo(item) > 12 && hero.isReady("jump"):
        hero.jumpTo(item.pos)
    else:
        hero.move(item.pos)

    if hero.canCast("haste")
        hero.cast("haste", hero)
    elif hero.isReady("reset-cooldown")
        hero.resetCooldown("haste")
