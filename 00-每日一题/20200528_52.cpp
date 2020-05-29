
class Solution {
public:
    int res=0;
    int totalNQueens(int n) {
        vector<pair<int,int>> temp;
        helper(n,0,temp);
        return res;
    }
    void helper(int& n,int i,vector<pair<int,int>>& temp)
    {
        if(i==n){
            res++;
            return;
        }
        for(int j=0;j<n;j++)
        {
            //判断 i j 是否合法
            int flag = 1;
            for(auto x:temp)
            {
                if(x.second==j || x.first-i==x.second-j || x.first-i==j-x.second)
                {
                    flag = 0;
                    break;
                }
            }
            if(flag)
            {
                // 如果合法 继续下一行递归
                temp.push_back(make_pair(i,j));
                helper(n,i+1,temp);
                temp.pop_back();
            }
        }
    }
};