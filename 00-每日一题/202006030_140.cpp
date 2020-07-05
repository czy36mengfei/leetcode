class Solution{
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        if(!wordBreak1(s,wordDict)) return vector<string>();
        int len = s.size();
        vector<vector<string>> dp = vector<vector<string>>(len+1,vector<string>());
        dp[0] = vector<string>(1,"");
        for(int j=1;j<=len;j++) {
            for (int i = 0; i < j; i++) {
                string temp="";
                if(dp[i].size()>0 && include(s.substr(i, j - i), wordDict))
                {
                    for(auto str:dp[i])
                    {
                        if(str=="")
                            temp=str+s.substr(i, j - i);
                        else
                            temp=str+" "+s.substr(i, j - i);
                        dp[j].push_back(temp);
                    }
                }
            }
        }
        return dp[len];
    }
private:
    bool wordBreak1(string s, vector<string>& wordDict) {
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

    bool include(string w, vector<string>& wordDict)
    {
        if(find(wordDict.begin(),wordDict.end(),w)==wordDict.end())
            return false;
        else
            return true;
    }
};

