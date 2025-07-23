# input string
name = input("masukkan nama lengkap anda: ")

# input integer
age = int(input("masukkan umur anda: "))

# input float
height = float(input("masukkan tinggi anda dalam cm: "))

# input boolean
bool_python_input = input("apakan anda suka python? (iya/tidak): ")
bool_python = bool_python_input.lower() == "iya"        # lower untuk menyetarakan ke lower case
                                                        # upper untuk menyetarakan ke upper case

# simpan jawaban dan label ke dalam list
answer = [name, age, height, bool_python]
labels = ["nama", "umur", "tinggi", "suka python"]

# tampilkan hasil tanpa menggunakan perulangan
print("\n===== OUTPUT DATA =====")
print(f"{labels[0]} : {answer[0]}")     # sintaks 'f' untuk mengkonfersi semua tipe data kedalam string
print(f"{labels[1]} : {answer[1]}")
print(f"{labels[2]} : {answer[2]}")
print(f"{labels[3]} : {answer[3]}")

# tampilkan tipe data dari setiap jawaban
print("\n===== TIPE DATA DARI SETIAP JAWABAN =====")
print(f"{labels[0]} : {type(answer[0])}")
print(f"{labels[1]} : {type(answer[1])}")
print(f"{labels[2]} : {type(answer[2])}")
print(f"{labels[3]} : {type(answer[3])}")