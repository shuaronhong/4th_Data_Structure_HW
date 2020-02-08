class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        def padzero(binnum, Len):
            res = "0" * Len + binnum
            return res[-Len:]

        Len = len(str(bin(max(nums)))) - 2
        res = 0
        trie = {}
        for num in nums:
            binnum = padzero(str(bin(num))[2:], Len)
            node = trie
            xor_node = node
            curr = 0
            for bitnumstr in binnum:
                bit = int(bitnumstr)
                if not bit in node:
                    node[bit] = {}
                node = node[bit]

                toggled_bit = 1 - bit
                if toggled_bit in xor_node:
                    curr = (curr << 1) | 1
                    xor_node = xor_node[toggled_bit]
                else:
                    curr = (curr << 1)
                    xor_node = xor_node[bit]
            res = max(res, curr)
        return res