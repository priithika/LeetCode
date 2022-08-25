class Solution:
    def firstnonrepeatingchar(string):
        freq={}

        for x in string:
            freq[x]=freq.get(x,0)+1

        for i in string:
            if freq[i]==1:
                return i

        return -1
    print(firstnonrepeatingchar('abcdabcef'))
    print(firstnonrepeatingchar('abcdabceefdf'))
