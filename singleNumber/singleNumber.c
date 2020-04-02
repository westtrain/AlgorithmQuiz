/*
 * Given a non-empty array of integers, every element appears twice except for one. Find that single one.
 * Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
 */

 int singleNumber(int* nums, int numsSize){

    int i = 0;
    int res = 0;
    if (!nums)
      return 0;
    while (i < numsSize)
    {
        res = res ^ nums[i];
        i++;
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
