### _Stylish Intent_

##### _Legend says:_
> Begin learning how to style various elements of a webpage.

##### _Goals:_
+ _Change the color of the `<p>` tags_
+ _Center the `<h1>` text_

##### _Topics:_
+ **Basic HTML**
+ **Basic CSS**

##### _Solutions:_
+ **[HTML](Stylish_Intent.html)**

##### _Rewards:_
+ 30  xp
+ 10 gems

##### _Victory words:_
+ _HOW DAPPER._

___

###### _Cascading Style Sheets (CSS)_

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

###### _Style tag_

The `<style>` tag can be used to style how the various elements behave.

It follows a special set of rules.

___

###### _`font-size` attribute_

The `font-size` property controls how big text should display.

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

###### _`text-align` attribute_

The `text-align` property sets where in an element text and other elements should be. `left` and `right` are example attribute values.

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

###### _`color` attribute_

The `color` property changes the color of text inside an element.

**Example:**

```html
<style>
    p {
        /* Set the color of all text to red. */
        color: red;
    }
</style>
```
