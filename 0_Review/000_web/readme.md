## Web Development Theory and Methods by Code Combat
___

### _Events_

> _Because I don't really remember - Am I posted it before or not._

An **event** is something that happens in the game world.

For example, a `"spawn"` event happens when a unit is created (spawned). A `"hear"` event happens when a unit hears another unit `say()` something.

You can register a function as an **event handler** using the `on(eventType, eventHandler)` method.

An **event handler** function is run when the specified type of event happens:

```javascript
// Define an event handler function:
function onHear() {
    pet.say("I heard something!");
}

// Register onHear as an event handler for "hear" events on the pet object.
pet.on("hear", onHear);
```

___
