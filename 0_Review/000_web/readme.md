## Web Development Theory and Methods by Code Combat

___


### HTML Theory

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


### HTML Tags

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

#### _Headers_

> The `<h1>`, `<h2>`, and `<h3>` tags are used to define **headers**.  `<h1>` is the largest header and `<h6>` is the smallest. They are good for labelling content.

**Example:**
```html
<h1>What a Great Title</h1>
<h3>A memoir</h3>
```

___
