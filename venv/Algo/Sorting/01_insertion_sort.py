"""
https://www.youtube.com/watch?time_continue=95&v=OGzPmgsI-pQ&feature=emb_logo
"""

mArr = [12, 11, 13, 5, 6]

print('------Before sorting---------')
print(mArr)

for i in range(1, len(mArr)):
    key = mArr[i]
    j = i-1
    while j>=0 and mArr[j]>key:
        mArr[j+1] = mArr[j]
        j = j-1
    mArr[j+1] = key


print('\n------after sorting---------')
print(mArr)