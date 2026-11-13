class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        string_list = []
        
        for char in s:
            if ((char >= "a" and char <= "z") 
                or (char >= "A" and char <= "Z")
                or (char >= "0" and char <= "9")):
                string_list.append(char.lower())

        stripped_string = "".join(string_list)
        
        p1 = 0
        p2 = len(stripped_string) - 1

        while (p2 >= p1):
            if stripped_string[p2] != stripped_string[p1]:
                return False
            p2 -= 1
            p1 += 1
        
        return True
