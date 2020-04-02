/*
 * Write an algorithm to determine if a number is "happy".
 *
 * A happy number is a number defined by the following process: Starting with any positive integer, 
 * replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay),
 * or it loops endlessly in a cycle which does not include 1.
 * Those numbers for which this process ends in 1 are happy numbers.
 */

 bool isHappy(int n){
    int temp = 1;
    int sum = n;
    if (n == 1 || n == 7)
        return true;
    while (sum > 6){
        sum = 0;
        while (n > 0){
            temp = n % 10;
            temp *= temp;
            sum += temp;
            n = n / 10;
        }
        n = sum;
    }
    return n == 1;
}

