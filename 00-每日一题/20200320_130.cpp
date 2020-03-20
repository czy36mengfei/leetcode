//
// Created by zanbo on 2020/3/14.
//

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
    void solve(vector<vector<char>>& board) {
        if (board.size()<2 || board[0].size()<2) return;
        int m = board.size();
        int n = board[0].size();
        //边界是O的回溯 将连通的O全变为$
        for(int j=0;j<n;j++)
        {
            dfs(board,0,j,m,n);
            dfs(board,m-1,j,m,n);
        }
        for(int i=1;i<m-1;i++)
        {
            dfs(board,i,0,m,n);
            dfs(board,i,n-1,m,n);
        }

        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(board[i][j]=='$')
                    board[i][j] = 'O';
                else if(board[i][j]=='O')
                    board[i][j]= 'X';
            }
        }
    }

    void dfs(vector<vector<char>>& board,int i,int j,int m,int n)
    {
        if( i<0 || i>=m || j<0 || j>=n || board[i][j]=='X' ||  board[i][j]=='$' )
            return;
        board[i][j]= '$';
        dfs(board,i-1,j,m,n);
        dfs(board,i+1,j,m,n);
        dfs(board,i,j-1,m,n);
        dfs(board,i,j+1,m,n);
   }
};

