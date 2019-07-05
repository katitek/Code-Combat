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
