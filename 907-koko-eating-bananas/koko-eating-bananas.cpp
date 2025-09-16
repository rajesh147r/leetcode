class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        sort(piles.begin(), piles.end());
        int low = 1, high = piles[piles.size()-1], mid, ans;
        while(low <= high){
            mid = low + (high-low)/2;
            long long hrs=0;
            for(int i = 0; i<piles.size(); i++){
                hrs += ceil(double(piles[i])/mid);
            }
            if (hrs <= h){
                ans = mid;
                high = mid -1;
            }
            else low = mid+1;
        }
        return ans;
    }
};