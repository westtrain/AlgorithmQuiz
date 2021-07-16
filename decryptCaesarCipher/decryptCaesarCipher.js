function decryptCaesarCipher(str, secret) {
  let decryptStr = '', alphbet = 'abcdefghijklmnopqrstuvwxyz', temp = 0;
  for(let i = 0; i < str.length; i++){
    if(str[i] === ' '){
      decryptStr += ' ';
    }else{
        for(let j = 0; j < alphbet.length; j++){
          if(j - secret < 0){
            temp = alphbet.length + j;
          }else{
            temp = j;
          }
          if(str[i] === alphbet[j]){
            decryptStr += alphbet[temp - secret];
          }
      }
    }
  }
  return decryptStr;
}

