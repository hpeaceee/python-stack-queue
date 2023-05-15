class TumpukanBuku:
    def __init__(self):
        self.tumpukan = []

    def tambahkan_buku(self, nama_buku, pengarang):
        buku = {'nama_buku': nama_buku, 'pengarang': pengarang}
        self.tumpukan.append(buku)
        print(f"Buku '{nama_buku}' oleh {pengarang} ditambahkan ke dalam tumpukan.")

    def hapus_buku_terakhir(self):
        if len(self.tumpukan) == 0:
            print("Tumpukan buku kosong.")
        else:
            buku_terakhir = self.tumpukan.pop()
            print(f"Buku '{buku_terakhir['nama_buku']}' oleh {buku_terakhir['pengarang']}' dihapus dari tumpukan.")

    def buku_teratas(self):
        if len(self.tumpukan) == 0:
            print("Tumpukan buku kosong.")
        else:
            buku_teratas = self.tumpukan[-1]
            print(f"Buku teratas: '{buku_teratas['nama_buku']}' oleh {buku_teratas['pengarang']}'.")


# Contoh penggunaan program
tumpukan = TumpukanBuku()

while True:
    print("\nMenu:")
    print("1. Tambahkan buku")
    print("2. Hapus buku terakhir")
    print("3. Tampilkan buku teratas")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan Anda (1/2/3/4): ")

    if pilihan == "1":
        nama_buku = input("Masukkan nama buku: ")
        pengarang = input("Masukkan nama pengarang: ")
        tumpukan.tambahkan_buku(nama_buku, pengarang)
    elif pilihan == "2":
        tumpukan.hapus_buku_terakhir()
    elif pilihan == "3":
        tumpukan.buku_teratas()
    elif pilihan == "4":
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")