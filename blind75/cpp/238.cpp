class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> forward = forwardProd(nums);
        reverse(nums.begin(), nums.end());
        vector<int> backward = forwardProd(nums);
        reverse(backward.begin(), backward.end());
        
        vector<int> result(nums.size(), 1);
        for(int i=0; i < nums.size(); i++)
        {
            result[i] = forward[i] * backward[i];
        }
        return result;
    }
    
    vector<int> forwardProd(vector<int> &vec){
        vector<int> prod(vec.size(), 1);
        prod[0] = 1;
        for(int i=1; i < vec.size(); i++)
        {
            prod[i] = vec[i-1] * prod[i-1];
        }
        return prod;
    }
    
    void printVec(vector<int>& vec){
        for (int i : vec)
            cout << i << ",";
        
        cout << endl;
    }
};
