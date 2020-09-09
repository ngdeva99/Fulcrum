class Solution:
    def toLowerCase(self, str: str) -> str:
        a=""
        
        q = 'a'
        print(ord('a'),ord('A'),ord('z'),ord('Z'))
        lower = ord('a')
        lower1 =ord('z')
        upper = ord('A')
        upper1=ord('Z')
        print(ord('&'))
        for i in str:
            if ord(i)<97 and (lower<=ord(i)<=lower1 or upper<=ord(i)<=upper1):
                i = chr(ord(i)+32)
                a+=i
            else:
                a+=i
        return a
