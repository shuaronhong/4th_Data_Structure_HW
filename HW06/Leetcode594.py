class Solution:
    """
    @param: source: A source string
    @param: target: A target string
    @return: An integer as index
    """

    def strStr2(self, source, target):
        def preprocess(target):
            # check the longest length of proper prefix that is also a suffix for each substring
            lps = [0] * len(target)
            end_idx = 1
            prefix_idx = 0
            while end_idx < len(target):
                if target[prefix_idx] == target[end_idx]:
                    lps[end_idx] = prefix_idx + 1
                    prefix_idx += 1
                    end_idx += 1
                else:
                    if prefix_idx != 0:
                        prefix_idx = lps[prefix_idx - 1]
                    else:
                        lps[end_idx] = 0
                        end_idx += 1
            return lps

        def KMP(source, target):
            lps = preprocess(target)
            i = 0
            j = 0
            while i < len(source):
                if source[i] == target[j]:
                    i += 1
                    j += 1
                    if j == len(target):
                        return i - len(target)
                else:
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        i += 1

            return -1

        if source is None or target is None:
            return -1
        if target == "":
            return 0
        return KMP(source, target)