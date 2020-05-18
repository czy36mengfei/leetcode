class Solution {
public:
    vector<vector<int>> res;
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        int n = nums.size();
        if(n==0)
            return res;
        unordered_map<int,int> map;
        for(auto num:nums)
        {
            map[num]+=1;
        }
        vector<int> temp;
        helper(temp,map,n);
        return res;
    }
    void helper(vector<int>& temp,unordered_map<int,int>&map,int& n)
    {
        if(temp.size()==n)
        {
            res.push_back(temp);
            return;
        }
        unordered_map<int,int>::iterator ite;
        for(ite=map.begin();ite!=map.end();ite++)
        {
            if(ite->second>0){
                temp.push_back(ite->first);
                map[ite->first]--;
                helper(temp,map,n);
                temp.pop_back();
                map[ite->first]++;
            }
        }
    }
};