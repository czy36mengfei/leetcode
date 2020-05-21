class Solution {
public:
    vector<vector<int>> res;
    vector<vector<int>> combinationSum3(int k, int n) {
        if(k==0) return res;
        vector<int> temp;
        helper(temp,k,n,0);
        return res;
    }
    void helper(vector<int>& temp,int& k,int n,int i)
    {
        if(temp.size()==k && n==0)
        {
            res.push_back(temp);
            return;
        }
        if(temp.size()==k) return;
        for(int j=i+1;j<=9;j++)
        {
            if(n-j<0) break;
            temp.push_back(j);
            helper(temp,k,n-j,j);
            temp.pop_back();
        }
    }
};

