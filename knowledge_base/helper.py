import re


def detect_product_info_type(message: str) -> str:
    message = message.lower()

    keyword_mapping = {
        "description": ["apa itu", "jelaskan", "deskripsi", "pengertian", "maksud", "informasi umum"],
        "features": ["fitur", "layanan", "fungsi", "digunakan untuk", "kegunaan"],
        "benefits": ["manfaat", "keuntungan", "kelebihan"],
        "requirements": ["syarat", "persyaratan", "ketentuan", "setoran awal", "dokumen"],
        "fees": ["biaya", "administrasi", "bayar", "tarif"],
        "limits": ["limit", "batas", "maksimum", "transfer maksimal", "tarik tunai", "top up"],
        "terms_and_conditions": ["pemegang kartu", "pengguna kartu", "aturan kartu", "tanggung jawab"],
        "availability": ["tersedia", "unduh", "play store", "app store", "download"],
        "mitra_kerjasama": ["kerjasama", "mitra", "instansi", "pemda", "rekanan"],
        "target_users": ["ditujukan untuk", "nasabah siapa", "siapa yang bisa"],
        "notes": ["catatan", "tambahan", "informasi lainnya"],
    }

    for info_type, keywords in keyword_mapping.items():
        if any(kw in message for kw in keywords):
            return info_type

    return "description"  # Default fallback


def detect_branch_info_type(message: str) -> str:
    message = message.lower()
    keyword_map = {
        "alamat": ["alamat", "lokasi", "dimana", "berada", "terletak"],
        "kategori": ["kategori", "jenis", "tipe", "macam"],
        "nama": ["nama", "disebut apa", "nama lengkap"]
    }

    for info_type, keywords in keyword_map.items():
        if any(keyword in message for keyword in keywords):
            return info_type
    return None  # fallback: ambil semua data


def detect_promo_info_type(message: str) -> str:
    message = message.lower()

    keyword_map = {
        # Deskripsi umum
        "description": [
            "apa itu", "jelaskan", "deskripsi", "informasi umum", "pengertian"
        ],

        # Manfaat, keunggulan, tujuan
        "benefits": [
            "manfaat", "keuntungan", "kegunaan", "kelebihan"
        ],

        # Syarat & ketentuan
        "requirements": [
            "syarat", "persyaratan", "ketentuan", "dokumen", "diperlukan", "dibutuhkan"
        ],

        # Merchant (lokasi promo)
        "merchants": [
            "merchant", "berlaku di mana", "toko", "lokasi", "tempat", "daftar merchant"
        ],

        # Periode promo (rentang waktu)
        "periode": [
            "periode", "berlaku sampai", "hingga kapan", "kapan saja", "durasi"
        ],

        # Tanggal mulai
        "start_date": [
            "mulai", "tanggal mulai", "awal berlaku"
        ],

        # Tanggal berakhir
        "end_date": [
            "berakhir", "selesai", "tanggal selesai", "tanggal berakhir"
        ],

        # Program khusus (contoh: EDC Cashback)
        "programs": [
            "program", "jenis promo", "kategori promo"
        ],

        # Skim produk (khusus promo KPR)
        "skim_produk": [
            "skim", "rincian", "kategori produk", "jenis produk"
        ],

        # Tidak termasuk (pengecualian)
        "tidak_termasuk": [
            "tidak termasuk", "tidak berlaku", "pengecualian"
        ]
    }

    for info_type, keywords in keyword_map.items():
        if any(kw in message for kw in keywords):
            return info_type

    # Default jika tidak ditemukan keyword spesifik
    return "description"

_WHITES = re.compile(r"\s+")
def _n(text: str) -> str:
    return _WHITES.sub(" ", text.lower()).strip()

def detect_entity_hint(message: str) -> str | None:
    """
    Kembalikan salah satu: 'atm' | 'capem' | 'branch' | 'branch_kas' | None
    """
    msg = _n(message)

    if re.search(r"\batm\b|\bmesin atm\b", msg):
        return "atm"
    if re.search(r"\bcapem\b|\bcabang pembantu\b|\bkantor capem\b", msg):
        return "capem"
    if re.search(r"\bunit kas\b|\bkantor kas\b|\bkas\b", msg):
        return "branch_kas"
    if re.search(r"\bcabang\b|\bkantor cabang\b", msg):
        return "branch"
    return None