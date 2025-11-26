import json
import os
from datetime import datetime


class PaketLiburan:
    """Class untuk merepresentasikan paket liburan"""
    
    def _init_(self, nama, harga, kesenangan, kategori="Umum"):
        self.nama = nama
        self.harga = harga
        self.kesenangan = kesenangan
        self.kategori = kategori
        self.rasio = kesenangan / harga if harga > 0 else 0
    
    def _repr_(self):
        return f"{self.nama} | Rp{self.harga:,} | Kesenangan: {self.kesenangan} | Rasio: {self.rasio:.4f}"
    
    def to_dict(self):
        """Convert object ke dictionary"""
        return {
            'nama': self.nama,
            'harga': self.harga,
            'kesenangan': self.kesenangan,
            'kategori': self.kategori,
            'rasio': self.rasio
        }


class SistemPaketLiburan:
    """Sistem manajemen paket liburan dengan algoritma Greedy"""
    
    def _init_(self):
        self.paket_tersedia = []
        self.paket_terpilih = []
        self.budget = 0
        self.total_harga = 0
        self.total_kesenangan = 0
    
    def tambah_paket(self, nama, harga, kesenangan, kategori="Umum"):
        """Menambahkan paket liburan baru"""
        paket = PaketLiburan(nama, harga, kesenangan, kategori)
        self.paket_tersedia.append(paket)
        print(f"✓ Paket '{nama}' berhasil ditambahkan!")
    
    def load_paket_default(self):
        """Load paket liburan default"""
        default_paket = [
            ("Pantai Kuta", 500000, 80, "Pantai"),
            ("Gunung Bromo", 750000, 95, "Gunung"),
            ("Taman Mini Indonesia", 200000, 50, "Taman"),
            ("Floating Market", 150000, 45, "Kuliner"),
            ("Kebun Raya Bogor", 100000, 35, "Taman"),
            ("Museum Angkut", 300000, 70, "Museum"),
            ("Desa Wisata Ubud", 250000, 60, "Budaya"),
            ("Kampung Warna-warni", 180000, 55, "Seni"),
            ("Taman Safari", 350000, 75, "Hewan"),
            ("Pantai Parangtritis", 120000, 40, "Pantai"),
        ]
        
        for nama, harga, kesenangan, kategori in default_paket:
            self.tambah_paket(nama, harga, kesenangan, kategori)
    
    def input_paket_manual(self):
        """Input paket liburan secara manual"""
        print("\n" + "="*70)
        print("INPUT PAKET LIBURAN MANUAL")
        print("="*70)
        
        while True:
            try:
                nama = input("\nNama Paket (atau 'selesai' untuk berhenti): ").strip()
                if nama.lower() == 'selesai':
                    break
                
                harga = int(input("Harga Paket (Rp): "))
                kesenangan = int(input("Nilai Kesenangan (1-100): "))
                kategori = input("Kategori (optional): ").strip() or "Umum"
                
                if harga <= 0 or kesenangan <= 0:
                    print("❌ Harga dan kesenangan harus lebih dari 0!")
                    continue
                
                self.tambah_paket(nama, harga, kesenangan, kategori)
                
            except ValueError:
                print("❌ Input tidak valid! Masukkan angka yang benar.")
            except KeyboardInterrupt:
                print("\n\n⚠  Input dibatalkan.")
                break
    
    def set_budget(self, budget):
        """Set budget untuk liburan"""
        if budget <= 0:
            print("❌ Budget harus lebih dari 0!")
            return False
        self.budget = budget
        print(f"✓ Budget diset: Rp{budget:,}")
        return True
    
    def greedy_pilih_paket(self):
        """Algoritma Greedy untuk memilih paket optimal"""
        if not self.paket_tersedia:
            print("❌ Tidak ada paket tersedia!")
            return
        
        if self.budget <= 0:
            print("❌ Budget belum diset!")
            return
        
        # Reset hasil sebelumnya
        self.paket_terpilih = []
        self.total_harga = 0
        self.total_kesenangan = 0
        
        # STEP 1: Sorting berdasarkan rasio (descending)
        paket_sorted = sorted(self.paket_tersedia, key=lambda x: x.rasio, reverse=True)
        
        print("\n" + "="*70)
        print("PROSES ALGORITMA GREEDY")
        print("="*70)
        print(f"Budget: Rp{self.budget:,}\n")
        
        # STEP 2: Greedy selection
        for i, paket in enumerate(paket_sorted, 1):
            print(f"[{i}] Evaluasi: {paket.nama}")
            print(f"    Harga: Rp{paket.harga:,} | Kesenangan: {paket.kesenangan} | Rasio: {paket.rasio:.4f}")
            
            if self.total_harga + paket.harga <= self.budget:
                self.paket_terpilih.append(paket)
                self.total_harga += paket.harga
                self.total_kesenangan += paket.kesenangan
                print(f"    ✓ DIPILIH! Sisa budget: Rp{self.budget - self.total_harga:,}")
            else:
                print(f"    ✗ Budget tidak cukup (butuh Rp{paket.harga:,}, tersisa Rp{self.budget - self.total_harga:,})")
            print()
        
        print("="*70)
        print("ALGORITMA SELESAI!")
        print("="*70)
    
    def tampilkan_hasil_optimal(self):
        """Menampilkan hasil pemilihan paket optimal"""
        if not self.paket_terpilih:
            print("\n❌ Belum ada paket terpilih. Jalankan algoritma Greedy terlebih dahulu!")
            return
        
        print("\n" + "="*70)
        print("HASIL OPTIMAL - PAKET LIBURAN TERPILIH")
        print("="*70)
        
        print(f"\n{'No':<4} {'Nama Paket':<25} {'Harga':<15} {'Kesenangan':<12} {'Rasio':<10} {'Kategori'}")
        print("-"*85)
        
        for i, paket in enumerate(self.paket_terpilih, 1):
            print(f"{i:<4} {paket.nama:<25} Rp{paket.harga:<13,} {paket.kesenangan:<12} {paket.rasio:<10.4f} {paket.kategori}")
        
        print("-"*85)
        print(f"\n📊 RINGKASAN:")
        print(f"   Total Paket         : {len(self.paket_terpilih)}")
        print(f"   Total Biaya         : Rp{self.total_harga:,}")
        print(f"   Budget Awal         : Rp{self.budget:,}")
        print(f"   Sisa Budget         : Rp{self.budget - self.total_harga:,}")
        print(f"   Total Kesenangan    : {self.total_kesenangan}")
        print(f"   Efisiensi Budget    : {(self.total_harga/self.budget)*100:.2f}%")
        print(f"   Rata-rata Kesenangan: {self.total_kesenangan/len(self.paket_terpilih):.2f}")
        print("="*70)
    
    def cek_urutan_paket(self):
        """Menampilkan urutan paket berdasarkan berbagai kriteria"""
        if not self.paket_tersedia:
            print("\n❌ Tidak ada paket tersedia!")
            return
        
        print("\n" + "="*70)
        print("CEK URUTAN PAKET")
        print("="*70)
        
        print("\n⿡  URUTAN BERDASARKAN RASIO (Greedy Strategy):")
        print("-"*70)
        sorted_rasio = sorted(self.paket_tersedia, key=lambda x: x.rasio, reverse=True)
        for i, paket in enumerate(sorted_rasio, 1):
            status = "✓ TERPILIH" if paket in self.paket_terpilih else ""
            print(f"{i}. {paket} {status}")
        
        print("\n⿢  URUTAN BERDASARKAN HARGA (Termurah → Termahal):")
        print("-"*70)
        sorted_harga = sorted(self.paket_tersedia, key=lambda x: x.harga)
        for i, paket in enumerate(sorted_harga, 1):
            status = "✓ TERPILIH" if paket in self.paket_terpilih else ""
            print(f"{i}. {paket} {status}")
        
        print("\n⿣  URUTAN BERDASARKAN KESENANGAN (Tertinggi → Terendah):")
        print("-"*70)
        sorted_kesenangan = sorted(self.paket_tersedia, key=lambda x: x.kesenangan, reverse=True)
        for i, paket in enumerate(sorted_kesenangan, 1):
            status = "✓ TERPILIH" if paket in self.paket_terpilih else ""
            print(f"{i}. {paket} {status}")
    
    def cek_budget(self):
        """Menampilkan informasi budget detail"""
        print("\n" + "="*70)
        print("INFORMASI BUDGET")
        print("="*70)
        
        print(f"\n💰 Budget Awal         : Rp{self.budget:,}")
        print(f"💸 Total Terpakai      : Rp{self.total_harga:,}")
        print(f"💵 Sisa Budget         : Rp{self.budget - self.total_harga:,}")
        print(f"📊 Persentase Terpakai : {(self.total_harga/self.budget)*100:.2f}%")
        
        sisa = self.budget - self.total_harga
        if sisa > 0:
            print(f"\n✅ Anda masih punya sisa budget Rp{sisa:,}")
            print("\n🔍 Paket yang bisa ditambahkan dengan sisa budget:")
            paket_bisa_ditambah = [p for p in self.paket_tersedia 
                                   if p not in self.paket_terpilih and p.harga <= sisa]
            
            if paket_bisa_ditambah:
                paket_bisa_ditambah.sort(key=lambda x: x.rasio, reverse=True)
                for i, paket in enumerate(paket_bisa_ditambah[:5], 1):
                    print(f"   {i}. {paket}")
            else:
                print("   Tidak ada paket lain yang bisa ditambahkan.")
        else:
            print("\n✅ Budget terpakai optimal!")
    
    def upgrade_paket(self):
        """Fitur upgrade paket dengan menukar paket yang sudah dipilih"""
        if not self.paket_terpilih:
            print("\n❌ Belum ada paket terpilih untuk di-upgrade!")
            return
        
        print("\n" + "="*70)
        print("UPGRADE PAKET")
        print("="*70)
        
        print("\n📦 Paket yang sudah dipilih:")
        for i, paket in enumerate(self.paket_terpilih, 1):
            print(f"{i}. {paket}")
        
        try:
            pilih = int(input("\nPilih nomor paket yang ingin di-upgrade (0 untuk batal): "))
            
            if pilih == 0:
                print("Upgrade dibatalkan.")
                return
            
            if pilih < 1 or pilih > len(self.paket_terpilih):
                print("❌ Nomor tidak valid!")
                return
            
            paket_lama = self.paket_terpilih[pilih - 1]
            print(f"\nAnda memilih: {paket_lama.nama}")
            
            # Hitung budget tersedia untuk upgrade
            budget_upgrade = self.budget - self.total_harga + paket_lama.harga
            
            print(f"\n💰 Budget tersedia untuk upgrade: Rp{budget_upgrade:,}")
            print("\n🔍 Paket alternatif yang tersedia:")
            
            paket_alternatif = [p for p in self.paket_tersedia 
                               if p not in self.paket_terpilih and p.harga <= budget_upgrade]
            
            if not paket_alternatif:
                print("❌ Tidak ada paket alternatif yang tersedia dalam budget.")
                return
            
            # Urutkan berdasarkan kesenangan
            paket_alternatif.sort(key=lambda x: x.kesenangan, reverse=True)
            
            for i, paket in enumerate(paket_alternatif[:10], 1):
                selisih = paket.kesenangan - paket_lama.kesenangan
                simbol = "⬆" if selisih > 0 else "⬇"
                print(f"{i}. {paket} | Selisih kesenangan: {simbol} {abs(selisih)}")
            
            pilih_baru = int(input("\nPilih nomor paket baru (0 untuk batal): "))
            
            if pilih_baru == 0:
                print("Upgrade dibatalkan.")
                return
            
            if pilih_baru < 1 or pilih_baru > len(paket_alternatif):
                print("❌ Nomor tidak valid!")
                return
            
            paket_baru = paket_alternatif[pilih_baru - 1]
            
            # Lakukan upgrade
            self.paket_terpilih[pilih - 1] = paket_baru
            self.total_harga = self.total_harga - paket_lama.harga + paket_baru.harga
            self.total_kesenangan = self.total_kesenangan - paket_lama.kesenangan + paket_baru.kesenangan
            
            print(f"\n✅ Upgrade berhasil!")
            print(f"   {paket_lama.nama} ➡  {paket_baru.nama}")
            print(f"   Selisih harga: Rp{paket_baru.harga - paket_lama.harga:,}")
            print(f"   Selisih kesenangan: {paket_baru.kesenangan - paket_lama.kesenangan}")
            
        except ValueError:
            print("❌ Input tidak valid!")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def export_hasil(self, filename="hasil_paket_liburan.json"):
        """Export hasil ke file JSON"""
        if not self.paket_terpilih:
            print("\n❌ Tidak ada hasil untuk di-export!")
            return
        
        data = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'budget': self.budget,
            'total_harga': self.total_harga,
            'total_kesenangan': self.total_kesenangan,
            'sisa_budget': self.budget - self.total_harga,
            'efisiensi': (self.total_harga/self.budget)*100,
            'paket_terpilih': [p.to_dict() for p in self.paket_terpilih]
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        
        print(f"\n✅ Hasil berhasil di-export ke '{filename}'")
    
    def tampilkan_statistik(self):
        """Menampilkan statistik lengkap"""
        if not self.paket_tersedia:
            print("\n❌ Tidak ada data paket!")
            return
        
        print("\n" + "="*70)
        print("STATISTIK PAKET LIBURAN")
        print("="*70)
        
        total_paket = len(self.paket_tersedia)
        total_terpilih = len(self.paket_terpilih)
        
        print(f"\n📊 STATISTIK UMUM:")
        print(f"   Total paket tersedia : {total_paket}")
        print(f"   Total paket terpilih : {total_terpilih}")
        print(f"   Persentase terpilih  : {(total_terpilih/total_paket)*100:.2f}%")
        
        if self.paket_tersedia:
            harga_list = [p.harga for p in self.paket_tersedia]
            kesenangan_list = [p.kesenangan for p in self.paket_tersedia]
            rasio_list = [p.rasio for p in self.paket_tersedia]
            
            print(f"\n💰 STATISTIK HARGA:")
            print(f"   Termurah  : Rp{min(harga_list):,}")
            print(f"   Termahal  : Rp{max(harga_list):,}")
            print(f"   Rata-rata : Rp{sum(harga_list)/len(harga_list):,.2f}")
            
            print(f"\n😊 STATISTIK KESENANGAN:")
            print(f"   Terendah  : {min(kesenangan_list)}")
            print(f"   Tertinggi : {max(kesenangan_list)}")
            print(f"   Rata-rata : {sum(kesenangan_list)/len(kesenangan_list):.2f}")
            
            print(f"\n📈 STATISTIK RASIO:")
            print(f"   Terendah  : {min(rasio_list):.4f}")
            print(f"   Tertinggi : {max(rasio_list):.4f}")
            print(f"   Rata-rata : {sum(rasio_list)/len(rasio_list):.4f}")
        
        if self.paket_terpilih:
            kategori_count = {}
            for paket in self.paket_terpilih:
                kategori_count[paket.kategori] = kategori_count.get(paket.kategori, 0) + 1
            
            print(f"\n🏷  DISTRIBUSI KATEGORI (Paket Terpilih):")
            for kategori, count in sorted(kategori_count.items(), key=lambda x: x[1], reverse=True):
                print(f"   {kategori:<15} : {count} paket")


def tampilkan_menu():
    """Menampilkan menu utama"""
    print("\n" + "="*70)
    print("SISTEM PEMILIHAN PAKET LIBURAN - ALGORITMA GREEDY")
    print("="*70)
    print("\n📋 MENU UTAMA:")
    print("   1. Input Paket Liburan Manual")
    print("   2. Load Paket Default")
    print("   3. Set Budget")
    print("   4. Jalankan Algoritma Greedy (Pilih Paket Optimal)")
    print("   5. Tampilkan Hasil Optimal")
    print("   6. Cek Urutan Paket")
    print("   7. Cek Budget & Sisa")
    print("   8. Upgrade Paket")
    print("   9. Tampilkan Statistik")
    print("   10. Export Hasil ke JSON")
    print("   0. Keluar")
    print("="*70)


def main():
    """Fungsi utama program"""
    sistem = SistemPaketLiburan()
    
    print("\n")
    print("="*70)
    print(" SELAMAT DATANG DI SISTEM PEMILIHAN PAKET LIBURAN ".center(70))
    print("="*70)
    print("\n🎯 Program ini menggunakan Algoritma Greedy untuk memilih")
    print("   paket liburan optimal berdasarkan rasio kesenangan/harga\n")
    
    while True:
        tampilkan_menu()
        
        try:
            pilihan = input("\n➡  Pilih menu (0-10): ").strip()
            
            if pilihan == '1':
                sistem.input_paket_manual()
            
            elif pilihan == '2':
                sistem.load_paket_default()
                print(f"✓ Berhasil load {len(sistem.paket_tersedia)} paket default!")
            
            elif pilihan == '3':
                try:
                    budget = int(input("\nMasukkan budget (Rp): "))
                    sistem.set_budget(budget)
                except ValueError:
                    print("❌ Input budget tidak valid!")
            
            elif pilihan == '4':
                sistem.greedy_pilih_paket()
            
            elif pilihan == '5':
                sistem.tampilkan_hasil_optimal()
            
            elif pilihan == '6':
                sistem.cek_urutan_paket()
            
            elif pilihan == '7':
                sistem.cek_budget()
            
            elif pilihan == '8':
                sistem.upgrade_paket()
            
            elif pilihan == '9':
                sistem.tampilkan_statistik()
            
            elif pilihan == '10':
                filename = input("Nama file (default: hasil_paket_liburan.json): ").strip()
                if not filename:
                    filename = "hasil_paket_liburan.json"
                sistem.export_hasil(filename)
            
            elif pilihan == '0':
                print("\n" + "="*70)
                print("Terima kasih telah menggunakan sistem ini!")
                print("="*70)
                break
            
            else:
                print("\n❌ Pilihan tidak valid! Silakan pilih 0-10.")
        
        except KeyboardInterrupt:
            print("\n\n⚠  Program dihentikan oleh user.")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
    
    print("\n👋 Sampai jumpa!\n")


if __name__ == "__main__":
    main()