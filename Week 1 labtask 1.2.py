def trailzeroes(A):
    no_ofzeros=0
    while A!=0:
        no_ofzeros+=A/5
        A/=5
    return no_ofzeros
        
n = int(raw_input("Enter a number: "))
print trailzeroes(n)