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
    bool exist(vector<vector<char>>& board, string word) {
        if(board.size()<1) return false;
        vector<vector<int>> visited(board.size(),vector<int>(board[0].size(),0));
        bool res=false;
        for(int i=0;i<board.size();i++)
        {
            for(int j=0;j<board[0].size();j++){
                res = helper(board,word,0,i,j,visited);
                if(res)
                    return res;
            }
        }
        return res;

    }

    bool helper(vector<vector<char>>& board,string &word,int index,int i,int j,vector<vector<int>>& visited)
    {
        //越界 或已访问 或字符不匹配
        if(i<0 || i>=board.size() || j<0 || j>=board[0].size() || visited[i][j] || board[i][j]!=word[index])
            return false;
        if(board[i][j]==word[index] && index==word.size()-1)
            return true;
        //剩下的情况是 board[i][j]==word[index] && index！=word.size()-1
        visited[i][j] = 1;
        bool res;
        res = helper(board,word,index+1,i-1,j,visited) || helper(board,word,index+1,i,j+1,visited)
                || helper(board,word,index+1,i+1,j,visited) ||helper(board,word,index+1,i,j-1,visited);
        if(!res)
        {
            visited[i][j]=0;
        }
        return res;
    }
};

int main()
{
    Solution s;
    vector<vector<char>> a = {{'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'}};
    bool res = s.exist(a,"ABCB");
    cout << res << endl;

}

