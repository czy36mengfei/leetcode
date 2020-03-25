class Solution {
public:
   
    int numberOfArithmeticSlices(vector<int>& A) {
        int n = A.size();
        if(n<=2) return 0;
        int res = 0;
        int dp[n];
        dp[0]=0;
        dp[1]=0;
        for(int i=2;i<n;i++)
        {
            if(A[i]-A[i-1]==A[i-1]-A[i-2])
            {
                dp[i]=dp[i-1]+1;
            }
            else
                dp[i]=0;
            res +=dp[i];
        }
        return res;
    }
};