class Solution {
public:
    bool isPalindrome(int x) {
      int remainder = 0, orignal = x;
      long int reverseForm = 0;
      while (x > 0) {
          remainder = x % 10;
          reverseForm = (reverseForm * 10) + remainder;
          x = x / 10;
      }
      if (orignal == reverseForm) {
          return true;
      }
      return false;   
    }
};