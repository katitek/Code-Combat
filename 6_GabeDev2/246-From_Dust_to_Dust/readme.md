### _From Dust to Dust_

##### _Legend says:_
> You can create game objects. However you can destroy or ruin them.

##### _Goals:_
+ _Block the forest passages and clear them later_
+ _Defeat 2 ogre generators_
+ _Beat the game_

##### _Topics:_
+ **Basic Syntax**
+ **Event Data**

##### _Solutions:_
+ **[JavaScript](fromDustToDust.js)**

##### _Rewards:_
+ 30 xp
+ 30 gems

##### _Victory words:_
+ _NOW I AM BECOME GAME MASTER, THE DESTROYER OF WORLDS._

___

##### _Defeat and Destroy_

The most time we `spawn` new objects for games. However, sometimes we need to remove them. There are two ways to do it:
+ units or attackable objects (ex. `generator`) can be "killed" with the method `.defeat()`.
+ any objects can be removed from the game scene with the method `.destroy()`.

```python
# Create and defeat a munchkin.
munchkin = game.spawnXY("munchkin", 10, 10)
munchkin.defeat() # We can see the defeated ogre.
# Create and remove a scout
scout = game.spawnXY("munchkin", 20, 20)
scout.destroy() # Nothing here
```

`defeat()` and `destroy()` are similar methods, however there is huge difference between them.

`defeat()` is like `unit.health = 0` and can be applied only to units or attackable objects like `"generator"`. Also the "defeated" object remains in the game scene. Plus it increases `game.defeated` counter for enemy units. You can use it for "restricted zones", ruin some objects on events and so on.

```javascript
var generator = game.spawnXY("generator", 40, 34);

while (true) {
    if (game.time == 10) {
        generator.defeat();   // It's ruined and we see some remained stones.
        player.say("I haven't touched it. It was broken itself.");
    }
}
```

`destroy()` removes an object from the game scene and can be used for anything. Especially it useful for obstacles, because they don't have `health` and can't be `defeat`ed. You can remove obstacles for some events, for example, clear forest passage in this level. There are more usages for that method which we will see later.

```javascript
var potion = game.spawnXY("potion", 40, 34);

while (true) {
    if (game.time == 10) {
        potion.destroy();  // Just an empty space.
        player.say("Where is it? It was here just a second ago.");
    }
}
```
