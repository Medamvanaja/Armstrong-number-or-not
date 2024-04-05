n=1614
temp=n
temp1=n
count=0
sum=0
while n>0:
  n=n//10
  count=count+10
  print(count)
  while temp>0:
    R=temp%10
    sum=sum+(R**count)
    temp=temp//10
    if temp==sum:
      print("armstrong number")
    else:
      print("not a armstrong number")
