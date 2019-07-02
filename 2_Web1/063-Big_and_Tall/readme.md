### _Big and Tall_

##### _Legend says:_
> Images can be any shape or size. Big and tall, or small and stout.

##### _Goals:_
+ _Add a third image_
+ _Alter the third image's size_

##### _Topics:_
+ **Basic HTML**
+ **Basic CSS**

##### _Solutions:_
+ **[HTML](Big_and_Tall.html)**

##### _Rewards:_
+ 30  xp
+ 10 gems

##### _Victory words:_
+ _ONE SIZE DOESN'T FIT ALL._

___

###### _Attibutes Con't_

There are more `attributes` than just `src`. To define the size of an `<img>` you can use `height` and `width`. `height` and `width` default to _"pixel"_ or `px` sizing. So setting a 200 pixel wide image to 50 will scale it down 25%, not 50%.

If only one of width or height is included, the image will scale proportionally. Or, that is, if width is set, then the image's height will automatically change to keep the image's original proportions.

If _both_ width and height are set, then image will force resize to match those numbers.

```html
<!-- An image tag with the width, height and src attributes. -->
<img width="200" height="300" src="file/db/thang.type
    /530e5926c06854403ba68693/portrait.png" />

```

___

###### _`width` attribute_

The `width` property sets how wider an element should display on the page.

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

###### _`height` attribute_

The `color` property sets how tall an element should display on the page.

**Example:**

```html
<style>
    img {
        /* All images will now be 300 pixels tall. */
        height:300px;
    }
</style>
```
