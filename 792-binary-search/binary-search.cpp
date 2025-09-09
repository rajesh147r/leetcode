class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        int low = 0;
        int high = n -1;
        int result = -1;
        while(low <= high){
            int mid = (low+high)/2;
            if(target == nums[mid]){
                result = mid;
                break;
            }
            else if(target < nums[mid]) high = mid - 1;
            else low = mid +1;
        }
        return result;
    }
};