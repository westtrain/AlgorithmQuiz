/*
 * Write an algorithm to determine if a number is "happy".
 *
 * A happy number is a number defined by the following process: Starting with any positive integer, 
 * replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay),
 * or it loops endlessly in a cycle which does not include 1.
 * Those numbers for which this process ends in 1 are happy numbers.
 *
 * Example: 
 * Input: 19
 * Output: true
 * Explanation: 
 * 1^2 + 9^2 = 82
 * 8^2 + 2^2 = 68
 * 6^2 + 8^2 = 100
 * 1^2 + 0^2 + 0^2 = 1
 *
 * Runtime: 0 ms
 * Memory Usage: 5 MB
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

/*
 * sample 0 ms Submission from leetcode.
 *
 int squareSum(int n)
{
    int sum = 0;
    while(n)
    {
        sum  += (n%10) * (n%10);
        n /= 10;
    }

    return sum;
}

bool isHappy(int n){
    int slow, fast;

    //    initialize slow and fast by n
    slow = fast = n;
    do
    {
        //    move slow number by one iteration
        slow = squareSum(slow);

        //    move fast number by two iteration
        fast = squareSum(squareSum(fast));

    }
    while (slow != fast);

    //    if both number meet at 1, then return true
    return (slow == 1);
}
*/
