"""

"""

S = [4, 3, 6, 2, 8]
def linear_sum(S, n):
    if n==0:
        return 0
    else:
        return linear_sum(S, n-1) + S[n-1]
print("Sum: ", linear_sum(S, 5))

S1 = [4, 3, 6, 2, 8, 9, 5]

def reverse(S, start, stop):
    if start<stop-1:
        S[start], S[stop-1] = S[stop-1], S[start] #reverse
        reverse(S, start+1, stop-1)
reverse(S1, 0, len(S1))
print(S1)