class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m >= n: a, b = nums1, nums2
        else: a, b, m, n = nums2, nums1, n, m

        if (m + n) % 2 == 0: N, flag = int((m + n) / 2) + 1, 0
        else: N, flag = int((m + n) // 2) + 1, 1

        ind = [0]
        for j in range(n):
            i = ind[j]
            while b[j] > a[i]:
                i += 1
                if i > m-1: break
            a.insert(i, b[j])
            ind.append(i)
            m += 1
            if ind[-1] >= N - 1:
                break

        if flag: med = a[N-1]
        else: med = (a[N-2] + a[N-1]) / 2

        return med


test = Solution()
med = test.findMedianSortedArrays([1, 2], [3, 4])
print("The Median is {}".format(med))
