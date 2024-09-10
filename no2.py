#input berat dan tinggi badan 
berat = float(input("masukkan berat badan dalam pounds: "))
tinggi = float(input("masukkan tinggi badan dalam inc: "))

#rumus perhitungan 
bmi = float ((703 * berat) / (tinggi**2))

if bmi < 18.5:
    print(f"{bmi:.1f}")
    print("underweight")
elif 18.5 <= bmi <= 24.9:
    print(f"{bmi:.1f}")
    print("normal")
elif 25.0 <= bmi <= 29.9:
    print(f"{bmi:.1f}")
    print("overweight")
elif bmi >= 30.0:
    print(f"{bmi:.1f}")
    print("obese")

