class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> last(128, -1);
        int ml = 0;
        int left = 0;

        for (int i = 0; i<s.size();i++){
            
                if (last[s[i]]>= left){
                    left = last[s[i]]+1;
                }
                last[s[i]]=i;
            

            

            ml = max(ml,i-left+1);
        }
        return ml;
    }
};
