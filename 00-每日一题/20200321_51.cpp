//
// Created by zanbo on 2020/3/21.
//

class Solution {
public:
    vector<vector<string>> res;
    vector<vector<string>> solveNQueens(int n) {
        vector<string> temp(n,string(n,'.'));
        dfs(0,temp,n);
        return res;
    }

    void dfs(int row, vector<string>& temp, int n)
    {
        if(row==n)
        {
            res.push_back(temp);
            return;
        }
        for(int j=0;j<n;j++)
        {
            if(isvalid(row,j,temp,n))
            {
                temp[row][j] = 'Q';
                dfs(row+1,temp,n);
                temp[row][j] = '.';
            }
        }
    }

    bool isvalid(int i,int j,vector<string> temp,int n)
    {
        // 分别判断所在列和两个斜线 是否有Q
        for(int k=0;k<i;k++)
        {
            if(temp[k][j]=='Q')
                return false;
        }
        for(int k=0;i-k>=0 && j-k>=0;k++)
        {
            if(temp[i-k][j-k]=='Q')
                return false;
        }
        for(int k=0;i-k>=0 && j+k<n;k++)
        {
            if(temp[i-k][j+k]=='Q')
                return false;
        }
        return true;
    }

};