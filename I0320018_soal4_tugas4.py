usia = int(input("Berapa usia kamu? "))
lulusUjian = input("Apakah Anda sudah lulus ujian kualifikasi (Y/T)? ")

if usia >= 21:
    if lulusUjian.upper() == 'Y':
        print("Anda dapat mendaftar di kursus")
    else:
        print("Anda tidak dapat mendaftar di kursus")
else:
    print("Anda tidak dapat mendaftar di kursus")
