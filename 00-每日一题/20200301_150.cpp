//
// Created by zanbo on 2020/3/2.
//
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> myStack;
        int res = 0;
        for(auto s:tokens)
        {
            //如果不是运算符 直接入栈
            if(s!="+" && s!="-" && s!="*" && s!="/")
            {
                myStack.push(atoi(s.c_str()));
            } else{
                //弹出两个值进行运算 结果再入栈
                int num1 = myStack.top();
                myStack.pop();
                int num2 = myStack.top();
                myStack.pop();
                myStack.push(cal(num1,num2,s));
            }
        }
        return myStack.top();
    }

    int cal(int num1_int, int num2_int, string opereator){
        switch(opereator[0]){
            case '+':
                return num1_int+num2_int;
            case '-':
                return num2_int-num1_int;
            case '*':
                return num1_int*num2_int;
            case '/':
                return num2_int/num1_int;
        }
        return 0;
    }
};
