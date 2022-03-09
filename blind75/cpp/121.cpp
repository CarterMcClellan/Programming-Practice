class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int lowestPrice=prices[0],maxProfit = 0;
        for(int i=1; i < prices.size(); i++)
        {
            lowestPrice = min(lowestPrice, prices[i]);
            maxProfit = max(maxProfit, prices[i] - lowestPrice);
        }
        return maxProfit;
    }
};
