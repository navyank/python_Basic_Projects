bus={
    "Routeno":5,
    "Driver":"Krishna",
    "Cleaner":"Manu",
    "points":["karamana","PMG","pattom"]

}
print(bus["Driver"])
print(bus.get("Driver"))
print(bus.keys())
print(bus.values())
print(bus.items())
bus["color"]="Red"

bus["Driver"]="Mohan"
print(bus)
# bus.pop("fare")########key error since fare key is not present
bus.popitem()
print(bus)

for x in bus:
    print(x)############x is key
for x in bus:
    print(bus[x]) #######bus[x]  is value  
# del bus["fare"]###############key error
bus.clear()
print(bus)
del bus