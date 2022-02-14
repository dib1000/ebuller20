// short :: Emma Buller, Shyne Choi
// SoftDev pd1
// K30 - canvas based JS drawing
// 2022-02-14
// time spent: 30

//retrieve node in DOM via ID
var c = document.getElementById("slate");

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

//init global state var
var mode = "rect";

var toggleMode = (e) => {
  console.log("toggling...");
  // if( ) {
  //
  // }
  // else {
  //
  // }
}

var drawRect = function(e) {
  var mouseX = offsetX;
  var mouseY = offsetY;
  console.log("mouseclick registed at ", mouseX, mouseY);

}
//
// var drawCircle = (e) => {
//   var mouseX =
//   var mouseY =
//   console.log("mouseclick registed at ", mouseX, mouseY);
// }
//
//   var draw = (e) => {
//     var mouseX =
//     var mouseY =
//     console.log("mouseclick registed at ", mouseX, mouseY);
//   }
//
// var wipeCanvas = () => {
//
// }
//
c.addEventListener("click", draw);
// var bToggler = document. ;
// bToggler. ;
// var clearB = ;
// clearB. ;
