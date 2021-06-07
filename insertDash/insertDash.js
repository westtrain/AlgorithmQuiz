function insertDash(str) {
  let newStr = '';
  for(let i = 0; i < str.length; i++){
    newStr += str[i];
    if(Number(str[i]) !== 0 && str[i + 1] !== undefined && Number(str[i]) % 2 !== 0 && Number(str[i + 1]) % 2 !== 0){
      newStr += '-';
    }
  }
  return newStr;
}

