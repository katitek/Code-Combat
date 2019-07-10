// Your pet should translate commands.
 
function onHear(event) {
    // The message the pet heard is in event.message
    var message = event.message;
    // If the message is "North":
    if (message == "North") {
        // The pet says "Htron".
        pet.say("Htron");
    }
    // If the message is "South":
    if (message == "South") {
        // The pet says "Htuos".
        pet.say("Htuos");
    }
    // If the message is "East":
    if (message == "East") {
        // The pet says "Tsae".
        pet.say("Tsae");
    }
        
}

// Assign the event handler.
pet.on("hear", onHear);

while (true) {
    var enemy = hero.findNearestEnemy();
    // Don't attack Brawlers.
    if (enemy && enemy.type != "brawler") {
        hero.attack(enemy);
    }
}
