function superIncreasing(arr) {
  let sum = 0;
  for(let i = 0; i < arr.length; i++){
    sum += arr[i];
    if(arr[i + 1] !== undefined && sum >= arr[i + 1]){
      return false;
    }
  }
  return true;
}

