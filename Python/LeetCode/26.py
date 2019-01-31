nums = [0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 5, 6]


# # ----------方法二------------#
# flag = nums[0]
# new = []
# for idx, x in enumerate(nums):
#     print((idx, x))
#     if idx == 0:
#         new.append(x)
#
#     if flag != x:
#         new.append(x)
#         flag = x
#         continue
#
# lens = len(nums)
# print(lens)
# print(new)
#
# # ----------方法二------------#
# nums_set = set(nums)
# nums_res = []
# for k, v in enumerate(nums_set):
#     nums_res.append(v)
#
# print(nums_res)
# ---------------方法三--------------------#
# if len(nums) <= 1:
#     print(len(nums))
# s = 0
# for f in range(1, len(nums)):
#     if nums[s] != nums[f]:
#         s += 1
#         nums[s] = nums[f]
# print(s + 1)
# print(nums[:s + 1])

# TODO  80.删除排序数组中的重复项II


# TODO   88.合并两个有序数组

# #方法一
# class Solution:
#     def merge(self, nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: void Do not return anything, modify nums1 in-place instead.
#         """
#         nums1[m:] = nums2
#         nums1.sort()
#
# s = Solution()
# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3
# s.merge(nums1=nums1, m=m, nums2=nums2, n=n)
# print(nums1)
# TODO 961.重复N次的元素
# A = [5, 1, 5, 2, 5, 3, 5, 4]
# num = len(A)
# N = num / 2
# for i in A:
#     if A.count(i) == N:
#         print(i)
#         break


# class Solution:
#
#     def addDigits(self, num):
#         """
#         :type num: int
#         :rtype: int
#         """
#
#         def sp(a):
#             l = []
#             while a != 0:
#                 l.append(a % 10)
#                 a = a // 10
#             return l
#
#         def cal(l):
#             num = 0
#             for i in l:
#                 num += i
#             return num
#
#         while len(sp(num)) != 0:
#             b = cal(sp(num))
#             num = b
#         return num
#
#
# s = Solution()
# res = s.addDigits(38)
# print(type(res))

509 斐波那契数列


class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        elif N == 1:
            return 1

        return self.fib(N - 1) + self.fib(N - 2)

