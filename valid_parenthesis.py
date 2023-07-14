class Solution:
    def isValid(self, s: str) -> bool:
        my_bool = True
        demo = list()
        for i in range(len(s)):
            if (s[i] == "(" or s[i]=="{" or s[i]=="[") and (len(s) > i+1) :
                demo.append(s[i])
            elif (s[i] == "(" or s[i]=="{" or s[i]=="[") and (len(s) <= i+1) :
                my_bool = not my_bool
                break
            elif (s[i] == ")" or s[i]=="]" or s[i]=="}") and len(demo)!=0 :
                if s[i]==")" and demo[len(demo)-1]=="(":
                    demo.pop()
                elif s[i]=="]" and demo[len(demo)-1]=="[":
                    demo.pop()
                elif s[i]=="}" and demo[len(demo)-1]=="{":
                    demo.pop()
                else:
                    my_bool = not my_bool
                    break
            else:
                my_bool = not my_bool
                break
        if len(demo)==0:
            return my_bool
        return False