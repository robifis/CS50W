Table of Content
- [Lecture 1](#lecture-1)
  - [HTML](#html)
  - [CSS](#css)
    - [Margin and padding](#margin-and-padding)
    - [Styling input fields](#styling-input-fields)
    - [Pseudo](#pseudo)
      - [Pseudo Class](#pseudo-class)
      - [Pseudo Elements](#pseudo-elements)
  - [Responsive Design](#responsive-design)
    - [Media Queries](#media-queries)
  - [Bootstrap](#bootstrap)
  - [SASS](#sass)
    - [Variables](#variables)
    - [Nesting](#nesting)
    - [Inheritance](#inheritance)


# Lecture 1

## HTML
There have been numerous new tags introduced into HTML5. Here are a few:
```
<nav>, <header>, <section>, <footer>, <audio>, <video> and <datalist>
```
There is a <datalist> example included in the html file that's accompanying this document. 
Essentially, a datalist will allow you use autocomplete from within the a specified set of data that you have added to the html document. It's an empty input field, so no dropdown. 

## CSS
### Margin and padding
There are two ways to add margin and padding to an element.

The first one is `margin : 5px`. This will add space to the outside of the "box" of the element, not affecting anything on the inside.
If we add `padding: 5px` on the other hand then it will affect the inside of the box of the element, spacing items away from the border of the box. 

### Styling input fields
`input[type=text]` will allow you to style only text input fields. Handy if you want to distinguish them visually.
`input[type=number]` will only allow you to style number input fields. 

### Pseudo 
#### Pseudo Class
Here is a [link](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes) for more info
A pseudo class is a special state of an element. Things like `button:hover` or `a:active` are pseudo classes.

#### Pseudo Elements
Here is a [link](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements) for more info
A pseudo element can apply multiple styles to elements that we all want to have the same styling.
For example, if you want each link to have a specific text we can use `a::before` which prepends the the link text with a certain kind of text or symbol. 
`a::after` obviously appends something. 
`p:selection` changes the look of the text that we select. 

## Responsive Design
To create a dynamic website that scales for both desktop and mobile we have several tools available. There are flexbox, grid and media queries. 

### Media Queries
Using `@media nameofdevice` allows you to be very specific how and when we want elements to show up. We can use `@media print` to hide certain elements if the website is page that will be printed often, for example. We can also use `@media (min-width: 500px)` to apply certain styling when the webpage is viewed on a very specific device. 

Combining this with the `::before` and `::after` tags can be a great way to only show certain text depending on screen size.

## Bootstrap
Here is a [link](https://getbootstrap.com/) for more info.

Bootstrap is a great way to create responsive and good looking websites without much effort. Bootstrap is a stylesheet that has plenty of pre-made styles available. 

Using bootstrap we can specify how content looks depending on the screen size by using class names such as `col-lg-3` and `col-md-6` in order to adjust how much space an element takes up, depending on screen size. 

## SASS
SASS is a CSS preprocessor that adds major functionality to css files.
We do, however, need to install an extra program in order to convert sass files to css files so that the browser can read those!

### Variables
Variables is one of the major benefits of using SASS as opposed to plain old CSS.
To create a variable we write the following code:
`$varname = attribiute`
`$fontcolor = red`
We can now use the $fontcolor variable everywhere instead of having to write red whenever we want to use that colour. 
Makes changing colour so much easier too as we only need to change one variable!

### Nesting
Nesting is another great benefit in Sass. 
It allows for much more readable code as it allows us to place the content we want styled inside the parents' curly braces.
```
div {
  font-size: 18px;
  color: $fontcolor;

  # Nested <p> element
  p {
    padding: 10px;
    font-size: 12px;
  }
}
```
### Inheritance
Finally, let's discuss inheritance. Inheritance has been designed, again, to make code much cleaner and much more reusable. 

We can create one main style that we want to apply to various elements and then simply extend a specific element with that pre-written code in order to minimize the amount we need to write.
Here is an example
```
# This is the main style that we want to apply to specific elements
%block {
  display: grid;
  grid-rows: 100px 1fr 1fr 100px;
  background-color: grey;
  font-size: 15px;
}
```
This is how you add the template inside of an element:
```
p {
  @extend %block
  font-weight: bold;
}
```
Simply adding the `@extend` part will apply all the styling from the block style and all we needed to do is change the font weight. 