function convertDoubleSpaceToSingle(str) {
  // Declare empty array and to copy string by split to array from str
  // Declare empty string variable call newStr.
  // Use for loop and find white space in the array index
  // Put letter into newStr from array.
  // When find white space, move index + 1 after to insert it.
  let arr = str.split('');
  let newStr = '';
  
  for(let i = 0; i < arr.length; i++){
    newStr += arr[i];
    if(arr[i + 1] === ' ' && arr[i] === ' '){
      i++;
    }
  }
  return newStr;
}

