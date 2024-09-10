biaya = float(input("masukkan total belanja: "))
mahasiswa = input("apakah kamu seorang mahasiswa (yes/no): ").strip().lower()

if mahasiswa == "yes":
    #menghitung diskon
    diskon = 0.20 * biaya
    hsetelah_diskon = biaya - diskon
    #menghitung pajak
    pajak = 0.05 * hsetelah_diskon
    #total 
    total = hsetelah_diskon + pajak
    print(f"harga yang harus dibayar adalah sebanyak $ {total:.2f}")
elif mahasiswa == "no":
    #menghitung pajak
    pajak = 0.05 * biaya
    #total 
    total = biaya + pajak
    print(f"harga yang harus dibayar adalah sebanyak $ {total:.2f}")