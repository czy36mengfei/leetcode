class Solution {
public:
    int numDecodings(string s) {
        int len = s.length();
        vector<int> dp(len+1,0);
        dp[0]=1;
        for(int i=1;i<=len;i++)
        {
            dp[i] += ifzero(s[i-1])*dp[i-1];
            if(i>=2)
                dp[i] += ifalfha(s[i-2],s[i-1])*dp[i-2];
        }
        return dp[len];
    }

private:
    int ifzero(char c){
        if(c=='0')
            return 0;
        else
            return 1;
    }

    int ifalfha(char c1,char c2){
        if(c1=='1')
            return 1;
        if(c1=='2' && c2<='6')
            return 1;
        return 0;
    }
};