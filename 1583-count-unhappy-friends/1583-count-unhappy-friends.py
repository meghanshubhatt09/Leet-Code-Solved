class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        # person: set of people they prefer over thier partner
        
        dict_pref = dict()
        for x,y in pairs:
            dict_pref[x] = set(preferences[x][:preferences[x].index(y)])
            dict_pref[y] = set(preferences[y][:preferences[y].index(x)])
            
        result = 0
        
        for x in dict_pref:
            for y in dict_pref[x]:
                if x in dict_pref[y]:
                    result+=1
                    break
        
        return result
        