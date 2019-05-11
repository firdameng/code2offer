# -*- coding:utf-8 -*-
class Solution:
    def getDigit(self,k):
        s = 0
        while k != 0:
            s = s + k % 10
            k = k // 10
        return s
    def canArrival(self,threshold, rows, cols,i,j):
        global visited
        if i >= 0 and i < rows and j >= 0 and j< cols and  not visited[i * cols + j] and (self.getDigit(i) + self.getDigit(j)) <= threshold:
            visited[i * cols + j] = True
            return 1 + self.canArrival(threshold, rows, cols,i + 1,j) + self.canArrival(threshold, rows, cols,i - 1,j) + self.canArrival(threshold, rows, cols,i,j + 1) + self.canArrival(threshold, rows, cols,i,j - 1)
        return 0
    def movingCount(self, threshold, rows, cols):
        # write code here
        global visited
        
        visited = [False] * rows * cols
        if threshold <= 0 or rows < 0 or cols < 0:
            return 0
        return self.canArrival(threshold, rows, cols,0,0)

# 该题与上一回溯不同,在于探索的是全局可行的区域，返回总数；
# 于是乎，从某一点开始，遇到不可达区域时，返回0即可，可达区域时加1；

# 而上一题时找全局中是否存在可行路径，因而没有找到时，必须回溯原始位置再接着探索。