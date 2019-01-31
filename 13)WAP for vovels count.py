#WAP to count the number of vowels  present in a string using sets
x=input("enter string: ")
count=0
vowels=set("aeiouAEIOU")
for i in x:
        if i in vowels:
            count += 1 
print("vowels count=")
print(count)            
