//time complexity : O(n)
//space complexiy : O(n)
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        for (int i = digits.size() - 1; i >= 0; i--) {
            //if ith digit is 9 change it to 0
            if (digits[i] == 9) {
                digits[i] = 0;
            }
            //if it isn't 9 just sum with 1 and return answer
            else {
                digits[i]++;
                return digits;
            }
        }
        //return a new vector that first index is 1. because other indexes was 9
        digits.insert(digits.begin(), 1);
        return digits;
    }
};