def input_data():
    nama_buku = input("Masukkan nama buku: ")
    nama_peminjam = input("Masukkan nama peminjam: ")
    while True:
        try:
            jumlah_hari_peminjaman = int(input("Masukkan jumlah hari peminjaman: "))
            if jumlah_hari_peminjaman <= 1:
                raise ValueError("Jumlah hari peminjaman harus lebih dari 1.")
            break
        except ValueError as e:
            print(f"Input tidak valid: {e}. Silakan coba lagi.")
    
    return nama_buku, nama_peminjam, jumlah_hari_peminjaman

def tampilkan_data(nama_buku, nama_peminjam, jumlah_hari_peminjaman):
    print("\nInformasi Peminjaman Buku")
    print("=========================")
    for hari in range(1, jumlah_hari_peminjaman + 1):
        print(f"Hari ke-{hari}: Nama Buku: {nama_buku}, Nama Peminjam: {nama_peminjam}")

    if jumlah_hari_peminjaman > 7:
        print("\nAnda terkena denda.")
    else:
        print("\nPeminjaman dalam masa tenggang.")

def main():
    nama_buku, nama_peminjam, jumlah_hari_peminjaman = input_data()
    tampilkan_data(nama_buku, nama_peminjam, jumlah_hari_peminjaman)

if __name__ == "__main__":
    main()