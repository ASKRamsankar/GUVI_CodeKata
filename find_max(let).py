string=input()
let=[]
count=[]
for i in string:
    if i.lower() not in let:
        let.append(i.lower())
        count.append(1)
    else:
        count[let.index(i)]+=1

print(let[count.index(max(count))])
