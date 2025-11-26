class PaketLiburan:
    def _init_(self, nama, harga, kesenangan):
        self.nama = nama
        self.harga = harga
        self.kesenangan = kesenangan
        self.rasio = kesenangan / harga


def greedy_pilih_paket(paket_list, budget):
    paket_sorted = sorted(paket_list, key=lambda x: x.rasio, reverse=True)

    paket_terpilih = []
    total_harga = 0
    total_kesenangan = 0

    for paket in paket_sorted:
        if total_harga + paket.harga <= budget:
            paket_terpilih.append(paket)
            total_harga += paket.harga
            total_kesenangan += paket.kesenangan

    sisa = budget - total_harga if total_harga <= budget else 0
    kurang = total_harga - budget if total_harga > budget else 0

    return paket_sorted, paket_terpilih, total_harga, total_kesenangan, sisa, kurang


# ============================
# ========== MENU =============
# ============================

paket_list = []
budget = 0

while True:
    print("\n==============================")
    print("   MENU GREEDY PAKET LIBURAN")
    print("==============================")
    print("1. Tambah Paket Liburan")
    print("2. Tampilkan Urutan Greedy (berdasarkan rasio)")
    print("3. Masukkan Budget")
    print("4. Hitung Paket Optimal")
    print("5. Keluar")
    print("==============================")

    pilihan = input("Pilih menu: ")

    # ------------------------------------------
    # 1. Input paket
    # ------------------------------------------
    if pilihan == "1":
        nama = input("Nama paket: ")
        harga = int(input("Harga paket: "))
        kesenangan = int(input("Nilai kesenangan (1–10): "))

        paket_list.append(PaketLiburan(nama, harga, kesenangan))
        print(f"Paket '{nama}' berhasil ditambahkan!")

    # ------------------------------------------
    # 2. Tampilkan urutan greedy
    # ------------------------------------------
    elif pilihan == "2":
        if not paket_list:
            print("Belum ada paket.")
            continue

        paket_sorted = sorted(paket_list, key=lambda x: x.rasio, reverse=True)

        print("\nUrutan paket berdasarkan rasio (kesenangan / harga):")
        for p in paket_sorted:
            print(f"- {p.nama} | Harga: {p.harga} | Kesenangan: {p.kesenangan} | Rasio: {p.rasio:.6f}")

    # ------------------------------------------
    # 3. Input budget
    # ------------------------------------------
    elif pilihan == "3":
        budget = int(input("Masukkan budget Anda: "))
        print(f"Budget tersimpan: Rp{budget}")

    # ------------------------------------------
    # 4. Hitung paket optimal
    # ------------------------------------------
    elif pilihan == "4":
        if not paket_list:
            print("Belum ada paket untuk dihitung.")
            continue
        if budget == 0:
            print("Masukkan budget terlebih dahulu!")
            continue

        paket_sorted, paket_terpilih, total_harga, total_kesenangan, sisa, kurang = greedy_pilih_paket(paket_list, budget)

        print("\n=== HASIL OPTIMAL GREEDY ===")
        print("Paket yang terpilih:")

        for p in paket_terpilih:
            print(f"- {p.nama} (Harga: {p.harga}, Kesenangan: {p.kesenangan})")

        print("\nTotal harga:", total_harga)
        print("Total kesenangan:", total_kesenangan)

        if sisa > 0:
            print(f"Sisa budget: Rp{sisa}")
        elif kurang > 0:
            print(f"Budget kurang: Rp{kurang}")
        else:
            print("Budget pas!")

    # ------------------------------------------
    # 5. Keluar
    # ------------------------------------------
    elif pilihan == "5":
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid. Coba lagi.")
