"""Modul contoh yang sudah dirapikan sesuai PEP 8."""


def jumlahkan_nilai(nilai_a, nilai_b, nilai_c):
    """Menjumlahkan tiga nilai.

    Args:
        nilai_a: Nilai pertama.
        nilai_b: Nilai kedua.
        nilai_c: Nilai ketiga.

    Returns:
        Hasil penjumlahan ketiga nilai.
    """
    return nilai_a + nilai_b + nilai_c


def main():
    """Fungsi utama program."""
    print(jumlahkan_nilai(1, 2, 3))


if __name__ == "__main__":
    main()