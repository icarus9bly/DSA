# https://leetcode.com/problems/group-anagrams/
# In this solution basically i tried to convert each string present in the array to a sorted string ( first converted into list then sort and than conveted them to string again) and stored them in the hashmap where key = string and values = its length so that we can get its anagram whose length is same as it along with all the character ( which is sorted so we can easily get them in our map) and other array u in which we save our answer in which we will use length of each string (original one ) as its index . and then when we get the anagram of previously stored string ( which we will know from map) we are gonna store in u array according to its length ( length which we will get from map as well for that particular string).
# complexity = O(n ^ 2)


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        u, f = [], {}
        for i in strs:
            a = ''.join(sorted(list(i)))
            h = len(u)
            if a not in f:
                f[a] = h
                u.append([i])
            else:
                u[f[a]].append(i)
        return u
