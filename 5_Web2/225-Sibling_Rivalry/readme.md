### _Sibling Rivalry_

##### _Legend says:_
> Select an element's neighbors to control the neighborhood!

##### _Goals:_
+ _Select one image_
+ _Select one div_

##### _Topics:_
+ None

##### _Solutions:_
+ **[HTML](Sibling_Rivalry.html)**

##### _Rewards:_
+ 60  xp
+ 20 gems

##### _Victory words:_
+ _IN THIS CASE, THERE CAN ONLY BE ONE! HIGHLIGHTED ONE, THAT IS._

___

##### _Hints_

The `siblings()` function returns a list of neighboring elements.

```javascript
var neighbor = $(this).siblings();
```

###### _`opacity` attribute_

The `opacity` property controls how transparent an element is. A value of 0 shows nothing. A value of 1 shows everything.  With 1 think 100% visible. A value of 0.50 will thus be halfway transparent.

**Example:**

```html
<style>
    .muted {
        /* Hide the element slightly. */
        opacity: 0.25;
    }
</style>
```

___

###### _Siblings_

The `siblings()` function finds all neighboring elements to the element it was called on. An element is 'neighboring' if they are nested at the same depth in the HTML document.

`siblings()` is useful when trying to find a programmatically-found element's neighbors.

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
