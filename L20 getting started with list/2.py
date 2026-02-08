l = [4,5,2,9,10,8,7]
count = 0
for i in l: 
    count += 1 
avg = count/len(l)
print(f"The sum = {count}")
print(f"The average = {avg}")

l.sort()
print((f"Smallest element is ",l[0]))
print((f"Largest element is ",l[-1]))

