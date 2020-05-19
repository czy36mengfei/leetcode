class Solution {
public:
    vector<vector<int>> res;
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        if(candidates.size()==0)
            return res;
        vector<int> temp;
        helper(temp,target,0,candidates,0);
        return res;
    }
    void helper(vector<int>& temp,int& target,int sum,vector<int>& candidates,int index)
    {
        if(sum==target)
        {
            res.push_back(temp);
            return;
        }
        for(int i=index;i<candidates.size();i++)
        {
            if(sum+candidates[i]<=target){
                temp.push_back(candidates[i]);
                helper(temp,target,sum+candidates[i],candidates,i);
                temp.pop_back();
            }
        }
    }
};