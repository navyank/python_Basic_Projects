numberNames={0:'Zero',1:'One',2:'Two',3:'Three',4:'four',5:'Five',6:'six',7:'seven',8:'Eight',9:'Nine'}
positionvalues={0:'ones',1:'tens',2:'Hundreds',3:'Thousands',4:'ten thousands',5:'lakhs',6:'ten lakhs',7:'crore',8:'ten crore'}
num=input("enter any number")
result=''
l=len(num)-1
for ch in num:
    key=int(ch)
    value=numberNames[key]
    result=result+' '+value+' '+positionvalues[l]
    l-=1
print("the number is:",num)
print("the number Name is:",result)    