"""
String Slicing: Substrings erzeugen

[<first element to include> : <first element to exclude> : <step> ]

a = "Teststring"
a[start:stop] beginnt bei start und endet bei stop - 1
"""

s = "the quick brown fox"
sub_1 = s[0:5]
print(sub_1) # the q

sub_1 = s[:5]
print(sub_1) # the q

quick = s[4:9]
print(quick) # quick

print(s[:-1]) # the quick brown fo
print(s[-4:-1]) #  fo

print(s[5:]) # von index 5 bis zum Ende
print(s[:]) # von index 0 bis zum Ende

print(s.replace("quick", ""))
print(s.find("quick")) # 4 (Index von quick)
print(s.find(" ", 4 + 1)) # 9 (Index von Leerzeichen nach quick)

numbers = "123456789"
print("Ungerade Zahlen:", numbers[::2])
print("gerade Zahlen:", numbers[1::2])

alpha = "abcdef"
print("umgedreht:", alpha[::-1])

numbers = "123456789"
print("umgedreht:", numbers[::-1])
print("umgedreht:", numbers[4:1:-1]) #543