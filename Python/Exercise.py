Weight = input("Weight: ")
Type = input("(K)gs or (L)bs: ")

if Type.upper() == "K":
    converted = float(Weight) / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = float(Weight) * 0.45
    print("Weight in Kgs: " + str(converted))