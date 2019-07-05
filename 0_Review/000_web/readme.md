## Web Development Theory and Methods by Code Combat

___


### Theory

___

#### _HTML Start/End Tags_

HTML has a few special `empty`tags, like `<br>`, but a majority of HTML tags require a `start` and `end` tag. Or, more commonly: `opening` and `closing` tags.

An `opening` tag is the one that tells the computer everything after it is `contained` within the rules of that tag. The `paragraph` element's `start` tag is `<p>`.

A `closing` tag tells the computer that it shouldn't apply any rules to the content after it. The `paragraph` element's `end` tag is `</p>`.

**Remember to close all tags, or your webpage will look weird!**

```html
<p>I am a standalone paragraph! I'm pretty neat.</p>
<p>I'm another paragraph, I'm cool too, I promise!</p>
```

Remember line-spacing doesn't matter to the computer! Using indentation and line breaks, you can make your HTML nice and easy to read. It'll get more messy in the future, so it's a good habit to practice now!

```html
<p>
    I'm still just a regular paragraph, nothing has changed.
</p>
<p>You can mix styles, as well! Depending on what feels like
    the best way.</p>
<p>
    You can even use the br-tag inside p-tags!
    <br>
    Look, I'm on another line, in a paragraph!
</p>
```

___

#### _Attributes_

`attributes` are pieces of information or data which is included inside of the HTML `tags` themselves. For example, `<img>` tags have a mandatory attribute called `src` which is the URL "source" for the image.

To add an `attribute` to an HTML tag, include it between the `<` and `>`. It must have a `=` and `"` surrounding the value assigned to that value. Not much different from creating a variable! But instead, you are setting the value for the `tag`.

```html
<img src=""/file/db/thang.type/52cee45a76ebd5196b00003a/portrait.png" />
```

___

#### _Cascading Style Sheets (CSS)_

Cascading Style Sheets, or CSS, is the web's way of formatting the various parts of a website.

To include special style rules, use the opening and closing `<style>` tag.

**Note: `<style>` is unlike other HTML tags! What you put between the two tags is different from other HTML tags!**

```html
<style>
/* This is the element selector. Use { and } to contain CSS rules */
p {
    /* The attribute name comes first, followed by value it should be set to. */
    color: red;

    /* Be sure to use a : between the name and value. Use a ; at the end! */
}

/* Selector */
div { /* Brackets { } */
    /* Attribute Name : Attribute Value ; */
    text-align: center;

    /* Note the : and ; */
}

img {
    width: 100px;
    height: 200px;
}
</style>
```

___

#### _Classes_

HTML and CSS make use of the idea of `classes`. A `class` is a way of grouping similar elements by giving them a repeatable name.

The `class` attribute is used to make styling elements easier. Assign the attribute to an element by including it inside an element's opening tag. Inside the `<style>` element, target specific classes using the `.` + `classname` CSS selector.

```html
<style>
    /* This sets all element with the "neat" class to the color : blue */

    .neat {
        color: blue;
    }
</style>

<!-- This <div> element has the "neat" class. -->
<div class="neat">
    <p>Hello, world!</p>
</div>
```

___

#### _ID Attribute_

The alternative to the CSS `class` is `id`. `id` attributes mark elements with a specific name to recall later. While a `class` can be repeated across multiple elements, and `id` is for **one** specific element. Think of it as an piece of identification like a school ID or driver's license.

```html
<style>
    #main {
        color: orange;
    }
</style>

<div id="main">
    There can only by one!
</div>
```

The `id` attribute is to assign a unique **identifier** to an element. This makes it easier to target inside your style.

```html
<style>
    /* This sets the element with id 'main' to a red background color. */

    #main {
        background-color: red;
    }
</style>

<!-- Notice the id attribute! -->
<div id="main">
    Hello, world!
</div>
```

___

#### _Events_

Events are things that can happen during use of your website. A button gets `"click"`ed on the `"mousemove"`s over an image.

It is possible to "hook" into these events with an `eventListener`. jQuery comes with a suite of tools to make it easier, but the easiest is the `on()` function.

___


### HTML Tags

___

#### _Style_

> The `<style>` tag can be used to style how the various elements behave. The `<style>` tag is for containing CSS rules, or Cascading **Style** Sheet rules. Styles change how content looks on a webpage.

**Example:**
```html
<style>
    p {
        color: red
    }
</style>
```

___

#### _Script_

> The `<script>` tag is for writing JavaScript to modify the page. It is possible to add event listeners and modify the webpage dynamically to make the page interactive.

**Example:**
```html
<script>
    // Set the text color for all divs to blue.
    var divElement = $("div");
    divElement.css("color", "blue");
</script>
```

___

#### _Division_

> The `<div>` tag creates a **division** of section. `<div>` tags are a way of organizing information on your website. They are used to group certain elements, as well as add line-breaks between various parts of content.

**Example:**
```html
<div>
    <h2>Hello, world!</h2>
    <p>
        It is a beautiful day!
    </p>
</div>
<div>
    <h2>Hot world...</h2>
    <p>
        It is miserable outside.
    </p>
</div>
```

___

#### _Line Brake_

> The `<br>` tag places (forces) a **break** between two lines of text.

**Example:**
```html
Dearest Deer,
<br><br>
I hope this message reaches you well.
<br><br>
Signed, Dear.
```

___

#### _Header_

> The `<h1>`, `<h2>`, and `<h3>` tags are used to define **headers**.  `<h1>` is the largest header and `<h6>` is the smallest. They are good for labelling content.

**Example:**
```html
<h1>What a Great Title</h1>
<h3>A memoir</h3>
```

___

#### _Paragraph_

> The `<p>` tag is used to group text into **paragraphs**. Don't confuse it with the `<br>` tag which is used to force a line-break!

**Example:**
```html
<p>
    This text is in its own block. It is away from any other p-tag blocks.
</p>
<p>
    This is another block of text. These two blocks of text are broken into paragraphs.
</p>
```

___

#### _Pre_

> The `<pre>` tag displays text with the same spacing for each letter including space characters. This is what is called a mono-spaced font. Think of using a typewriter.

**Example:**
```html
<pre>This text will appear with even spacing
     ...</pre>
```

___

#### _Image_

> The `<img>` tag is used for adding image to the page. The `<img>` tag requires _URL_ inside it's `src` attribute to understand what image to display.

**Example:**
```html
<img src='/file/db/thang.type
    /54eb540b49fa2d5c905ddf1a/portrait.png'>
    is a image on my webpage!
```

___

#### _Unordered List_

> The `<ul>` tag is for creating **unordered _(unsorted)_ lists** on a page. For the computer to know what items are apart of a list, be sure to use the `<li>` tag which stands for **list item** before the closing `</ul>` tag.

**Example:**
```html
<h3>Grocery List</h3>
<ul>
    <li>Milk</li>
    <li>Eggs</li>
    <li>Bread</li>
</ul>
```

___

#### _Ordered list_

> The `<ol>` tag is for creating **ordered lists** on a page. The contained `<li>` elements have an order, like a list of instructions.

**Example:**
```html
<h3>Instructions for Winning</h3>
<ol>
    <li>Consider the objective.</li>
    <li>Attempt to solve.</li>
    <li>Go back to 1.</li>
</ol>
```

___

#### _List Item_

> The `<li>` tag creates a `list item` inside of lists like the `<ul>` or `<ol>` tags.

**Example:**
```html
<h3>Today's To-do List</h3>
<ul>
    <li>Wash the dog.</li>
    <li>Think about washing the cat.</li>
    <li>Wash the car.</li>
</ul>
```

___

#### _Button_

> The `<button>` tag adds a clickable button to the page.

**Example:**
```html
<button>Submit</button>
```

___


### CSS Rules

___

#### _`background-color`_

> The `background-color` property changes the background color of an element.

**Example:**
```html
<style>
    div {
        /* Set the background color to blue. */
        background-color: blue;
    }
</style>
```

___

#### _`border-color`_

> The `border-color` property sets the color of the border, when one is defined with `border-style`.

**Example:**
```css
<style>
    div {
        border-style: solid;
        border-color: red;
    }
</style>
```

___

#### _`border-style`_

> The `border-style` property defines if a border should be displayed around an element. Suitable values are `solid`, `dotted`, `dashed`.

**Example:**
```css
<style>
    div {
        border-style: dashed;
    }
</style>
```

___

#### _`border-width`_

> The `border-width` property controls how wide the border will be.

**Example:**
```css
<style>
    div {
        border-style: dotted;
        border-width: 2px;
    }
</style>
```

___

#### _`border`_

> The `border` property is a shorthand property for `border-style`, `border-width` and `border-color`. The property values can be in any order.

**Example:**
```css
<style>
    div {
        border: 2px dotted green;
    }
</style>
```

___

#### _`color`_

> The `color` property changes the color of text inside an element.

**Example:**
```html
<style>
    p {
        /* Set the color of all text to red. */
        color: red;
    }
</style>
```

___

#### _`cursor`_

> The `cursor` property changes what the cursor looks like when mousing over certain elements. Some `<div>`s are clickable, so they are given the `pointer` property.

**Example:**
```html
<style>
    .selectable {
        cursor: pointer;
    }
</style>
``` 

___

#### _`font-size`_

> The `font-size` property controls how big text should display.

**Example:**
```html
<style>
    h1 {
        /* Make all text inside h1 to be HUGE. */
        font-size: 9em;
    }
</style>
```

___


#### _`font-weight`_

> The `font-weight` property sets the weight of the font. It can make it `bold` (thicker), or `light` (thinner).

**Example:**
```html
<style>
    .thickText {
        font-weight:thick;
    }
</style>
``` 

___

#### _`height`_

> The `height` property sets how tall an element should display on the page.

**Example:**
```html
<style>
    img {
        /* All images will now be 300 pixels tall. */
        height:300px;
    }
</style>
```

___

#### _`opacity`_

> The `opacity` property controls how transparent an element is. A value of 0 shows nothing. A value of 1 shows everything.  With 1 think 100% visible. A value of 0.50 will thus be halfway transparent.

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

#### _`text-align`_

> The `text-align` property sets where in an element text and other elements should be. `left` and `right` are example attribute values.

**Example:**
```html
<style>
    div {
        /* All text inside divs will be aligned to the center of all div elements. */
        text-align:center;
    }
</style>
```

___

#### _`text-decoration`_

> The `text-decoration` property specifies how the text should be decorated. `strike-through` and `underline` are example property values.

**Example:**
```html
<style>
    .important {
        text-decoration: underline;
    }
</style>
```

___

#### _`width`_

> The `width` property sets how wider an element should display on the page.

**Example:**
```html
<style>
    img {
        /* All images will now be 200 pixels wide. */
        width:200px;
    }
</style>
```

___


### jQuery Functions

___


#### _`$(query)`_

> `$` is the `jQuery` function. It returns a jQuery object baesd on the `query` used.

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
+ **`query`**: `string` (ex. `".selected"`) - _This is a CSS selector_

**Returns:**
+ `object`: jQuery object

___

#### _`$(this)`_

> `$(this)` returns a callback function's current target. Use it to find which specific element was selected when applying the same event listener to multiple elements.

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
+ **`this`**: `keyword` (ex. `this`) - _This is the context for the function_

**Returns:**
+ `object`: jQuery object of function context

___


#### _`element.css(property)`_

> `css` is used to get and set the CSS rules of a jQuery object.

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
+ **`property`**: `string` (ex. `"background-color"`) - _This is a CSS property name_

**Optional Parameters:**
+ **`value`**: `string` (ex. `"red"`) - _If included, this is what to set the CSS property to._

**Returns:**
+ `string`: `property value`

___

#### _`element.on(event, callback)`_

> The `on` function takes two arguments. A string of an event to monitor, and a function to call when the event occurs.

**Example:**
```html
<button id="theButton">Click me to hide me!</button>
<script>
    var button = $("#theButton");
    function hideOnClick() {
        // This only happens when the button is clicked.
        button.hide();
    }
    // This is what calls the function above.
    button.on("click", hideOnClick);
</script>
```

**Required Parameters:**
+ **`event`**: `string` (ex. `"click"`) - _This is the event name._
+ **`callback`**: `function` (ex. `hideOnClick`) - _This is the function that is performed when the event is fulfilled._

___

#### _`element.hide()` and `element.show()`_

> `hide` makes an element invisible.

> `show` makes an element visible.

**Example:**
```html
<div>
    <h3>Information of Valuability</h3>
    <div class="info">
        Valued information goes here.
    </div>
</div>
<script>
    // Hide all infoDivs at the start of the script.
    $(".infoDiv").hide();
    function showInfoChild() {
        // Show the clicked target's infoDiv.
        $(".infoDiv", this).show()
    }
    $(".infoDiv").parent().on('click', showInfoChild)
</script>
```

___

#### _`element.toggleClass(class)`_

> `toggleClass()` will add or remove a class depending if an element already has that class on it. If it has the class on it, it will remove it. if it doesn't have the class on it, it will add it.

**Example:**
```html
<div id="mainElement" class="strike">
    I contain information!
</div>
<style>
    .strike {
        text-decoration: line-through;
    }
</style>
<script>
    // Remove the "strike" class to the mainElement div.
    var target = $("#mainElement");
    target.toggleClass("strike");
</script>
```

**Required Parameters:**
+ **`class`**: `string` (ex. `"selected"`) - _A string of a CSS class name._

___

#### _`element.addClass(class)` and `element.removeClass(class)`_

> `addClass` adds a specific CSS class to an element.

> `removeClass` removes a specific CSS class from an element.

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
+ **`className`**: `string` (ex. `"selected"`) - _A string of a CSS class name_

___

#### _`element.siblings([selector])`_

> The `siblings()` function finds all neighboring elements to the element it was called on. An element is 'neighboring' if they are nested at the same depth in the HTML document. `siblings()` is useful when trying to find a programmatically-found element's neighbors. `siblings` returns a jQuery object of all neighboring elements. An element is a sibling if it is nested at the same level as the selected element.

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
+ **`selector`**: `string` (ex. `".className"`) - _A string to only select elements matching the CSS selector_

**Returns:**
+ `object`: jQuery object

___
