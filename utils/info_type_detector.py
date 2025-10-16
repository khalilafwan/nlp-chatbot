def detect_info_type(message: str) -> str:
    message = message.lower()

    # Deskripsi umum
    if any(kw in message for kw in ["apa itu", "jelaskan", "deskripsi", "pengertian", "maksud", "informasi umum"]):
        return "description"

    # Fitur atau layanan
    if any(kw in message for kw in ["fitur", "layanan", "bisa apa", "digunakan untuk", "keunggulan"]):
        return "features"

    # Manfaat/keuntungan
    if any(kw in message for kw in ["manfaat", "keuntungan", "kelebihan"]):
        return "benefits"

    # Persyaratan/syarat
    if any(kw in message for kw in ["syarat", "persyaratan", "ketentuan"]):
        return "requirements"

    # Biaya
    if any(kw in message for kw in ["biaya", "administrasi", "bayar", "harga"]):
        return "fees"

    # Limit transaksi
    if any(kw in message for kw in ["limit", "batas", "maksimum", "transfer maksimal", "tarik tunai"]):
        return "limits"

    # Ketentuan pengguna kartu
    if any(kw in message for kw in ["pemegang kartu", "pengguna kartu", "aturan kartu"]):
        return "terms_and_conditions"

    # Ketersediaan aplikasi
    if any(kw in message for kw in ["unduh", "download", "tersedia di", "play store", "app store"]):
        return "availability"

    # Jika tidak yakin, fallback ke deskripsi
    return "description"
