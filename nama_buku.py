
def input_data():
    nama_buku = input("Masukkan nama buku: ")
    nama_peminjam = input("Masukkan nama peminjam: ")
    jumlah_hari_peminjaman = input("Masukkan jumlah hari peminjaman: ")
    
    return nama_buku, nama_peminjam, jumlah_hari_peminjaman

def tampilkan_data(nama_buku, nama_peminjam, jumlah_hari_peminjaman):
    print("\nInformasi Peminjaman Buku")
    print("=========================")
    print(f"Nama Buku: {nama_buku}")
    print(f"Nama Peminjam: {nama_peminjam}")
    print(f"Jumlah Hari Peminjaman: {jumlah_hari_peminjaman} hari")

def main():
    nama_buku, nama_peminjam, jumlah_hari_peminjaman = input_data()
    tampilkan_data(nama_buku, nama_peminjam, jumlah_hari_peminjaman)

if __name__ == "__main__":
    main()