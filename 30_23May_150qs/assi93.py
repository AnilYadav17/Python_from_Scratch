'''93 Match strings with wildcard characters ($\*$, ?).'''
#Pattern = "a?c", Text = "axcde"   -> TRUE

p = input("Enter pattern: ")
t = input("Enter text: ")
ch = input("")
symbol = "$\*, ?"

for i in p:
    for j in t:
        if i==j:


INCOMPLETE