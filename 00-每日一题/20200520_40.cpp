class Solution {
public:
    vector<vector<int>> res;
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(),candidates.end());
        vector<int> temp;
        helper(temp,0,target,candidates,0);
        return res;
    }
    void helper(vector<int>& temp,int index,int& target,vector<int>& candidates,int sum)
    {
        if(target==sum)
        {
            res.push_back(temp);
            return;
        }
        for(int i=index;i<candidates.size();i++)
        {
            if(i>index && candidates[i]==candidates[i-1]) // 去重
                continue;
            if(sum+candidates[i]<=target){ // prune
                  temp.push_back(candidates[i]);
                helper(temp,i+1,target,candidates,sum+candidates[i]);
                temp.pop_back();
            } 
        }
    }
};

