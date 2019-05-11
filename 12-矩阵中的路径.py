# -*- coding:utf-8 -*-
class Solution:
    def findpath(self,matrix,rows,cols,i,j,path):
        global visited
        index = i * cols + j 
        if not path:
            return True
        haspath = False
        if i >= 0 and i < rows and j >= 0 and j < cols and not visited[index] and matrix[index] == path[0]:
            visited[index] = True
            haspath = self.findpath(matrix,rows,cols,i + 1,j,path[1:]) or self.findpath(matrix,rows,cols,i - 1,j,path[1:]) or self.findpath(matrix,rows,cols,i,j + 1,path[1:]) or self.findpath(matrix,rows,cols,i,j - 1,path[1:])
            if not haspath:
                visited[index] = False
        return haspath

    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix or not path:
            return False
        global visited
        visited = [False] * rows * cols
        for i in xrange(rows):
            for j in xrange(cols):
                if self.findpath(matrix,rows,cols,i,j,path):
                    return True
        return False

# 寻找最优路径时，回溯法的精髓在于：

#1）尝试不成功时，能够回退原先版本


#if not haspath:
    # visited[index] = False

# 这2行代码就完成了回退。

