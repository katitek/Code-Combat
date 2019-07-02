### _Query Confirmed_

##### _Legend says:_
> Get introduced to the basics of the web's most popular library: jQuery.

##### _Goals:_
+ _Change the image's width_

##### _Topics:_
+ **Basic HTML**
+ **Basic CSS**
+ **Basic Web Scripting**

##### _Solutions:_
+ **[HTML](query_confirmed.html)**

##### _Rewards:_
+ 60  xp
+ 20 gems

##### _Victory words:_
+ _THE WONDERS OF WEB SCRIPTING!_

___

##### _Hints_

Change the size of the image, using the `css()` jQuery function.

```javascript
var image = $("#theImage");  // Selects the element with id "theImage"
image.css("background-color", "red");  // Sets the image's background color to red
```

___

###### _Script tag_

The `<script>` tag is for writing JavaScript to modify the page. It is possible to add event listeners and modify the webpage dynamically to make the page interactive.

**Example:**

```html
<script>
    // Set the text color for all divs to blue.
    var divElement = $("div");
    divElement.css("color", "blue");
</script>
```

___

##### _jQuery_

CodeCombat Web Development uses **jQuery** to make web-based JavaScript easier. **jQuery** introduces 2 new functions: `jQuery()` and `$()`. They both do the exact same thing, but the `$()` was added to simplify things. `$` is no different from `enemy` or `moveLeft` to JavaScript! CodeCombat uses the `$()` because it is easier to type, and is iconic for the _jQuery_ library.


###### _$_

`$` is the `jQuery` function. It returns a jQuery object baesd on the `queryString` used.

**Example:**

```html
<button id="theButton">Click me!</button>
<div class="blogPost">
    <h3>Today</h3>
    <p>
        I went to the beach.
    </p>
</div>
<script>
    var button = $("#theButton"); // Set "button" to the element with the id "theButton".
    var blogPosts = $(".blogPost"); // Set "blogPosts" to an array of all elements with class "blogPost".
    var paragraphs = $("p"); // Set "paragraphs" to an array of all "p" elements.
</script>
```

**Required Parameters:**
+ `queryString`: `string` (ex. `".selected"`). _This is a CSS selector_


`$` is a function, so remember to call it using parenthesis `(` and `)`. The most common `argument` to pass in is a `"string"`. Specifically, `$()` is expecting a CSS-style _selector_.

```javascript
var image = $("#theImage");

// The "image" variable is now set to a special jQuery object.
// "image" now has a lot of useful methods to help with manipulating the element!

// For example, the "css()" function takes a property name and a value and changes that element's CSS!
image.css("background-color", "red");
```


###### _css function_

`css` is used to get and set the CSS rules of a jQuery object.

**Example:**

```html
<div id="header">
    <h1>Welcome!</h1>
</div>
<script>
    // Get the element h1 header's current background-color.
    var color = $("h1").css("background-color")
    
    // Set the element h1 header's background-color to "red".
    $("h1").css("background-color", "red")
</script>
```

**Required Parameters:**
+ `propertyName`: `string` (ex. `"background-color"`). _This is a CSS property name_

**Optional Parameters:**
+ `value`: `string` (ex. `"red"`). _If included, this is what to set the CSS property to._
