// short (Emma Buller and Shyne Choi)
// SoftDev
// K27 -- Where Does JS live?
// 2022-02-04
// time spent: 30
// --------------------------------------------------


// as a duo...
// pair programming style,
// implement a fact and fib fxn
var fact = function(n) {
  if (n <= 1) {
    return 1;
  }
  return n * fact(n - 1);
}

var fib = function(n) {
  if (n < 1) {
    return 0;
  }
  if(n == 1) {
    return 1;
  }
  return fib(n - 1) + fib(n - 2)
}
//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T.
