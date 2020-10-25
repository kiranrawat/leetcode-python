res=[]
s= "10#11#12"
mydict = {'1':'a', '2':'b','3':'c','4':'d',
            '5':'e','6':'f','7':'g','8':'h',
            '9':'i','10#':'j','11#':'k',
            '12#':'l', '13#':'m', '14#':'n', 
            '15#':'o', '16#':'p',  '17#':'q', 
            '18#':'r','19#':'s', '20#':'t',
            '21#':'u', '22#':'v', '23#':'w',
            '24#':'x', '25#':'y','26#':'z'}
i = 0
while i < len(s):
    if ((i+2) < len(s)) and (s[i+2] == '#'):
        res.append(mydict[''.join(s[i]+s[i+1]+s[i+2])])
        i=i+3
    else:
        res.append(mydict[s[i]])
        i=i+1

print(''.join(res))


# Runtime: 20 ms, faster than 70.06% of Python online submissions for Decrypt String from Alphabet to Integer Mapping.
# Memory Usage: 13.5 MB, less than 23.84% of Python online submissions for Decrypt String from Alphabet to Integer Mapping.