a = ["Hello", "Hallo", "Settings", "Einstellungen"]
b = 1
while True:
    if b%2==0: #if b is divisible with 2 (Every Second)
        print(a[b]) 
        b = b + 1
    else: #If b isn't divisible by 2
        b=b+1 
