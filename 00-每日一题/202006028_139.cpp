class Solution{
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        int len = s.size();
        vector<bool> dp = vector<bool>(len+1, false);
        dp[0] = true;
        for(int j=1;j<=len;j++)
            for(int i=0;i<j;i++)
            {
                dp[j] = dp[i] && include(s.substr(i,j-i),wordDict);
                if(dp[j])
                    break;
            }
        return dp[len];
    }
private:
    bool include(string w, vector<string>& wordDict)
    {
        if(find(wordDict.begin(),wordDict.end(),w)==wordDict.end())
            return false;
        else
            return true;
    }
};