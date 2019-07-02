### _Border Patrol_

##### _Legend says:_
> Adding borders to elements helps separate them from other elements

##### _Goals:_
+ _Give `<img>` tags a border_
+ _Give `<ol>` tags a border_
+ _Give `<li>` tags a border_

##### _Topics:_
+ None

##### _Solutions:_
+ **[HTML](Border_Patrol.html)**

##### _Rewards:_
+ 60  xp
+ 20 gems

##### _Victory words:_
+ _WE NEED TO ESTABLISH SOME BOUNDARIES._

___

##### _Border_

`border` is used to put a nice looking border around one's elements.

```css
div {
    border: 3px double purple;
}
```

The `border` shorthand property is made up of 3 sub-properties - `border-style`, `border-width` and `border-color`. These three control the shape, size, and color of borders you will put around your elements.

`border`s go around elements and separate content from outside elements.

```css
img {
    border-style: dotted;
    border-color: green;
    border-width: 2px;
}

div {
    border: 1px solid black;
}
```

###### _`border` attribute_

The `border` property is a shorthand property for `border-style`, `border-width` and `border-color`.

The property values can be in any order.

**Example:**

```css
<style>
    div {
        border: 2px dotted green;
    }
</style>
```

###### _`border-style` attribute_

The `border-style` property defines if a border should be displayed around an element. Suitable values are `solid`, `dotted`, `dashed`.

**Example:**

```css
<style>
    div {
        border-style: dashed;
    }
</style>
```

###### _`border-width` attribute_

The `border-width` property controls how wide the border will be.

**Example:**

```css
<style>
    div {
        border-style: dotted;
        border-width: 2px;
    }
</style>
```

###### _`border-color` attribute_

The `border-color` property sets the color of the border, when one is defined with `border-style`.

**Example:**

```css
<style>
    div {
        border-style: solid;
        border-color: red;
    }
</style>
```
