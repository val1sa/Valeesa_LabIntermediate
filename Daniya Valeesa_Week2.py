secret_code = "ikan"
tebakan = ["", "", "", ""]
kesempatan = 6
huruf_terpakai = []

print("Selamat Datang di Mini Game Hangman")

while kesempatan > 0:
    print("Tebakan kata: ", tebakan)
    print("Sisa Kesempatan: ", kesempatan)
    print("Huruf yang sudah dicoba: ", huruf_terpakai)
    
    tebak_huruf = input("Tebak satu huruf: ")
    
    if tebak_huruf in huruf_terpakai:
        print("Tebak huruf lain!")
    else:
     huruf_terpakai.append(tebak_huruf)
        
if tebak_huruf in secret_code:
            print("Benar, Good job!")
           
            if tebak_huruf == "i":
                tebakan[0] = "i"
            if tebak_huruf == "k":
                tebakan[1] = "k"
            if tebak_huruf == "a":
                tebakan[2] = "a"
            if tebak_huruf == "n":
                tebakan[3] = "n"
else:
            print("Salah!")
            kesempatan = kesempatan - 1

if "_" not in tebakan:
        print("Selamat! Kamu menang, katanya adalah:", 
secret_code)

if kesempatan == 0:
    print("You lose! Nyawa habis, well played.")