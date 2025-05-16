# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


# ok before we just start coding on this lets try to think it through
#
# next()
# -> if the current item is a integer
#    -> increment the idx
#    -> return the current item
# 
# -> else (this item is a nested list)
#   -> call next on the nested iterator
#   -> check has next
#       -> if not increment self.idx
# 
# hasNext()
# -> 
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nl = []
        for e in nestedList:
            if e.isInteger():
                self.nl.append(e.getInteger())
            else:
                l = e.getList()
                nI = NestedIterator(l)
                
                if nI.hasNext(): # dont include deep empty lists :)
                    self.nl.append(nI)

        self.idx = 0
        self.N = len(self.nl)
    
    def next(self) -> int:
        curr = self.nl[self.idx]

        if isinstance(curr, int):
            self.idx += 1
            return curr
        else:
            ans = curr.next()

            if not curr.hasNext():
                self.idx += 1
            
            return ans
    
    def hasNext(self) -> bool:
        if self.idx >= self.N:
            return False
        
        if self.idx == self.N-1:
            curr = self.nl[self.idx]
            if isinstance(curr, int):
                return True
            else:
                return curr.hasNext()
        
        return True

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())