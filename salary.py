bs=int(input("enter the basic salary:"))
if bs<10000:
    da=bs*0.25
    hr=bs*0.3
    pf=bs*0.08
elif bs>=10000 and bs<20000:
    da=bs*0.20
    hr=bs*0.25
    pf=bs*0.06
elif bs>=20000 and bs<30000:
    da=bs*0.15
    hr=bs*0.2
    pf=bs*0.04        
else:
    da=bs*0.10
    hr=bs*0.15
    pf=bs*0.02
ns=bs+da+hr-pf
print("Basic salary",bs)        
print("DA",da)
print("HRA",hr)
print("pf",pf)
print("net salary",ns)