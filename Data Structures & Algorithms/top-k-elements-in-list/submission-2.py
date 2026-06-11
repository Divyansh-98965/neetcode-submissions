class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted_nums = sorted(nums, reverse = True)
        frequency_dict = {}
        outp = k

        for i in sorted_nums:
            if i in frequency_dict:
                frequency_dict[i] += 1
            else:
                frequency_dict[i] = 1
        
        return_list = []
        sorted_dict = sorted(frequency_dict.items(), key=lambda item: item[1], reverse = True)
        for key,value in sorted_dict:
            if outp > 0:
                return_list.append(key)
                outp -= 1
        
        return return_list        

        
