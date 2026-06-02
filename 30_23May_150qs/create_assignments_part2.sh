#!/bin/bash

# Q116
cat << 'EOF' > assi116.py
'''116. Check if a string is a valid shuffle of two other strings.'''
# S1 = "xy", S2 = "12", S3 = "x1y2" -> TRUE
s1 = input("Enter String 1: ")
s2 = input("Enter String 2: ")
s3 = input("Enter Shuffle String (String 3): ")

if len(s1) + len(s2) != len(s3):
    print("FALSE")
else:
    i, j, k = 0, 0, 0
    valid = True
    while k < len(s3):
        if i < len(s1) and s3[k] == s1[i]:
            i += 1
        elif j < len(s2) and s3[k] == s2[j]:
            j += 1
        else:
            valid = False
            break
        k += 1
    
    if valid and i == len(s1) and j == len(s2):
        print("TRUE")
    else:
        print("FALSE")
EOF

# Q117
cat << 'EOF' > assi117.py
'''117. Check if a string contains duplicate substrings.'''
# S = "ababa" -> True (e.g., "aba")
s = input("Enter string: ")
found = False

# Try substring lengths from 2 up to half the length of string
for length in range(2, len(s) // 2 + 1):
    for i in range(len(s) - length + 1):
        sub = s[i:i+length]
        # Check if this substring appears again later in the string
        if s.count(sub) > 1:
            print("True (e.g., \"" + sub + "\")")
            found = True
            break
    if found:
        break

if not found:
    print("False")
EOF

# Q118
cat << 'EOF' > assi118.py
'''118. Find the longest repeated substring.'''
# S = "banana" -> "ana"
s = input("Enter string: ")
longest = ""

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        sub = s[i:j]
        if s.count(sub) > 1:
            if len(sub) > len(longest):
                longest = sub

print("Longest repeated substring =", longest)
EOF

# Q119
cat << 'EOF' > assi119.py
'''119. Find the smallest substring containing all vowels.'''
# S = "aeiouy" -> "aeiou"
s = input("Enter string: ")
vowels = "aeiou"
smallest = ""

for i in range(len(s)):
    for j in range(i, len(s)):
        sub = s[i:j+1]
        # Check if all vowels are present
        has_all = True
        for v in vowels:
            if v not in sub.lower():
                has_all = False
                break
        if has_all:
            if smallest == "" or len(sub) < len(smallest):
                smallest = sub

print("Smallest substring with all vowels =", smallest)
EOF

# Q120
cat << 'EOF' > assi120.py
'''120. Find the longest substring containing only vowels.'''
# S = "abaeiouy" -> "aeiou"
s = input("Enter string: ")
vowels = "aeiouAEIOU"
longest = ""
current = ""

for char in s:
    if char in vowels:
        current += char
        if len(current) > len(longest):
            longest = current
    else:
        current = ""

print("Longest vowel-only substring =", longest)
EOF

# Q121
cat << 'EOF' > assi121.py
'''121. Check if a string contains only binary digits (0/1).'''
# S1 = "1010" -> True, S2 = "102" -> False
s = input("Enter string: ")
is_binary = True

if len(s) == 0:
    is_binary = False

for char in s:
    if char != '0' and char != '1':
        is_binary = False
        break

if is_binary:
    print("True")
else:
    print("False")
EOF

# Q122
cat << 'EOF' > assi122.py
'''122. Convert a binary string to decimal.'''
# S = "101" -> 5
s = input("Enter binary string: ")
decimal = 0
valid = True

for char in s:
    if char != '0' and char != '1':
        valid = False
        break
    decimal = decimal * 2 + int(char)

if valid:
    print("Decimal value =", decimal)
else:
    print("Invalid binary string")
EOF

# Q123
cat << 'EOF' > assi123.py
'''123. Convert a decimal number to binary string.'''
# N = 5 -> "101"
n = int(input("Enter decimal number: "))

if n == 0:
    binary = "0"
else:
    binary = ""
    temp = n
    while temp > 0:
        binary = str(temp % 2) + binary
        temp = temp // 2

print("Binary string =", binary)
EOF

# Q124
cat << 'EOF' > assi124.py
'''124. Find the longest common subsequence of two strings.'''
# S1 = "AGGTAB", S2 = "GXTXAYB" -> "GTAB"
s1 = input("Enter String 1: ")
s2 = input("Enter String 2: ")

m, n = len(s1), len(s2)
dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# Reconstruct the string
lcs = ""
i, j = m, n
while i > 0 and j > 0:
    if s1[i-1] == s2[j-1]:
        lcs = s1[i-1] + lcs
        i -= 1
        j -= 1
    elif dp[i-1][j] > dp[i][j-1]:
        i -= 1
    else:
        j -= 1

print("Longest Common Subsequence =", lcs)
EOF

# Q125
cat << 'EOF' > assi125.py
'''125. Find the shortest common supersequence of two strings.'''
# S1 = "AGGTAB", S2 = "GXTXAYB" -> "AGGXTXAYB"
s1 = input("Enter String 1: ")
s2 = input("Enter String 2: ")

m, n = len(s1), len(s2)
dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# Reconstruct the supersequence string
scs = ""
i, j = m, n
while i > 0 and j > 0:
    if s1[i-1] == s2[j-1]:
        scs = s1[i-1] + scs
        i -= 1
        j -= 1
    elif dp[i-1][j] > dp[i][j-1]:
        scs = s1[i-1] + scs
        i -= 1
    else:
        scs = s2[j-1] + scs
        j -= 1

while i > 0:
    scs = s1[i-1] + scs
    i -= 1
while j > 0:
    scs = s2[j-1] + scs
    j -= 1

print("Shortest Common Supersequence =", scs)
EOF

# Q126
cat << 'EOF' > assi126.py
'''126. Print all anagrams of a string.'''
# S = "cat" -> "cat, cta, act, atc, tca, tac"
def get_permutations(string):
    if len(string) <= 1:
        return [string]
    perms = []
    for i in range(len(string)):
        current = string[i]
        remaining = string[:i] + string[i+1:]
        for p in get_permutations(remaining):
            if current + p not in perms:
                perms.append(current + p)
    return perms

s = input("Enter string: ")
results = get_permutations(s)
print("Anagrams:", ", ".join(results))
EOF

# Q127
cat << 'EOF' > assi127.py
'''127. Group words that are anagrams from an array of strings.'''
# Arr = ["eat", "tea", "tan", "ate", "nat"] -> [["eat", "tea", "ate"], ["tan", "nat"]]
s_input = input("Enter words separated by spaces: ")
words = s_input.split()

grouped = []
visited = [False] * len(words)

for i in range(len(words)):
    if not visited[i]:
        current_group = [words[i]]
        visited[i] = True
        
        # Helper to sort characters manually
        w1_sorted = sorted(words[i])
        
        for j in range(i + 1, len(words)):
            if not visited[j] and len(words[i]) == len(words[j]):
                if w1_sorted == sorted(words[j]):
                    current_group.append(words[j])
                    visited[j] = True
        grouped.append(current_group)

print("Grouped Anagrams:", grouped)
EOF

# Q128
cat << 'EOF' > assi128.py
'''128. Check if a string follows a given pattern.'''
# Pattern = "abba", S = "dog cat cat dog" -> TRUE
pattern = input("Enter pattern (e.g., abba): ")
s_input = input("Enter string (e.g., dog cat cat dog): ")
words = s_input.split()

if len(pattern) != len(words):
    print("FALSE")
else:
    valid = True
    # Pairwise cross-validation checking
    for i in range(len(pattern)):
        for j in range(i + 1, len(pattern)):
            # If patterns match, words must match
            if pattern[i] == pattern[j] and words[i] != words[j]:
                valid = False
            # If patterns don't match, words must not match
            if pattern[i] != pattern[j] and words[i] == words[j]:
                valid = False
    
    if valid:
        print("TRUE")
    else:
        print("FALSE")
EOF

# Q129
cat << 'EOF' > assi129.py
'''129. Find the smallest window containing all distinct characters.'''
# S = "aabcbae" -> "aabcbae" -> "aabcde" from snapshot example
s = input("Enter string: ")

# Find all distinct characters in the input string
distinct_chars = []
for char in s:
    if char not in distinct_chars:
        distinct_chars.append(char)

smallest = ""
for i in range(len(s)):
    for j in range(i, len(s)):
        sub = s[i:j+1]
        
        # Check if substring contains all unique characters
        contains_all = True
        for char in distinct_chars:
            if char not in sub:
                contains_all = False
                break
                
        if contains_all:
            if smallest == "" or len(sub) < len(smallest):
                smallest = sub

print("Smallest window containing distinct characters =", smallest)
EOF

# Q130
cat << 'EOF' > assi130.py
'''130. Find the maximum occurring word.'''
# S = "a b a c a" -> 'a'
s = input("Enter string: ")
words = s.split()

max_word = ""
max_count = 0

for w in words:
    count = words.count(w)
    if count > max_count:
        max_count = count
        max_word = w

print("Maximum occurring word =", max_word)
EOF

echo "All assignments (assi116.py to assi130.py) successfully created!"
