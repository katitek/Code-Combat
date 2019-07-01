### _Paragraph Paragon_

##### _Legend says:_
> Learn a better way of grouping content using paragraphs!

##### _Goals:_
+ _Have 4 `<p>` tags_
+ _All `<p>` tags should have words in them_

##### _Topics:_
+ **Basic HTML**

##### _Solutions:_
+ **[HTML](Paragraph_Paragon.html)**

##### _Rewards:_
+ 30  xp
+ 10 gems

##### _Victory words:_
+ _TEXT: ORGANIZED._

___

##### _HTML Start/End Tags_

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

###### _`<p>` tag_

The `<p>` tag is used to group text into **paragraphs**.

Don't confuse it with the `<br>` tag which is used to force a line-break!

**Example:**

```html
<p>
    This text is in its own block. It is away from any other p-tag blocks.
</p>
<p>
    This is another block of text. These two blocks of text are broken into paragraphs.
</p>
```
