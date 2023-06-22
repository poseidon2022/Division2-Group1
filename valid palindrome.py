class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)==1 or len(s)==0:
            return True
        my_str = ""
        for i in s:
            if i.isnumeric()==True or i.isalpha()==True:
                if i.isalpha()==True:
                    my_str+=i.lower()
                else:
                    my_str+=i
        return my_str == my_str[::-1]