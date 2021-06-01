function computeWhenDouble(interestRate) {
  let years = 0;
  let rate = interestRate / 100; //Change to floating point number.
  let principal = 1;
  while(principal < 2){ //Until principal to reach double
    principal = principal + (principal * rate);
    years++;
  }  
  return years;
}
