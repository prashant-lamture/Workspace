# print("Hello World")
# a="python"
# x=list(a)
# print(x)
# a=[2,10.15,"python"]
# print (a[2]) #accesing
# a[2]="java"
# print (a[2]) #modifier


# Dictionary...// Use Key & Value Pair

# a={ 1:"a","b":2,3:"a"}
# print(a.keys())
# print(a.values())


# EVEN/ODD NUMBER

# num=int(input("Enter Number")) #TAKE INPUT FROM USER
# while
# if num%2==0:
#     print("Even Number: ")
# else:
#     print("Odd Numeber: ")


# ONLY ODD NUMBERS
# i=1
# n=int(input("Enter Number")) #TAKE INPUT FROM USER
# while i<=n:
#     if i%2 !=0:
#         print(i)
#         i=i+1


########
# x=[1,2]
# y=[4,5]
# for i in x:
#     for j in y:
#       print(i,j)


# SUBTRACTION OPERATOR

# val1 = 20
# val2 = 10
# yes = val1-val2
# print(yes)


# BREAK STATEMENT

# for b in range(10):
#     if b>5:
#         break
#     print(b)

# SLICING OPERATOR

# n=str(input("Enter String: "))
# print("Original String")
# print(n)
# print("After InterChanging: ")
# print(n[-1]+n[1:-1]+n[0])



# FUNCTION DEFINITION 

# def calculate_sum(a,b): #PARAMETES
#     return a*b
# sum = calculate_sum(10,5) #FUNCTION CALL; ARGUMENTS
# print(sum)


# Updating List

# list2=['prashant','lamture','16-Dec',2003]
# print("Details :")
# print(list2)
# list2[2]="17-Dec"
# print(list2)

# Insert value

# List3=['Prashant','Athnag']
# List3.append("Riyansh")
# print(List3)


# Delete Value

# list4=['Athang','Riyansh','Shiva']
# print(list4)
# print("After Deleting :")
# list4.remove('Shiva')
# print(list4)

# Count()Method

#list5=['p','r','a','s','h','a','n','t','l','a','m','t','u','r','e']
#print(list5.count('t'))

# for i in range(1, 5):
#     for j in range(1, i+1):
#         print('*', end='  ')
#         print()



n = int(input("Enter a number: ")) 
sum = 0
length = len(str(n))
temp = n

while temp > 0:
    digit = temp % 10
    sum += digit ** length
    temp //= 10

if sum == n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")


