// Use for loop, iterate to increase i until str.length.
  // While iterating, find whitespace in str.
  // if find it, to add value of next index(i++) of str into newStr.
  // When iteration is over, return newStr.
  let newStr = '';
  if(str.length !== 0){
    newStr = str[0];
    for(let i = 1; i < str.length; i++){
      if(str[i] === ' '){
        i++;
        newStr += str[i];
      }
    }
  }
  return newStr;
}

