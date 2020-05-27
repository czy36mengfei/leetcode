class Solution {
public:
    vector<vector<int>> res;
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& matrix) {
        int m = matrix.size();
        if(m==0) return res;
        int n = matrix[0].size();
        vector<vector<int>> visited = vector<vector<int>>(m,vector<int>(n,0));
        vector<vector<int>> p= vector<vector<int>>(m,vector<int>(n,0));
        vector<vector<int>> a= vector<vector<int>>(m,vector<int>(n,0));
        for(int j=0;j<n;j++)
        {
            helper_p(matrix,visited,m,n,0,j,p);
        }
        for(int i=0;i<m;i++)
        {
            helper_p(matrix,visited,m,n,i,0,p);
        }
        visited = vector<vector<int>>(m,vector<int>(n,0));
        for(int j=0;j<n;j++)
        {
            helper_a(matrix,visited,m,n,m-1,j,a);
        }
        for(int i=0;i<m;i++)
        {
            helper_a(matrix,visited,m,n,i,n-1,a);
        }
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(p[i][j]==1 && a[i][j]==1)
                {
                    vector<int> temp = {i,j};
                    res.push_back(temp);
                }
            }
        }
        return  res;
    }
    void helper_p(vector<vector<int>>& matrix,vector<vector<int>>& visited,int& m,int& n,int i,int j,vector<vector<int>>& p)
    {
        if(visited[i][j]==1) // 之前访问过 无需重复计算
        {
            return;
        }
        visited[i][j] = 1;
        p[i][j]=1;
        // 上
        if(i>0 && matrix[i-1][j]>=matrix[i][j] && visited[i-1][j]!=-2)
            helper_p(matrix, visited, m, n, i - 1, j,p);
        // 下
        if(i<m-1 && matrix[i+1][j]>=matrix[i][j] && visited[i+1][j]!=-2)
            helper_p(matrix,visited,m,n,i+1,j,p);
        // 左
        if(j>0 && matrix[i][j-1]>=matrix[i][j] && visited[i][j-1]!=-2)
            helper_p(matrix,visited,m,n,i,j-1,p);
        // 右
        if(j<n-1 && matrix[i][j+1]>=matrix[i][j] && visited[i][j+1]!=-2)
            helper_p(matrix,visited,m,n,i,j+1,p);
    }
    void helper_a(vector<vector<int>>& matrix,vector<vector<int>>& visited,int& m,int& n,int i,int j,vector<vector<int>>& a)
    {
        if(visited[i][j]==1) // 之前访问过 无需重复计算
        {
            return;
        }
        visited[i][j] = 1;
        a[i][j]=1;
        // 上
        if(i>0 && matrix[i-1][j]>=matrix[i][j] && visited[i-1][j]!=-2)
            helper_a(matrix, visited, m, n, i - 1, j,a);
        // 下
        if(i<m-1 && matrix[i+1][j]>=matrix[i][j] && visited[i+1][j]!=-2)
            helper_a(matrix,visited,m,n,i+1,j,a);
        // 左
        if(j>0 && matrix[i][j-1]>=matrix[i][j] && visited[i][j-1]!=-2)
            helper_a(matrix,visited,m,n,i,j-1,a);
        // 右
        if(j<n-1 && matrix[i][j+1]>=matrix[i][j] && visited[i][j+1]!=-2)
            helper_a(matrix,visited,m,n,i,j+1,a);
    }
};

