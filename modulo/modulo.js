function modulo(num1, num2) {
  // TODO: 여기에 코드를 작성합니다.
  // Use while loop, iterate until num1 >= num2
  // To subtract num1 by num2 while iterating
  // return num1 after while loop is over.
  if(num2 === 0){
    return 'Error: cannot divide by zero';
  }
  while(num1 >= num2){
    num1 -= num2;
  }
  return num1;
}

