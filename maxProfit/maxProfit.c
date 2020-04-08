/*
 * Say you have an array for which the ith element is the price of a given stock on day i.
 * 
 * Design an algorithm to find the maximum profit. You may complete as many transactions as you like
 * (i.e., buy one and sell one share of the stock multiple times).
 * 
 * Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
 *
 * Example 1:
 * Input: [7,1,5,3,6,4]
 * Output: 7
 * Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
 *              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
 *
 * Example 2:
 * Input: [1,2,3,4,5]
 * Output: 4
 * Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
 *              Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
 *              engaging multiple transactions at the same time. You must sell before buying again.
 *
 * Example 3:
 * Input: [7,6,4,3,1]
 * Output: 0
 * Explanation: In this case, no transaction is done, i.e. max profit = 0.
 *
 * Runtime: 4 ms
 * Memory Usage: 6.4 MB
 */

int maxProfit(int* prices, int pricesSize){
    int profit = 0;
    int buy = prices[0];
    int i = 1;
    if (pricesSize <= 1)
        return 0;
    while (i < pricesSize)
    {
        if (buy > prices[i])
            buy = prices[i];
        else
        {
            profit = profit + (prices[i] - buy);
            buy = prices[i];
        }
        i++;
    }
    return profit;
    // too slow code below
    // Runtime: 8 ms
    // Memory Usage: 6.3 MB
    // while (--pricesSize > 0)
    // {
    //     if (prices[pricesSize] > prices[pricesSize - 1])
    //         buy = prices[pricesSize];
    //     else
    //         buy = prices[--pricesSize];
    //     if (pricesSize != 0 && buy > prices[pricesSize - 1])
    //         profit = profit + (buy - prices[pricesSize - 1]);
    // }
    // return profit;
}

/*
 * sample 0 ms submission from leetcode.
 *
int maxProfit(int* prices, int pricesSize){
    int result = 0;
    for (int i = 0; i < pricesSize-1; i++) {
        if (prices[i] < prices[i+1]) result += prices[i+1] - prices[i];
    }
    return result;
}
*/
