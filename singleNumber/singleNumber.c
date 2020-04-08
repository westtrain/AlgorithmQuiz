/*
 * Given a non-empty array of integers, every element appears twice except for one. Find that single one.
 *
 * Note:
 * Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
 *
 * Example 1:
 * Input: [2,2,1]
 * Output: 1
 *
 * Example 2:
 * Input: [4,1,2,1,2]
 * Output: 4
 *
 * Runtime: 8 ms
 * Memory Usage: 6.7 MB
 */

 int singleNumber(int* nums, int numsSize){

    int i = 0;
    int res = 0;
    while (i < numsSize)
    {
        res = res ^ nums[i];
        i++;
        // too slow code below
        // Runtime: 16 ms
        // while (j < numsSize)
        // {
        //     if (nums[i] == nums[j] && i != j)
        //         break;
        //     j++;
        // }
        // if (j == numsSize)
        //     return nums[i];
        // i++;
        // j = 0;
    }
    return res;
}

/*
 * sample 0 ms from leetcode.
 * 
 int singleNumber(int* nums, int numsSize){
    int sum=0, i=0;
    for (i=0; i<numsSize; i++){
        sum ^= nums[i];
    }
    return sum;
}
*/
