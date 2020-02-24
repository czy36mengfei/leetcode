//
// Created by zanbo on 2020/2/24.
//

class Solution {

public:
    bool isHappy(int n) {
        unordered_set<int> mySet;
        while(1)
        {
            int num = newNum(n);
            if(num == 1)
                return true;
            if(mySet.find(num)!=mySet.end())
                return false;
            mySet.insert(num);
            n = num;
        }
    }

    int newNum(int x)
    {
        int sum=0;
        while(x)
        {
            sum += pow(x%10,2);
            x /= 10;
        }
        return sum;
    }
};