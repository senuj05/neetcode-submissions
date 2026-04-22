class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # step 1: creat the hashmap (dictionary in python)
        map={}

        # step 2: loop through each word
        for s in strs:
             #step 3: sort the word to get the key
             key = "".join(sorted(s))

             #step4 : if the key does not excistm, create empty list
             if key not in map:
                map[key] = []

             #step5 : Add original word to the list
             map[key].append(s)

        #step 6: return all the groups
        return list(map.values())
