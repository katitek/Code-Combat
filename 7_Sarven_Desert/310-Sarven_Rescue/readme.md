## _Sarven Rescue_

#### _Legend says:_
> Rescue the captured peasant and return her to the village. _Created by player **Kevin Holland**. This is an optional challenge level._

#### _Goals:_
+ _Lead the peasant to her village_
+ _Bonus: Loot the treasure chest_
+ _Bonus: Knock out the sand yak_

#### _Topics:_
+ None

#### _Solutions:_
+ **[JavaScript](sarvenResque.js)** _warrior_
+ **[Python](sarven_rescue.py)** _wizard_

#### _Rewards:_
+ 150-375 xp
+ 102-254 gems

#### _Victory words:_
+ _DEFINITELY A GREAT PLACE FOR A VILLAGE: RIGHT NEXT TO A BANDIT CAMP. LOOTED THE TREASURE CHEST. KILLED THE YAK, TOO._

___

### _HINTS_

![](img/continuous_alchemy.jpeg)

Use the `continue` statement to stop the current iteration of a loop, and start over at the beginning of the next one.

```javascript
while(true) {
    if(!enemy) {
        continue;
    }

    hero.say("I see an enemy!");
}
```

Use an `if`-sstatement to check if the potion's type is `"poison"`

```javascript
if (item.type == "poison") {

}
```

If the item type is poison: `continue` through the loop.

Remember that `continue` skips the rest of the commands in a loop and returns to the back to the start of a loop.

```javascript
continue;
```

If there is an enemy, and an item, and the item type isn't poison, move to the bottle of water!

```javascript
hero.moveXY(44, 35);
```

Be sure to move back to the safety-X so Omarn doesn't throw a potion on your head!

___

This level will teach you the uses of the `continue` statement. When the program points to a `continue` statement, the rest of the code in the current iteration of the loop is discarded and the next cycle of the loop begins.

Omarn Brewstone is an important man. It is important to check that there is an enemy to ambush, and, there are no other items on the field.

Be sure to check the `item.type` as to not accidentally drink some poison!

Continue can be used to skip blocks of code until a condition is met:

```javascript
while (true) {
    if (!enemy) {
        continue;
    }

    hero.say("I see an enemy!");
}
```

Do not let the Munchkin reach the Water! The desert dehydrated Ogres will become powerful if they're given the opportunity to quench their thirst.

___
