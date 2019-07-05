## Code Combat Theory and Methods
___

### _Calling Methods_

The `hero` has actions or **methods** they can perform based on what gear they have.

The simplest case are the `moveUp`, `moveDown`, `moveLeft` and `moveRight` **methods**. To **call** a **method**, use `()` at the end of the **method**'s name.

**For example:**
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

### _Method Arguments_

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

___

### _Directional Movement_

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

___

### _Strings_

A `string` is a piece of **text** information. To tell the computer about a string, surround **text** with `"`.

For example,

```javascript
"Brak";  // This is a string!
"Hello, world";
"soldier";
```

Often times the use of a `string` is as an argument in a **method**.

For example,

```javascript
// The hero's attack method requires a name or unit:
hero.attack("Brak");
// The hero can say things to help debug:
hero.say("Bonjour: blue-marble.");
```

___

### _Attacking (Strings)_

Escaping the Dungeon of Kithgard is dangerous work. Sometimes a little muscle is required to break out!

By now, the `hero` has the `attack` method which is valuable when facing enemies toe-to-toe.

Check above an enemy's head for their name and **call** the `attack` method using the name **string** as an **argument**.

Munchkins in the Dungeon must be attacked **twice** to defeat them! You will need to call the method **twice**!

An example:

```javascript
hero.attack("Brak");
// You must attack twice to defeat munchkins:
hero.attack("Brak");
```

___

### _Comments_

Comments are a way for two programmers to communicate with each other. They are even useful for a single programmer to remember what they were doing to resume later!

In CodeCombat, we add comments to help you structure your code and give vital hints. Read them to understand what the objective is and what code you need to write to accomplish it.

In this level you will need to read the comments we provide to find the answer, to escape the prison cell!

Comments are pieces of information put in the code editor to help guide your coding.

It is extremely valuable to read each of the lines of code before jumping in!

We provide you with the instructions inside of levels themselves, just read it line by line!

For example, a level might start like this:

```javascript
// Move Up
// Attack Bob
// Say "I win!"
```

Then it is your job to fill in the blanks:

```javascript
// Move Up
hero.moveUp();
// Attack Bob
hero.attack("Bob");
// Say "I win!"
hero.say("I win!");
```

___

### _Say/Speaking_

The `hero` always has access to the `say` method. This creates a speech bubble above the `hero`'s head saying whatever is inside.

In certain levels this is a requirement! But it can be a useful debugging tool.

```python
hero.say("Let me out!")
hero.say("Kazaam!")
hero.say("I'm here now.")
```

___


### _Looping (While-True)_

Sometimes a certain piece of code needs to be repeated **forever**! Dodging **fireballs** or escaping a long **maze** are two of many use cases! A `while-true` loop can do this!

A `while-true` loop could be considered a **container** of your code that repeats it over and over.

With this concept, it is important to match the **syntax** closely, as this is what the computer reads to perform it.

For example:

```javascript
while (true) {  // Notice while, true and {
    hero.moveRight();  // Notice the indentation
    hero.moveUp();  // Notice the indentation
}  // Notice the }
```

Code outside of the `while-true` loop will **NEVER** run!

Once you enter a `while-true` loop, no more code after will be ran!
An example:

```javascript
while (true) {
    // Everything between the { and } repeats!
    // Yes
}

// And code down here will NEVER run!
// The code will be stuck in while-true loop.
```

___

### _How To Use while-true Loops_

First, we start a loop with the `while` keyword. This tells your program **WHILE** something is true, repeat the **body** of the loop.

For now we want our loops to continue forever, so we'll use a **while-true loop**. Because true is always true! 

Don't worry about this true stuff too much for now. We'll explain it more later. Just remember that a **while-true loop** is a loop that never ends.

This is how you code a **while-true loop**:

```javascript
// Start the while-true loop with "while (true) {"
// Anything between the { and } is considered INSIDE the loop

while (true) {
    hero.moveRight();
    hero.moveLeft();
}

hero.say("This line is not inside the loop!");

// Tip: the indention (spacec at the start of the lines) is optional
// in javaScript (but not in Python), but it makes your code easier to read!
```

> _Tip: You can put whatever you want inside a while-true loop! But for this level, we only need to repeat two commands: `moveRight()` and `moveLeft()`._

___

### _Code Before While_

Code cannot be added after a `while-true` loop, but there can be code that is executed before a `while-true`.

This is because a **programm** that tells the `hero` what to do reads the lines one-by-one.
It will only get "stuck" in a `while-true` loop once it reaches it.

For example:

```javascript
hero.moveUp();     // This code happens first
hero.moveRight();  // This line happens second

while (true) {     // This line happens third, starting the loop
    hero.attack("Burt");  // This line happens fourth, fifth, sixth etc.
}

hero.say("I'm free!");  // This line NEVER happens
```

___

### _Code Limits_

Some levels have a strict amount of lines of code you're required to write!

If you find yourself going over the limit, consider using a `while-true` loop to shorten your code.

For example:

```javascript
hero.moveRight();
hero.moveUp();
hero.moveRight();
hero.moveUp();
hero.moveRight();
hero.moveUp();
```

Becomes:

```javascript
while (true) {
    hero.moveRight();
    hero.moveUp();
}
```

___

### _Variables_

A _variable_ lets you hold on to a value for later. Some of those values are **strings** like names or phrases.

```javascript
var phrase = "This is a phrase";
hero.say(phrase);
```

A _variable_ is a way of holding on to a **value** so you can use it any time. The value of a variable can be a string, a number, or almost anything else.

Use the equals sign (`=`) to _set_ the value of a variable:

```javascript
var phrase = "This is a phrase";
```

Once it's set, you can use the variable anywhere in your code that you would use the value it holds.

```javascript
hero.say(phrase);  // Hero says "This is a phrase"
```

Note that a variable is _not_ a string, so you don't put quotes around it.

___

### _Variables (simple)_

`variables` are a way of storing information to use over and over.

`variables` are made up a **name** and an `=`. The `=` (**equals**) assigns the variable information to the **name**.

```javascript
// JavaScript must DECLARE variables using var (or let in ES5+)
var boop = "Snoot";
// Read as: create a variable named boop and set it equal to "Snoot"
// Now boop can be used in place of "Snoot" anythere in your code.
```

Further,

```javascript
var enemy1 = "Kratt";  // enemy1 now stores "Kratt"
hero.attack("Kratt");  // Is the same as:
hero.attack(enemy1);   // this!
```

`variables` **names** are **NOT** linked to their content at all! A `variable` can have **ANY name**!

Example:

```javascript
var hello = "Kratt";
var kratt = "Kratt";
var dance = "Kratt";  // hello, kratt and dance all are the same thing!

hero.attack(hello);
hero.attack(kratt);
hero.attack(dance);
```

___

### _Finding Nearby Enemies_

With glasses, the `hero` has access to the `findNearestEnemy` **method**.

But, the interesting thing about this **method** is that it **returns** something! It returns the nearest enemy to the `hero`.

The **method** on it's own isn't too useful. However when combined with a `variable`, it can be used to find any nearby enemy and attack them!

```javascript
hero.findNearestEnemy();  // This find nearest enemy, but doesn't store it anywhere!
var enemy = hero.findNearestEnemy();  // Now there is a variable to attack!

hero.attack(enemy);
```

___

### _Attack Nearby Enemies_

The `attack` **method** can be used to target enemy units, as well!

If the hero knows the name of the enemy:

```javascript
hero.attack("name of the enemy");
```

If the `hero` doesn't know the enemy's name, passing in a **reference** to the unit allows the `hero` to `attack` them.

```javascript
var foe = hero.findNearestEnemy();  // Set foe to a nearby enemy.
hero.attack(foe);  // Attack the enemy in the foe variable.
```

___

### _Multiple Arguments_

Some **methods** can take multiple **arguments**!

To insert multiple **arguments** into a **method**, include `,` between each of the **arguments**.

**Methods** like `buildXY` require a very strict order for their **arguments** so be sure to check for examples and read the guide.

```javascript
// buildXY takes 3 arguments!
// That means you need 2 comas to separate all 3 arguments.
hero.buildXY("fence", 20, 20);
hero.buildXY("fire-trap", 40, 40);
```

___

### _Building Defenses_

When the `hero` has a **hummer**, they can build defenses like `"fence"`s and `"fire-trap"`s.

However, the `hero` need to know the exact **coordinate** location of where to build! That is why the **method** is called `buildXY`, because it needs an `x` and `y` position.

Mouse-over the level map and after a second the **coordinates** will appear. Use this to guide where to `buildXY`.

The **arguments** in order are:
+ item *type* as a `string` such as `"fence"` and `"fire-trap"`.
+ item position `x`, which is always a number.
+ item position `y`, which is always a number.

For example:

```javascript
hero.buildXY("fence", 20, 20);
```

___

### _X, Y Coordinates_

A position on the game map is represented as two numbers: `x` and `y` coordinates.

`x` represents the **right-left** (horizontal) direction.

`y` represents the **up-down** (vertical) direction.

Moving in the **right** direction, the `x` number **increases**. Moving in the **left** direction, the `x` number **decreases**.

Moving in the **up** direction, the `y` number **increases**. Moving in the **down** direction, the `y` number **decreases**.

The bottom left corner of the map is `0, 0` (**x** is zero, **y** is zero).

___
