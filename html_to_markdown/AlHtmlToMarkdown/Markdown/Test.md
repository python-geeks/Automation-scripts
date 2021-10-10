


Page Title



* {
 box-sizing: border-box;
}

/* Style the body */
body {
 font-family: Arial, Helvetica, sans-serif;
 margin: 0;
}

/* Header/logo Title */
.header {
 padding: 80px;
 text-align: center;
 background: #1abc9c;
 color: white;
}

/* Increase the font size of the heading */
.header h1 {
 font-size: 40px;
}

/* Sticky navbar - toggles between relative and fixed, depending on the scroll position. It is positioned relative until a given offset position is met in the viewport - then it "sticks" in place (like position:fixed). The sticky value is not supported in IE or Edge 15 and earlier versions. However, for these versions the navbar will inherit default position */
.navbar {
 overflow: hidden;
 background-color: #333;
 position: sticky;
 position: -webkit-sticky;
 top: 0;
}

/* Style the navigation bar links */
.navbar a {
 float: left;
 display: block;
 color: white;
 text-align: center;
 padding: 14px 20px;
 text-decoration: none;
}


/* Right-aligned link */
.navbar a.right {
 float: right;
}

/* Change color on hover */
.navbar a:hover {
 background-color: #ddd;
 color: black;
}

/* Active/current link */
.navbar a.active {
 background-color: #666;
 color: white;
}

/* Column container */
.row { 
 display: -ms-flexbox; /* IE10 */
 display: flex;
 -ms-flex-wrap: wrap; /* IE10 */
 flex-wrap: wrap;
}

/* Create two unequal columns that sits next to each other */
/* Sidebar/left column */
.side {
 -ms-flex: 30%; /* IE10 */
 flex: 30%;
 background-color: #f1f1f1;
 padding: 20px;
}

/* Main column */
.main { 
 -ms-flex: 70%; /* IE10 */
 flex: 70%;
 background-color: white;
 padding: 20px;
}

/* Fake image, just for this example */
.fakeimg {
 background-color: #aaa;
 width: 100%;
 padding: 20px;
}

/* Footer */
.footer {
 padding: 20px;
 text-align: center;
 background: #ddd;
}

/* Responsive layout - when the screen is less than 700px wide, make the two columns stack on top of each other instead of next to each other */
@media screen and (max-width: 700px) {
 .row { 
 flex-direction: column;
 }
}

/* Responsive layout - when the screen is less than 400px wide, make the navigation links stack on top of each other instead of next to each other */
@media screen and (max-width: 400px) {
 .navbar a {
 float: none;
 width: 100%;
 }
}




# My Website


A **responsive** website created by me.




[Home](#)
[Link](#)
[Link](#)
[Link](#)



## About Me


##### Photo of me:


Image
Some text about me in culpa qui officia deserunt mollit anim..


### More Text


Lorem ipsum dolor sit ame.


Image  

Image  

Image


## TITLE HEADING


##### Title description, Dec 7, 2017


Image
Some text..


Sunt in culpa qui officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco.


  

## TITLE HEADING


##### Title description, Sep 2, 2017


Image
Some text..


Sunt in culpa qui officia deserunt mollit anim id est laborum consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco.





## Footer





