res=[]
s= "10#11#12"
i = 0
while i < len(s):
    if ((i+2) < len(s)) and (s[i+2] == '#'):
        res.append(chr(int(''.join(s[i]+s[i+1]))+96))
        i=i+3
    else:
        res.append(chr(int(s[i])+96))
        i=i+1

print(''.join(res))



# Runtime: 28 ms, faster than 14.53% of Python online submissions for Decrypt String from Alphabet to Integer Mapping.
# Memory Usage: 13.3 MB, less than 23.84% of Python online submissions for Decrypt String from Alphabet to Integer Mapping.

#using regex
# return ''.join(chr(int(i[:2]) + 96) for i in re.findall(r'\d\d#|\d', s))