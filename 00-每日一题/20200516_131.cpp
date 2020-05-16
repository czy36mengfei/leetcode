class Solution {
public:
    vector<vector<string>> res;
    vector<vector<string>> partition(string s) {
        if(s.length()==0) return res;
        vector<string> temp;
        helper(temp,s,0);
        return res;
    }
    void helper(vector<string>& temp,string& s,int start){  // start表示开始字符的index
        if(s.length()==start)
        {
            res.push_back(temp);
            return;
        }
        for(int i=1;i+start-1<s.length();i++)
        {
            string x = s.substr(start,i);
            if(!ispara(x))
                continue;
            temp.push_back(x);
            helper(temp,s,start+i);
            temp.pop_back();
        }
    }

    bool ispara(string s){
        // 判断是不是回文
        for(int i=0;i<s.length()/2;i++)
        {
            if(s[i]!=s[s.length()-1-i])
                return false;
        }
        return true;
    }
};

