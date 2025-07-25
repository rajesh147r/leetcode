class Solution {
public:
    int maxSum(vector<int>& nums) {
        bool alnegative = true;
        int maxvalue = INT_MIN;
        for (int num : nums){
            if (num >= 0) alnegative = false;
            if (num > maxvalue) maxvalue = num;
        }
        if (alnegative) return maxvalue;
        unordered_set<int> unique(nums.begin(), nums.end());
        int sum = 0;
        for (int n : unique){
            if (n > 0) sum += n;
        }
        return sum;

    }
};