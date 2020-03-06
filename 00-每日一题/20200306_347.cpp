//
// Created by zanbo on 2020/3/6.
//
class Solution
{
public:
    vector<int> topKFrequent(vector<int>& nums, int k)
    {
        unordered_map<int,int> myMap;
        vector<int> res;
        for(int x:nums)
        {
            myMap[x]++;
        }
        // 优先队列 最小堆
        priority_queue< pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>> > q;
        for(auto val:myMap)
        {
            q.push(make_pair(val.second,val.first));
            if(q.size()>k)
                q.pop();
        }
        while(!q.empty())
        {
            res.push_back(q.top().second);
            q.pop();
        }
        return res;
    }
};

