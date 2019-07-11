## _Stars_

___


**Table of Contents:**

* [Boss Star I](#boss-star-i)

___

### _Boss Star I_

This token of leadership lets you summon and command soldiers–as long as you have the gold.

![](img/star1.png)


#### `hero.costOf`

Returns the gold cost for the given build or summon type.

**Example:**
```javascript
hero.costOf("soldier");
```

**Required Parameters:**
+ `buildType`: `string` (ex. `"soldier"`) - _The type of unit to build_

**Returns:**
+ `number`


#### `hero.summon(summonType)`

Summons a friendly unit for you to command, if you have enough gold.

**Example:**
```javascript
hero.summon("soldier");
```

**Required Parameters:**
+ `summonType`: `string` (ex. `"soldier"`) - _The type of unit to summon_


#### `hero.command()`

`command` allows you to call any of `commandableMethods` (ex. `['move', 'attack', 'defend']`) on allied minions. You can command minions of types in `commandableTypes` (ex. `['soldier', 'archer']`.

_(you may not be able to summon all of these types)_

**Example:**
```javascript
var friend = hero.getNearestFriend();
hero.command(friend, 'move', hero.pos);
```

**Required Parameters:**
+ `summonType`: `string` (ex. `"soldier"`) - _The type of unit to summon_


#### `hero.commandableTypes`

> `array`

These are all the allied minion types that you can command.

_(you may not be able to summon all of these types)_


#### `hero.commandableMethods`

> `array`

These are all the method names that you can call on allied minion units.

___
