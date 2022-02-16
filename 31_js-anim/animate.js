// Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon
// SoftDev pd0
// K31 -- canvas based JS animation
// 2022-02-15t

// model for HTML5 canvas-based animation

// SKEELTON


//access canvas and buttons via DOM
var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");

//prepare to interact with canvas in 2D
var ctx = c.getContext("2d");

//set fill color to team color
ctx.fillStyle = 'rgb(0, 255, 255)';
ctx.strokeStyle = "black";
ctx.lineWidth = 0.5;

var requestID;  //init global var for use with animation frames


//var clear = function(e) {
var clear = (e) => {
  console.log("clear invoked...")

  // YOUR CODE HERE
};


var radius = 0;
var growing = true; //turns false when circle radius reaches 250 

//var drawDot = function() {
var drawDot = () => {
  console.log("drawDot invoked...")
  var fillingCircle = new Path2D();
  fillingCircle.arc(250,250,50,0,Math.PI * 2);
  ctx.fill(fillingCircle);
  ctx.stroke(fillingCircle);

  // YOUR CODE HERE

  /*
    ...to
    Wipe the canvas,
    Repaint the circle,
    ...and somewhere (where/when is the right time?)
    Update requestID to propagate the animation.
    You will need
    window.cancelAnimationFrame()
    window.requestAnimationFrame()
   */
};


//var stopIt = function() {
var stopIt = () => {
  console.log("stopIt invoked...")
  console.log( requestID );

  // YOUR CODE HERE
  /*
    ...to
    Stop the animation
    You will need
    window.cancelAnimationFrame()
  */
};


dotButton.addEventListener( "click", drawDot );
stopButton.addEventListener( "click",  stopIt );
