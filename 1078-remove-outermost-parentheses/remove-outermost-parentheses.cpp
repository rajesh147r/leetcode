class Solution {
public:
    string removeOuterParentheses(string s) {
        string res;
        int n = 0;
        for(char c:s){
            if (c == '(' && n++ >0) res +=c;
            else{
                if(c==')' && n-- >1) res +=c;
            }
        }
        return res;
    }
};