# Lecture 7 - User Interfaces

- [Lecture 7 - User Interfaces](#lecture-7---user-interfaces)
  - [Introduction](#introduction)
  - [Single Page Applications](#single-page-applications)
    - [Getting the buttons to work](#getting-the-buttons-to-work)
  - [Combining Django and JavaScript](#combining-django-and-javascript)
    - [Remembering Sections with JavaScript History API](#remembering-sections-with-javascript-history-api)
    - [Scrolling](#scrolling)
    - [Animation](#animation)
      - [Javascript Event](#javascript-event)
    - [Controlling CSS with JavaScript](#controlling-css-with-javascript)
  - [React](#react)
    - [Imperative Programming](#imperative-programming)
    - [Declarative Programming](#declarative-programming)
    - [React Props](#react-props)
    - [State in React](#state-in-react)
      - [Creating State](#creating-state)
      - [Calling a function to update state](#calling-a-function-to-update-state)
      - [onKeyPress](#onkeypress)

## Introduction

## Single Page Applications

Using JavaScript, we are able to create single page applications in order to reduce the number of html pages we have to create so that we can create one dynamic html page that only updates portions of the page.

```html
<body>
  <button data-page="page1">Page 1</button>
  <button data-page="page2">Page 2</button>
  <button data-page="page3">Page 3</button>
</body>
```

This is the basic layout of the page and each button we're trying to access.

```javascript
function showPage(page) {
    document.querySelectorAll('div').forEach(div => {
      div.style.display = 'none' ;
      // This line first hides all the divs before displaying the one we want to display.
    })
    document.querySelector(`#${page}`).style.display = 'block';
    // Now show only the div I select!
}
```

We are essentially getting the page here via a query selector but instead of having to create a new function to grab each page, we can use the `<button data-page="pageN">Page N</button>` selector to get
the page we are clicking on!

### Getting the buttons to work

```javascript
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('button').forEach(button => {
    button.onclick = function () {
      showPage(this.dataset.page);
    }
  })
});
```

This is how we would get the buttons to work by efficiently accessing their `data-page` attribute which we have defined. In the function above, we first wait for the page to load (only if we write the JS inside of the same file!). We then attach an onclick even to each button via the forEach method and we then use the `this.dataset.page` in order to pass in the page we want to display. This is the argument that will be passed into the function called `showPage(page)` .  This then displays each page when we click on it but hides all the ones we don't want to see.

## Combining Django and JavaScript

Here we are starting to combine Django and JavaScript in order to be able to dynamically load data from our from an API into the application depending on the need of the user.

Similar to the example above where we loaded a page based on which button was pressed by the user, we can do a fetch request using JavaScript to display content dynamically, depending on what the user pressed.
We can also query our own server that has the text stored in a Django Application and use JavaScript to display the text dynamically.  

This way we can make fewer requests to the server and only load the sections of the page that we need in order to make the page a lot more efficient and less resource intense. This is a great way of combining Django and JavaScript into one to create a dynamic web application.

### Remembering Sections with JavaScript History API

```javascript
// Pushing State to the browser history!
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('button').forEach(button => {
    button.onclick = function () {
      const section = this.dataset.section;
      history.pushState({section:section}, "", `section${section}`);
      showSection(section)
    };
  });
});
```

The `history.pushState` part of the function push the state of the function up to the browsers history in order to be able to access the part of the page we were on. This, again, is better than having to request the section from the server every time we want to access it, as it will now be stored in the browsers cache.

**The arguments are as follows:**

1. First will be the data that will be associated with that state (so`{section: section}`). This is stored as a JSON object!.
2. Second part is the title, which is usually left blank because most browsers disregard that.
3. The third part is what we actually want to be visible inside of the URL. Here we can define the path. in this case it would be: www.url.com/sectionN as defined by `section${section}`.

Doing this will allow me to link to specific sections if I wanted to which makes linking much easier.

```javascript
window.onpopstate = function(event) {
  showSection(event.state.section)
}
```

We can add this function inside of our JavaScript in order for us to allow the browser to be able to use the "back" button in our browser and go back to the previous section. This data (I presume) will be stored inside of our browser history to minimize API calls!
It is effectively saving the "state" of the application. The state meaning what is currently displayed on the page.

### Scrolling

Scrolling in and of itself is a very basic concept and not one that is thought about much. However, modern websites can take advantage of the scrolling behavior in websites in order to interact with the user. Scrolling can help a page create an endless page, where, instead of making the user jump from page to page, they can scroll continuously. This technique is often used on blog or news sites.

A lot of the properties can be found [here](https://developer.mozilla.org/en-US/docs/Web/API/Window), the mozilla window documentation.

### Animation

We can use animations on websites in order to add a visual layer to our page, instead of just having a static page.
This is usually done with either CSS or JavaScript, but CSS is often the preferred tool to create these as it offers animations out of the box.

```css
h1 {
    @keyframe move {
        0% {
          font-size: 20px
        }
        50% {
          font-size: 40px
        }
        100% {
          font-size: 20px
        }
    }

    h1 {
        animation-name: move;
        animation-duration: 2s;
        animation-iteration-count: 2;
        animation-fill-mode: forwards;
    }
}
```

Here we have created a simple animation that resizes all the h1 tags on the page from 20px to 40px and then back again to 20px over the course of 2 seconds.
It's pretty straightforward but we can then use Javascript too to apply more control to that animation.

Using the keyword `style.animationPlayState` we can control CSS animations in order to give the user some interactivity with the page.

#### Javascript Event

If we add an eventlistener to something, we also get access to a something called `event`. We can pass this as an argument to a function:

```javascript
document.addEventListener('click', event => {
  const element = event.target;
  if (element.className === 'hide') {
    element.parentElement.remove();
  }
});
```

`event.target` is the thing that is being clicked on. We can save this inside of a variable, which is `const element` in this case.
`event.target` will figure out for us what  was  clicked on. We can then make an if statement, that if a certain button was clicked, do something.
In our case, if the thing that we clicked on contains the class of 'hide' then remove that parent element (which is the div).

### Controlling CSS with JavaScript

We can also add a CSS style property. We could do the following;
`element.parentElement.style.display: "none"` which would hide the element instead of remove it.

In situations like this, it could be helpful to create an animation in order to be able show the user that the post is being removed.

We can also add an event to be triggered once a CSS animation is over. For example we can do the following:

```javascript
element.parentElement.addEventListener('animationend', () => {
  element.parentElement.remove();
  // This effectively removes the element once the animation has ended.
});
```

## React

React is based on the concept of Declarative Programming. Declarative Programming is different to the usual types of programming that we're used to.
React allows us to create components and manipulate the component based on some underlying state. We then only need to update the state of the variable and react will take care of updating html for us.

React components are represented by JavaScript classes. This is how we can display those inside of our app.

One reason React is so powerful is because we can reuse components inside of our app, thus allowing us to write less code and make our pages more efficient.

### Imperative Programming

We're used to Imperative Programming, which is that we would create a heading in our HTML first. We would then create the logic inside of JavaScript where we would get the number printed (if we used the counter program as an example) inside of the heading tag and store that as a variable. We would then add +1 to the number and then fill the heading in with the new number.

### Declarative Programming

Declarative programming is slight different in the sense that the syntax is much simpler, especially when it comes to basic tasks such as incrementing a counter variable.

```javascript
// View
<h1>{num}</h1>

// Logic
num += 1;
```

That is much simpler than what we did above and there is a lot less syntax to write.

### React Props

Similar to python, we can pass "variables" into the HTML via the use of props.

``` javascript
class Hello extends React.Component {
  render () {
    return (
      <h1>Hello, {this.props.name}!</h1>
    );
  }
}

class App extends React.Component {
  render () {
    return (
      <Hello name='Bobby' />
    );
  }
}
```

We're passing a variable, called name, into our component by adding it to the end of the component that is being rendered out.

This is what a simple react component would look like.

### State in React

We can store multiple items inside of our state, it isn't just limited to 1 item!

```javascript
class App extends React.Component {
constructor(props) {
  super(props);
  this.state = {
    count: 0
  };
}
render () {
    return (
      <div>
        <h1>{this.state.count}</h1>
        <button onClick={this.count}>Count</button>
      </div>
    );
  }

  count = () => {
    this.setState(state =>( {
      count: state.count +1
    }));
  }

}
```

The code above is how you set state inside of the react app.

#### Creating State

First, we set the state when the page launches. This is done via the constructor, where we pass in the props. We set state via
`this.state = {count: 0}`.

#### Calling a function to update state

We can then apply a function to the button (we have to use onClick here) where we run a function when the button is clicked `button onClick={this.count}`.

We can then create the function below which will update the state every time we press the button!

```javascript
 count = () => {
    this.setState(state =>( {
      count: state.count +1
    }));
```

We now don't need to use JavaScript in order to update the heading (in our case). React will take care of the place wherever the state is used.

React states can apply to multiple items. It can be the data from an input field, it can be numbers that, it can be a text item.

In order to be able to store data from an input field inside of react we need to create a function that will update every time the value of the input field changes!

```javascript
<input onChange={this.updateResponse} value={this.state.response}>

updateResponse = (event) => {
  this setState(state => ({
    response: event.target.value
  }))
}
```

Here we are constantly updating the value that is being passed into the input field via the event parameter. We now have the ability to get the data from the input field and constantly update its state,  whenever there is a change inside of the field (It calls the `this.updateResponse` function!)

#### onKeyPress

Using `onKeyPress` in react will allow us to run a function based on a specific button the user has pressed.

So with regards to the app that is being created, we can do the following:

```javascript
<input onKeyPress = {this.inputKeyPress}>

inputKeyPress = (event) => {
  if (event,key === 'Enter') {
    const answers = parseInt(this.state.response)
    const sum = this.state.num1 + this.state.num2
      if (sum ===  answer {
        this.setState(state => ({
          score: state.score + 1,
          // Update numbers once the question has been answered
          num1: Math.ceil(Math.random() * 10),
          num2: Math.ceil(Math.random() * 10),
          response: ''"
        }));
      else {
          num1: Math.ceil(Math.random() * 10),
          num2: Math.ceil(Math.random() * 10),
          response: ""
      }
  }
}
```
