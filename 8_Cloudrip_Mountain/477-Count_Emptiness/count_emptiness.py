def moveNSteps(n):
    hero.moveXY(hero.pos.x + 8 * n, hero.pos.y)


riddle = hero.findNearestEnemy().riddle
trimmed = riddle.trim()
moveNSteps(riddle.length - trimmed.length)
hero.say("Gotcha!")
