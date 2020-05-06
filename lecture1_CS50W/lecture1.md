Table of Content
- [Lecture 1](#lecture-1)
  - [Advanced Git Commands](#advanced-git-commands)
    - [Git Branch](#git-branch)
    - [Git Checkout](#git-checkout)
    - [Git Merge](#git-merge)
    - [Git Pull](#git-pull)
    - [Forks](#forks)
    - [Pull Requests](#pull-requests)
  - [HTML](#html)
  - [CSS](#css)
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

## Advanced Git Commands
### Git Branch
`git branch` is a command that's used split off code from the working master code. This is typically done in order to work on a new feature without affecting the master branch of the code. This is helpful in order to avoid bugs in the main code as well as to be able to test new features on a separate website, for example.
Using the command will list all the current branches that are available. 

`git branch name` will add a branch. The code will not be visible on GitHub unless you push it!

`HEAD` in git means that it is the current branch that is being worked on. Whatever repository we were to pull down (feature branch or master) would be the head.

### Git Checkout
`git checkout` is the command that is used to switch between branches. Using `git checkout name` will switch to the branch with a specific name. `git checkout master` will switch back to the master branch.
Switching branches will change the file that is being worked on to the most up to date one on the particular branch! 

### Git Merge 
`git merge` is a command in order to merge a branch to the master. `git merge name` is the full command, where name is the name of the branch you want to merge into the master.

### Git Pull
`git pull` combines both `git fetch` and `git merge origin/master` into one command. It updates the repo on your machine to the the version that's currently stored on GitHub!

### Forks 
Forking a project won't affect the original repo on GiHub but it allows you to work on the project yourself. This is commonly used in open source projects. 

### Pull Requests
A pull request brings in changes from the your repo into another repo. Pull requests are a great way to get feedback about your code. Remember that a pull request won't automatically merge your code with the project, but it will go into a review stage where the code will be examined by the other developer. 
It's a very visual way to see your changes vs the project you have forked. 

## HTML
There have been numerous new tags introduced into HTML5. Here are a few:
```
<nav>, <header>, <section>, <footer>, <audio>, <video> and <datalist>
```
There is a <datalist> example included in the html file that's accompanying this document. 
Essentially, a datalist will allow you use autocomplete from within the a specified set of data that you have added to the html document. It's an empty input field, so no dropdown. 

## CSS
### Styling input fields
`input[type=text]` will allow you to style only text input fields. Handy if you want to distinguish them visually.
`input[type=number]` will only allow you to style number input fields. 

### Pseudo 
#### Pseudo Class
Here is a[link](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes) for more info
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





