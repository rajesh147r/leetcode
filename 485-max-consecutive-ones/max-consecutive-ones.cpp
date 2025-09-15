class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int cnt = 0;
        int max_cnt = 0;
        for(int num:nums){
            if(num == 1){
                cnt += 1;
                max_cnt = max(max_cnt, cnt);
            }
            else cnt = 0;
        }
        return max_cnt;
    }
};