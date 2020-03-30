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
    // 拓扑排序 如果图中有环 则输出空列表
    /*
     * 1.把所有入度为0的点放入队列中
     * 2.从队首取一个点 放入结果集 同时将它指向的点 入度减一 如果有入度为0的 入队
     * 3.队列为空时 判断结果集元素个数和总节点个数是否相同
     */
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> res;
        if(numCourses==0) return res;
        // 每个节点的入度数目
        int inNum[numCourses];
        memset(inNum,0, sizeof(inNum));
        // 每个节点指向的节点index
        vector<vector<int>> adj(numCourses);
        for(vector<int> x:prerequisites)
        {
            inNum[x[0]]+=1;
            adj[x[1]].push_back(x[0]);
        }
        //把所有入度为0的点放入队列中
        queue<int> q;
        for(int i=0;i<numCourses;i++)
        {
            if(inNum[i]==0)
                q.push(i);
        }
        int count = 0;
        while(!q.empty())
        {
            //从队首取一个点 放入结果集
            int top=q.front();
            q.pop();
            count ++;
            res.push_back(top);
            //同时将它指向的点 入度减一
            for(int i=0;i<adj[top].size();i++)
            {
                int temp=inNum[adj[top][i]];
                inNum[adj[top][i]] -=1;
                // 如果有入度为0的 入队
                if(temp==1)
                {
                    q.push(adj[top][i]);
                }
            }
        }
        if(count!=numCourses)
            res.clear();
        return res;
    }
};