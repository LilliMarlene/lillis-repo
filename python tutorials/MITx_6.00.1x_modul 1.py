
######### WHILE LOOPS ############

#varA = 2
#varB = 3
#if isinstance(varA, str) or isinstance(varB, str):
#    print("string involved")
#elif varA > varB:
#    print("bigger")
#elif varA == varB:
#    print("equal")
#else:
#    print("smaller")

#var = 0
#while var < 10:
#    var += 2
#    print(var)
#print("Goodbye!")

#var = 12
#print("Hello!")
#while var > 2:
#    var -= 2
#    print(var)

#end = 6
#i = 0
#result = 0
#while i < end:
#    i = 1 + i
#    result = result + i
#print(result)


######### FOR LOOPS ############

#for n in range(2,12,2):
#    print(n)
#print("Goodbye!")
    
#print("Hello!")
#for n in range(10,0,-2):
#    print(n)

#end = 6
#result = 0
#for i in range(end+1):
#    result = result + i
#print (result)


###### PROBLEM SET 1 ###########
#count = 0
#s = 'azcbobobegghakl'
#for char in s:
#    if char in "aeiouAEIOU":
#        count = count + 1
#print (count)


###### PROBLEM SET 2 ###########
#s = 'yooboobbobbobobzoboobbobobrbbobb'
#sb = 'bob'
#results = 0
#sub_len = len(sb)
#for i in range(len(s)):
#    if s[i:i+sub_len] == sb:
#        results += 1
#print('Number of times ',sb,' occurs is: ',results)

###### PROBLEM SET 3 ###########
#s = 'abcbcd'
#longest_substring = ''
#any_substring = ''

#for char in s:
#nimm den ersten buchstaben aus s
#    if any_substring == "":
#        any_substring = char
#schauen ob der nächste buchstabe größer ist als der letzte vom substring
#wenn ja - nimm ihn mit
#    elif any_substring[-1] <= char:
#        any_substring += char
#wenn nein
#schau ob der aktuelle subtring länger als der bisher längste ist
#    elif any_substring[-1] > char:
#        if len(longest_substring) < len(any_substring):
#            longest_substring = any_substring
#            any_substring = char
#und mach in jedem fall weiter mit den nächsten buchstaben
#        else:
#            any_substring = char
#if len(any_substring) > len(longest_substring):
#    longest_substring = any_substring
        
#print('Longest substring in alphabetical order is: ',longest_substring)



