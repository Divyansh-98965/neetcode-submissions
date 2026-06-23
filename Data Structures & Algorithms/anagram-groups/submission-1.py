class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #if frequency of each letter in word same anagram 
        hash_table = {}
        #making a list containg sorted strings that can be used as 
        for i in strs:
            sorted_string = "".join(sorted(i))
            if sorted_string in hash_table:
                hash_table[sorted_string].append(i)
            else:
                hash_table[sorted_string] = [i]
            
        return list(hash_table.values())

        
