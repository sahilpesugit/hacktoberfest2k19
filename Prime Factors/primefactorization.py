n=int(input("Enter an integer:"))
print("Factors are:")
for i in range(1,n,1):
    while(i<=n):
        k=0
        if(n%i==0):
            j=1
            while(j<=i):
                if(i%j==1):
                    k+=1
                j+=1
            if(k==2):
                print(i)
        i+=1   
