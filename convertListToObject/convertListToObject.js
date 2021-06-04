function convertListToObject(arr) {
  // Declare empty object call obj
  // Use for loop and to put array's element into obj
  // Return obj
  let obj = {};
  for(el of arr){
    if(el.length !== 0 && !(el[0] in obj)){
      obj[el[0]] = el[1];
    }
  }
  return obj;
}

