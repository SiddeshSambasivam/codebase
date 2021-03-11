
def lengthOfLongestSubstring(s: str) -> int:

    if not len(s):
        return 0

    # abcabcbbcb
    # {
    #   char: latest seen index
    # }
    # if there is the char is seen before in the past
    #   if so: move the left pointer to the next position
    #   else: add the character to the dict

    seen = dict()
    maxlen = 0
    start = 0

    longest_substring = ""

    for i in range(len(s)):

        if s[i] in seen and start <= seen[s[i]]:
            start = seen[s[i]] + 1
        else:
            # calculate the maximum length
            maxlen =  max(maxlen, i-start+1)
            if len(s[start:i+1]) >= maxlen:
                longest_substring = s[start:i+1]
        
        seen[s[i]] = i

    print(maxlen, longest_substring)

    return maxlen

lengthOfLongestSubstring("tmmzuxt")

