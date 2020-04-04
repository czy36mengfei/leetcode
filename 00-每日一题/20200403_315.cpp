//
// Created by zanbo on 2020/4/4.
//

class BIT{
    int* arr; // 元素值为0 or 1   1->k 求和 表示在小于k的元素数 由于更新元素的顺序是从右至左，可以保证取得的是该元素右边满足条件的元素
    int len;
public:
    BIT(int n) {
        arr = new int[n+1];
        memset(arr,0,(n+1)* sizeof(int));
        len = n+1;
    }
    void update(int i,int val)
    {
        while(i<len)
        {
            arr[i]+=val;
            i += i &(-i);
        }
    }
    int sum(int i)
    {
        int res = 0;
        while(i>0)
        {
            res += arr[i];
            i -= i&(-i);
        }
        return res;
    }
};


class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n,0);
        unordered_map<int,int> htabel;
        vector<int> copynums=nums;
        sort(copynums.begin(),copynums.end());
        for(int i=0;i<copynums.size();i++)
            htabel[copynums[i]] = i; // key是nums中的元素 value：是其排序后的排名
        BIT* tree = new BIT(n);
        for(int i=n-1;i>=0;i--)
        {
            res[i] = tree->sum(htabel[nums[i]]);
            tree->update(htabel[nums[i]]+1,1);
        }
        return res;
    }
};