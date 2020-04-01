#include <vector>
#include <stdlib.h>
#include <iostream>
#include <map>
#include <unordered_map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <stdio.h>
#include <fstream>

using namespace std;


class Solution {
public:
    int count;
    vector<int> parrent;
    int findCircleNum(vector<vector<int>>& M) {
        int N = M.size();
        count = N;
        for(int i=0;i<N;i++)
            parrent.push_back(i);
        // 连通操作
        for(int x=0;x<N;x++)
        {
            for(int y=1;y<N;y++)
            {
                if(y<=x) continue;
                if(M[x][y])
                    union_opp(x,y);
            }
        }
        return count;
    }
    // 找x节点的根节点 【优化：最大化压缩树的高度 为后续查找降低时间成本】
    int find(int x)
    {
        int root = x;
        while(parrent[root]!=root)
            root = parrent[root];
        while(parrent[x]!=x)
        {
            int temp = parrent[x];
            parrent[x] = root;
            x = temp;
        }
        return root;
    }
    void union_opp(int x,int y) // 将x、y连通
    {
        int root_x = find(x);
        int root_y = find(y);
        if(root_x==root_y)
            return;
        parrent[root_x] = root_y;
        count --;
    }
};


int main()
{
    Solution s;
    vector<vector<int>> M = {{1,0,0,1},{0,1,1,0},{0,1,1,1},{1,0,1,1}};
    s.findCircleNum(M);
}
