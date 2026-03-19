class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp=''
        leng=[]

        if s != '':

            for x in s:
                if x in temp:
                    leng.append(len(temp))
                    ind=temp.index(x)
                    temp=temp[ind+1:]
                temp+=x
            if len(leng)==0 or len(temp)>max(leng):
                return len(temp) 
            return max(leng)
        else:
            return 0
