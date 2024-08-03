class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        m_t = max(target)
        m_a = max(arr)
        if m_a != m_t:
            return False
        l_a = [0] * (m_a+1)
        l_t = [0] * (m_t+1)
        def list_maker(l, l_l):
            for i in l:
                l_l[i] += 1
            return l_l
        l_a = list_maker(arr, l_a)
        l_t = list_maker(target, l_t)
        if l_a == l_t:
            return True
