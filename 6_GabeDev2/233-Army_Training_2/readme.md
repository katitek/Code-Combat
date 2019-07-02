### _Army Training 2_

##### _Legend says:_
> Direct your army in combat!

##### _Goals:_
+ _Spawn 2 soldiers_
+ _Spawn 2 archers_
+ _Defeat the ogres_

##### _Topics:_
+ None

##### _Solutions:_
+ **[JavaScript](armyTraining2.js)**

##### _Rewards:_
+ 30 xp
+ 10 gems

##### _Victory words:_
+ _THEY UNDERESTIMATED YOUR TRAINING._

___

###### _Hints_

If you hace a lot of units, use `game.setActionFor(unitType, eventType, eventHandlerFunction)` to set actions for all of them at once!

```python
game.spawnXY("soldier", 30, 20)
game.spawnXY("soldier", 35, 20)
game.spawnXY("soldier", 40, 20)
game.spawnXY("soldier", 45, 20)

def lol(event):
    while True:
        unit = event.target
        unit.say("lol")

game.setActionFor("soldier", "spawn", lol)
```

Notice that your event handler function can define a parameter.

This parameter contains the `event` data.

You can use `event.target` to access the unit that this event is being run on (for example, your soldier).

```javascript
function soldierLogic(event) {
    var soldier = event.target;
    var enemy = soldier.findNearestEnemy();
}
```

###### _`game.setActionFor(type, event, handler)` method_

Sets an event handler on all units of a particular type, whether they are spawned before or after this command is executed.

**Example:**

```javascript
game.setActionFor("munchkin", "spawn", runAway);
game.setActionFor("soldier", "spawn", fightEnemies);
game.setActionFor("archer", "spawn", fightEnemies);
```

**Required Parameters:**
+ `type`: `string` (ex. `"soldier"`). _The type of unit to setActionFor_
+ `event`: `string` (ex. `"spawn"`). _The type of event_
+ `handler`: `function` (ex. `fightEnemiesd`). _The function that is called when the event is triggered_
