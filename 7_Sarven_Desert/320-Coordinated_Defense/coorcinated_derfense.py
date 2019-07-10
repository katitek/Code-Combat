while True:
    enemies = hero.findEnemies()
    if enemies.length > 0:
        hero.attack(enemies[0])
        hero.moveXY(40, 20)
