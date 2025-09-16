class Solution {
public:
    int findmax(vector<int>& piles){
        int maxi = 0;
        int n = piles.size();
        for(int i = 0; i<n; i++){
            maxi = max(maxi, piles[i]);
        }
        return maxi;
    }
    long long calculatetotalhrs(vector<int>& piles, int k){
        long long total_hrs = 0;
        int n = piles.size();
        for(int i = 0; i<n; i++){
            total_hrs += ceil((double)piles[i]/(double)k);
        }
        return total_hrs;
    }
    int minEatingSpeed(vector<int>& piles, int h) {
        int low = 1;
        int high = findmax(piles);
        int ans = INT_MAX;
        while(low <= high){
            int mid = low + (high-low)/2;
            long long totalh = calculatetotalhrs(piles, mid);
            if (totalh <= h){
                high = mid -1;
                ans = mid;
            }
            else low = mid + 1;
        }
        return ans;
    }
};