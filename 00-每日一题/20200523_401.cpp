class Solution {
public:
    vector<string> res;
    vector<string> readBinaryWatch(int num) {
        vector<int> nums = {1,2,4,8,11,12,14,18,26,42}; // 前四个表示小时 后6个表示分钟 为了方便取值 分钟数值 +10
        helper(nums,0,0,num,-1);
        return res;
    }
    void helper(vector<int>& nums,int hour,int min,int num,int index)
    {
        if(num==0)
        {
            // 处理hour min为字符串
            string s = to_string(hour)+":";
            if(min<10)
                s+="0";
            s+=to_string(min);
            res.push_back(s);
            return;
        }
        for(int i=index+1;i<nums.size();i++)
        {
            if(i<=3)
            {
                if(hour+nums[i]<=11)
                    helper(nums,hour+nums[i],min,num-1,i);
            } else{
                if(min+nums[i]-10<=59)
                    helper(nums,hour,min+nums[i]-10,num-1,i);
            }
        }
    }
};