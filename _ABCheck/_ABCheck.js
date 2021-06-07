function ABCheck(str) {
  if(str.length > 4){
    for(let i = 0; i < str.length; i++){
      if((str[i] === 'A' || str[i] === 'a') && (str[i + 4] === 'B' || str[i + 4] === 'b')){
        return true;
      }else if((str[i] === 'B' || str[i] === 'b') && (str[i + 4] === 'A' || str[i + 4] === 'a')){
        return true;
      }
    }
  }
  return false;
}
