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
#include <math.h>

using namespace std;
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
struct ListNode {
         int val;
         ListNode *next;
         ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        // 保存这些状态 方便直接判断在某个位置 某个词是否可行
        vector<vector<bool>> r = vector<vector<bool>>(9,vector<bool>(9, false));// r[i][j]代表第i行数字j+1是否出现过
        vector<vector<bool>> c  = vector<vector<bool>>(9,vector<bool>(9,false));// c[i][j]代表第i列数字j+1是否出现过
        vector<vector<bool>> s = vector<vector<bool>>(10,vector<bool>(9,false));// s[i][j]代表第s个块数字j+1是否出现过
        for(int i=0;i<9;i++)
        {
            for(int j=0;j<9;j++)
            {
                if(board[i][j]=='.') continue;
                int temp = board[i][j]-'0';
                r[i][temp-1]= true;
                c[j][temp-1] = true;
                s[(i/3)*3+j/3+1][temp-1] = true;
            }
        }
        bool res = helper(board,r,c,s,0);
        cout<<res<<endl;
    }
    bool helper(vector<vector<char>>& board,vector<vector<bool>>& r,vector<vector<bool>>& c,vector<vector<bool>>& s,int index)
    {
        int i;
        for(i=index;i<81;i++)
        {
            if(board[i/9][i%9]=='.') break; //找到index及其后第一个空格之处 从这里开始继续回溯
        }
        if(i==81) return true; // 后面都填满了 满足要求
        for(int x=1;x<=9;x++) // 1-9逐个尝试是否可行
        {
            if(r[i/9][x-1] || c[i%9][x-1] || s[(i/9/3)*3+(i%9)/3+1][x-1]) continue; // 不可行
            //若可行 修改各个状态 然后继续回溯
            r[i/9][x-1] = true;
            c[i%9][x-1] = true;
            s[(i/9/3)*3+(i%9)/3+1][x-1] = true;
            board[i/9][i%9] = '0'+x;
            if(helper(board,r,c,s,i+1))
                return true;
            else
            {
                // 这条路走不通 状态需要改回来
                r[i/9][x-1] = false;
                c[i%9][x-1] = false;
                s[(i/9/3)*3+(i%9)/3+1][x-1] = false;
                board[i/9][i%9] = '.';
            }
        }
        return false;
    }
};


int main() {
       Solution s;
       vector<vector<char>> a = {{'5','3','.','.','7','.','.','.','.'},{'6','.','.','1','9','5','.','.','.'},
    {'.','9','8','.','.','.','.','6','.'},{'8','.','.','.','6','.','.','.','3'},
    {'4','.','.','8','.','3','.','.','1'},{'7','.','.','.','2','.','.','.','6'},
    {'.','6','.','.','.','.','2','8','.'},{'.','.','.','4','1','9','.','.','5'},
    {'.','.','.','.','8','.','.','7','9'}};
       s.solveSudoku(a);
}