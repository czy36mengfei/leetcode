class Solution {
public:
    bool wordPattern(string pattern, string str) {
        unordered_map<char,string> cmap;
        unordered_map<string,char> smap;
        int i=0;
        int j=0;
        while(i<pattern.size() && j<str.size())
        {
            char a = pattern[i];
            string temp ="";
            while(str[j]!=' ' && j<str.size())
            {
                temp+=str[j];
                j++; 
            }
            j++;
            if(cmap.count(a)==0 && smap.count(temp)==0)
            {
                cmap[a] = temp;
                smap[temp] = a;
            }
            else if(cmap[a]!=temp)
                return false;
            i++;
        }
        if(i<pattern.size() || j<str.size())
            return false;
        return true;
       
    }
};