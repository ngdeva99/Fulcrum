class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        if K == 0 or len(A) < K:
            return 0
        res = 0
        left, left_k = 0, 0
        counter = dict()
        for right in range(len(A)):
            counter[A[right]] = counter.get(A[right], 0) + 1
            if len(counter) == K + 1:
                counter.pop(A[left_k])
                left_k += 1
                left = left_k
            if len(counter) == K:
                while counter[A[left_k]] > 1:
                    counter[A[left_k]] -= 1
                    left_k += 1
                res += left_k - left + 1
        return res
