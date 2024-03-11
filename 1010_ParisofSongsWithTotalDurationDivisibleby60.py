# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#1010. Pairs of Songs With Total Durations Divisible by 60

def numPairsDivisibleBy60(time):
    num = 0
    L= len(time)
    if L==0:
        return 0

    for i in range(L):
        for j in range(i+1,L):

            if (time[i]+time[j])%60==0:
                print(i,j)
                num = num+1
    return num

test = [30,20,150,100,40]
print(numPairsDivisibleBy60(test))