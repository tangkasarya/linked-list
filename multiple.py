class Penulis:
    def __init__(self, nama):
        self.nama = nama
        self.next = None

class Buku:
    def __init__(self, judul, penulis, kategori):
        self.judul = judul
        self.penulis = penulis
        self.kategori = kategori
        self.next = None

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def tambah(self, buku):
        node_baru = Node(buku)
        node_baru.next = self.head
        self.head = node_baru

    def tampilkan(self):
        if not self.head:
            print("Daftar Kosong")
            return

        current = self.head
        while True:
            print("Judul:", current.data.judul)
            print("Penulis:", ', '.join([penulis.nama for penulis in current.data.penulis]))
            print("Kategori:", current.data.kategori)
            print()
            current = current.next
            if current == self.head:
                break

    def pinjam_buku(self, judul):
        if not self.head:
            print("Daftar kosong")
            return False

        current = self.head
        prev_node = None
        ditemukan = False

        while True:
            if current.data.judul == judul:
                if current == self.head and current.next == self.head:
                    self.head = None
                elif current == self.head and current.next != self.head:
                    self.head = current.next
                else:
                    prev_node.next = current.next
                ditemukan = True
                break

            prev_node = current
            current = current.next

            if current == self.head:
                break

        if ditemukan:
            print(f"Buku '{judul}' berhasil dipinjam.")
            return True
        else:
            print(f"Buku '{judul}' tidak ditemukan dalam daftar.")
            return False

if __name__ == "__main__":
    penulis1 = Penulis("John Doe")
    penulis2 = Penulis("Jane Smith")
    penulis3 = Penulis("David Johnson")

    buku1 = Buku("Pemrograman Python", [penulis1], "Pemrograman")
    buku2 = Buku("Struktur Data dan Algoritma", [penulis2, penulis3], "Ilmu Komputer")

    buku_tersedia = CircularLinkedList()
    buku_tersedia.tambah(buku1)
    buku_tersedia.tambah(buku2)

    print("Daftar Buku yang Tersedia untuk Dipinjam:")
    buku_tersedia.tampilkan()

    # Meminjam buku "Pemrograman Python"
    buku_tersedia.pinjam_buku("Pemrograman Python")

    print("\nDaftar Buku yang Tersedia setelah Meminjam:")
    buku_tersedia.tampilkan()
