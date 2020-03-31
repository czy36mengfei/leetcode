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


class WordDictionary {

    struct TrieNode{
        TrieNode *child[26];
        bool isword;
        TrieNode(): isword(false){
            for(auto &x:child)
            {
                x = NULL;
            }
        }
    };

private:
    TrieNode* root;
public:
    /** Initialize your data structure here. */
    WordDictionary() {
         root = new TrieNode();
    }

    /** Adds a word into the data structure. */
    void addWord(string word) {
        TrieNode* p = root;
        for(char c:word)
        {
            int temp = c-'a';
            if(p->child[temp]==NULL)
            {
                p->child[temp] = new TrieNode();
            }
            p=p->child[temp];
        }
        p->isword = true;
    }

    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    bool search(string word) {
        return helper(word,0,root);
    }

    bool helper(string word,int index,TrieNode* p)
    {
        if(index == word.size())
            return p->isword;
        int temp = word[index] - 'a';
        if(word[index]=='.')
        {
            for(auto child:p->child)
            {
                if(child && helper(word,index+1,child))
                    return true;
            }
            return false;
        } else
            return  p->child[temp]!=NULL && helper(word,index+1,p->child[temp]);
    }
};


int main()
{
    WordDictionary* obj = new WordDictionary();
    vector<string> v = {"a","ab"};
    //["pad"],["bad"],[".ad"],["b.."]];
    for(int i=0;i<v.size();i++)
    {
        obj->addWord(v[i]);
    }
    obj->search("a.");
    obj->search("bad");
    obj->search(".ad");
    obj->search("b..");
}
