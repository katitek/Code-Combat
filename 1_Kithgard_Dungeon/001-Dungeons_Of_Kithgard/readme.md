### _So, here we are. On the start line of new adventure._. It's doesn't matter which hero you'll choose to play so far - they're all the same just looks different.

##### _Legend says:_
> Grab the gem and escape the dungeon but don’t run into anything else.
In this level, you’ll learn basic movements for your hero.

##### _Goals:_
+ _Avoid the spikes_
+ _Collect the gem_
+ _**Bonus**: Clean code (no warnings)_

##### _Topics:_
+ **Basic Sintax**

##### _Items we've got (- or need):_
+ Simple boots
+ _Optional: Elemental codex 1+_

![](img/simple-boots.jpg) 

##### _Solutions:_
+ **[JavaScript](dungeonsOfKithgard.js)**
+ **[Python](dungeons_of_kithgard.py)**

##### _Rewards:_
+ 10-15 xp
+ 17-26 gems
+ Leather Belt (+5 max HP)

![](img/leather-belt.jpg)

##### _Victory words:_
+ _YOU COMPLETED DUNGEONS OF KITHGARD!_

___

##### _Hints_
The journey begins! To escape the dungeon of Kithgard, your hero has to move. You tell them where to move by writing _code_. 

Type a code into the editor to give your hero instructions. Heroes read and execute these instructions themselves when told to. To direct your hero, refer to them in code with `hero`.

Now that you know how to call on your hero, instruct them to move with direction commands, moveDown and moveRight. Write it like this:
```javascript
hero.moveDown();
hero.moveRight();
```
To pass this level, move right, down, and right to grab the gem. Remember, you only need three lines of code.

![](img/dungeons-of-kithgard.jpeg)

The code you write here is very similar to the code you might write to tell a computer how to do all kinds of things, from playing music to displaying a web page. You're taking your first steps towards being a coder!

___

##### _Calling Methods_
The `hero` has actions or **methods** they can perform based on what gear they have.

The simplest case are the `moveUp`, `moveDown`, `moveLeft` and `moveRight` **methods**. To **call** a **method**, use `()` at the end of the **method**'s name.

For example:
```javascript
hero.moveRight();  // This tells the hero to move to the right.
hero.moveUp();
hero.moveLeft();
```

Note, the `hero` will do nothing if the `()` are executed!
```javascript
hero.moveDown;  // Nothing will happen!
```

___

##### _Directional Movement_
First level greets you with a brand new **_Simple boots_**. This equipment allows your hero to move using simple Up, Down, Left, Right commands.

In the Dungeon, the `hero` has access to the following **methods**:
+ `moveUp` - moves the hero up (north) a bit
+ `moveDown` - moves the hero down (south) a bit
+ `moveLeft` - moves the hero left (west) a bit
+ `moveRight` - moves the hero right (east) a bit

Use these to navigate the perilous passages!

> Remember! These methods are `hero` object methods. To use them you need to run it within an `hero` object, for example:
```javascript
hero.moveUp();
hero.moveRight();
hero.moveRight();
hero.moveDown();
```
