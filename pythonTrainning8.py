# import unittest

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         seen = {}  # Stores value -> index mapping

#         for i, num in enumerate(nums):
#             complement = target - num
            
#             # Check if the needed complement is already in the dictionary
#             if complement in seen:
#                 return [seen[complement], i]
            
#             # Store current value and its index
#             seen[num] = i
# a = 5 + 6j
# print(a + 6)
# s = r"c:\abc\abc\abc.txt"
# print(s)
# z = "Python is cool "
# print(z.split(" "))
# print("--".join(["python", "is", "cool"]))
# b = [1,2,3]
# c = [4,5]
# print(b*2)
# print(c+b)
# d = [x*2 for x in b]
# print(d)
# e = (5)
# f = (5, )
# print(type(e))
# print(type(f))
# i = 0 
# while i<9:
#     i+=1
#     if i == 3:
#         print("Skip this loop")
#         break

#     print(i)
# else:
#         print("Loop ends")
# def tri_recursion(k):
#      if(k > 0):
#           result = k + tri_recursion(k-1)
#           print(result)
#      else:
#           result = 0
#      return result
# tri_recursion(6)
 
# import sys
# print(sys.path)
# print(sys.platform)
# import numpy as np
# a = np.array([1,2,3])
# b = np.array([2,3,4])
# c = a * b
# d = np.array([[1,2,3],[2,3,4]])
# e = d * 2
# print(e)
# print(c)
# f = np.zeros(5, dtype=int)
# g = np.ones(5, dtype=int)
# print(f)
# print(g)
# h = np.full(8, 6.6667)
# i = np.arange(1,25,1)
# j = i.reshape(3,8)
# print(i)
# print(j)
# print(a.size)
# print(a.ndim)
# print(a.shape)
# print(a.dtype)
# import matplotlib as plt
# x = np.



import matplotlib.pyplot as plt
x = [1, 2, 4]
y = [ 4, 6, 3]
names = ["class 1", "class 2", "class 3"]
plt.plot(x,y)
print(plt.xticks(x, names))
print(plt.bar(x,y, colors=['b', "r", "g"]))

