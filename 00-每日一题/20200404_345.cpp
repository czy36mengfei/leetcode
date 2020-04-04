//
// Created by zanbo on 2020/4/4.
//

class Solution {
public:
    string reverseVowels(string s) {
        int n=s.size();
        if(n<=1) return s;
        int i=0;
        int j=n-1;
        while(i<j)
        {
            while(i<j && tolower(s[i])!='a' && tolower(s[i])!='e' && tolower(s[i])!='i' && tolower(s[i])!='o' &&tolower(s[i])!='u')
            {
                i++;
            }
            while(i<j && tolower(s[j])!='a' && tolower(s[j])!='e' && tolower(s[j])!='i' && tolower(s[j])!='o' &&tolower(s[j])!='u')
            {
                j--;
            }
            if(i<j)
            {
                char temp = s[i];
                s[i] = s[j];
                s[j] = temp;
                i++;
                j--;
            }
        }
        return s;
    }
};
