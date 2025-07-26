class Solution {
public:
    bool checkDivisibility(int n) {
        int sum = 0;
        int product = 1;
        int num = n;
        while (num >0){
            int digit = num%10;
            sum += digit;
            product *= digit;
            num /= 10;
        }
        int s = sum + product;
        if(n%s == 0){
            return true;
        }
        else return false;
    }
};