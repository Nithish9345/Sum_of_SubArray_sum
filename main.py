
class Solution:

    def Sum_of_all_SubArray(self,array):
        Sum=0
        n=len(array)
        for i in range(n):
            """formula ->(i+1)*(n-i) with array element
            """

            Sum+= array[i]*(i+1)*(n-i)
        return Sum

array=list(map(int,input().split()))
object = Solution()
print(object.Sum_of_all_SubArray(array))
