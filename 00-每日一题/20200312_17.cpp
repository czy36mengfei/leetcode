//
// Created by zanbo on 2020/3/12.
//

class Solution {
    //回溯法
public:
    vector<string> dic = {"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
    vector<string> res;
    vector<string> letterCombinations(string digits) {
        if(!digits.length()) return res;
        int index = 0;
        string pre = "";
        dfs(digits,index,pre);
        return res;
    }

    void dfs(string digits, int index, string pre)
    {
        if(index==digits.length())
        {
            res.push_back(pre);
            return;
        }
        int num = digits[index]-'0';
        for(char x:dic[num])
        {
            dfs(digits,index+1,pre+x);
        }
    }
};
