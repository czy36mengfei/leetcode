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
public:
    // 关健： 找到n和m最高的不同位 将包括其及之后所有位置为0 【所有数字某一位有一个为0，结果该位即为0；m到n遍历过程中不断进位 1->0 】
    int rangeBitwiseAnd(int m, int n) {
        while(n>m)
        {
            n = n&(n-1); // 将最右的1置为0；
        }
        return n;
    }
};
