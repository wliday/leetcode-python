class Solution(object):
    def groupAnagrams(self, strs):
        if not strs: return []

        result = [[] for _ in range(len(strs))]
        hash_dict = {}

        index = 0
        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str not in hash_dict:
                hash_dict[sorted_str] = index
                result[index].append(str)
                index += 1
            else:
                result[hash_dict[sorted_str]].append(str)

        result = [sorted(x) for x in result if x]

        return result