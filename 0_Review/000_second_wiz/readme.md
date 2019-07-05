## _Secondary - Wizard_

___


### _Druid_

___

#### _BOOK OF LIFE I_

Grants Regen, which heals 12 hit points per second for 5 seconds with a 7.5 second cooldown.

![](img/life1.png)

##### _`hero.canCast(spell [, target])`_ method

Whether the given spell is ready. If a target is specified, also checks whether the target can be affected.

**Example:**

```javascript
hero.canCast("drain-life", hero.findNearestEnemy());
```

**Required Parameters:**
+ `spell`: `string` (ex. `"drain-life"`) - _The name of the spell to check_

**Optional Parameters:**
+ `target`: `object` (ex. `hero.findNearestEnemy()`) - _The unit to check spell efficacy against_

**Returns:**
+ `boolean`

##### _`hero.cast(spell, target)`_ method

Cast a spell at a target. Use `canCast` to see whether the spell is ready, and look at `spellNames` to see which spells are available.

**Example:**

```javascript
hero.cast("drain-life", hero.findNearestEnemy());
```

**Required Parameters:**
+ `spell`: `string` (ex. `"drain-life"`) - _The name of the spell to cast_
+ `target`: `object` (ex. `hero.findNearestEnemy()`) - _The unit to cast spell on_

##### _`hero.cast("regen", target)`_ method

Casts a `"regen"` spell on `target` if within `30m`, giving the target an extra `2.4` HP every `0.2s` for `5` seconds.

**Level 1 Stats:**
+ Name: `"regen"`
+ Regen: `2.4/0.2s` (`12/s`)
+ Duration: `5s`
+ Range: `30m`
+ Time: `0.75s`
+ Cooldown: `7.5s`

**Example:**

```javascript
hero.cast("regen", hero);
```

**Required Parameters:**
+ `target`: `object` (ex. `hero`) - _The target to regenerate_


##### _`hero.spellNames`_ property

The names of the spells this hero can cast.

___

#### _BOOK OF LIFE II_

Grants Shrink, which halves a target's health and doubles its speed for 5 seconds with a cooldown of 7.5 seconds. Increases Regen to restore 17.5 health per second.

![](img/life2.png)

+ `hero.canCast(spell [, target])`
+ `hero.cast(spell, target)`
+ `hero.cast("regen", target)`
+ `hero.spellNames`

##### _`hero.cast("shrink", target)`_ method

Casts a `"shrink"` spell on `target` if within `spells.shrink.rangem`, causing shrinkage, faster movement by a factor of `spells.shrink.speedFactor`, and weaker attacks by a factor of `spells.shrink.healthFactor` for `spells.shrink.duration` seconds.


##### _`hero.spells`_ property

Which spells this hero can cast.

___

#### _BOOK OF LIFE III_

Grants Grow, which doubles a target's health and halves its speed for 5 seconds with a 7.5 second cooldown. Increases Regen's healing to 36 hit points per second. Lowers Shrink's cooldown to 3.7 seconds.

![](img/life3.png)

+ `hero.canCast(spell [, target])`
+ `hero.cast(spell, target)`
+ `hero.cast("regen", target)`
+ `hero.cast("shrink", target)`
+ `hero.spellNames`
+ `hero.spells`

##### _`hero.cast("grow", target)`_ method

Casts a `"grow"` spell on `target` if within `spells.grow.rangem`, causing growth, slower movement by a factor of `spells.grow.speedFactor`; and greater health and stronger attacks by a factor of `spells.grow.healthFactor` for `spells.grow.duration seconds`.

___

#### _BOOK OF LIFE IV_

Grants Time Warp. Increases Regeneration to 51.5 hit points per second. Reduces the Shrink and Grow cooldowns to 2.6 seconds.

![](img/life4.png)

+ `hero.canCast(spell [, target])`
+ `hero.cast(spell, target)`
+ `hero.cast("grow", target)`
+ `hero.cast("regen", target)`
+ `hero.cast("shrink", target)`
+ `hero.spellNames`
+ `hero.spells`

##### _`hero.cast("time-warp")`_ method

Casts a mighty `'time-warp'` spell, which adjusts the speed of all units (including the `hero` and any `missiles`) caught within `spells.time-warp.radiusm` by a factor of `spells.time-warp.factor` for `spells.time-warp.durations`.

___

#### _BOOK OF LIFE V_

Enables Dispel. Increases Regen to 101 hit points per second. Reduces Grow and Shrink cooldown times to 1.3 seconds.

![](img/Life5.png)

+ `hero.canCast(spell [, target])`
+ `hero.cast(spell, target)`
+ `hero.cast("grow", target)`
+ `hero.cast("regen", target)`
+ `hero.cast("shrink", target)`
+ `hero.cast("time-warp")`
+ `hero.spellNames`
+ `hero.spells`

##### _`hero.cast("dispel", target)`_ method

Casts a `"dispel"` spell on `target` if within `spells.dispel.rangem`, dispeling all effects.

___


### _Elemental_

___

#### _ELEMENTAL CODEX I_

Grants Haste, which increases speed 2x for 4.5 seconds with a 10 second cooldown.

![](img/elemet1.png)

+ `hero.canCast(spell [, target])`
+ `hero.cast(spell, target)`
+ `hero.spellNames`

##### _`hero.cast("haste", target)`_ method

Casts a `"haste"` spell on `target` if within 30m, causing faster movement and attack speed by a factor of `2` for `5` seconds.

**Level 1 Stats:**
+ Name: `"haste"`
+ Speed: `+ 100%`
+ Duration: `5s`
+ Range: `30m`
+ Time: `0.5s`
+ Cooldown: `10s`

**Example:**

```javascript
hero.cast("haste", hero);
```

**Required Parameters:**
+ `target`: `object` (ex. `hero`) - _The target to haste_

___

#### _ELEMENTAL CODEX II_

Grants Slow, which reduces a target's speed by 50% for 5 seconds with a 10 second cooldown.

![](img/elemet2.png)

+ `hero.canCast(spell [, target])`
+ `hero.cast(spell, target)`
+ `hero.cast("haste", target)`
+ `hero.spellNames`
+ `hero.spells`

##### _`hero.cast("slow", target)`_ method

Casts a `"slow"` spell on target if within `spells.slow.rangem`, slowing down its movement and attack (and all passage of time) by a factor of `spells.slow.factor` for `spells.slow.duration seconds`.

___

#### _ELEMENTAL CODEX III_

Grants Shockwave, which deals 50 damage to enemies in a 20 meter radius around the target and knocks them back. Shockwave has a 15 second cooldown.

![](img/elemet3.png)

+ `hero.canCast(spell [, target])`
+ `hero.cast(spell, target)`
+ `hero.cast("haste", target)`
+ `hero.cast("slow", target)`
+ `hero.spellNames`
+ `hero.spells`

##### _`hero.cast("shockwave", target)`_ method

Casts a `"shockwave"` spell on `target` if within `spells.shockwave.rangem`, blasting it back away from the caster and dealing up to `spells.shockwave.damage` to units caught in the epicenter.

___

#### _ELEMENTAL CODEX IV_

Grants Swap. Increases Shockwave's damage to 79 with increased knockback.

![](img/elemet4.png)

+ `hero.canCast(spell [, target])`
+ `hero.cast(spell, target)`
+ `hero.cast("haste", target)`
+ `hero.cast("shockwave", target)`
+ `hero.cast("slow", target)`
+ `hero.spellNames`
+ `hero.spells`

##### _`hero.cast("swap", target)`_ method

Casts a `"swap"` spell on `target` if within `spells.swap.rangem`, swapping its position with yours.

___

#### _ELEMENTAL CODEX V_

Grants Flame Armor. Increases Shockwave's damage to 125 with increased knockback.

![](img/elemet5.png)

+ `hero.canCast(spell [, target])`
+ `hero.cast(spell, target)`
+ `hero.cast("haste", target)`
+ `hero.cast("shockwave", target)`
+ `hero.cast("slow", target)`
+ `hero.cast("swap", target)`
+ `hero.spellNames`
+ `hero.spells`

##### _`hero.cast("flame-armor", target)`_ method

Casts a `"flame-armor"` spell on target if within `spells['flame-armor'].rangem`, granting `spells['flame-armor'].healthFactorx` health and `maxHealth` for `spells['flame-armor'].duration` seconds. During that time, any enemy that attacks with a melee weapon takes `spells['flame-armor'].damage` damage each time they attack.

___


### _Necromance_

___

#### _UNHOLY TOME I_

Grants Drain Life, which drains 8 DPS from a target up to 15 meters away.

![](img/unholy1.png)

+ `hero.canCast(spell [, target])`
+ `hero.cast(spell, target)`
+ `hero.spellNames`

##### _`hero.cast("drain-life", target)`_ method

Casts a `"drain-life"` spell on `target` if within `15m`, stealing `6` health from it and giving it to the hero.

**Level 5 Stats:**
+ Name: `"drain-life""`
+ Damage: `57.1`
+ Heals: `57.1`
+ Range: `15m`
+ Time: `0.75s`
+ Cooldown: --

**Example:**

```javascript
hero.cast("drain-life", hero.findNearestEnemy());
```

**Required Parameters:**
+ `target`: `object` (ex. `hero.findNearestEnemy()`) - _The target on which to cast "drain-life"_

___

#### _UNHOLY TOME II_

Grants Fear, which causes a target enemy to flee for 5 seconds with a 10 second cooldown. Drain Life increased to 18 DPS.

![](img/unholy2.png)

+ `hero.canCast(spell [, target])`
+ `hero.cast(spell, target)`
+ `hero.cast("drain-life", target)`
+ `hero.spellNames`
+ `hero.spells`

##### _`hero.cast("fear", target)`_ method

Casts a `"fear"` spell on `target` if within 25m, causing it to run in terror for 5 seconds.

**Level 5 Stats:**
+ Name: `"fear""`
+ Duration: `5s`
+ Range: `25m`
+ Time: `0.75s`
+ Cooldown: `10s`

**Example:**

```javascript
hero.cast("fear", hero.findNearestEnemy());
```

**Required Parameters:**
+ `target`: `object` (ex. `hero.findNearestEnemy()`) - _The target on which to cast "fear"_

___

#### _UNHOLY TOME III_

Enables Raise-Dead, which raises 100 power worth of dead units at half health for 10 seconds at random in a 20 meter range. Drain Life DPS increased to 24.

![](img/unholy3.png)

+ `hero.canCast(spell [, target])`
+ `hero.cast(spell, target)`
+ `hero.cast("drain-life", target)`
+ `hero.cast("fear", target)`
+ `hero.spellNames`
+ `hero.spells`

##### _`hero.cast("raise-dead")`_ method

Casts a `'raise-dead'` spell, bringing back `1200` power worth of corpses back to life as zombies for `10` at half health and speed. The zombies are chosen randomly from corpses within `20m`.

**Level 5 Stats:**
+ Name: `"raise-dead""`
+ Power: `1200`
+ Radius: `20m`
+ Duration: `10s`
+ Time: `0.5s`
+ Cooldown: `10s`

**Example:**

```javascript
if (hero.canCast('raise-dead'))
    hero.cast('raise-dead');
```

##### _`hero.findCorpses()`_ method

Returns an `array` of all dead units (friend and foe alike).

___

#### _UNHOLY TOME IV_

Grants Poison Cloud, which deals 30 DPS for 5s in a 10 meter range and has a 15-second cooldown. Increases Drain Life DPS to 45. Increases the total power of targets Raise Dead can affect.

![](img/unholy4.png)

+ `hero.canCast(spell [, target])`
+ `hero.cast(spell, target)`
+ `hero.cast("drain-life", target)`
+ `hero.cast("fear", target)`
+ `hero.cast("raise-dead")`
+ `hero.findCorpses()`
+ `hero.spellNames`
+ `hero.spells`

##### _`hero.cast("poison-cloud", target)`_ method

Casts a `"poison-cloud"` spell on `target` if within `30m`, poisoning every unit within a radius of `10`.

**Level 5 Stats:**
+ Name: `"poison-cloud""`
+ Damage: `50/s`
+ Duration: `5s`
+ Range: `30m`
+ Radius: `10m`
+ Time: `0.75s`
+ Cooldown: `15s`

**Example:**

```javascript
hero.cast("poison-cloud", hero.findNearestEnemy());
```

**Required Parameters:**
+ `target`: `object` (ex. `hero.findNearestEnemy()`) - _The target unit or position to poison_

___

#### _UNHOLY TOME V_

Grants Summon Undead. Increases Drain Life DPS to 76. Increases the number of targets Raise Dead affects. Increases Poison Cloud DPS to 50.

![](img/unholy5.png)

+ `hero.canCast(spell [, target])`
+ `hero.cast(spell, target)`
+ `hero.cast("drain-life", target)`
+ `hero.cast("fear", target)`
+ `hero.cast("poison-cloud", target)`
+ `hero.cast("raise-dead")`
+ `hero.findCorpses()`
+ `hero.spellNames`
+ `hero.spells`

##### _`hero.cast("summon-undead")`_ method

Casts a `"summon-undead"` spell to summon `2` undead minions.

**Level 5 Stats:**
+ Name: `"summon-undead""`
+ Count: `2`
+ Time: `0.75s`
+ Cooldown: `7.5s`

**Example:**

```javascript
hero.cast("summon-undead");
```

___
