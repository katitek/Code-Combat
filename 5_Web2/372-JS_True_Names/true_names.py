hero.attack("Brak")
hero.attack("Treg")
item = hero.findNearestItem()
hero.moveXY(item.pos.x, item.pos.y)
