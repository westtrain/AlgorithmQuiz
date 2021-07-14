function numberSearch(str) {
  // 문자열속에서 숫자를 찾아 모두 더하고 숫자와 공백을 제외한 나머지 문자열의 길이와 나눈 값을 반환
  let sum = 0, exceptLen = 0;
  if(str.length !== 0){
    for(let i = 0; i<str.length; i++){
      if(Number(str[i])){
        sum += Number(str[i]);
        exceptLen++;
      }
      if(str[i] === ' '){
        exceptLen++;
      }
    }
  sum /= (str.length - exceptLen);
  }
  return Math.round(sum);
}

