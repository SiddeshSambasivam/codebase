def isUnique(string:str) -> bool:
	# Time -> O(n)
	# Space -> O(n)

	charCount = dict()
	for char in string:
		if charCount.get(char):
			return False
		else:
			charCount[char] = 1

	return True

def checkPermutation(str1:str, str2:str) -> bool:

    if len(str1) == 0 or len(str2) == 0:
        return False

    count1 = dict()
    count2 = dict()

    for char in str1:
        if count1.get(char):
            count1[char] += 1
        else:
            count1[char] = 1

    for char in str2:
        if count2.get(char):
            count2[char] += 1
        else:
            count2[char] = 1
	
    if count1 == count2:
        return True
    
    return False


if __name__ == "__main__":
    print(isUnique('tre'))
    print(checkPermutation('', 'abcabc'))