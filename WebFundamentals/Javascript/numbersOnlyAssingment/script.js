function numbersOnly(arr) {
  var arrnew=[];
  for (var idx = 0; idx < arr.length; idx++ ) {
    if (typeof arr[idx] === "number") {
    arrnew.push(arr[idx]); 
  }
  }
return arrnew;
}

console.log(numbersOnly([1, "apple", -3, "orange", 0.5]));