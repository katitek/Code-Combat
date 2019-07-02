### _Eventful Selectors_

##### _Legend says:_
> Use a single event listener to act on multiple elements.

##### _Goals:_
+ _Bold one of the `h2`s_
+ _Strike-through at least 3 list items_

##### _Topics:_
+ None

##### _Solutions:_
+ **[HTML](Eventful_Selectors.html)**

##### _Rewards:_
+ 60  xp
+ 20 gems

##### _Victory words:_
+ _THIS IS SOME POWERFUL CODE!_

___

##### _Hints_

When an event function is called, it adds a variabled called `this`.

When used with the jQuery object, it selects the specific element that it was called on.


###### _`font-weight` attribute_

The `font-weight` property sets the weight of the font. It can make it `bold` (thicker), or `light` (thinner).

**Example:**

```html
<style>
    .thickText {
        font-weight:thick;
    }
</style>
``` 


###### _`cursor` attribute_

The `cursor` property changes what the cursor looks like when mousing over certain elements. Some `<div>`s are clickable, so they are given the `pointer` property.

**Example:**

```html
<style>
    .selectable {
        cursor: pointer;
    }
</style>
``` 

___

##### _$(this)_

`$(this)` returns a callback function's current target.

Use it to find which specific element was selected when applying the same event listener to multiple elements.

**Example:**

```html
<button>A</button>
<button>B</button>
<button>C</button>
<script>
    var button = $("button");
    button.on("click", hideClicked);
    function hideClicked() {
        var target = $(this); // This sets 'target' to the clicked button.
        target.hide(); // This hides that specific button, not all the buttons.
    }
</script>
```

**Required Parameters:**
+ `this`: `keyword` (ex. `this`). _This is the context for the function_

`this` is a special keyword in JavaScript. Inside of the jQuery function, `$` it selects an event function's specific target.

`$(this)` is a very powerful tool when using events!


```javascript
function hideClicked() {
    var element = $(this);  // This is the specific <li>
    element.hide();  // This hides the specific <li>
}

var listItem = $("li");
listItem.on("click", hideClicked);
```

###### _`addClass` and `removeClass`_

`addClass` adds a specific CSS class to an element.

`removeClass` removes a specific CSS class from an element.

**Example:**

```html
<div id="mainElement">
    I contain information!
</div>

<div id="secondElement" class="strike">
    I contain information!
</div>

<style>
    .strike {
        text-decoration: line-through;
    }
</style>

<script>
    // Add the "strike" class to the mainElement div.
    var targetToAdd = $("#mainElement");
    targetToAdd.addClass("strike");

    // Remove the "strike" class from the secondElement div
    var targetToRemove = $("#secondElement");
    targetToRemove.removeClass("strike");
</script>
```

**Required Parameters:**
+ `className`: `string` (ex. `"selected"`). _A string of a CSS class name_

###### _`siblings`_

`siblings` returns a jQuery object of all neighboring elements. An element is a sibling if it is nested at the same level as the selected element.

**Example:**

```html
<ul>
    <li id="firstElement">One</li>
    <li>Dos</li>
    <li>Drei</li>
</ul>
<script>
    // Hide all elements but One.
    var target = $("#firstElement");
    target.siblings().hide();
</script>
```

**Optional Parameters:**
+ `selector`: `string` (ex. `".className"`). _A string to only select elements matching the CSS selector_
