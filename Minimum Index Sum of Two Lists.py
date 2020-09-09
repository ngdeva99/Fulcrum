class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        
        m={}
        n={}
        for i in list1:
            if i not in m:
                m[i] = list1.index(i)
        
        
        for j in list2:
            if j in m:
                n[j]=m[j]+list2.index(j)
                
        return [k for k,v in n.iteritems() if v==min(n.values())]
