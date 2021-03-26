import calc_bmi

print("BMIを計算するよ!")
d = int(input("体重(kg):"))
s = float(input("身長(m):"))
print(f"あなたのBMIは{calc_bmi.get_bmi(d,s)}です")
print(f"bmiは{calc_bmi.get_bmi(d,s)}です")
