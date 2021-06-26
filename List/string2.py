mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
subStr =[ "over" ]
for i in subStr:
    mainStr=mainStr.replace(' '+ i +' ',' ')
print(mainStr)