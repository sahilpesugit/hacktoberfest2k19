# Armstrong Number
Armstrong number:  A number is called Armstrong number if it is equal to the sum of the cubes of its own digits.
Write a program to generate and check if a number is an Armstrong number.
n=int(input("enter the number:"))
temp=n
while n>0:
    d=n%10
    n=n//10
    sum=sum+pow(d,3)
if sum==temp:
    print("amstrong number.")
else:
    print("not amstrong number.")

Built by [Vamsi Krishna][lk]

[lk]:https://github.com/vamshikrishna10
