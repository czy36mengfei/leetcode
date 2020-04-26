//
// Created by zanbo on 2020/4/26.
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


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution1 { // leetcode 超时
public:
    vector<vector<string>> res;
    int min_path = INT_MAX;

    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        auto first= find(wordList.begin(),wordList.end(),endWord);
        int end_index = first-wordList.begin();
        int n = wordList.size();
        if(end_index==n)
            return res; //end不在wordlist中 返回空
        vector<vector<int>> adj(n,vector<int>(n,0));
        adj = bfs(end_index,wordList);
        //下一步dfs回溯
        vector<int> visited(n,0);
        vector<string> path;
        path.push_back(beginWord);
        for(int i=0;i<wordList.size();i++)
        {
            //有边&未访问
            if(isadj(beginWord,wordList[i]))
                dfs(adj,wordList,end_index,visited,i,path);
        }
        return res;
    }
    void dfs(vector<vector<int>> & adj,vector<string>& wordList,int& endindex,vector<int>& visited,int tempindex,vector<string>& path)
    {
        //放入结果集
        path.push_back(wordList[tempindex]);
        //visited数组变化
        visited[tempindex]=1;
        //判断是不是尾节点
        if(tempindex==endindex)
        {
            if (path.size()==min_path)
            {
                res.push_back(path);
            } else if(path.size()<min_path){
                res.clear();
                res.push_back(path);
                min_path = path.size();
            }
        }
        else{
            //如果不是的话 继续回溯
            for(int i=0;i<wordList.size();i++)
            {
                //有边&未访问
                if(adj[i][tempindex] && !visited[i])
                    dfs(adj,wordList,endindex,visited,i,path);
            }
        }
        //改回visited
        visited[tempindex]=0;
        path.pop_back();
    }


    // bfs得到有用信息的邻接矩阵 （从末节点开始遍历 而不是建立整个图的邻接矩阵）
    vector<vector<int>> bfs(int endindex,vector<string>& wordList)
    {
        int n = wordList.size();
        //邻接矩阵
        vector<vector<int>> adj(n,vector<int>(n,0));
        // 访问标志
        vector<int> visited(n,0);
        visited[endindex]=1;
        queue<int> q;
        q.push(endindex);
        while(!q.empty())
        {
            int temp = q.front();
            q.pop();
            for(int i=0;i<n;i++)
            {
                if(adj[temp][i]==0 && isadj(wordList[i],wordList[temp]))
                {
                    adj[temp][i]=1;
                    if(!visited[i])
                    {
                        q.push(i);
                        visited[i] = 1;
                    }
                }
            }
        }
        return adj;
    }
    bool isadj(string a,string b)
    {
        //判断两个字符串是否相邻（只有一个字符不同）
        int cnt=0;
        for(int i=0;i<a.size();i++)
        {
            if(a[i]!=b[i])
                cnt++;
            if(cnt>1)
                return false;
        }
        return cnt==1;
    }
};


int main() {
    Solution1 s;
    vector<string> x = {"hot", "dot", "dog", "lot", "log", "cog"};
    s.findLadders("hit", "cog", x);
}