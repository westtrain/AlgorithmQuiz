function firstReverse(str) {
  // code here ... :)
  let strRev = '';
  if(str.length !== 0){
    let arr = str.split('');
    let revArr = arr.reverse();
    for(letter of revArr){
      strRev += letter;
    }
  } 
  return strRev;
}

