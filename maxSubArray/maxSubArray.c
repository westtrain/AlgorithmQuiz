/*
 * Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
 * Example:
 * Input: [-2,1,-3,4,-1,2,1,-5,4],
 * Output: 6
 * Explanation: [4,-1,2,1] has the largest sum = 6.
 *
 * Follow up:
 * If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
 * Also you can use Kadane’s Algorithm for solve it.
 *
 * Runtime: 4 ms
 * Memory Usage: 6 MB
 */

int maxSubArray(int* nums, int numsSizei)
{
    int i = 0;
    int sum = 0;
    int largeSum = nums[0];
    
    while (i < numsSize)
    {
        sum += nums[i];
        if (largeSum < sum)
            largeSum = sum;
        if (sum < 0)
            sum = 0;
        i++;
    }
    return largeSum;
}
