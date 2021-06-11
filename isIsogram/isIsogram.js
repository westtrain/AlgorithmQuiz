function isIsogram(str) {
  for(let i = 0; i < str.length; i++){
    for(let j = i + 1; j < str.length; j++){
      if(str[i].toLowerCase() === str[j].toLowerCase()){
        return false;
      }
    }
  }
  return true;
}
