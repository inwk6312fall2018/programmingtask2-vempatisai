file=open('Crime.csv')
list=[]
list2=[]
dic1={}
dic2={}
for line in file:
  line=line.strip()
  l=line.split(',')
  list.append(l[-1])
  for words in list:
    if words not in dic1:
      dic1[words]=1
    else:
      dic1[words]+=1
  list2.append(l[-2])
  for words in list2:
    if words not in dic2:
      dic2[words]=1
    else:
      dic2[words]+=1
  print('crime type ' '*20','crime count' '*20')
  for key,value in dic1.items():
    print("{:<20} {:<20}".format(key,value))
