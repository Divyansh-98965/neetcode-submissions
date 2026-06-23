class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #if frequency of each letter in word same anagram 
        big_list = []
        sorted_list = []
        hash_table = {}
        #making a list containg sorted strings that can be used as 
        for i in strs:
            if "".join(sorted(i)) in sorted_list:
                continue

            else:
                result = "".join(sorted(i))
                sorted_list.append(result)
        """now that we have list_for sorted items so we can use
         them as indexes in the dictionary"""
        #empty hash table
        for j in sorted_list:
            hash_table[j] = []
            
        for k in strs:
            for l in sorted_list:
                if ("".join(sorted(k)) == l):
                    hash_table[l].append(k)
        

        for key,value in hash_table.items():
            big_list.append(value)

        return big_list

        
