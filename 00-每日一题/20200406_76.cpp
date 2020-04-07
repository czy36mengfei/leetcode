//
// Created by zanbo on 2020/4/6.
//


class Solution {
public:
    string minWindow(string s, string t) {
        int min_win = s.size() + 1;
        string res;
        map<char,int> T_map;
        for(int i=0;i<t.size();i++)
        {
            T_map[t[i]]+=1; //----------- 注意语法 可以直接+=1 不需要先判断是否存在 和java不同
        }
        int T_num = t.size();
        int count = T_num;
        //特殊 边界
        if(T_num > s.size())
            return "";
        int l=0,r=0;
        for(;r<s.size();r++)
        {
            if(T_map.count(s[r])==0)
                continue;
            else {
                T_map[s[r]] --;
                if(T_map[s[r]]>=0)
                    count --;
                //判断此时是否满足条件
                while(count == 0)
                {
                    //记录子串
                    if(r-l+1<min_win)
                    {
                        min_win = r-l+1;
                        res = s.substr(l,min_win);
                    }
                    //如果是其他字符 直接收缩
                    if(T_map.count(s[l])!=0){
                        T_map[s[l]]+=1;
                        if(T_map[s[l]]>0)
                        {
                            count++;
                        }
                    }
                    l++;
                }
            }
        }
        if (min_win == s.size()+1)
            return "";
        else
            return res;
    }
};
