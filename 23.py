class strutils:
    @staticmethod
    def ispalindrome(word):
        stringword = ''.join(i for i in word if i.isalnum()).lower()
        return stringword == stringword[::-1]
    
wordtocheck = "hardee"
if strutils.ispalindrome(wordtocheck):
    print(f"{wordtocheck} palindrome")
else:
    print(f"{wordtocheck} not palindrome")
