### _Forgetful Gemsmith (practice)_
#### First premium level.

##### _Legend says:_
> There are gems scattered all over the dungeons in Kithgard!

##### _Goals:_
+ _Your hero must survive_
+ _Collect all 4 gems_
+ _Get to the exit_
+ _**Bonus**: Clean code (no warnings)_
+ _**Bonus**: Under 9 statements_

##### _Topics:_
+ **Basic Sintax**
+ **Arguments**

##### _Items we've got (- or need):_
+ Simple boots
+ _Optional: Elemental codex 1+_

##### _Solutions:_
+ **[JavaScript](forgetfulGemsmith.js)**
+ **[Python](forgetful_gemsmith.py)**

##### _Rewards:_
+ 9-17 xp
+ 13-27 gems

___

##### _Hints_

Collect the gems by using your move commands!

```javascript
hero.moveDown();
hero.moveRight();
```

___

This one takes several commands, so make sure to use the autocomplete to write your code faster. You can type `r`, Enter to autocomplete a `moveRight()` command.

After you're done practicing simple movement with this level, it's time to learn `attack`-ing, so keep trying!

___

##### _Method Arguments_

No, not a fight with methods! But information that can be **passed** into a method to make it behave differently.

The **argument** is information included between the `(` and `)` when **calling** a function.

For example:

```javascript
hero.moveRight(2);  // The hero will move right twice!
```

There are methods that require **arguments** or else they won't know what to do!

Another example:

```javascript
hero.attack('Brak');  // The hero will attack Brak.

hero.attack();  // The hero doesn't know what to attack! This is an error!
```
