/*
   your PPTASK:

   Test drive each bit of code in this file,
    and insert comments galore, indicating anything
     you discover,
    	have questions about,
    		or otherwise deem notable.

    		Write with your future self or teammates in mind.

    		If you find yourself falling out of flow mode, consult
    		other teams
    		MDN

   A few comments have been pre-filled for you...

   (delete this block comment once you are done)
*/

// Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon
// SoftDev pd0
// K28 -- Getting more comfortable with the dev console and the DOM
// 2022-02-08t
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-J in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
var f = function(x) {
  var j=30; //comment out this and it's just 20 + x due to j being declared earlier
  //get rid of var in front of j, it still works because j was declared earlier
  return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy', //like json wow
          age : 15,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) { //funciton in dictionary! wow
            return x+30; //how do you use this function?
          }
        }; //different types in one dictionary


var addItem = function(text) { //add item to list on the html file?
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};


var removeItem = function(n) { //remove list
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove(); //n has to be in bound with the range of the list
};


var red = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};


var stripe = function() {
  var items = document.getElementsByTagName("li");
  for(var i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

//insert your implementations here for...
// FIB
// FAC
var fact = function(n) {
  if (n <= 1) {
    return 1;
  }
  return n * fact(n - 1);
};

var fib = function(n) {
  if (n < 1) {
    return 0;
  }
  if(n == 1) {
    return 1;
  }
  return fib(n - 1) + fib(n - 2)
}; //semicolons at the end of function definitions!
// GCD
