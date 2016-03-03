class Solution(object):
    def groupAnagrams(self, strs):
        if not strs: return []

        strs.sort()
        hash_dict = {}
        
        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str not in hash_dict:
                hash_dict[sorted_str] = [str]
            else:
                hash_dict[sorted_str].append(str)

        return hash_dict.values()
