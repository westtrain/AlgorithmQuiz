function transformFirstAndLast(arr) {
  let obj = {};
  if(arr.length === 0){
    return obj;
  }
  let firstEle = arr[0];
  obj = {[firstEle]: arr[arr.length - 1],};
    //If insert a element to key from array, use [] into object.
  return obj;
}

