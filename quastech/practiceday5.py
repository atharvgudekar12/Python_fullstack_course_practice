str = "maam"

reverse = ''

for i in str:
    reverse = i + reverse
print(reverse)

if str == reverse:
    print("is palindrome")
else:
    print("is not a palindrome")


def palindrome(value):
    rev = ""
    for i in value:
        rev = i + rev
    return rev == value

result = palindrome('man')
print(result)