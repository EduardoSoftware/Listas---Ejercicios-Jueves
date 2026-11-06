def superReducedString(s):
    chars = list(s)
    i = 0
    
    while i < len(chars) - 1:
        if chars[i] == chars[i + 1]:
            del chars[i:i + 2]
            if i > 0:
                i -= 1
        else:
            i += 1
            
    if len(chars) == 0:
        return "Empty String"
    else:
        return "".join(chars)

print(superReducedString("aaabccddd"))
print(superReducedString("aa"))
print(superReducedString("baab"))