function powerOfTwo(num) {
  // Use while loop and iterate until num > 0
  // While iterate, use if loop and to check num divide by 2.
  // If remainder is 0, iteration to continue and return true when iteration is over.
  // Else if return false.
  while(num > 0){
    if(num === 1){
      return true;
    }
    if(num % 2 === 0){
      num /= 2;
      continue;
    }else{
      return false;
    }
  }
  return true;
}

