training_data = [
    # Greeting
    {"text": "Halo", "intent": "greeting"},
    {"text": "Hai", "intent": "greeting"},
    {"text": "Selamat pagi", "intent": "greeting"},
    {"text": "Selamat siang", "intent": "greeting"},
    {"text": "Selamat sore", "intent": "greeting"},
    {"text": "Selamat malam", "intent": "greeting"},
    {"text": "Assalamualaikum", "intent": "greeting"},
    {"text": "Salam sejahtera", "intent": "greeting"},
    {"text": "Syalom", "intent": "greeting"},
    {"text": "Pagi", "intent": "greeting"},
    {"text": "Siang", "intent": "greeting"},
    {"text": "Sore", "intent": "greeting"},
    {"text": "Malam", "intent": "greeting"},
    {"text": "Permisi", "intent": "greeting"},
    {"text": "Yo", "intent": "greeting"},
    {"text": "Hey", "intent": "greeting"},
    {"text": "Hi", "intent": "greeting"},
    {"text": "Cuy", "intent": "greeting"},
    {"text": "Bro", "intent": "greeting"},
    {"text": "Sis", "intent": "greeting"},
    {"text": "Gan", "intent": "greeting"},
    {"text": "Sob", "intent": "greeting"},
    {"text": "Halo, chatbot!", "intent": "greeting"},
    {"text": "Hai bot", "intent": "greeting"},
    {"text": "Bot, selamat siang", "intent": "greeting"},
    {"text": "Met pagi", "intent": "greeting"},
    {"text": "Selamat datang", "intent": "greeting"},
    {"text": "Hai, selamat datang", "intent": "greeting"},
    {"text": "Halo Bank Nagari", "intent": "greeting"},
    {"text": "Hi Bank Nagari", "intent": "greeting"},
    {"text": "Good morning", "intent": "greeting"},
    {"text": "Good afternoon", "intent": "greeting"},
    {"text": "Good evening", "intent": "greeting"},
    {"text": "Hello there", "intent": "greeting"},
    {"text": "helo", "intent": "greeting"},
    {"text": "hallo", "intent": "greeting"},
    {"text": "heloo", "intent": "greeting"},
    {"text": "hii", "intent": "greeting"},
    {"text": "hy", "intent": "greeting"},
    {"text": "met siang", "intent": "greeting"},
    {"text": "met malem", "intent": "greeting"},
    {"text": "aslm", "intent": "greeting"},
    {"text": "Pagi!", "intent": "greeting"},
    {"text": "Halo 😊", "intent": "greeting"},
    {"text": "Hai!", "intent": "greeting"},
    {"text": "Yo!", "intent": "greeting"},

    # Thanks
    {"text": "Terima kasih", "intent": "thanks"},
    {"text": "Terima kasih banyak", "intent": "thanks"},
    {"text": "Sangat berterima kasih", "intent": "thanks"},
    {"text": "Terima kasih atas bantuannya", "intent": "thanks"},
    {"text": "Terima kasih atas informasinya", "intent": "thanks"},
    {"text": "Terima kasih kembali", "intent": "thanks"},
    {"text": "Baik, terima kasih", "intent": "thanks"},
    {"text": "Mantap, terima kasih", "intent": "thanks"},
    {"text": "Terima kasih Bank Nagari", "intent": "thanks"},
    {"text": "Makasih", "intent": "thanks"},
    {"text": "Makasih ya", "intent": "thanks"},
    {"text": "Makasih banyak", "intent": "thanks"},
    {"text": "Makasih sekali", "intent": "thanks"},
    {"text": "makasih banyak ya", "intent": "thanks"},
    {"text": "makasih infonya", "intent": "thanks"},
    {"text": "Oke, makasih", "intent": "thanks"},
    {"text": "Sip, makasih", "intent": "thanks"},
    {"text": "Thanks banget", "intent": "thanks"},
    {"text": "Thanks ya bot", "intent": "thanks"},
    {"text": "Bot, makasih", "intent": "thanks"},
    {"text": "Bot, terima kasih", "intent": "thanks"},
    {"text": "alhamdulillah, makasih", "intent": "thanks"},
    {"text": "Thanks", "intent": "thanks"},
    {"text": "Thanks a lot", "intent": "thanks"},
    {"text": "Thank you", "intent": "thanks"},
    {"text": "Thanks for the help", "intent": "thanks"},
    {"text": "Thank you so much", "intent": "thanks"},
    {"text": "Thx", "intent": "thanks"},
    {"text": "Tq", "intent": "thanks"},
    {"text": "Tqsm", "intent": "thanks"},
    {"text": "Trims", "intent": "thanks"},
    {"text": "Trimakasih", "intent": "thanks"},
    {"text": "Terimakasih", "intent": "thanks"},
    {"text": "Makasi", "intent": "thanks"},
    {"text": "Makash", "intent": "thanks"},
    {"text": "mksh", "intent": "thanks"},
    {"text": "y mksh!", "intent": "thanks"},
    {"text": "Thanks!", "intent": "thanks"},
    {"text": "Terima kasih 😊", "intent": "thanks"},
    {"text": "Thank you 🙏", "intent": "thanks"},
    {"text": "Makasih banyak 🙏", "intent": "thanks"},
    {"text": "Thanks ya!", "intent": "thanks"},
    {"text": "Mantap, makasih!", "intent": "thanks"},
    {"text": "Wah, makasih banyak!", "intent": "thanks"},
    {"text": "Terima kasih, jawabannya jelas sekali", "intent": "thanks"},
    {"text": "Makasih, sangat membantu", "intent": "thanks"},
    {"text": "Thanks, keren banget", "intent": "thanks"},
    {"text": "Terima kasih, mantap", "intent": "thanks"},

    # SIMPEDA Product Inquiry
    {"text": "Apa itu tabungan Simpeda?", "intent": "product_inquiry",
        "entities": {"product_name": "simpeda"}},
    {"text": "Apa yang dimaksud dengan tabungan Simpeda?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Bisa jelaskan tentang tabungan Simpeda?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Tabungan Simpeda itu apa sih?", "intent": "product_inquiry",
        "entities": {"product_name": "simpeda"}},
    {"text": "Apa saja manfaat dari tabungan Simpeda?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Tabungan Simpeda itu bagaimana ya?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Saya ingin tahu tentang tabungan Simpeda, apa itu?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Apa kelebihan dari tabungan Simpeda?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Bagaimana cara kerja tabungan Simpeda?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Apa keuntungan yang bisa didapat dari tabungan Simpeda?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},

    {"text": "Apa saja keuntungan dari tabungan Simpeda?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Apa keuntungan yang bisa diperoleh dari tabungan Simpeda?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Keuntungan apa saja yang ada pada tabungan Simpeda?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Tabungan Simpeda itu punya keuntungan apa saja?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Apa saja manfaat yang didapat dari tabungan Simpeda?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Apa keuntungan utama dari tabungan Simpeda?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Dapat apa saja kalau memilih tabungan Simpeda?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Tabungan Simpeda memiliki keuntungan apa saja?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Keuntungan apa yang ditawarkan oleh tabungan Simpeda?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Tabungan Simpeda, apa saja keuntungan yang bisa didapatkan?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Keuntungan apa saja yang bisa didapatkan dari tabungan Simpeda?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Apa saja keuntungan yang ditawarkan oleh tabungan Simpeda?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Tabungan Simpeda memberikan keuntungan apa saja?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Apa keuntungan yang bisa kita peroleh dari tabungan Simpeda?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Tabungan Simpeda itu memberikan manfaat apa saja?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Keuntungan apa yang bisa diperoleh dari memilih tabungan Simpeda?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Apa saja keuntungan yang bisa didapat dengan membuka tabungan Simpeda?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Keuntungan apa saja yang ada pada tabungan Simpeda?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Tabungan Simpeda menawarkan keuntungan apa saja?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},

    {"text": "Berapa setoran awal untuk tabungan Simpeda?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Setoran awal untuk tabungan Simpeda itu berapa?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Berapa minimal setoran awal yang diperlukan untuk tabungan Simpeda?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Tabungan Simpeda, setoran awalnya berapa ya?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Untuk membuka tabungan Simpeda, berapa setoran awalnya?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Setoran pertama untuk tabungan Simpeda berapa sih?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Berapa jumlah setoran awal yang dibutuhkan untuk tabungan Simpeda?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Tabungan Simpeda, setoran awalnya sebesar berapa?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Setoran minimal untuk tabungan Simpeda itu berapa?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Berapa besar setoran awal yang harus dilakukan untuk tabungan Simpeda?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Apa syarat untuk membuka rekening Simpeda di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},

    {"text": "Berapa biaya administrasi tabungan Simpeda?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Biaya administrasi untuk tabungan Simpeda berapa?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Berapa biaya yang dikenakan sebagai biaya administrasi tabungan Simpeda?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Tabungan Simpeda, berapa biaya administrasinya?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Berapa biaya administrasi yang harus dibayar untuk tabungan Simpeda?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Tabungan Simpeda memiliki biaya administrasi berapa?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Biaya administrasi untuk tabungan Simpeda itu berapa per bulannya?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Tabungan Simpeda, berapa biaya administrasi yang dikenakan setiap bulan?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Berapa biaya administrasi yang harus dibayar jika memiliki tabungan Simpeda?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},
    {"text": "Biaya administrasi untuk tabungan Simpeda sebesar berapa?",
        "intent": "product_inquiry", "entities": {"product_name": "simpeda"}},

    # Tabungan Sikoci Product Inquiry
    {"text": "Apa itu Tabungan Sikoci?", "intent": "product_inquiry",
        "entities": {"product_name": "sikoci"}},
    {"text": "Apa yang dimaksud dengan Tabungan Sikoci?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Tabungan Sikoci itu apa sih?", "intent": "product_inquiry",
        "entities": {"product_name": "sikoci"}},
    {"text": "Bisa jelaskan tentang Tabungan Sikoci?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Apa sebenarnya Tabungan Sikoci?", "intent": "product_inquiry",
        "entities": {"product_name": "sikoci"}},
    {"text": "Tabungan Sikoci itu apa dan bagaimana cara kerjanya?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Tabungan Sikoci itu apa manfaatnya?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Apa tujuan dari Tabungan Sikoci?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Bagaimana cara kerja Tabungan Sikoci?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},

    {"text": "Apa saja keuntungan dari Tabungan Sikoci?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Apa saja keuntungan yang didapat dari Tabungan Sikoci?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Tabungan Sikoci memiliki manfaat apa saja?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Keuntungan apa yang bisa diperoleh dengan Tabungan Sikoci?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Apa keuntungan utama dari Tabungan Sikoci?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Tabungan Sikoci, apa manfaatnya?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Apa yang membuat Tabungan Sikoci menguntungkan?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Keuntungan apa saja yang ditawarkan oleh Tabungan Sikoci?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Tabungan Sikoci memberikan keuntungan apa saja?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Apa saja keuntungan jika saya membuka Tabungan Sikoci?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},

    {"text": "Berapa setoran awal untuk Tabungan Sikoci?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Berapa setoran awal yang diperlukan untuk membuka Tabungan Sikoci?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Setoran pertama untuk Tabungan Sikoci itu berapa?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Tabungan Sikoci, berapa setoran awal yang dibutuhkan?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Setoran awal untuk membuka Tabungan Sikoci itu berapa ya?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Berapa banyak setoran pertama yang diperlukan untuk Tabungan Sikoci?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Berapa minimal setoran awal untuk Tabungan Sikoci?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Setoran pertama untuk Tabungan Sikoci itu sebesar berapa?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Tabungan Sikoci, setoran pertama yang harus dibayar berapa?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Setoran awal Tabungan Sikoci, berapa jumlahnya?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},

    {"text": "Apakah ada biaya administrasi untuk Tabungan Sikoci?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Tabungan Sikoci, apakah dikenakan biaya administrasi?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Berapa biaya administrasi yang dikenakan pada Tabungan Sikoci?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Tabungan Sikoci memiliki biaya administrasi tidak?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Adakah biaya administrasi untuk Tabungan Sikoci?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Biaya administrasi yang dibebankan untuk Tabungan Sikoci berapa?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Apakah Tabungan Sikoci mengenakan biaya administrasi bulanan?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Tabungan Sikoci, ada biaya administrasi tambahan nggak?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Berapa biaya administrasi per bulan untuk Tabungan Sikoci?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Biaya administrasi untuk Tabungan Sikoci itu besarannya berapa?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},

    {"text": "Apa syarat untuk membuka Tabungan Sikoci?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Untuk membuka Tabungan Sikoci, syaratnya apa saja?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Tabungan Sikoci, apa saja syarat yang diperlukan untuk membuka?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Apa yang harus dipenuhi untuk membuka Tabungan Sikoci?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Tabungan Sikoci, apa syarat pembukaannya?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Untuk memiliki Tabungan Sikoci, apa saja persyaratannya?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Tabungan Sikoci, ada persyaratan apa saja untuk membuka akun?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Tabungan Sikoci, syaratnya apa yang harus dipenuhi?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Bagaimana cara membuka Tabungan Sikoci dan apa syaratnya?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},
    {"text": "Tabungan Sikoci, apa saja ketentuan untuk membuka rekening?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci"}},

    # Giro Product Inquiry
    {"text": "Apa itu Giro di Bank Nagari?", "intent": "product_inquiry",
        "entities": {"product_name": "giro"}},
    {"text": "Giro di Bank Nagari itu apa sih?",
        "intent": "product_inquiry", "entities": {"product_name": "giro"}},
    {"text": "Bisa jelaskan apa itu Giro di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "giro"}},
    {"text": "Apa sebenarnya Giro di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "giro"}},
    {"text": "Tabungan Giro di Bank Nagari itu seperti apa?",
        "intent": "product_inquiry", "entities": {"product_name": "giro"}},
    {"text": "Apa manfaat dari Giro di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "giro"}},
    {"text": "Giro di Bank Nagari itu berbeda dengan tabungan biasa, kan?",
        "intent": "product_inquiry", "entities": {"product_name": "giro"}},
    {"text": "Bagaimana cara kerja Giro di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "giro"}},
    {"text": "Apa tujuan dari Giro di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "giro"}},

    {"text": "Apa saja keuntungan dari Giro di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "giro"}},
    {"text": "Apa saja keuntungan yang ditawarkan oleh Giro di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "giro"}},
    {"text": "Giro di Bank Nagari, apa manfaatnya?",
        "intent": "product_inquiry", "entities": {"product_name": "giro"}},
    {"text": "Keuntungan apa saja yang bisa diperoleh dengan Giro di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "giro"}},
    {"text": "Apa keuntungan utama dari Giro di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "giro"}},
    {"text": "Tabungan Giro di Bank Nagari memberikan keuntungan apa saja?",
        "intent": "product_inquiry", "entities": {"product_name": "giro"}},
    {"text": "Apa yang membedakan Giro di Bank Nagari dengan produk tabungan lainnya?",
        "intent": "product_inquiry", "entities": {"product_name": "giro"}},
    {"text": "Giro di Bank Nagari, apa kelebihannya dibandingkan tabungan biasa?",
        "intent": "product_inquiry", "entities": {"product_name": "giro"}},
    {"text": "Apa saja keuntungan jika saya memilih Giro di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "giro"}},
    {"text": "Giro di Bank Nagari memberikan keuntungan apa saja bagi nasabah?",
        "intent": "product_inquiry", "entities": {"product_name": "giro"}},

    {"text": "Bagaimana cara membuka rekening Giro?",
        "intent": "product_inquiry", "entities": {"product_name": "giro"}},
    {"text": "Bagaimana cara membuka rekening Giro di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "giro"}},
    {"text": "Apa langkah-langkah yang perlu dilakukan untuk membuka rekening Giro?",
        "intent": "product_inquiry", "entities": {"product_name": "giro"}},
    {"text": "Apa yang perlu saya persiapkan untuk membuka rekening Giro di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "giro"}},
    {"text": "Giro di Bank Nagari, bagaimana cara membuka rekeningnya?",
        "intent": "product_inquiry", "entities": {"product_name": "giro"}},
    {"text": "Bagaimana prosedur membuka rekening Giro di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "giro"}},
    {"text": "Apa syarat dan cara membuka rekening Giro di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "giro"}},
    {"text": "Mau buka rekening Giro di Bank Nagari, gimana caranya?",
        "intent": "product_inquiry", "entities": {"product_name": "giro"}},
    {"text": "Untuk membuka rekening Giro di Bank Nagari, apa saja yang harus dilakukan?",
        "intent": "product_inquiry", "entities": {"product_name": "giro"}},
    {"text": "Bagaimana cara membuka rekening Giro dan apa saja syaratnya?",
        "intent": "product_inquiry", "entities": {"product_name": "giro"}},
    {"text": "Apa syarat untuk membuka Giro di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "giro"}},

    # Sikoci Rencana Product Inquiry
    {"text": "Apa itu Tabungan Sikoci Rencana?", "intent": "product_inquiry",
        "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Apa yang dimaksud dengan Tabungan Sikoci Rencana?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Tabungan Sikoci Rencana itu apa sih?", "intent": "product_inquiry",
        "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Bisa jelaskan apa itu Tabungan Sikoci Rencana?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Apa sebenarnya Tabungan Sikoci Rencana?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Tabungan Sikoci Rencana itu seperti apa?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Apa manfaat yang didapat dari Tabungan Sikoci Rencana?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Apa tujuan dari Tabungan Sikoci Rencana?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Bagaimana cara kerja Tabungan Sikoci Rencana?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Tabungan Sikoci Rencana, apa bedanya dengan tabungan biasa?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},

    {"text": "Apa keuntungan dari Tabungan Sikoci Rencana?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Apa saja keuntungan yang didapat dari Tabungan Sikoci Rencana?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Tabungan Sikoci Rencana menawarkan keuntungan apa saja?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Keuntungan apa yang bisa diperoleh dengan Tabungan Sikoci Rencana?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Apa manfaat utama dari Tabungan Sikoci Rencana?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Tabungan Sikoci Rencana, apa saja keuntungan yang diberikan?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Keuntungan utama apa yang ditawarkan oleh Tabungan Sikoci Rencana?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Apa keuntungan jika saya memilih Tabungan Sikoci Rencana?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Apa saja manfaat yang didapatkan dari Tabungan Sikoci Rencana?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Tabungan Sikoci Rencana memberikan manfaat apa bagi nasabah?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},

    {"text": "Berapa setoran awal untuk Tabungan Sikoci Rencana?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Berapa setoran awal yang diperlukan untuk membuka Tabungan Sikoci Rencana?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Setoran pertama untuk Tabungan Sikoci Rencana itu berapa?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Tabungan Sikoci Rencana, berapa setoran awal yang dibutuhkan?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Berapa banyak setoran awal yang harus dibayar untuk Tabungan Sikoci Rencana?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Setoran pertama untuk Tabungan Sikoci Rencana itu sebesar berapa?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Berapa jumlah setoran awal yang diperlukan untuk membuka Tabungan Sikoci Rencana?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Tabungan Sikoci Rencana, setoran pertama yang dibutuhkan berapa?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Setoran awal Tabungan Sikoci Rencana, berapa jumlahnya?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Setoran pertama untuk Tabungan Sikoci Rencana itu wajib berapa?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Apa syarat untuk membuka Tabungan Sikoci Rencana?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},

    {"text": "Apakah ada biaya administrasi untuk Tabungan Sikoci Rencana?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Tabungan Sikoci Rencana, apakah dikenakan biaya administrasi?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Biaya administrasi untuk Tabungan Sikoci Rencana itu berapa?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Tabungan Sikoci Rencana, ada biaya administrasi bulanan tidak?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Berapa biaya administrasi yang dikenakan untuk Tabungan Sikoci Rencana?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Ada biaya administrasi tidak untuk Tabungan Sikoci Rencana?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Tabungan Sikoci Rencana, apakah ada biaya administrasi yang perlu dibayar?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Biaya administrasi yang berlaku untuk Tabungan Sikoci Rencana berapa?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},
    {"text": "Tabungan Sikoci Rencana, apakah ada biaya administrasi tambahan?",
        "intent": "product_inquiry", "entites": {"product_name": "sikoci_rencana"}},

    # Sikoci Pendidikan Product Inquiry
    {"text": "Apa itu Tabungan Sikoci Pendidikan?", "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Apa yang dimaksud dengan Tabungan Sikoci Pendidikan?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Tabungan Sikoci Pendidikan itu apa sih?", "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Bisa jelaskan lebih lanjut tentang Tabungan Sikoci Pendidikan?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Tabungan Sikoci Pendidikan, apa keuntungannya?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Apa fitur utama dari Tabungan Sikoci Pendidikan?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Tabungan Sikoci Pendidikan itu bagaimana cara kerjanya?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Tabungan Sikoci Pendidikan, apa tujuan utama produk ini?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Apa keunggulan dari Tabungan Sikoci Pendidikan dibandingkan produk lainnya?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},

    {"text": "Apa keuntungan dari Tabungan Sikoci Pendidikan?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Apa saja keuntungan yang ditawarkan oleh Tabungan Sikoci Pendidikan?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Tabungan Sikoci Pendidikan, apa manfaat yang didapatkan nasabah?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Keuntungan utama apa yang bisa diperoleh dengan Tabungan Sikoci Pendidikan?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Apa manfaat finansial yang ditawarkan oleh Tabungan Sikoci Pendidikan?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Apa keuntungan jangka panjang dari Tabungan Sikoci Pendidikan?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Tabungan Sikoci Pendidikan memberikan keuntungan apa bagi nasabah?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Apa manfaat yang didapat jika membuka Tabungan Sikoci Pendidikan?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Keuntungan apa yang membedakan Tabungan Sikoci Pendidikan dari tabungan lainnya?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},

    {"text": "Berapa setoran awal untuk Tabungan Sikoci Pendidikan?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Berapa jumlah setoran awal yang dibutuhkan untuk membuka Tabungan Sikoci Pendidikan?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Setoran pertama untuk Tabungan Sikoci Pendidikan itu berapa?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Tabungan Sikoci Pendidikan, setoran awalnya berapa?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Berapa setoran pertama yang diperlukan untuk membuka Tabungan Sikoci Pendidikan?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Setoran awal untuk Tabungan Sikoci Pendidikan, berapa banyak?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Tabungan Sikoci Pendidikan, berapa setoran pertama yang harus dibayar?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Berapa besar setoran awal untuk Tabungan Sikoci Pendidikan?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Tabungan Sikoci Pendidikan, setoran pertama wajib berapa?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},

    {"text": "Apa syarat untuk membuka Tabungan Sikoci Pendidikan?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Apa saja syarat untuk membuka Tabungan Sikoci Pendidikan?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Untuk membuka Tabungan Sikoci Pendidikan, apa saja yang diperlukan?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Tabungan Sikoci Pendidikan, syaratnya apa saja untuk membukanya?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Apa persyaratan untuk membuka Tabungan Sikoci Pendidikan?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Untuk membuka Tabungan Sikoci Pendidikan, apa saja ketentuan yang harus dipenuhi?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Apa saja dokumen yang diperlukan untuk membuka Tabungan Sikoci Pendidikan?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Syarat-syarat apa yang harus dipenuhi untuk membuka Tabungan Sikoci Pendidikan?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Untuk membuka Tabungan Sikoci Pendidikan, ada syarat khusus tidak?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},

    {"text": "Apakah ada biaya administrasi untuk Tabungan Sikoci Pendidikan?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Apakah ada biaya administrasi untuk Tabungan Sikoci Pendidikan?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Tabungan Sikoci Pendidikan, apakah dikenakan biaya administrasi?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Berapa biaya administrasi yang dibebankan pada Tabungan Sikoci Pendidikan?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Tabungan Sikoci Pendidikan, ada biaya administrasi bulanan nggak?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Tabungan Sikoci Pendidikan, apakah ada biaya administrasi tambahan?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Berapa biaya administrasi yang perlu dibayar untuk Tabungan Sikoci Pendidikan?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Ada biaya administrasi tidak untuk Tabungan Sikoci Pendidikan?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},
    {"text": "Berapa besar biaya administrasi untuk Tabungan Sikoci Pendidikan?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_pendidikan"}},

    {
        "text": "Apa itu Tabungan Sikoci Pensiun?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Apa saja keuntungan dari membuka Tabungan Sikoci Pensiun?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Berapa setoran awal minimal untuk membuka Tabungan Sikoci Pensiun?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Apa syarat dan ketentuan untuk memiliki Tabungan Sikoci Pensiun?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Apakah Tabungan Sikoci Pensiun dikenakan biaya administrasi bulanan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Apa saja fitur tambahan dari Tabungan Sikoci Pensiun?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Saya ingin tahu informasi lengkap tentang Tabungan Sikoci Pensiun, bisa dijelaskan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Apakah nasabah bisa punya lebih dari satu rekening Tabungan Sikoci Pensiun?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Kalau saya ingin tarik dana tambahan dari Sikoci Pensiun sebelum jatuh tempo, ada biayanya?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Apa itu Tabungan Sikoci Pensiun?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Bisa dijelaskan Tabungan Sikoci Pensiun itu seperti apa?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Saya ingin tahu detail tentang Sikoci Pensiun dari Bank Nagari.",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Apa saja manfaat dari membuka Tabungan Sikoci Pensiun?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Keuntungan apa yang saya dapatkan dari Sikoci Pensiun?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Apa saja benefit Tabungan Sikoci Pensiun dibanding tabungan biasa?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Saya dengar Sikoci Pensiun punya bunga lebih tinggi, benar begitu?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Apakah Sikoci Pensiun dilengkapi asuransi jiwa gratis?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Tabungan Sikoci Pensiun bebas biaya administrasi ya?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Apakah saldo Sikoci Pensiun ada batas maksimalnya?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Apakah rekening Sikoci Pensiun bisa dianggap dorman jika lama tidak aktif?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Berapa setoran awal untuk Tabungan Sikoci Pensiun?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Setoran bulanannya minimal berapa untuk Sikoci Pensiun?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Adakah kelipatan khusus untuk setor rutin di Sikoci Pensiun?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Setoran rutin di Sikoci Pensiun dibayar tiap bulan atau langsung beberapa bulan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Berapa lama minimal saya harus menabung di Sikoci Pensiun?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Apakah jangka waktu menabung Sikoci Pensiun bisa sampai masa pensiun?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Apakah saya perlu punya rekening lain untuk autodebet Sikoci Pensiun?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Apakah ada biaya saat menutup rekening Sikoci Pensiun setelah selesai program?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Kalau saya tutup Sikoci Pensiun sebelum selesai, kena penalti berapa?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Apa yang terjadi kalau saya gagal setor rutin selama 3 bulan berturut-turut di Sikoci Pensiun?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Saya bisa tarik setoran tambahan dari Sikoci Pensiun gak sebelum jatuh tempo?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Berapa biaya admin kalau saya tarik dana tambahan dari Sikoci Pensiun?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Apakah Sikoci Pensiun punya buku tabungan fisik?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Kalau buku tabungan Sikoci Pensiun penuh, bisa diganti gratis gak?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Fasilitas autodebet Sikoci Pensiun dilakukan tanggal berapa biasanya?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Apakah saya bisa setor tambahan ke Sikoci Pensiun lewat e-channel?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Apa Sikoci Pensiun menyediakan notifikasi SMS setiap transaksi?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Apakah nasabah Sikoci Pensiun bisa akses CMS rekening koran?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Saya boleh punya dua rekening Sikoci Pensiun sekaligus?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },
    {
        "text": "Saya butuh tabungan pensiun yang aman dan fleksibel, cocok gak pakai Sikoci Pensiun?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pensiun"}
    },

    # Sikoci Bisnis Product Inquiry
    {"text": "Apa itu Tabungan Sikoci Bisnis?", "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_bisnis"}},
    {"text": "Apa yang dimaksud dengan Tabungan Sikoci Bisnis?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_bisnis"}},
    {"text": "Tabungan Sikoci Bisnis itu apa sih?", "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_bisnis"}},
    {"text": "Bisa jelaskan lebih lanjut tentang Tabungan Sikoci Bisnis?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_bisnis"}},
    {"text": "Apa tujuan dari Tabungan Sikoci Bisnis?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_bisnis"}},
    {"text": "Tabungan Sikoci Bisnis itu cocok untuk siapa?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_bisnis"}},
    {"text": "Apa keunggulan Tabungan Sikoci Bisnis dibandingkan produk lain?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_bisnis"}},
    {"text": "Tabungan Sikoci Bisnis, apa saja manfaat yang diberikan?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_bisnis"}},
    {"text": "Apa yang membedakan Tabungan Sikoci Bisnis dengan tabungan pribadi?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_bisnis"}},

    {"text": "Apa keuntungan dari Tabungan Sikoci Bisnis?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_bisnis"}},
    {"text": "Apa saja keuntungan yang ditawarkan oleh Tabungan Sikoci Bisnis?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_bisnis"}},
    {"text": "Tabungan Sikoci Bisnis, apa saja manfaat yang bisa diperoleh?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_bisnis"}},
    {"text": "Keuntungan apa saja yang dapat diperoleh dengan Tabungan Sikoci Bisnis?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_bisnis"}},
    {"text": "Apa keuntungan utama dari menggunakan Tabungan Sikoci Bisnis?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_bisnis"}},
    {"text": "Tabungan Sikoci Bisnis memberikan keuntungan apa saja bagi pemilik usaha?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_bisnis"}},
    {"text": "Keuntungan jangka panjang apa yang didapat dari Tabungan Sikoci Bisnis?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_bisnis"}},
    {"text": "Apa manfaat finansial dari Tabungan Sikoci Bisnis?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_bisnis"}},
    {"text": "Tabungan Sikoci Bisnis, apa yang membedakan dengan produk serupa?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_bisnis"}},
    {"text": "Apa saja fitur dari Tabungan Sikoci Bisnis?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_bisnis"}},

    {"text": "Berapa setoran awal untuk Tabungan Sikoci Bisnis?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_bisnis"}},
    {"text": "Berapa besar setoran awal untuk membuka Tabungan Sikoci Bisnis?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_bisnis"}},
    {"text": "Setoran pertama yang dibutuhkan untuk membuka Tabungan Sikoci Bisnis itu berapa?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_bisnis"}},
    {"text": "Berapa jumlah setoran awal untuk Tabungan Sikoci Bisnis?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_bisnis"}},
    {"text": "Tabungan Sikoci Bisnis, setoran pertama berapa yang harus dibayar?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_bisnis"}},
    {"text": "Setoran awal untuk membuka Tabungan Sikoci Bisnis itu wajib berapa?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_bisnis"}},
    {"text": "Tabungan Sikoci Bisnis, berapa banyak setoran pertama yang diperlukan?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_bisnis"}},
    {"text": "Untuk membuka Tabungan Sikoci Bisnis, berapa jumlah setoran awalnya?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_bisnis"}},
    {"text": "Setoran pertama untuk Tabungan Sikoci Bisnis, berapa nominalnya?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_bisnis"}},

    {"text": "Apakah ada biaya administrasi untuk Tabungan Sikoci Bisnis?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_bisnis"}},
    {"text": "Apakah ada biaya administrasi untuk Tabungan Sikoci Bisnis?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_bisnis"}},
    {"text": "Tabungan Sikoci Bisnis, apakah dikenakan biaya administrasi?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_bisnis"}},
    {"text": "Berapa biaya administrasi yang dibebankan pada Tabungan Sikoci Bisnis?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_bisnis"}},
    {"text": "Tabungan Sikoci Bisnis, ada biaya administrasi bulanan tidak?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_bisnis"}},
    {"text": "Tabungan Sikoci Bisnis, apakah ada biaya administrasi tahunan?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_bisnis"}},
    {"text": "Tabungan Sikoci Bisnis, berapa biaya administrasi yang perlu dibayar?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_bisnis"}},
    {"text": "Ada biaya administrasi tidak untuk Tabungan Sikoci Bisnis?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_bisnis"}},
    {"text": "Berapa besar biaya administrasi yang dikenakan pada Tabungan Sikoci Bisnis?",
        "intent": "product_inquiry", "entities": {"product_name": "sikoci_bisnis"}},

    # Deposito Product Inquiry
    {"text": "Apa itu Deposito di Bank Nagari?", "intent": "product_inquiry",
        "entities": {"product_name": "deposito"}},
    {"text": "Apa yang dimaksud dengan Deposito di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito"}},
    {"text": "Deposito di Bank Nagari itu apa sih?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito"}},
    {"text": "Bisa jelaskan lebih lanjut tentang Deposito di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito"}},
    {"text": "Apa keunggulan yang ditawarkan oleh Deposito di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito"}},
    {"text": "Apa tujuan utama dari Deposito di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito"}},
    {"text": "Deposito di Bank Nagari, bagaimana cara kerjanya?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito"}},
    {"text": "Apa saja manfaat memiliki Deposito di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito"}},

    {"text": "Apa saja keuntungan dari Deposito di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito"}},
    {"text": "Apa saja keuntungan yang bisa didapatkan dengan Deposito di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito"}},
    {"text": "Apa manfaat utama dari Deposito di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito"}},
    {"text": "Keuntungan apa yang ditawarkan oleh Deposito di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito"}},
    {"text": "Apa yang membedakan keuntungan Deposito di Bank Nagari dengan deposito di bank lain?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito"}},
    {"text": "Apa keuntungan jangka panjang dari Deposito di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito"}},
    {"text": "Apa saja benefit yang diberikan Deposito di Bank Nagari bagi nasabah?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito"}},
    {"text": "Deposito di Bank Nagari, apa saja keuntungannya?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito"}},
    {"text": "Apa keuntungan finansial yang dapat diperoleh dengan Deposito di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito"}},

    {"text": "Berapa setoran awal untuk membuka Deposito?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito"}},
    {"text": "Apa syarat untuk membuka Deposito di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito"}},
    {"text": "Berapa besar setoran awal untuk membuka Deposito di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito"}},
    {"text": "Setoran awal yang diperlukan untuk membuka Deposito di Bank Nagari berapa?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito"}},
    {"text": "Tabungan Deposito di Bank Nagari, setoran pertama berapa yang diperlukan?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito"}},
    {"text": "Setoran awal untuk membuka Deposito di Bank Nagari itu wajib berapa?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito"}},
    {"text": "Berapa banyak setoran awal yang dibutuhkan untuk membuka Deposito?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito"}},
    {"text": "Tabungan Deposito di Bank Nagari, berapa jumlah setoran pertama yang harus dibayar?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito"}},
    {"text": "Untuk membuka Deposito di Bank Nagari, berapa jumlah setoran awalnya?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito"}},
    {"text": "Setoran pertama untuk Deposito di Bank Nagari, berapa nominalnya?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito"}},

    {"text": "Apakah ada biaya administrasi untuk Deposito di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito"}},
    {"text": "Apakah ada biaya administrasi untuk Deposito di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito"}},
    {"text": "Deposito di Bank Nagari, apakah dikenakan biaya administrasi?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito"}},
    {"text": "Berapa biaya administrasi yang dibebankan pada Deposito di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito"}},
    {"text": "Tabungan Deposito di Bank Nagari, ada biaya administrasi bulanan tidak?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito"}},
    {"text": "Tabungan Deposito di Bank Nagari, ada biaya administrasi tahunan?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito"}},
    {"text": "Deposito di Bank Nagari, berapa biaya administrasi yang dikenakan?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito"}},
    {"text": "Apakah ada biaya administrasi tambahan yang dibebankan pada Deposito di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito"}},
    {"text": "Berapa besar biaya administrasi yang harus dibayar untuk Deposito di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito"}},

    {
        "text": "Apa itu KPUM SIMAMAK dari Bank Nagari?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kpum_simamak"}
    },
    {
        "text": "Saya ingin tahu lebih lanjut tentang pinjaman KPUM SIMAMAK.",
        "intent": "product_inquiry",
        "entities": {"product_name": "kpum_simamak"}
    },
    {
        "text": "Apakah KPUM SIMAMAK hanya untuk usaha mikro?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kpum_simamak"}
    },
    {
        "text": "Apa tujuan utama dari program pinjaman KPUM SIMAMAK ini?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kpum_simamak"}
    },
    {
        "text": "Pinjaman KPUM SIMAMAK bisa digunakan untuk apa saja?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kpum_simamak"}
    },
    {
        "text": "Kalau saya butuh modal kerja, bisa pakai KPUM SIMAMAK?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kpum_simamak"}
    },
    {
        "text": "Bisakah pinjaman KPUM SIMAMAK digunakan untuk beli bahan baku?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kpum_simamak"}
    },
    {
        "text": "Untuk keperluan investasi usaha seperti beli mesin, bisa ajukan KPUM SIMAMAK?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kpum_simamak"}
    },
    {
        "text": "Saya ingin memperluas tempat usaha, bisa pakai fasilitas KPUM SIMAMAK?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kpum_simamak"}
    },
    {
        "text": "Apakah plafon pinjaman KPUM SIMAMAK bisa sampai 250 juta rupiah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kpum_simamak"}
    },
    {
        "text": "Berapa maksimal nominal pinjaman dari program KPUM SIMAMAK?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kpum_simamak"}
    },
    {
        "text": "Berapa lama jangka waktu pinjaman KPUM SIMAMAK untuk investasi?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kpum_simamak"}
    },
    {
        "text": "Berapa maksimal tenor KPUM SIMAMAK untuk keperluan modal kerja?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kpum_simamak"}
    },
    {
        "text": "Apakah bunga KPUM SIMAMAK kompetitif?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kpum_simamak"}
    },
    {
        "text": "Apakah biaya administrasi untuk KPUM SIMAMAK tergolong ringan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kpum_simamak"}
    },
    {
        "text": "Bisakah pinjaman KPUM SIMAMAK diperpanjang setelah jatuh tempo?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kpum_simamak"}
    },
    {
        "text": "Apa saja persyaratan untuk mengajukan pinjaman KPUM SIMAMAK?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kpum_simamak"}
    },
    {
        "text": "Dokumen apa yang dibutuhkan untuk KPUM SIMAMAK?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kpum_simamak"}
    },
    {
        "text": "Apakah saya harus menyerahkan bukti kepemilikan agunan untuk KPUM SIMAMAK?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kpum_simamak"}
    },
    {
        "text": "Fotokopi perizinan usaha diperlukan tidak untuk ajukan KPUM SIMAMAK?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kpum_simamak"}
    },
    {
        "text": "Apakah saya harus melampirkan foto usaha dan foto agunan saat mengajukan KPUM SIMAMAK?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kpum_simamak"}
    },
    {
        "text": "Apa saja identitas diri yang harus saya lampirkan untuk pinjaman KPUM SIMAMAK?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kpum_simamak"}
    },
    {
        "text": "Apakah fotokopi rekening listrik dan air bulan terakhir dibutuhkan untuk KPUM SIMAMAK?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kpum_simamak"}
    },
    {
        "text": "Apakah KPUM SIMAMAK cocok untuk pelaku usaha kecil menengah yang ingin berkembang?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kpum_simamak"}
    },
    {
        "text": "Saya butuh tambahan stok dagangan, apakah bisa dibiayai lewat KPUM SIMAMAK?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kpum_simamak"}
    },
    {
        "text": "Apakah kredit KPUM SIMAMAK bisa digunakan untuk biaya operasional usaha harian?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kpum_simamak"}
    },
    {
        "text": "Bank Nagari punya program kredit yang bantu UMKM lepas dari rentenir?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kpum_simamak"}
    },
    {
        "text": "Saya ingin mengembangkan usaha kecil saya, apakah KPUM SIMAMAK bisa membantu?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kpum_simamak"}
    },
    {
        "text": "Apakah program KPUM SIMAMAK bisa diakses dengan proses yang cepat dan mudah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kpum_simamak"}
    },
    {
        "text": "Pinjaman KPUM SIMAMAK ini cocok untuk pengusaha mikro, ya?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kpum_simamak"}
    },
    {"text": "Apa itu KMK Bangkit dari Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_bangkit"}},
    {"text": "Bisa dijelaskan program Kredit Modal Kerja Bangkit?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_bangkit"}},
    {"text": "Apa kegunaan KMK Bangkit untuk UMKM yang terdampak pandemi?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_bangkit"}},
    {"text": "Apakah KMK Bangkit termasuk program PEN?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_bangkit"}},
    {"text": "Siapa saja yang bisa mengajukan pinjaman KMK Bangkit?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_bangkit"}},
    {"text": "Apa saja syarat untuk mengajukan KMK Bangkit?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_bangkit"}},
    {"text": "Sektor usaha apa saja yang bisa dibiayai lewat KMK Bangkit?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_bangkit"}},
    {"text": "Berapa besar pinjaman maksimal dari KMK Bangkit?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_bangkit"}},
    {"text": "Apakah plafon KMK Bangkit bisa sampai 10 miliar?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_bangkit"}},
    {"text": "Apakah pemerintah ikut menjamin kredit KMK Bangkit?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_bangkit"}},
    {"text": "KMK Bangkit ini ditujukan untuk usaha apa saja?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_bangkit"}},
    {"text": "Apa saja dokumen yang dibutuhkan untuk KMK Bangkit?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_bangkit"}},
    {"text": "Saya punya usaha perdagangan, apakah bisa ikut KMK Bangkit?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_bangkit"}},
    {"text": "Usaha saya terdampak Covid-19, apakah bisa ajukan KMK Bangkit?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_bangkit"}},
    {"text": "Adakah pernyataan khusus terkait pandemi untuk pengajuan KMK Bangkit?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_bangkit"}},
    {"text": "Apa perbedaan KMK Bangkit revolfing dan non revolfing?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_bangkit"}},
    {"text": "Apakah koperasi bisa ikut serta dalam program KMK Bangkit?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_bangkit"}},
    {"text": "Bisakah badan usaha mengakses KMK Bangkit?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_bangkit"}},
    {"text": "Apakah Kredit Modal Kerja Bangkit hanya untuk UMKM?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_bangkit"}},
    {"text": "KMK Bangkit tersedia untuk sektor pertanian juga?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_bangkit"}},
    {"text": "Bagaimana proses pengajuan pinjaman KMK Bangkit?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_bangkit"}},
    {"text": "Apakah ada syarat NPWP untuk KMK Bangkit?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_bangkit"}},
    {"text": "Apakah perlu perizinan usaha untuk KMK Bangkit?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_bangkit"}},
    {"text": "Apa itu surat pernyataan terdampak Covid-19 dalam KMK Bangkit?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_bangkit"}},
    {"text": "Apa yang dimaksud debitur tidak boleh menerima fasilitas serupa dalam KMK Bangkit?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_bangkit"}},
    {"text": "Apa saja kelebihan program KMK Bangkit dibanding kredit biasa?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_bangkit"}},
    {"text": "Berapa jangka waktu maksimum pinjaman KMK Bangkit?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_bangkit"}},
    {"text": "Apakah KMK Bangkit termasuk restrukturisasi?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_bangkit"}},
    {"text": "Apakah usaha pengolahan makanan bisa didanai oleh KMK Bangkit?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_bangkit"}},
    {"text": "Apa itu KUR Super Mikro dari Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro"}},
    {"text": "Saya ingin tahu detail tentang program KUR Super Mikro.",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro"}},
    {"text": "Apakah benar plafon maksimal KUR Super Mikro sebesar 10 juta?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro"}},
    {"text": "KUR Super Mikro ditujukan untuk siapa saja?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro"}},
    {"text": "Apakah program KUR Super Mikro mewajibkan agunan?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro"}},
    {"text": "Apakah saya bisa ajukan KUR Super Mikro jika belum pernah menerima KUR sebelumnya?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro"}},
    {"text": "Apakah ada syarat khusus jika usaha saya baru berjalan 3 bulan untuk ikut KUR Super Mikro?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro"}},
    {"text": "Kalau usaha saya baru dimulai, apa yang dibutuhkan untuk mengakses KUR Super Mikro?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro"}},
    {"text": "Saya tergabung dalam kelompok usaha, apakah bisa ikut program KUR Super Mikro?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro"}},
    {"text": "Apa saja dokumen izin usaha yang harus saya siapkan untuk KUR Super Mikro?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro"}},
    {"text": "Apakah NIB bisa digunakan sebagai izin usaha untuk ajukan KUR Super Mikro?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro"}},
    {"text": "Kalau saya punya Surat Keterangan Usaha dari lurah, bisa ikut KUR Super Mikro?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro"}},
    {"text": "Saya sudah pernah ambil KUR, apakah masih bisa ikut KUR Super Mikro?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro"}},
    {"text": "Berapa lama jangka waktu kredit KUR Super Mikro untuk modal kerja?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro"}},
    {"text": "Jangka waktu maksimal KUR Super Mikro untuk investasi berapa tahun?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro"}},
    {"text": "Apakah bisa memperpanjang kredit KUR Super Mikro setelah 3 tahun?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro"}},
    {"text": "Apakah masa pinjaman KUR Super Mikro untuk investasi bisa sampai 7 tahun?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro"}},
    {"text": "Jika anggota keluarga saya sudah punya usaha, apakah saya bisa ajukan KUR Super Mikro?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro"}},
    {"text": "Saya sudah ikut pelatihan kewirausahaan, apakah bisa ikut program KUR Super Mikro?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro"}},
    {"text": "Apakah syarat pelatihan atau pendampingan berlaku untuk usaha yang baru dimulai?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro"}},
    {"text": "Apakah KUR Super Mikro berlaku untuk usaha rumahan kecil-kecilan?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro"}},
    {"text": "KUR Super Mikro hanya untuk usaha mikro ya? Boleh untuk warung kecil?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro"}},
    {"text": "Apakah ada batasan akumulasi plafon pada program KUR Super Mikro?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro"}},
    {"text": "Apakah saya bisa mengajukan kembali KUR Super Mikro jika sudah lunas?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro"}},
    {"text": "KUR Super Mikro cocok untuk usaha skala kecil yang baru mulai kan?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro"}},
    {"text": "Bolehkah menggunakan dokumen dari RT/RW untuk pengajuan KUR Super Mikro?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro"}},
    {"text": "Jika saya belum punya NIB, apakah masih bisa ikut program KUR Super Mikro?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro"}},
    {"text": "Apakah wajib ikut pelatihan formal untuk mengakses KUR Super Mikro?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro"}},
    {"text": "Apakah program KUR Super Mikro bisa diperpanjang tanpa ajukan baru?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro"}},
    {"text": "Apa itu program KUR Super Mikro MARANDANG dari Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro_marandang"}},
    {"text": "Saya tertarik dengan KUR MARANDANG, bisa dijelaskan kegunaannya?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro_marandang"}},
    {"text": "Apakah program MARANDANG bisa membantu usaha mikro di Minangkabau?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro_marandang"}},
    {"text": "Berapakah plafon maksimum untuk KUR Super Mikro MARANDANG?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro_marandang"}},
    {"text": "Berapa bunga tahunan dari program KUR MARANDANG ini?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro_marandang"}},
    {"text": "Sistem bunga seperti apa yang digunakan di KUR Super Mikro MARANDANG?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro_marandang"}},
    {"text": "Apakah benar bunga di KUR MARANDANG hanya 6 persen per tahun?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro_marandang"}},
    {"text": "Saya dengar KUR MARANDANG pakai sistem bunga sliding harian, maksudnya apa?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro_marandang"}},
    {"text": "Berapa lama maksimal jangka waktu pinjaman di program MARANDANG?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro_marandang"}},
    {"text": "Apakah pengajuan KUR MARANDANG bisa dilakukan secara cepat?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro_marandang"}},
    {"text": "Apakah biaya administrasi program KUR MARANDANG tinggi?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro_marandang"}},
    {"text": "Apa saja dokumen yang diperlukan untuk pengajuan KUR MARANDANG?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro_marandang"}},
    {"text": "Apakah saya perlu melampirkan foto suami istri saat mendaftar MARANDANG?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro_marandang"}},
    {"text": "KTP siapa saja yang harus disertakan dalam pengajuan KUR MARANDANG?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro_marandang"}},
    {"text": "Apakah surat nikah wajib disertakan saat mengajukan KUR MARANDANG?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro_marandang"}},
    {"text": "Saya punya usaha kecil di Padang, bisa ikut KUR MARANDANG?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro_marandang"}},
    {"text": "Apakah program MARANDANG bisa menggantikan ketergantungan ke rentenir?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro_marandang"}},
    {"text": "Apakah KUR Super Mikro MARANDANG termasuk kategori pembiayaan mikro tanpa agunan?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro_marandang"}},
    {"text": "Saya butuh modal cepat untuk warung kecil, apakah MARANDANG cocok?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro_marandang"}},
    {"text": "Surat Keterangan Usaha dari kelurahan bisa dipakai untuk KUR MARANDANG?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro_marandang"}},
    {"text": "Apa saja keuntungan utama dari KUR Super Mikro MARANDANG?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro_marandang"}},
    {"text": "KUR MARANDANG punya jangka waktu pinjaman berapa bulan maksimal?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro_marandang"}},
    {"text": "Kalau saya punya SKDP, apakah bisa digunakan untuk MARANDANG?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro_marandang"}},
    {"text": "Berapa besar pinjaman yang bisa saya ajukan melalui program MARANDANG?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro_marandang"}},
    {"text": "Adakah potongan atau promo bunga untuk KUR MARANDANG saat ini?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro_marandang"}},
    {"text": "Apakah program MARANDANG hanya untuk pelaku usaha Minangkabau?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro_marandang"}},
    {"text": "Program MARANDANG dari Bank Nagari ini dimaksudkan untuk siapa saja?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro_marandang"}},
    {"text": "Kalau saya tidak menikah, apa saja dokumen alternatif untuk MARANDANG?",
        "intent": "product_inquiry", "entities": {"product_name": "kur_super_mikro_marandang"}},
    {"text": "Apa itu KMK Multi Guna Faskes yang ditawarkan oleh Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_faskes"}},
    {"text": "Saya ingin tahu lebih banyak tentang fasilitas KMK-MG FASKES dari Bank Nagari.",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_faskes"}},
    {"text": "Apa manfaat utama dari KMK MG Faskes untuk fasilitas kesehatan mitra BPJS?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_faskes"}},
    {"text": "Siapa saja yang bisa mengajukan pinjaman KMK-MG Faskes?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_faskes"}},
    {"text": "Apakah Faskes swasta juga bisa mendapatkan pembiayaan dari KMK MG FASKES?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_faskes"}},
    {"text": "Faskes BLU apakah dapat mengajukan KMK MG FASKES?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_faskes"}},
    {"text": "Faskes saya adalah BLUD, apakah bisa menggunakan fasilitas KMK MG Faskes ini?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_faskes"}},
    {"text": "Untuk apa saja tujuan pembiayaan dari KMK-MG FASKES digunakan?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_faskes"}},
    {"text": "Apakah KMK MG FASKES membantu pencairan tagihan BPJS secara cepat?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_faskes"}},
    {"text": "Berapa maksimal plafon kredit dalam program KMK MG FASKES?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_faskes"}},
    {"text": "Apakah plafon pembiayaan KMK MG Faskes berdasarkan nilai FPK dari BPJS?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_faskes"}},
    {"text": "Apakah plafon KMK MG Faskes bisa sampai 90 persen dari Surat Konfirmasi BPJS?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_faskes"}},
    {"text": "Berapa lama jangka waktu maksimal pembiayaan KMK MG FASKES?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_faskes"}},
    {"text": "Apakah tenor pembiayaan KMK MG Faskes hanya sampai 6 bulan?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_faskes"}},
    {"text": "Apa saja dokumen yang diperlukan untuk mengajukan KMK MG Faskes?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_faskes"}},
    {"text": "Apa surat permohonan pembiayaan perlu ditandatangani pengurus inti Faskes?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_faskes"}},
    {"text": "Apakah saya harus melampirkan perjanjian kerja sama Faskes dengan BPJS?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_faskes"}},
    {"text": "Apa diperlukan dokumen legalitas dan izin Faskes untuk mengajukan KMK MG Faskes?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_faskes"}},
    {"text": "Print out rekening giro di Bank Nagari termasuk syarat pengajuan KMK MG Faskes?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_faskes"}},
    {"text": "Apakah laporan keuangan Faskes juga diminta dalam pengajuan KMK MG Faskes?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_faskes"}},
    {"text": "Apa saja yang dimaksud dokumen tambahan dalam persyaratan KMK MG Faskes?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_faskes"}},
    {"text": "Faskes saya sudah kerja sama dengan BPJS, apakah saya bisa ajukan KMK MG Faskes?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_faskes"}},
    {"text": "Klaim tagihan DJS BPJS bisa dipercepat dengan pembiayaan KMK MG Faskes?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_faskes"}},
    {"text": "Apa fungsi utama KMK MG Faskes untuk rumah sakit yang bekerja sama dengan BPJS?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_faskes"}},
    {"text": "Apakah hasil pengecekan iDeb atau SLIK OJK juga harus disertakan?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_faskes"}},
    {"text": "Print out accepted invoice termasuk syarat untuk KMK MG Faskes, bukan?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_faskes"}},
    {"text": "Saya butuh dana operasional klinik swasta yang kerja sama BPJS, apakah bisa ajukan KMK MG Faskes?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_faskes"}},
    {"text": "Apa keunggulan pembiayaan KMK MG Faskes dibanding kredit biasa?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_faskes"}},
    {"text": "Faskes kami BLU, apakah perlu dokumen izin pembiayaan dari instansi terkait?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_faskes"}},
    {"text": "Apakah KMK MG Faskes bisa diajukan lebih dari sekali dalam setahun?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_faskes"}},
    {"text": "Apa itu fasilitas KMK-MG KP dari Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_kp"}},
    {"text": "Saya ingin tahu detail tentang Kredit Modal Kerja Multi Guna Konstruksi Perumahan.",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_kp"}},
    {"text": "Siapa yang bisa mengajukan KMK MG KP?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_kp"}},
    {"text": "Apakah developer rumah tapak bisa menggunakan KMK-MG KP?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_kp"}},
    {"text": "KMK-MG KP ditujukan untuk pengembang apa saja?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_kp"}},
    {"text": "Apakah rusunami termasuk proyek yang bisa dibiayai KMK MG KP?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_kp"}},
    {"text": "Untuk tujuan apa saja dana KMK MG KP bisa digunakan?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_kp"}},
    {"text": "Apakah KMK MG KP bisa digunakan untuk membangun infrastruktur dalam proyek perumahan?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_kp"}},
    {"text": "Apakah pembelian lahan termasuk dalam pembiayaan KMK-MG KP?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_kp"}},
    {"text": "Kalau proyek saya termasuk program pemerintah, apakah pembebasan lahan bisa dibiayai?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_kp"}},
    {"text": "Berapa plafon maksimal pinjaman KMK-MG KP yang diberikan Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_kp"}},
    {"text": "Plafon pembiayaan KMK MG KP itu sampai berapa persen dari RAB proyek?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_kp"}},
    {"text": "Kalau proyek saya masuk program pemerintah, berapa plafon maksimal KMK MG KP?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_kp"}},
    {"text": "Berapa lama tenor maksimal KMK MG KP?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_kp"}},
    {"text": "Apakah jangka waktu kredit KMK-MG KP bisa sampai 2 tahun?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_kp"}},
    {"text": "Apa saja dokumen yang dibutuhkan untuk mengajukan KMK MG KP?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_kp"}},
    {"text": "Apakah saya perlu bukti keanggotaan REI untuk mengajukan KMK MG KP?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_kp"}},
    {"text": "Apakah anggota Apersi dapat mengajukan fasilitas KMK-MG KP?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_kp"}},
    {"text": "Dokumen apa saja yang membuktikan legalitas proyek perumahan untuk KMK MG KP?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_kp"}},
    {"text": "Saya perlu menyerahkan laporan keuangan untuk KMK MG KP?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_kp"}},
    {"text": "Berapa tahun laporan keuangan yang harus dilampirkan untuk KMK MG KP?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_kp"}},
    {"text": "Apakah perlu melampirkan sales contract dari instansi pembeli rumah?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_kp"}},
    {"text": "Apa itu surat perintah penyaluran dana atau standing instruction dalam KMK MG KP?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_kp"}},
    {"text": "Print out rekening giro di Bank Nagari termasuk persyaratan KMK MG KP?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_kp"}},
    {"text": "Kalau saya punya proyek pembangunan ruko, bisa ajukan KMK MG KP?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_kp"}},
    {"text": "Bisa tidak KMK MG KP dipakai untuk bangun rumah kantor (rukan)?", "intent": "product_inquiry", "entities": {
        "product_name": "kmk_mg_kp"}},
    {"text": "Kalau saya mau bangun rusunawa, apakah bisa dibiayai KMK MG KP?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_kp"}},
    {"text": "Apa manfaat utama dari KMK MG KP bagi pengembang perumahan?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_kp"}},
    {"text": "Saya ingin tahu prosedur lengkap pengajuan KMK MG KP.",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_kp"}},
    {"text": "Apakah program KMK MG KP termasuk jenis pembiayaan modal kerja jangka pendek?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg_kp"}},
    {"text": "Apa itu Bank Garansi di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "bank_garansi"}},
    {"text": "Saya ingin tahu fungsi dari fasilitas Bank Garansi yang ditawarkan Bank Nagari.",
        "intent": "product_inquiry", "entities": {"product_name": "bank_garansi"}},
    {"text": "Jenis-jenis Bank Garansi apa saja yang tersedia di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "bank_garansi"}},
    {"text": "Apakah Bank Garansi meliputi Jaminan Pelaksanaan dan Uang Muka?",
        "intent": "product_inquiry", "entities": {"product_name": "bank_garansi"}},
    {"text": "Apakah Bank Garansi dari Bank Nagari bisa digunakan untuk proyek APBN?",
        "intent": "product_inquiry", "entities": {"product_name": "bank_garansi"}},
    {"text": "Saya butuh Jaminan Penawaran untuk proyek BUMN, apakah Bank Nagari bisa bantu?",
        "intent": "product_inquiry", "entities": {"product_name": "bank_garansi"}},
    {"text": "Apa manfaat dari Jaminan Pemeliharaan dalam Bank Garansi?",
        "intent": "product_inquiry", "entities": {"product_name": "bank_garansi"}},
    {"text": "Bisakah Bank Garansi digunakan untuk proyek swasta?",
        "intent": "product_inquiry", "entities": {"product_name": "bank_garansi"}},
    {"text": "Apakah semua jenis Bank Garansi dikenakan biaya provisi di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "bank_garansi"}},
    {"text": "Benarkah Bank Garansi di Bank Nagari tidak ada biaya provisi dan supervisi?",
        "intent": "product_inquiry", "entities": {"product_name": "bank_garansi"}},
    {"text": "Berapa lama jangka waktu Bank Garansi bisa diberikan?",
        "intent": "product_inquiry", "entities": {"product_name": "bank_garansi"}},
    {"text": "Apakah jangka waktu Bank Garansi mengikuti masa kontrak proyek?",
        "intent": "product_inquiry", "entities": {"product_name": "bank_garansi"}},
    {"text": "Nominal Bank Garansi disesuaikan dengan apa saja?",
        "intent": "product_inquiry", "entities": {"product_name": "bank_garansi"}},
    {"text": "Apakah ada fleksibilitas nominal Bank Garansi tergantung kebutuhan proyek?",
        "intent": "product_inquiry", "entities": {"product_name": "bank_garansi"}},
    {"text": "Saya ingin tahu apa saja syarat dokumen untuk mengajukan Bank Garansi.",
        "intent": "product_inquiry", "entities": {"product_name": "bank_garansi"}},
    {"text": "Apakah perlu surat permohonan resmi dari perusahaan untuk Bank Garansi?",
        "intent": "product_inquiry", "entities": {"product_name": "bank_garansi"}},
    {"text": "Apa saja data pengurus perusahaan yang perlu dilampirkan saat ajukan Bank Garansi?",
        "intent": "product_inquiry", "entities": {"product_name": "bank_garansi"}},
    {"text": "Apakah diperlukan akta perubahan perusahaan untuk Bank Garansi?",
        "intent": "product_inquiry", "entities": {"product_name": "bank_garansi"}},
    {"text": "Perizinan usaha apa saja yang harus dilampirkan saat mengajukan Bank Garansi?",
        "intent": "product_inquiry", "entities": {"product_name": "bank_garansi"}},
    {"text": "Untuk Jaminan Uang Muka, dokumen apa yang dibutuhkan?",
        "intent": "product_inquiry", "entities": {"product_name": "bank_garansi"}},
    {"text": "Perusahaan saya punya proyek konstruksi, apakah bisa pakai Bank Garansi dari Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "bank_garansi"}},
    {"text": "Apakah laporan keuangan perusahaan wajib dilampirkan saat mengajukan Bank Garansi?",
        "intent": "product_inquiry", "entities": {"product_name": "bank_garansi"}},
    {"text": "Saya punya rekening giro di Bank Nagari, apakah itu mendukung pengajuan Bank Garansi?",
        "intent": "product_inquiry", "entities": {"product_name": "bank_garansi"}},
    {"text": "Bolehkah menggunakan Bank Garansi untuk kontrak proyek dari APBD?",
        "intent": "product_inquiry", "entities": {"product_name": "bank_garansi"}},
    {"text": "Bank Nagari menyediakan Jaminan Penawaran dan Jaminan Pelaksanaan ya?",
        "intent": "product_inquiry", "entities": {"product_name": "bank_garansi"}},
    {"text": "Bagaimana proses pengajuan Bank Garansi di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "bank_garansi"}},
    {"text": "Apakah SITU dan TDP juga termasuk syarat untuk Bank Garansi?",
        "intent": "product_inquiry", "entities": {"product_name": "bank_garansi"}},
    {"text": "Apa itu Jaminan Pemeliharaan dalam konteks Bank Garansi Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "bank_garansi"}},
    {"text": "Untuk mendapatkan Bank Garansi, perlu daftar riwayat hidup pengurus ya?",
        "intent": "product_inquiry", "entities": {"product_name": "bank_garansi"}},
    {"text": "Saya tertarik mengajukan Bank Garansi untuk proyek pengadaan barang, bagaimana caranya?",
        "intent": "product_inquiry", "entities": {"product_name": "bank_garansi"}},
    {"text": "Apa itu produk KMKK yang ditawarkan Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "kmkk"}},
    {"text": "Saya ingin tahu lebih lanjut mengenai Kredit Modal Kerja Kontraktor di Bank Nagari.",
        "intent": "product_inquiry", "entities": {"product_name": "kmkk"}},
    {"text": "Apa saja jenis pembiayaan yang termasuk dalam KMKK?",
        "intent": "product_inquiry", "entities": {"product_name": "kmkk"}},
    {"text": "Apakah KMKK tersedia dalam bentuk Standby Loan?",
        "intent": "product_inquiry", "entities": {"product_name": "kmkk"}},
    {"text": "KMK Per-Proyek itu maksudnya apa dalam produk KMKK?",
        "intent": "product_inquiry", "entities": {"product_name": "kmkk"}},
    {"text": "KMKK ditujukan untuk siapa saja?",
        "intent": "product_inquiry", "entities": {"product_name": "kmkk"}},
    {"text": "Apakah kontraktor proyek APBN bisa mengajukan KMKK di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "kmkk"}},
    {"text": "Saya pemborong proyek pemerintah, apakah saya bisa ajukan KMKK?",
        "intent": "product_inquiry", "entities": {"product_name": "kmkk"}},
    {"text": "Apa keuntungan utama dari menggunakan fasilitas KMKK?",
        "intent": "product_inquiry", "entities": {"product_name": "kmkk"}},
    {"text": "Berapa jangka waktu maksimum kredit untuk KMKK?",
        "intent": "product_inquiry", "entities": {"product_name": "kmkk"}},
    {"text": "Apakah jangka waktu KMKK bisa diperpanjang setelah proyek selesai?",
        "intent": "product_inquiry", "entities": {"product_name": "kmkk"}},
    {"text": "Berapa persen pembiayaan sendiri yang harus disiapkan peminjam KMKK?",
        "intent": "product_inquiry", "entities": {"product_name": "kmkk"}},
    {"text": "Apakah pembiayaan KMKK harus didukung dana pribadi?",
        "intent": "product_inquiry", "entities": {"product_name": "kmkk"}},
    {"text": "Bagaimana perhitungan maksimal kredit KMKK dilakukan?",
        "intent": "product_inquiry", "entities": {"product_name": "kmkk"}},
    {"text": "Apa saja komponen yang mengurangi nilai kontrak saat menghitung plafon KMKK?",
        "intent": "product_inquiry", "entities": {"product_name": "kmkk"}},
    {"text": "Syarat apa saja yang harus dipenuhi untuk ajukan KMKK?",
        "intent": "product_inquiry", "entities": {"product_name": "kmkk"}},
    {"text": "Apakah perlu mengisi formulir aplikasi untuk mengajukan KMKK?",
        "intent": "product_inquiry", "entities": {"product_name": "kmkk"}},
    {"text": "Apa saja dokumen legal perusahaan yang perlu disiapkan untuk KMKK?",
        "intent": "product_inquiry", "entities": {"product_name": "kmkk"}},
    {"text": "Perlu lampirkan SIUP dan TDP untuk ajukan Kredit KMKK ya?",
        "intent": "product_inquiry", "entities": {"product_name": "kmkk"}},
    {"text": "Apakah saya harus melampirkan laporan keuangan saat mengajukan KMKK?",
        "intent": "product_inquiry", "entities": {"product_name": "kmkk"}},
    {"text": "Apakah kontrak proyek wajib dilampirkan saat pengajuan KMKK?",
        "intent": "product_inquiry", "entities": {"product_name": "kmkk"}},
    {"text": "Kalau saya punya jaminan tambahan, bisa digunakan untuk KMKK?",
        "intent": "product_inquiry", "entities": {"product_name": "kmkk"}},
    {"text": "Apa saja dokumen identitas manajemen perusahaan yang dibutuhkan untuk KMKK?",
        "intent": "product_inquiry", "entities": {"product_name": "kmkk"}},
    {"text": "Bagaimana proses verifikasi riwayat hidup manajemen untuk KMKK?",
        "intent": "product_inquiry", "entities": {"product_name": "kmkk"}},
    {"text": "Perusahaan saya sedang kerjakan proyek BUMD, bisa dapat KMKK?",
        "intent": "product_inquiry", "entities": {"product_name": "kmkk"}},
    {"text": "Apakah kontraktor swasta juga bisa memanfaatkan fasilitas KMKK?",
        "intent": "product_inquiry", "entities": {"product_name": "kmkk"}},
    {"text": "Bagaimana skema realisasi pinjaman secara bertahap pada KMKK Standby Loan?",
        "intent": "product_inquiry", "entities": {"product_name": "kmkk"}},
    {"text": "Apakah rekening giro perusahaan wajib dibuka di Bank Nagari untuk KMKK?",
        "intent": "product_inquiry", "entities": {"product_name": "kmkk"}},
    {"text": "Berapa lama waktu proses pengajuan KMKK biasanya?",
        "intent": "product_inquiry", "entities": {"product_name": "kmkk"}},
    {"text": "Apa keuntungan menggunakan KMKK dibanding pinjaman biasa?",
        "intent": "product_inquiry", "entities": {"product_name": "kmkk"}},
    {"text": "Apa itu KMK-MG dari Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg"}},
    {"text": "Saya mau tanya tentang produk Kredit Modal Kerja Multi Guna, bisa dijelaskan?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg"}},
    {"text": "KMK-MG itu ditujukan untuk siapa saja?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg"}},
    {"text": "Apakah individu bisa mengajukan KMK-MG atau hanya untuk badan usaha?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg"}},
    {"text": "Berapa plafon minimum yang ditawarkan oleh KMK-MG?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg"}},
    {"text": "Saya ingin tahu plafon pinjaman KMK-MG mulai dari berapa?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg"}},
    {"text": "Berapa lama jangka waktu maksimal pinjaman untuk produk KMK-MG?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg"}},
    {"text": "Apakah KMK-MG bisa digunakan untuk usaha di bidang pertanian?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg"}},
    {"text": "Jenis usaha apa saja yang didukung oleh pembiayaan KMK-MG?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg"}},
    {"text": "Bagaimana skema bunga pada produk KMK-MG?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg"}},
    {"text": "Apakah bunga KMK-MG bersifat tetap atau mengikuti sistem anuitas?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg"}},
    {"text": "Berapa bunga yang dikenakan untuk kredit KMK-MG?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg"}},
    {"text": "Saya penasaran dengan biaya administrasi pada KMK-MG, apakah besar?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg"}},
    {"text": "Apa saja syarat utama untuk bisa mengajukan KMK-MG?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg"}},
    {"text": "Apakah perlu melampirkan KTP dan surat nikah saat ajukan KMK-MG?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg"}},
    {"text": "Saya perlu fotokopi surat nikah untuk KMK-MG jika sudah menikah?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg"}},
    {"text": "Apakah perlu melampirkan laporan keuangan saat mengajukan KMK-MG?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg"}},
    {"text": "Dokumen usaha apa saja yang harus dilengkapi untuk KMK-MG?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg"}},
    {"text": "Apakah agunan wajib disertakan untuk pinjaman KMK-MG?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg"}},
    {"text": "Kalau saya punya usaha kecil, bisa ajukan KMK-MG?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg"}},
    {"text": "Bisakah pemerintah daerah juga mengakses fasilitas KMK-MG?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg"}},
    {"text": "Saya pemilik toko kelontong, apakah bisa pinjam lewat KMK-MG?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg"}},
    {"text": "KMK-MG bisa dipakai untuk modal kerja usaha produksi makanan?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg"}},
    {"text": "Kalau usaha saya belum punya izin, apakah tetap bisa ajukan KMK-MG?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg"}},
    {"text": "Untuk pembiayaan KMK-MG, apakah rekening giro wajib dari Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg"}},
    {"text": "Adakah formulir khusus yang harus diisi untuk KMK-MG?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg"}},
    {"text": "Fotokopi buku tabungan termasuk dokumen wajib untuk KMK-MG ya?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg"}},
    {"text": "Siapa saja pihak yang bisa menjadi penjamin untuk kredit KMK-MG?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg"}},
    {"text": "Berapa maksimal tenor kredit jika saya ajukan KMK-MG?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg"}},
    {"text": "Apakah bisa memperpanjang masa kredit KMK-MG setelah 5 tahun?",
        "intent": "product_inquiry", "entities": {"product_name": "kmk_mg"}},
    {"text": "Apa itu fasilitas pembiayaan KI-MG dari Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "ki_mg"}},
    {"text": "Saya ingin tahu lebih lanjut mengenai produk Kredit Investasi Multi Guna, bisa bantu?",
        "intent": "product_inquiry", "entities": {"product_name": "ki_mg"}},
    {"text": "Apakah KI-MG bisa diajukan oleh badan usaha?",
        "intent": "product_inquiry", "entities": {"product_name": "ki_mg"}},
    {"text": "Apakah KI-MG tersedia juga untuk perorangan?",
        "intent": "product_inquiry", "entities": {"product_name": "ki_mg"}},
    {"text": "Pemerintah daerah bisa mengajukan pembiayaan KI-MG juga?",
        "intent": "product_inquiry", "entities": {"product_name": "ki_mg"}},
    {"text": "Jenis investasi apa saja yang bisa didukung oleh KI-MG?",
        "intent": "product_inquiry", "entities": {"product_name": "ki_mg"}},
    {"text": "Berapa plafon pinjaman yang ditawarkan KI-MG?",
        "intent": "product_inquiry", "entities": {"product_name": "ki_mg"}},
    {"text": "Apakah plafon KI-MG bisa disesuaikan dengan nilai proyek investasi?",
        "intent": "product_inquiry", "entities": {"product_name": "ki_mg"}},
    {"text": "Berapa lama maksimal tenor kredit untuk KI-MG?",
        "intent": "product_inquiry", "entities": {"product_name": "ki_mg"}},
    {"text": "Apakah jangka waktu KI-MG fleksibel tergantung kemampuan bayar?",
        "intent": "product_inquiry", "entities": {"product_name": "ki_mg"}},
    {"text": "Bagaimana sistem bunga yang berlaku di KI-MG?",
        "intent": "product_inquiry", "entities": {"product_name": "ki_mg"}},
    {"text": "Apakah saya bisa memilih bunga flat atau anuitas untuk KI-MG?",
        "intent": "product_inquiry", "entities": {"product_name": "ki_mg"}},
    {"text": "Berapakah kisaran bunga dari kredit KI-MG?",
        "intent": "product_inquiry", "entities": {"product_name": "ki_mg"}},
    {"text": "Bagaimana dengan biaya-biaya lain untuk pengajuan KI-MG?",
        "intent": "product_inquiry", "entities": {"product_name": "ki_mg"}},
    {"text": "Saya ingin mengajukan KI-MG, apa saja syarat dokumen yang dibutuhkan?",
        "intent": "product_inquiry", "entities": {"product_name": "ki_mg"}},
    {"text": "Perlu fotokopi KTP dan pas foto juga untuk KI-MG?",
        "intent": "product_inquiry", "entities": {"product_name": "ki_mg"}},
    {"text": "Jika saya sudah menikah, apakah harus menyertakan fotokopi KK atau surat nikah?",
        "intent": "product_inquiry", "entities": {"product_name": "ki_mg"}},
    {"text": "Apakah saya harus menyertakan laporan keuangan saat mengajukan KI-MG?",
        "intent": "product_inquiry", "entities": {"product_name": "ki_mg"}},
    {"text": "Adakah dokumen legalitas yang wajib disertakan untuk KI-MG?",
        "intent": "product_inquiry", "entities": {"product_name": "ki_mg"}},
    {"text": "Kalau saya ingin membangun gudang usaha, bisa dibiayai lewat KI-MG?",
        "intent": "product_inquiry", "entities": {"product_name": "ki_mg"}},
    {"text": "Bolehkah KI-MG digunakan untuk investasi sektor pertanian?",
        "intent": "product_inquiry", "entities": {"product_name": "ki_mg"}},
    {"text": "Bagaimana proses pengajuan KI-MG di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "ki_mg"}},
    {"text": "Apakah agunan wajib disertakan dalam permohonan KI-MG?",
        "intent": "product_inquiry", "entities": {"product_name": "ki_mg"}},
    {"text": "Apakah KI-MG menerima rekening tabungan sebagai bukti dukungan keuangan?",
        "intent": "product_inquiry", "entities": {"product_name": "ki_mg"}},
    {"text": "Kalau usaha saya kecil tapi produktif, bisa mengajukan KI-MG?",
        "intent": "product_inquiry", "entities": {"product_name": "ki_mg"}},
    {"text": "Saya punya objek investasi berupa kendaraan operasional, apakah itu bisa dibiayai KI-MG?",
        "intent": "product_inquiry", "entities": {"product_name": "ki_mg"}},
    {"text": "Untuk usaha berbadan hukum, apakah ada syarat tambahan untuk KI-MG?",
        "intent": "product_inquiry", "entities": {"product_name": "ki_mg"}},
    {"text": "Bisakah pengajuan KI-MG dilakukan oleh koperasi atau lembaga sosial?",
        "intent": "product_inquiry", "entities": {"product_name": "ki_mg"}},
    {"text": "Saya butuh pembiayaan untuk perluasan pabrik, produk yang cocok KI-MG ya?",
        "intent": "product_inquiry", "entities": {"product_name": "ki_mg"}},
    {"text": "Bisa nggak saya lihat simulasi cicilan KI-MG dengan sistem bunga anuitas?",
        "intent": "product_inquiry", "entities": {"product_name": "ki_mg"}},
    {"text": "Apa itu Kredit Rekening Koran dari Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "krk"}},
    {"text": "Saya ingin tahu detail tentang fasilitas KRK, bisa bantu?",
        "intent": "product_inquiry", "entities": {"product_name": "krk"}},
    {"text": "KRK itu termasuk kredit modal kerja atau investasi?",
        "intent": "product_inquiry", "entities": {"product_name": "krk"}},
    {"text": "KRK cocok untuk usaha seperti apa?",
        "intent": "product_inquiry", "entities": {"product_name": "krk"}},
    {"text": "Apakah KRK cocok untuk usaha dengan arus kas tinggi?",
        "intent": "product_inquiry", "entities": {"product_name": "krk"}},
    {"text": "KRK bisa digunakan oleh pelaku usaha di sektor apa saja?",
        "intent": "product_inquiry", "entities": {"product_name": "krk"}},
    {"text": "Apakah KRK bisa digunakan secara berulang?",
        "intent": "product_inquiry", "entities": {"product_name": "krk"}},
    {"text": "Bagaimana sistem revolving di KRK bekerja?",
        "intent": "product_inquiry", "entities": {"product_name": "krk"}},
    {"text": "Berapa plafon minimum yang bisa diajukan untuk KRK?",
        "intent": "product_inquiry", "entities": {"product_name": "krk"}},
    {"text": "Apakah KRK tersedia untuk pinjaman di bawah 250 juta?",
        "intent": "product_inquiry", "entities": {"product_name": "krk"}},
    {"text": "Berapa lama tenor kredit KRK?",
        "intent": "product_inquiry", "entities": {"product_name": "krk"}},
    {"text": "Apakah kredit KRK bisa diperpanjang setelah 1 tahun?",
        "intent": "product_inquiry", "entities": {"product_name": "krk"}},
    {"text": "Bagaimana suku bunga yang berlaku untuk KRK?",
        "intent": "product_inquiry", "entities": {"product_name": "krk"}},
    {"text": "Apakah bunga KRK bersifat tetap atau mengambang?",
        "intent": "product_inquiry", "entities": {"product_name": "krk"}},
    {"text": "KRK menggunakan bunga harian ya? Bisa dijelaskan?",
        "intent": "product_inquiry", "entities": {"product_name": "krk"}},
    {"text": "Apa itu sistem sliding harian pada bunga KRK?",
        "intent": "product_inquiry", "entities": {"product_name": "krk"}},
    {"text": "Saya tertarik dengan fleksibilitas KRK, bagaimana cara ajukannya?",
        "intent": "product_inquiry", "entities": {"product_name": "krk"}},
    {"text": "Dokumen apa saja yang harus saya siapkan untuk mengajukan KRK?",
        "intent": "product_inquiry", "entities": {"product_name": "krk"}},
    {"text": "Kalau sudah menikah, perlu fotokopi KK juga untuk KRK?",
        "intent": "product_inquiry", "entities": {"product_name": "krk"}},
    {"text": "Apakah pas foto juga diperlukan untuk pengajuan KRK?",
        "intent": "product_inquiry", "entities": {"product_name": "krk"}},
    {"text": "Perizinan usaha apa saja yang harus disiapkan untuk KRK?",
        "intent": "product_inquiry", "entities": {"product_name": "krk"}},
    {"text": "Kalau saya punya badan usaha, dokumen apa yang harus saya lampirkan untuk KRK?",
        "intent": "product_inquiry", "entities": {"product_name": "krk"}},
    {"text": "Apakah laporan keuangan usaha wajib untuk mengajukan KRK?",
        "intent": "product_inquiry", "entities": {"product_name": "krk"}},
    {"text": "KRK membutuhkan agunan tidak?",
        "intent": "product_inquiry", "entities": {"product_name": "krk"}},
    {"text": "Apakah rekening giro saya harus di Bank Nagari untuk KRK?",
        "intent": "product_inquiry", "entities": {"product_name": "krk"}},
    {"text": "Bisakah saya menggunakan buku tabungan sebagai bukti keuangan untuk KRK?",
        "intent": "product_inquiry", "entities": {"product_name": "krk"}},
    {"text": "Apakah biaya untuk KRK tergolong ringan dibanding kredit lain?",
        "intent": "product_inquiry", "entities": {"product_name": "krk"}},
    {"text": "Kalau usaha saya perlu fleksibilitas tarik dana, apakah KRK cocok?",
        "intent": "product_inquiry", "entities": {"product_name": "krk"}},
    {"text": "Saya ingin mengajukan kredit usaha dengan sistem rekening koran, itu termasuk KRK?",
        "intent": "product_inquiry", "entities": {"product_name": "krk"}},
    {"text": "Kredit jenis KRK bisa digunakan untuk transaksi via cek ya?",
        "intent": "product_inquiry", "entities": {"product_name": "krk"}},
    {"text": "Apa itu fasilitas KK-BPR di Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_bpr"}},
    {"text": "Bisa jelaskan produk Kredit Modal Kerja untuk BPR?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_bpr"}},
    {"text": "KK-BPR ini diberikan untuk lembaga seperti apa?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_bpr"}},
    {"text": "Apakah hanya BPR berbadan hukum yang bisa mengajukan KK-BPR?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_bpr"}},
    {"text": "Siapa saja target penerima kredit KK-BPR ini?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_bpr"}},
    {"text": "Untuk apa saja kredit KK-BPR bisa digunakan?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_bpr"}},
    {"text": "Apa bedanya penggunaan kredit KMK-BPR dan KI-BPR dalam KK-BPR?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_bpr"}},
    {"text": "Bisakah kredit ini digunakan untuk investasi jangka panjang?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_bpr"}},
    {"text": "Saya ingin menggunakan KK-BPR untuk operasional BPR, apakah bisa?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_bpr"}},
    {"text": "Apakah bisa menggunakan kredit KK-BPR untuk beli kendaraan operasional?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_bpr"}},
    {"text": "Berapa plafon maksimal yang ditawarkan untuk KK-BPR?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_bpr"}},
    {"text": "Berapa lama tenor kredit untuk KMK-BPR?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_bpr"}},
    {"text": "Untuk KI-BPR, jangka waktu pinjamannya bisa sampai berapa tahun?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_bpr"}},
    {"text": "Apakah suku bunga KK-BPR bersifat kompetitif?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_bpr"}},
    {"text": "Dokumen apa saja yang perlu saya siapkan untuk mengajukan KK-BPR?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_bpr"}},
    {"text": "Apakah fotokopi KTP Komisaris wajib disertakan untuk KK-BPR?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_bpr"}},
    {"text": "BPR kami berdiri sebelum 1990, izin usaha apa yang dibutuhkan untuk KK-BPR?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_bpr"}},
    {"text": "Apakah anggaran dasar perusahaan wajib dilampirkan dalam pengajuan KK-BPR?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_bpr"}},
    {"text": "Surat pernyataan direksi tidak rangkap jabatan, apakah diperlukan untuk KK-BPR?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_bpr"}},
    {"text": "Apakah perlu menyertakan bukti setor premi ke LPS untuk KK-BPR?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_bpr"}},
    {"text": "Laporan keuangan seperti apa yang diminta untuk KK-BPR?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_bpr"}},
    {"text": "Jika aset BPR kami di bawah Rp10 Miliar, apa laporan keuangan cukup disetujui RUPS?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_bpr"}},
    {"text": "Apa syarat tambahan jika aset BPR kami di atas Rp10 Miliar?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_bpr"}},
    {"text": "Apakah perlu laporan bulanan juga selain laporan tahunan untuk KK-BPR?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_bpr"}},
    {"text": "Apakah jaminan wajib disertakan saat mengajukan KK-BPR?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_bpr"}},
    {"text": "Indikator kesehatan apa saja yang perlu disertakan dalam pengajuan KK-BPR?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_bpr"}},
    {"text": "Apa saja indikator seperti CAR, KAP, ROA yang diminta untuk KK-BPR?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_bpr"}},
    {"text": "Untuk KMK-BPR, apakah saya harus membuat rencana penggunaan dana?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_bpr"}},
    {"text": "Apa proyeksi arus kas 12 bulan itu wajib untuk KK-BPR?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_bpr"}},
    {"text": "KK-BPR bisa diajukan oleh BPR koperasi?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_bpr"}},
    {"text": "Apa itu kredit KK-KOPERASI dari Bank Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_koperasi"}},
    {"text": "Bisa jelaskan fasilitas Kredit Kepada Koperasi yang tersedia?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_koperasi"}},
    {"text": "Siapa saja yang bisa menerima kredit KK-KOPERASI?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_koperasi"}},
    {"text": "Apakah koperasi pegawai swasta bisa mengajukan KK-KOPERASI?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_koperasi"}},
    {"text": "Apakah kredit ini hanya untuk koperasi pemerintah saja?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_koperasi"}},
    {"text": "Untuk kebutuhan apa kredit KK-KOPERASI bisa digunakan?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_koperasi"}},
    {"text": "Bisakah KK-KOPERASI digunakan untuk usaha koperasi simpan pinjam?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_koperasi"}},
    {"text": "Berapa plafon maksimal yang diberikan untuk KK-KOPERASI?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_koperasi"}},
    {"text": "Apa yang menentukan plafon kredit KK-KOPERASI?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_koperasi"}},
    {"text": "Berapa lama tenor pinjaman untuk KK-KOPERASI?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_koperasi"}},
    {"text": "Bagaimana sistem bunga yang diterapkan pada KK-KOPERASI?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_koperasi"}},
    {"text": "Apakah bunga KK-KOPERASI menggunakan sistem sliding harian?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_koperasi"}},
    {"text": "Apakah suku bunga KK-KOPERASI tergolong bersaing?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_koperasi"}},
    {"text": "Apa saja syarat yang dibutuhkan untuk mengajukan kredit KK-KOPERASI?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_koperasi"}},
    {"text": "Pengurus koperasi perlu melampirkan dokumen apa saja untuk KK-KOPERASI?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_koperasi"}},
    {"text": "Apakah diperlukan surat keputusan pengangkatan pengurus koperasi untuk kredit ini?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_koperasi"}},
    {"text": "Adakah syarat khusus untuk pengurus koperasi terkait rangkap jabatan?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_koperasi"}},
    {"text": "Apakah anggota koperasi harus berstatus pegawai tetap?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_koperasi"}},
    {"text": "Saya dengar perlu ada surat pernyataan anggota koperasi, apa isinya?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_koperasi"}},
    {"text": "Apakah ada format surat khusus dari bank untuk anggota koperasi?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_koperasi"}},
    {"text": "Apakah harus menyatakan bahwa kredit hanya digunakan untuk simpan pinjam?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_koperasi"}},
    {"text": "Perlu daftar riwayat hidup pengurus juga?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_koperasi"}},
    {"text": "Bagaimana dengan dokumen legal koperasi? Apa saja yang harus disiapkan?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_koperasi"}},
    {"text": "Apakah NPWP dan SIUP diperlukan untuk mengajukan KK-KOPERASI?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_koperasi"}},
    {"text": "Perlukah rekomendasi dari Dinas Koperasi untuk kredit ini?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_koperasi"}},
    {"text": "Kalau koperasi swasta, rekomendasinya dari siapa?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_koperasi"}},
    {"text": "Perlu menyertakan laporan keuangan juga untuk KK-KOPERASI?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_koperasi"}},
    {"text": "Apa yang dimaksud daftar nominatif anggota koperasi untuk pengajuan kredit?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_koperasi"}},
    {"text": "Print out rekening koperasi juga wajib dilampirkan ya?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_koperasi"}},
    {"text": "Bagaimana cara mengajukan Kredit Kepada Koperasi ini?",
        "intent": "product_inquiry", "entities": {"product_name": "kk_koperasi"}},

    # Produk Pembiayaan Multijasa
    {"text": "Apa itu Pembiayaan Multijasa?", "intent": "product_inquiry",
        "entities": {"product_name": "pembiayaan_multijasa"}},
    {"text": "Apa yang dimaksud dengan Pembiayaan Multijasa?",
        "intent": "product_inquiry", "entities": {"product_name": "pembiayaan_multijasa"}},
    {"text": "Pembiayaan Multijasa itu apa sih?", "intent": "product_inquiry",
        "entities": {"product_name": "pembiayaan_multijasa"}},
    {"text": "Bisa jelaskan lebih lanjut tentang Pembiayaan Multijasa?",
        "intent": "product_inquiry", "entities": {"product_name": "pembiayaan_multijasa"}},
    {"text": "Apa tujuan utama dari Pembiayaan Multijasa?", "intent": "product_inquiry",
        "entities": {"product_name": "pembiayaan_multijasa"}},
    {"text": "Apa saja produk yang termasuk dalam Pembiayaan Multijasa?",
        "intent": "product_inquiry", "entities": {"product_name": "pembiayaan_multijasa"}},
    {"text": "Bagaimana cara kerja Pembiayaan Multijasa?", "intent": "product_inquiry",
        "entities": {"product_name": "pembiayaan_multijasa"}},
    {"text": "Pembiayaan Multijasa, siapa saja yang dapat mengaksesnya?",
        "intent": "product_inquiry", "entities": {"product_name": "pembiayaan_multijasa"}},
    {"text": "Apa keuntungan menggunakan Pembiayaan Multijasa?",
        "intent": "product_inquiry", "entities": {"product_name": "pembiayaan_multijasa"}},

    {"text": "Apa saja kebutuhan yang dibiayai oleh Pembiayaan Multijasa?",
        "intent": "product_inquiry", "entities": {"product_name": "pembiayaan_multijasa"}},
    {"text": "Apa saja kebutuhan yang dapat dibiayai dengan Pembiayaan Multijasa?",
        "intent": "product_inquiry", "entities": {"product_name": "pembiayaan_multijasa"}},
    {"text": "Pembiayaan Multijasa bisa digunakan untuk kebutuhan apa saja?",
        "intent": "product_inquiry", "entities": {"product_name": "pembiayaan_multijasa"}},
    {"text": "Jenis kebutuhan apa yang dapat dibiayai melalui Pembiayaan Multijasa?",
        "intent": "product_inquiry", "entities": {"product_name": "pembiayaan_multijasa"}},
    {"text": "Pembiayaan Multijasa, untuk tujuan apa saja bisa digunakan?",
        "intent": "product_inquiry", "entities": {"product_name": "pembiayaan_multijasa"}},
    {"text": "Apa saja jenis pembiayaan yang termasuk dalam Pembiayaan Multijasa?",
        "intent": "product_inquiry", "entities": {"product_name": "pembiayaan_multijasa"}},
    {"text": "Kebutuhan pribadi atau bisnis apa saja yang dapat didanai melalui Pembiayaan Multijasa?",
        "intent": "product_inquiry", "entities": {"product_name": "pembiayaan_multijasa"}},
    {"text": "Pembiayaan Multijasa dapat digunakan untuk apa saja?",
        "intent": "product_inquiry", "entities": {"product_name": "pembiayaan_multijasa"}},
    {"text": "Kebutuhan apa yang paling cocok dibiayai dengan Pembiayaan Multijasa?",
        "intent": "product_inquiry", "entities": {"product_name": "pembiayaan_multijasa"}},

    {"text": "Siapa yang bisa mendapatkan Pembiayaan Multijasa?",
        "intent": "product_inquiry", "entities": {"product_name": "pembiayaan_multijasa"}},
    {"text": "Siapa saja yang bisa mengajukan Pembiayaan Multijasa?",
        "intent": "product_inquiry", "entities": {"product_name": "pembiayaan_multijasa"}},
    {"text": "Pembiayaan Multijasa ditujukan untuk siapa saja?",
        "intent": "product_inquiry", "entities": {"product_name": "pembiayaan_multijasa"}},
    {"text": "Siapa yang memenuhi syarat untuk mendapatkan Pembiayaan Multijasa?",
        "intent": "product_inquiry", "entities": {"product_name": "pembiayaan_multijasa"}},
    {"text": "Apakah Pembiayaan Multijasa hanya untuk perorangan atau juga untuk perusahaan?",
        "intent": "product_inquiry", "entities": {"product_name": "pembiayaan_multijasa"}},
    {"text": "Siapa saja yang dapat mengakses Pembiayaan Multijasa?",
        "intent": "product_inquiry", "entities": {"product_name": "pembiayaan_multijasa"}},
    {"text": "Pembiayaan Multijasa tersedia untuk individu atau juga badan usaha?",
        "intent": "product_inquiry", "entities": {"product_name": "pembiayaan_multijasa"}},
    {"text": "Apakah ada persyaratan khusus untuk menjadi penerima Pembiayaan Multijasa?",
        "intent": "product_inquiry", "entities": {"product_name": "pembiayaan_multijasa"}},
    {"text": "Siapa yang dapat memanfaatkan Pembiayaan Multijasa ini?",
        "intent": "product_inquiry", "entities": {"product_name": "pembiayaan_multijasa"}},

    {"text": "Apa syarat pembiayaan multijasa?", "intent": "product_inquiry",
        "entities": {"product_name": "pembiayaan_multijasa"}},
    {"text": "Apa saja syarat untuk mendapatkan Pembiayaan Multijasa?",
        "intent": "product_inquiry", "entities": {"product_name": "pembiayaan_multijasa"}},
    {"text": "Apa persyaratan untuk mengajukan Pembiayaan Multijasa?",
        "intent": "product_inquiry", "entities": {"product_name": "pembiayaan_multijasa"}},
    {"text": "Syarat apa yang harus dipenuhi untuk mengajukan Pembiayaan Multijasa?",
        "intent": "product_inquiry", "entities": {"product_name": "pembiayaan_multijasa"}},
    {"text": "Apakah ada persyaratan dokumen untuk mengajukan Pembiayaan Multijasa?",
        "intent": "product_inquiry", "entities": {"product_name": "pembiayaan_multijasa"}},
    {"text": "Bagaimana cara mengajukan Pembiayaan Multijasa dan apa saja syaratnya?",
        "intent": "product_inquiry", "entities": {"product_name": "pembiayaan_multijasa"}},
    {"text": "Apa yang harus dipenuhi agar bisa mendapatkan Pembiayaan Multijasa?",
        "intent": "product_inquiry", "entities": {"product_name": "pembiayaan_multijasa"}},
    {"text": "Untuk mendapatkan Pembiayaan Multijasa, ada syarat khusus tidak?",
        "intent": "product_inquiry", "entities": {"product_name": "pembiayaan_multijasa"}},
    {"text": "Apa saja ketentuan yang perlu dipenuhi untuk mendapatkan Pembiayaan Multijasa?",
        "intent": "product_inquiry", "entities": {"product_name": "pembiayaan_multijasa"}},

    {
        "text": "Apa itu Tabungan Sikoci Pendidikan Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pendidikan_syariah"}
    },
    {
        "text": "Bisa dijelaskan seperti apa Sikoci Pendidikan Syariah itu?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pendidikan_syariah"}
    },
    {
        "text": "Saya ingin tahu detail tentang Tabungan Sikoci Pendidikan Syariah.",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pendidikan_syariah"}
    },
    {
        "text": "Sikoci Pendidikan Syariah cocok untuk anak usia berapa ya?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pendidikan_syariah"}
    },
    {
        "text": "Tabungan Sikoci Pendidikan Syariah ini bisa dipakai untuk usia 18 tahun ke atas?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pendidikan_syariah"}
    },
    {
        "text": "Apa saja manfaat dari membuka Sikoci Pendidikan Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pendidikan_syariah"}
    },
    {
        "text": "Apakah Sikoci Pendidikan Syariah diawasi oleh Dewan Pengawas Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pendidikan_syariah"}
    },
    {
        "text": "Apakah tabungan Sikoci Pendidikan Syariah mengikuti prinsip-prinsip syariah Islam?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pendidikan_syariah"}
    },
    {
        "text": "Apa perbedaan antara akad Wadi’ah dan Mudharabah dalam Sikoci Pendidikan Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pendidikan_syariah"}
    },
    {
        "text": "Saya ingin buka tabungan anak syariah, apakah Sikoci Pendidikan Syariah bisa?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pendidikan_syariah"}
    },
    {
        "text": "Apakah Sikoci Pendidikan Syariah tersedia dalam mata uang rupiah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pendidikan_syariah"}
    },
    {
        "text": "Untuk membuka Sikoci Pendidikan Syariah, apakah ada setoran awal?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pendidikan_syariah"}
    },
    {
        "text": "Berapa minimal setoran awal untuk Tabungan Sikoci Pendidikan Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pendidikan_syariah"}
    },
    {
        "text": "Berapa jumlah setoran selanjutnya untuk Sikoci Pendidikan Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pendidikan_syariah"}
    },
    {
        "text": "Syarat usia untuk buka Sikoci Pendidikan Syariah itu sampai umur berapa?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pendidikan_syariah"}
    },
    {
        "text": "Apakah nasabah Sikoci Pendidikan Syariah harus belum menikah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pendidikan_syariah"}
    },
    {
        "text": "Untuk membuka Sikoci Pendidikan Syariah, apakah saya harus WNI?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pendidikan_syariah"}
    },
    {
        "text": "Apakah Sikoci Pendidikan Syariah tersedia untuk anak di bawah 17 tahun?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pendidikan_syariah"}
    },
    {
        "text": "Dokumen apa saja yang dibutuhkan untuk buka Sikoci Pendidikan Syariah untuk anak?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pendidikan_syariah"}
    },
    {
        "text": "Kalau saya masih 20 tahun, bisa buka Sikoci Pendidikan Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pendidikan_syariah"}
    },
    {
        "text": "Apakah Sikoci Pendidikan Syariah mensyaratkan KTP orang tua juga?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pendidikan_syariah"}
    },
    {
        "text": "Kalau saya di bawah 17 tahun, dokumen apa yang perlu saya siapkan untuk buka Sikoci Pendidikan Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pendidikan_syariah"}
    },
    {
        "text": "Apakah Sikoci Pendidikan Syariah menggunakan sistem bagi hasil?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pendidikan_syariah"}
    },
    {
        "text": "Bagaimana sistem titipan pada Sikoci Pendidikan Syariah itu bekerja?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pendidikan_syariah"}
    },
    {
        "text": "Sikoci Pendidikan Syariah menyediakan pilihan akad ya? Bisa pilih yang mana?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pendidikan_syariah"}
    },
    {
        "text": "Apakah saya bisa pilih antara akad Wadi’ah dan Mudharabah saat buka Sikoci Pendidikan Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pendidikan_syariah"}
    },
    {
        "text": "Apakah ada biaya administrasi bulanan untuk Sikoci Pendidikan Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pendidikan_syariah"}
    },
    {
        "text": "Apakah ada penalti jika menutup Sikoci Pendidikan Syariah sebelum waktu tertentu?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pendidikan_syariah"}
    },
    {
        "text": "Kalau saya ingin tabungan pendidikan berbasis syariah, apakah Sikoci Pendidikan Syariah cocok?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pendidikan_syariah"}
    },
    {
        "text": "Saya sedang cari tabungan anak yang sesuai syariat Islam, bisa jelaskan tentang Sikoci Pendidikan Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_pendidikan_syariah"}
    },

    {
        "text": "Apa itu Tabungan Tabsyir?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabsyir"}
    },
    {
        "text": "Bisa jelaskan Tabungan Tabsyir secara singkat?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabsyir"}
    },
    {
        "text": "Saya ingin tahu lebih lanjut tentang produk Tabsyir dari Bank Nagari.",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabsyir"}
    },
    {
        "text": "Tabungan Tabsyir ditujukan untuk siapa saja?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabsyir"}
    },
    {
        "text": "Apakah Tabsyir bisa dibuka oleh lembaga atau perusahaan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabsyir"}
    },
    {
        "text": "Apa saja keuntungan membuka Tabungan Tabsyir?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabsyir"}
    },
    {
        "text": "Apakah Tabsyir menggunakan sistem bagi hasil?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabsyir"}
    },
    {
        "text": "Akad yang digunakan pada Tabungan Tabsyir itu apa?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabsyir"}
    },
    {
        "text": "Apakah nisbah di Tabsyir lebih tinggi dari tabungan reguler?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabsyir"}
    },
    {
        "text": "Berapakah nisbah yang ditawarkan untuk Tabsyir?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabsyir"}
    },
    {
        "text": "Kalau saldo saya cuma 2 juta, apa masih dapat nisbah dari Tabsyir?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabsyir"}
    },
    {
        "text": "Minimal saldo berapa agar dapat nisbah di Tabsyir?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabsyir"}
    },
    {
        "text": "Berapa setoran awal untuk membuka Tabsyir?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabsyir"}
    },
    {
        "text": "Tabungan Tabsyir butuh saldo minimum berapa supaya tetap aktif?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabsyir"}
    },
    {
        "text": "Apakah Tabsyir mendukung transaksi internasional?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabsyir"}
    },
    {
        "text": "Saya ingin kirim uang ke luar negeri, bisa pakai Tabsyir?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabsyir"}
    },
    {
        "text": "Tabsyir punya akses 24 jam ke layanan perbankan gak?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabsyir"}
    },
    {
        "text": "Apakah Tabsyir terintegrasi dengan fitur digital banking seperti Ollin?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabsyir"}
    },
    {
        "text": "Fitur digital apa saja yang tersedia di Tabungan Tabsyir?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabsyir"}
    },
    {
        "text": "Apakah Tabsyir bisa digunakan untuk auto debet dan notifikasi transaksi?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabsyir"}
    },
    {
        "text": "Saya butuh tabungan bisnis syariah dengan akses ATM, cocok gak pakai Tabsyir?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabsyir"}
    },
    {
        "text": "Apakah Tabsyir bisa digunakan oleh WNA juga?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabsyir"}
    },
    {
        "text": "Dokumen apa saja yang dibutuhkan untuk buka Tabsyir atas nama pribadi?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabsyir"}
    },
    {
        "text": "Kalau saya WNI dan mau buka Tabsyir, butuh NPWP juga gak?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabsyir"}
    },
    {
        "text": "Kalau saya wakili perusahaan, dokumen apa saja yang perlu untuk buka Tabsyir?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabsyir"}
    },
    {
        "text": "Apakah akta pendirian perusahaan diperlukan untuk buka rekening Tabsyir non-perorangan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabsyir"}
    },
    {
        "text": "Apakah ada biaya bulanan atau penalti jika tidak aktif di Tabsyir?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabsyir"}
    },
    {
        "text": "Tabungan Tabsyir menggunakan prinsip syariah, apakah diawasi oleh DPS juga?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabsyir"}
    },
    {
        "text": "Kalau saya ingin buka tabungan untuk usaha kecil, apakah Tabsyir cocok?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabsyir"}
    },
    {
        "text": "Apakah Tabsyir mendukung lembaga pendidikan atau organisasi sosial sebagai nasabah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabsyir"}
    },
    {
        "text": "Saya butuh rekening syariah untuk bisnis dan transfer lintas negara, bisa pakai Tabsyir?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabsyir"}
    },
    {
        "text": "Apakah produk Tabsyir bisa digunakan sepenuhnya via layanan digital?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabsyir"}
    },
    {
        "text": "Apa saja fitur unggulan Tabsyir dibanding tabungan syariah lainnya?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabsyir"}
    },

    {
        "text": "Apa itu Tabungan Tahari Muda?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tahari_muda"}
    },
    {
        "text": "Bisa jelaskan secara singkat tentang Tahari Muda?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tahari_muda"}
    },
    {
        "text": "Apa saja keunggulan dari Tabungan Tahari Muda?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tahari_muda"}
    },
    {
        "text": "Untuk siapa Tabungan Tahari Muda diperuntukkan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tahari_muda"}
    },
    {
        "text": "Apakah Tahari Muda ditujukan untuk nasabah di bawah 21 tahun?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tahari_muda"}
    },
    {
        "text": "Apakah Tabungan Tahari Muda bisa digunakan untuk biaya haji?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tahari_muda"}
    },
    {
        "text": "Saya ingin mulai rencana haji dari sekarang, apakah Tahari Muda cocok?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tahari_muda"}
    },
    {
        "text": "Tahari Muda pakai akad apa ya?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tahari_muda"}
    },
    {
        "text": "Apakah Tahari Muda menggunakan akad Wadi’ah atau Mudharabah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tahari_muda"}
    },
    {
        "text": "Kalau saya ingin akad titipan, bisa dipilih saat buka Tahari Muda?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tahari_muda"}
    },
    {
        "text": "Apa saja manfaat menabung di Tahari Muda sejak dini?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tahari_muda"}
    },
    {
        "text": "Apakah Tahari Muda cocok untuk anak remaja yang ingin merencanakan ibadah haji?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tahari_muda"}
    },
    {
        "text": "Apakah Tahari Muda membantu membangun kebiasaan menabung untuk ibadah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tahari_muda"}
    },
    {
        "text": "Berapa setoran awal untuk membuka Tahari Muda?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tahari_muda"}
    },
    {
        "text": "Setoran pertama di Tahari Muda minimal berapa rupiah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tahari_muda"}
    },
    {
        "text": "Berapa jumlah setoran selanjutnya setelah buka Tahari Muda?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tahari_muda"}
    },
    {
        "text": "Apakah bisa setor Rp 10.000 untuk Tahari Muda setiap bulan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tahari_muda"}
    },
    {
        "text": "Apa syarat usia untuk membuka Tabungan Tahari Muda?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tahari_muda"}
    },
    {
        "text": "Tahari Muda bisa dibuka oleh anak usia 15 tahun?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tahari_muda"}
    },
    {
        "text": "Apakah harus WNI untuk membuka Tahari Muda?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tahari_muda"}
    },
    {
        "text": "Saya berusia 20 tahun dan belum menikah, apakah bisa buka Tahari Muda?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tahari_muda"}
    },
    {
        "text": "Apa saja dokumen yang diperlukan untuk buka Tahari Muda?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tahari_muda"}
    },
    {
        "text": "Kalau saya masih di bawah 17 tahun, dokumen apa saja yang harus disiapkan untuk buka Tahari Muda?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tahari_muda"}
    },
    {
        "text": "Saya 18 tahun, buka Tahari Muda cukup pakai KTP saya dan orang tua?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tahari_muda"}
    },
    {
        "text": "Apakah Tahari Muda bebas biaya administrasi?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tahari_muda"}
    },
    {
        "text": "Adakah penalti jika menutup Tahari Muda sebelum waktu tertentu?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tahari_muda"}
    },
    {
        "text": "Saya ingin buka tabungan haji syariah untuk anak, apakah Tahari Muda tepat?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tahari_muda"}
    },
    {
        "text": "Apa perbedaan Tahari Muda dengan tabungan haji lainnya?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tahari_muda"}
    },
    {
        "text": "Apakah saya bisa menabung di Tahari Muda meski belum daftar haji resmi?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tahari_muda"}
    },
    {
        "text": "Tabungan Tahari Muda diawasi oleh Dewan Pengawas Syariah juga?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tahari_muda"}
    },
    {
        "text": "Saya butuh tabungan syariah khusus rencana haji anak, bisa info tentang Tahari Muda?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tahari_muda"}
    },
    {
        "text": "Apa itu pembiayaan PKB Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "pkb_syariah"}
    },
    {
        "text": "Bisa dijelaskan fasilitas PKB Syariah dari Bank Nagari?",
        "intent": "product_inquiry",
        "entities": {"product_name": "pkb_syariah"}
    },
    {
        "text": "Saya ingin membeli mobil, apakah bisa pakai pembiayaan PKB Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "pkb_syariah"}
    },
    {
        "text": "Apakah PKB Syariah bisa digunakan untuk beli kendaraan bekas?",
        "intent": "product_inquiry",
        "entities": {"product_name": "pkb_syariah"}
    },
    {
        "text": "Apakah PKB Syariah juga bisa untuk refinancing kendaraan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "pkb_syariah"}
    },
    {
        "text": "Apakah PKB Syariah menggunakan sistem riba?",
        "intent": "product_inquiry",
        "entities": {"product_name": "pkb_syariah"}
    },
    {
        "text": "Apa saja keunggulan dari PKB Syariah dibanding pembiayaan konvensional?",
        "intent": "product_inquiry",
        "entities": {"product_name": "pkb_syariah"}
    },
    {
        "text": "Apakah PKB Syariah menggunakan prinsip syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "pkb_syariah"}
    },
    {
        "text": "Untuk siapa saja pembiayaan PKB Syariah ini tersedia?",
        "intent": "product_inquiry",
        "entities": {"product_name": "pkb_syariah"}
    },
    {
        "text": "Apakah PKB Syariah bisa diajukan oleh pensiunan PNS?",
        "intent": "product_inquiry",
        "entities": {"product_name": "pkb_syariah"}
    },
    {
        "text": "Saya seorang wiraswasta, apakah bisa mengajukan PKB Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "pkb_syariah"}
    },
    {
        "text": "Berapa lama jangka waktu pembiayaan PKB Syariah bisa diberikan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "pkb_syariah"}
    },
    {
        "text": "Apakah tenor PKB Syariah bisa sampai 84 bulan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "pkb_syariah"}
    },
    {
        "text": "Berapa biaya administrasi untuk mengajukan PKB Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "pkb_syariah"}
    },
    {
        "text": "Saya perlu tahu besaran dana sendiri yang harus disiapkan untuk PKB Syariah.",
        "intent": "product_inquiry",
        "entities": {"product_name": "pkb_syariah"}
    },
    {
        "text": "Berapa persen minimal uang muka untuk PKB Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "pkb_syariah"}
    },
    {
        "text": "Apakah saya harus WNI untuk bisa mengajukan pembiayaan PKB Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "pkb_syariah"}
    },
    {
        "text": "Apakah usia saya 68 tahun masih bisa mengajukan PKB Syariah sebagai pensiunan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "pkb_syariah"}
    },
    {
        "text": "Apa batasan usia maksimal untuk nasabah PKB Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "pkb_syariah"}
    },
    {
        "text": "Apakah ada golongan tertentu yang tidak boleh mengajukan PKB Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "pkb_syariah"}
    },
    {
        "text": "Berapa margin/ujrah untuk tenor 1 sampai 12 bulan di PKB Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "pkb_syariah"}
    },
    {
        "text": "Kalau saya pilih tenor 5 tahun, berapa ujrah yang dikenakan di PKB Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "pkb_syariah"}
    },
    {
        "text": "Ujrah untuk pembiayaan 6 tahun di PKB Syariah itu berapa persen?",
        "intent": "product_inquiry",
        "entities": {"product_name": "pkb_syariah"}
    },
    {
        "text": "Apakah ada program khusus untuk kepemilikan mobil di PKB Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "pkb_syariah"}
    },
    {
        "text": "PKB Syariah punya skema Car Ownership Program?",
        "intent": "product_inquiry",
        "entities": {"product_name": "pkb_syariah"}
    },
    {
        "text": "Apa perbedaan skema reguler dengan Car Ownership Program di PKB Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "pkb_syariah"}
    },
    {
        "text": "Saya dapat tunjangan transportasi dari kantor, apakah PKB Syariah cocok untuk saya?",
        "intent": "product_inquiry",
        "entities": {"product_name": "pkb_syariah"}
    },
    {
        "text": "Bisakah kendaraan yang saya punya dijadikan agunan untuk PKB Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "pkb_syariah"}
    },
    {
        "text": "Apakah PKB Syariah bisa untuk refinancing kendaraan yang sudah saya miliki?",
        "intent": "product_inquiry",
        "entities": {"product_name": "pkb_syariah"}
    },
    {
        "text": "PKB Syariah tersedia juga untuk pembiayaan take over dari bank lain?",
        "intent": "product_inquiry",
        "entities": {"product_name": "pkb_syariah"}
    },
    {
        "text": "Apakah plafon pembiayaan PKB Syariah disesuaikan dengan harga pasar kendaraan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "pkb_syariah"}
    },
    {
        "text": "Saya ingin pembiayaan mobil syariah tanpa riba, bisa dijelaskan tentang PKB Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "pkb_syariah"}
    },
    {
        "text": "Apa saja fitur utama dari produk PKB Syariah yang membedakannya dari kredit kendaraan biasa?",
        "intent": "product_inquiry",
        "entities": {"product_name": "pkb_syariah"}
    },
    {
        "text": "Apa itu Tabungan Tahari Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabungan_tahari_syariah"}
    },
    {
        "text": "Bisa jelaskan Tabungan Tahari Syariah secara singkat?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabungan_tahari_syariah"}
    },
    {
        "text": "Tabungan Tahari Syariah itu ditujukan untuk siapa?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabungan_tahari_syariah"}
    },
    {
        "text": "Apakah Tabungan Tahari Syariah bisa digunakan untuk persiapan haji?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabungan_tahari_syariah"}
    },
    {
        "text": "Apa manfaat dari memiliki Tabungan Tahari Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabungan_tahari_syariah"}
    },
    {
        "text": "Apakah Tabungan Tahari Syariah mengikuti prinsip syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabungan_tahari_syariah"}
    },
    {
        "text": "Saya ingin menabung untuk haji, apakah cocok buka Tahari Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabungan_tahari_syariah"}
    },
    {
        "text": "Apakah Tabungan Tahari Syariah bebas riba?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabungan_tahari_syariah"}
    },
    {
        "text": "Apakah tabungan ini bisa digunakan sebagai syarat daftar haji reguler?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabungan_tahari_syariah"}
    },
    {
        "text": "Berapa saldo minimal untuk bisa daftar haji lewat Tabungan Tahari Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabungan_tahari_syariah"}
    },
    {
        "text": "Saya dengar saldo minimal untuk daftar haji adalah 25 juta, apa benar di Tahari Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabungan_tahari_syariah"}
    },
    {
        "text": "Berapa setoran awal untuk membuka Tabungan Tahari Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabungan_tahari_syariah"}
    },
    {
        "text": "Saldo minimum yang harus dijaga di Tahari Syariah itu berapa?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabungan_tahari_syariah"}
    },
    {
        "text": "Apakah saya bisa mulai menabung haji dengan Rp 100.000 lewat Tahari Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabungan_tahari_syariah"}
    },
    {
        "text": "Apa saja dokumen yang dibutuhkan untuk buka Tabungan Tahari Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabungan_tahari_syariah"}
    },
    {
        "text": "Apakah saya perlu mengisi formulir pembukaan rekening untuk Tahari Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabungan_tahari_syariah"}
    },
    {
        "text": "Apakah saya perlu melampirkan FDN dan KTP untuk buka Tahari Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabungan_tahari_syariah"}
    },
    {
        "text": "Kalau saya WNA, apa bisa buka Tahari Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabungan_tahari_syariah"}
    },
    {
        "text": "Apakah WNA harus pakai ITAS/ITAP untuk buka Tabungan Tahari Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabungan_tahari_syariah"}
    },
    {
        "text": "Kenapa perlu pas foto banyak untuk buka Tahari Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabungan_tahari_syariah"}
    },
    {
        "text": "Berapa banyak pas foto yang dibutuhkan untuk buka Tahari Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabungan_tahari_syariah"}
    },
    {
        "text": "Apakah Tabungan Tahari Syariah transparan dalam akadnya?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabungan_tahari_syariah"}
    },
    {
        "text": "Adakah biaya administrasi untuk Tabungan Tahari Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabungan_tahari_syariah"}
    },
    {
        "text": "Saya cari tabungan haji berbasis syariah, apakah Tahari Syariah bisa jadi pilihan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabungan_tahari_syariah"}
    },
    {
        "text": "Kalau sudah punya Tahari Syariah, apa bisa gabung dengan pembiayaan haji nanti?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabungan_tahari_syariah"}
    },
    {
        "text": "Apa Tahari Syariah bisa dikombinasikan dengan program pembiayaan haji?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabungan_tahari_syariah"}
    },
    {
        "text": "Apa keuntungan utama dari Tabungan Tahari Syariah dibanding tabungan biasa?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabungan_tahari_syariah"}
    },
    {
        "text": "Saya ingin membuka tabungan khusus untuk daftar haji, apakah Tahari Syariah cocok?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabungan_tahari_syariah"}
    },
    {
        "text": "Apakah saldo di Tahari Syariah otomatis bisa digunakan untuk daftar haji reguler?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabungan_tahari_syariah"}
    },
    {
        "text": "Saya butuh tabungan syariah yang diarahkan untuk ibadah haji, bisa info tentang Tahari Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "tabungan_tahari_syariah"}
    },
    {
        "text": "Apa itu Tabungan Sikoci Umroh?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_umroh"}
    },
    {
        "text": "Bisa jelaskan tentang produk Sikoci Umroh?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_umroh"}
    },
    {
        "text": "Apakah Sikoci Umroh termasuk tabungan syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_umroh"}
    },
    {
        "text": "Tabungan Sikoci Umroh cocok untuk apa saja?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_umroh"}
    },
    {
        "text": "Apakah tabungan Sikoci Umroh bisa dicairkan kapan saja?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_umroh"}
    },
    {
        "text": "Kapan dana Sikoci Umroh boleh dicairkan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_umroh"}
    },
    {
        "text": "Apakah hanya bisa dicairkan jika dana cukup untuk umroh?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_umroh"}
    },
    {
        "text": "Bagaimana jika saya butuh dana mendesak, apakah bisa tarik dari Sikoci Umroh?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_umroh"}
    },
    {
        "text": "Kalau saya sakit dan butuh dana, bisa tarik tabungan Sikoci Umroh?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_umroh"}
    },
    {
        "text": "Apa saja syarat pencairan dana dari Sikoci Umroh?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_umroh"}
    },
    {
        "text": "Apakah Sikoci Umroh bebas biaya administrasi?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_umroh"}
    },
    {
        "text": "Apakah saya bisa buka Sikoci Umroh di kantor cabang Bank Nagari konvensional?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_umroh"}
    },
    {
        "text": "Apakah Sikoci Umroh bisa dilayani di seluruh kantor Bank Nagari?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_umroh"}
    },
    {
        "text": "Apa manfaat membuka Sikoci Umroh dibanding tabungan biasa?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_umroh"}
    },
    {
        "text": "Apa keunggulan Sikoci Umroh dari Bank Nagari?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_umroh"}
    },
    {
        "text": "Berapa setoran awal untuk buka tabungan Sikoci Umroh?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_umroh"}
    },
    {
        "text": "Setoran pertama Sikoci Umroh minimal berapa rupiah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_umroh"}
    },
    {
        "text": "Berapa minimal setoran lanjutan pada tabungan Sikoci Umroh?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_umroh"}
    },
    {
        "text": "Apakah Sikoci Umroh hanya bisa dimiliki oleh WNI?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_umroh"}
    },
    {
        "text": "Apakah tabungan Sikoci Umroh bisa dibuka oleh perorangan saja?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_umroh"}
    },
    {
        "text": "Sikoci Umroh menggunakan akad apa?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_umroh"}
    },
    {
        "text": "Akad apa yang digunakan dalam Sikoci Umroh, mudharabah atau wadiah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_umroh"}
    },
    {
        "text": "Apakah saya bisa pilih akad dalam tabungan Sikoci Umroh?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_umroh"}
    },
    {
        "text": "Apakah Sikoci Umroh cocok untuk menabung umroh keluarga?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_umroh"}
    },
    {
        "text": "Saya ingin menabung umroh bersama komunitas, cocok pakai Sikoci Umroh?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_umroh"}
    },
    {
        "text": "Apakah Sikoci Umroh bisa digunakan untuk perencanaan umroh pribadi?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_umroh"}
    },
    {
        "text": "Apakah Sikoci Umroh bisa bantu mencapai target dana umroh?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_umroh"}
    },
    {
        "text": "Apakah Sikoci Umroh bisa dipakai untuk tujuan selain umroh?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_umroh"}
    },
    {
        "text": "Apakah Sikoci Umroh bisa digunakan untuk dana pensiun?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_umroh"}
    },
    {
        "text": "Bisakah Sikoci Umroh dijadikan rekening afiliasi untuk pembiayaan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_umroh"}
    },
    {
        "text": "Saya ingin tabungan umroh tanpa biaya admin, apakah Sikoci Umroh cocok?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_umroh"}
    },
    {
        "text": "Apa itu Tabungan Sikoci Qurban?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_qurban"}
    },
    {
        "text": "Bisa dijelaskan mengenai produk Sikoci Qurban?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_qurban"}
    },
    {
        "text": "Sikoci Qurban itu tabungan khusus untuk apa?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_qurban"}
    },
    {
        "text": "Apakah Sikoci Qurban termasuk tabungan syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_qurban"}
    },
    {
        "text": "Apakah dana di Sikoci Qurban bisa diambil kapan saja?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_qurban"}
    },
    {
        "text": "Kapan dana tabungan Sikoci Qurban boleh dicairkan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_qurban"}
    },
    {
        "text": "Apakah tabungan Sikoci Qurban hanya bisa dicairkan saat jelang Idul Adha?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_qurban"}
    },
    {
        "text": "Bagaimana jika ada kondisi darurat, apakah dana Sikoci Qurban bisa ditarik?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_qurban"}
    },
    {
        "text": "Apakah saya perlu surat keterangan resmi untuk mencairkan dana darurat dari Sikoci Qurban?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_qurban"}
    },
    {
        "text": "Berapa setoran awal untuk membuka tabungan Sikoci Qurban?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_qurban"}
    },
    {
        "text": "Setoran awal Sikoci Qurban minimal berapa rupiah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_qurban"}
    },
    {
        "text": "Berapa minimal setoran lanjutan untuk Sikoci Qurban?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_qurban"}
    },
    {
        "text": "Apakah Sikoci Qurban bebas biaya administrasi bulanan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_qurban"}
    },
    {
        "text": "Apa saja keunggulan Sikoci Qurban dibanding tabungan biasa?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_qurban"}
    },
    {
        "text": "Sikoci Qurban pakai akad apa, Mudharabah atau Wadiah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_qurban"}
    },
    {
        "text": "Apakah saya bisa memilih akad dalam tabungan Sikoci Qurban?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_qurban"}
    },
    {
        "text": "Apakah Sikoci Qurban hanya untuk nasabah perorangan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_qurban"}
    },
    {
        "text": "Saya mewakili organisasi masjid, apakah bisa buka tabungan Sikoci Qurban?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_qurban"}
    },
    {
        "text": "Apakah institusi atau komunitas juga bisa menabung lewat Sikoci Qurban?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_qurban"}
    },
    {
        "text": "Apakah Sikoci Qurban bisa dibuka oleh lembaga masyarakat?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_qurban"}
    },
    {
        "text": "Apakah Sikoci Qurban bisa digunakan untuk tabungan qurban keluarga?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_qurban"}
    },
    {
        "text": "Saya ingin mengelola dana qurban bersama teman-teman, cocok gak pakai Sikoci Qurban?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_qurban"}
    },
    {
        "text": "Apakah Sikoci Qurban cocok untuk program tabungan qurban bersama?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_qurban"}
    },
    {
        "text": "Apa kelebihan Sikoci Qurban dalam membantu akumulasi dana qurban?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_qurban"}
    },
    {
        "text": "Apakah Sikoci Qurban membantu perencanaan ibadah qurban secara bertahap?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_qurban"}
    },
    {
        "text": "Apakah Sikoci Qurban bisa digunakan sebagai rekening afiliasi pembiayaan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_qurban"}
    },
    {
        "text": "Apakah Sikoci Qurban bisa jadi rekening penerimaan dana pensiun?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_qurban"}
    },
    {
        "text": "Saya butuh tabungan syariah untuk ibadah qurban, apakah Sikoci Qurban tepat?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_qurban"}
    },
    {
        "text": "Apakah Sikoci Qurban bisa dibuka di seluruh cabang Bank Nagari?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_qurban"}
    },
    {
        "text": "Saya ingin tabungan qurban tanpa biaya admin, bisa jelaskan Sikoci Qurban?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_qurban"}
    },
    {
        "text": "Apa saja fitur unggulan dari produk Sikoci Qurban?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_qurban"}
    },
    {
        "text": "Apa itu KUR Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kur_syariah"}
    },
    {
        "text": "Bisa dijelaskan tentang produk KUR Syariah dari Bank Nagari?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kur_syariah"}
    },
    {
        "text": "KUR Syariah itu ditujukan untuk siapa saja?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kur_syariah"}
    },
    {
        "text": "Apa tujuan utama dari KUR Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kur_syariah"}
    },
    {
        "text": "Apakah KUR Syariah menggunakan sistem bunga?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kur_syariah"}
    },
    {
        "text": "Apakah KUR Syariah bebas dari riba?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kur_syariah"}
    },
    {
        "text": "Apakah KUR Syariah berdasarkan prinsip syariah Islam?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kur_syariah"}
    },
    {
        "text": "Apa saja sektor usaha yang didukung oleh KUR Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kur_syariah"}
    },
    {
        "text": "Apakah KUR Syariah bisa digunakan untuk semua sektor ekonomi?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kur_syariah"}
    },
    {
        "text": "KUR Syariah bisa untuk usaha kuliner atau warung kecil?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kur_syariah"}
    },
    {
        "text": "Apa itu KUR Syariah Super Mikro?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kur_syariah"}
    },
    {
        "text": "Berapa plafon maksimal KUR Syariah Super Mikro?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kur_syariah"}
    },
    {
        "text": "Apa perbedaan KUR Syariah Mikro dan Super Mikro?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kur_syariah"}
    },
    {
        "text": "KUR Syariah Mikro bisa sampai berapa juta?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kur_syariah"}
    },
    {
        "text": "Saya butuh modal usaha 100 juta, apakah bisa lewat KUR Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kur_syariah"}
    },
    {
        "text": "Berapa batas plafon maksimal untuk KUR Syariah Kecil?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kur_syariah"}
    },
    {
        "text": "Apa saja persyaratan untuk mengajukan KUR Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kur_syariah"}
    },
    {
        "text": "Apakah perlu mengisi aplikasi pembiayaan untuk KUR Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kur_syariah"}
    },
    {
        "text": "Apakah fotokopi KTP dan KK wajib untuk KUR Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kur_syariah"}
    },
    {
        "text": "Saya sudah menikah, apakah perlu fotokopi buku nikah untuk ajukan KUR Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kur_syariah"}
    },
    {
        "text": "Apakah perlu pas foto suami istri untuk ajukan KUR Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kur_syariah"}
    },
    {
        "text": "Apa pentingnya foto usaha dalam pengajuan KUR Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kur_syariah"}
    },
    {
        "text": "Apakah Surat Keterangan Usaha wajib untuk mengajukan KUR Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kur_syariah"}
    },
    {
        "text": "Berapa lama minimal usaha saya harus berjalan untuk bisa ajukan KUR Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kur_syariah"}
    },
    {
        "text": "Apakah harus menyertakan agunan untuk pengajuan KUR Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kur_syariah"}
    },
    {
        "text": "Saya dengar harus lampirkan buku tabungan Bank Nagari untuk KUR Syariah, benar?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kur_syariah"}
    },
    {
        "text": "Apakah pengajuan KUR Syariah harus lolos verifikasi SIKP?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kur_syariah"}
    },
    {
        "text": "Apakah ada biaya administrasi dalam pengajuan KUR Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kur_syariah"}
    },
    {
        "text": "Apakah KUR Syariah bisa diajukan oleh badan usaha kecil?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kur_syariah"}
    },
    {
        "text": "Saya butuh pinjaman untuk kembangkan usaha syariah, bisa lewat KUR Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kur_syariah"}
    },
    {
        "text": "Apakah KUR Syariah tersedia di seluruh cabang Bank Nagari?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kur_syariah"}
    },
    {
        "text": "Apa itu Tabungan Sikoci Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_syariah"}
    },
    {
        "text": "Bisa jelaskan produk Sikoci Syariah secara singkat?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_syariah"}
    },
    {
        "text": "Sikoci Syariah itu termasuk tabungan apa?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_syariah"}
    },
    {
        "text": "Apakah Sikoci Syariah mengikuti prinsip syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_syariah"}
    },
    {
        "text": "Akad apa yang digunakan dalam Sikoci Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_syariah"}
    },
    {
        "text": "Apakah saya bisa pilih antara Wadiah dan Mudharabah saat buka Sikoci Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_syariah"}
    },
    {
        "text": "Apakah dana di Sikoci Syariah bisa ditarik kapan saja?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_syariah"}
    },
    {
        "text": "Apakah penarikan dana dari Sikoci Syariah fleksibel?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_syariah"}
    },
    {
        "text": "Sikoci Syariah bisa digunakan oleh siapa saja?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_syariah"}
    },
    {
        "text": "Apakah organisasi masyarakat bisa membuka tabungan Sikoci Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_syariah"}
    },
    {
        "text": "Apakah institusi boleh menggunakan produk Sikoci Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_syariah"}
    },
    {
        "text": "Berapa setoran awal minimal untuk membuka Sikoci Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_syariah"}
    },
    {
        "text": "Saldo minimal yang harus dijaga di Sikoci Syariah berapa ya?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_syariah"}
    },
    {
        "text": "Apa saja syarat untuk membuka rekening Sikoci Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_syariah"}
    },
    {
        "text": "Apakah saya harus mengisi formulir pembukaan dan FDN untuk buka Sikoci Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_syariah"}
    },
    {
        "text": "Untuk perseorangan, apa saja dokumen yang dibutuhkan untuk buka Sikoci Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_syariah"}
    },
    {
        "text": "Kalau perusahaan mau buka Sikoci Syariah, apa saja dokumen yang diperlukan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_syariah"}
    },
    {
        "text": "Apakah harus menyertakan SIUP dan NPWP untuk buka Sikoci Syariah atas nama perusahaan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_syariah"}
    },
    {
        "text": "Berapa biaya administrasi bulanan untuk Sikoci Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_syariah"}
    },
    {
        "text": "Biaya ATM bulanan Sikoci Syariah berapa ya?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_syariah"}
    },
    {
        "text": "Apakah biaya admin Sikoci Syariah diambil dari hasil bagi hasil?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_syariah"}
    },
    {
        "text": "Apakah Sikoci Syariah mendukung layanan Nagari Mobile Banking?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_syariah"}
    },
    {
        "text": "Apakah saya bisa cek saldo Sikoci Syariah lewat SMS Banking?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_syariah"}
    },
    {
        "text": "Sikoci Syariah terhubung dengan jaringan ATM apa saja?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_syariah"}
    },
    {
        "text": "Apakah Sikoci Syariah bisa digunakan lewat ATM Bersama dan ATM Prima?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_syariah"}
    },
    {
        "text": "Apa keuntungan utama dari Sikoci Syariah dibanding tabungan konvensional?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_syariah"}
    },
    {
        "text": "Saya cari tabungan syariah fleksibel, cocokkah jika pilih Sikoci Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_syariah"}
    },
    {
        "text": "Apakah Sikoci Syariah punya fitur cash management (NCM)?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_syariah"}
    },
    {
        "text": "Apakah ada notifikasi transaksi untuk tabungan Sikoci Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_syariah"}
    },
    {
        "text": "Apa saja fasilitas digital yang tersedia untuk Sikoci Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "sikoci_syariah"}
    },
    {
        "text": "Apa itu pembiayaan MMQ Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "mmq_syariah"}
    },
    {
        "text": "Bisa dijelaskan konsep Musyarakah Mutanaqisah yang digunakan di MMQ Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "mmq_syariah"}
    },
    {
        "text": "Bagaimana cara kerja sistem bagi hasil di pembiayaan MMQ Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "mmq_syariah"}
    },
    {
        "text": "Apakah kepemilikan aset dalam MMQ Syariah bisa berpindah ke nasabah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "mmq_syariah"}
    },
    {
        "text": "Apa saja manfaat dari pembiayaan MMQ Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "mmq_syariah"}
    },
    {
        "text": "Apakah MMQ Syariah cocok untuk pembelian rumah atau ruko?",
        "intent": "product_inquiry",
        "entities": {"product_name": "mmq_syariah"}
    },
    {
        "text": "Bisa nggak pakai MMQ Syariah untuk beli kendaraan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "mmq_syariah"}
    },
    {
        "text": "MMQ Syariah bisa digunakan untuk pembelian aset produktif ya?",
        "intent": "product_inquiry",
        "entities": {"product_name": "mmq_syariah"}
    },
    {
        "text": "Saya ingin investasi pabrik, apakah bisa pakai MMQ Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "mmq_syariah"}
    },
    {
        "text": "Apakah pembiayaan MMQ Syariah juga tersedia untuk kebutuhan konsumtif?",
        "intent": "product_inquiry",
        "entities": {"product_name": "mmq_syariah"}
    },
    {
        "text": "Saya ingin take over dari bank lain, bisa menggunakan MMQ Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "mmq_syariah"}
    },
    {
        "text": "Apakah MMQ Syariah tersedia untuk pengalihan hutang dari bank konvensional?",
        "intent": "product_inquiry",
        "entities": {"product_name": "mmq_syariah"}
    },
    {
        "text": "Siapa saja yang bisa mengajukan pembiayaan MMQ Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "mmq_syariah"}
    },
    {
        "text": "Apakah badan usaha bisa ikut MMQ Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "mmq_syariah"}
    },
    {
        "text": "MMQ Syariah bisa untuk koperasi dan pemerintah daerah juga?",
        "intent": "product_inquiry",
        "entities": {"product_name": "mmq_syariah"}
    },
    {
        "text": "Apa saja dokumen yang harus disiapkan untuk mengajukan MMQ Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "mmq_syariah"}
    },
    {
        "text": "Apakah saya perlu menyertakan laporan keuangan untuk MMQ Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "mmq_syariah"}
    },
    {
        "text": "Apakah harus menyertakan NPWP saat mengajukan MMQ Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "mmq_syariah"}
    },
    {
        "text": "Apakah agunan diperlukan untuk pembiayaan MMQ Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "mmq_syariah"}
    },
    {
        "text": "Berapa jumlah pas foto yang harus disertakan saat mengajukan MMQ Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "mmq_syariah"}
    },
    {
        "text": "Apakah saya bisa mengajukan MMQ Syariah dengan identitas SIM atau Paspor?",
        "intent": "product_inquiry",
        "entities": {"product_name": "mmq_syariah"}
    },
    {
        "text": "Apakah MMQ Syariah bisa digunakan untuk refinancing aset usaha?",
        "intent": "product_inquiry",
        "entities": {"product_name": "mmq_syariah"}
    },
    {
        "text": "Apakah pembiayaan MMQ Syariah cocok untuk pengembangan usaha kecil?",
        "intent": "product_inquiry",
        "entities": {"product_name": "mmq_syariah"}
    },
    {
        "text": "Apakah bisa pakai MMQ Syariah untuk beli properti pribadi?",
        "intent": "product_inquiry",
        "entities": {"product_name": "mmq_syariah"}
    },
    {
        "text": "Saya ingin beli rumah secara syariah, apakah MMQ Syariah solusinya?",
        "intent": "product_inquiry",
        "entities": {"product_name": "mmq_syariah"}
    },
    {
        "text": "Kalau saya profesional, bisa nggak ikut pembiayaan MMQ Syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "mmq_syariah"}
    },
    {
        "text": "Apa keunggulan MMQ Syariah dibandingkan kredit biasa?",
        "intent": "product_inquiry",
        "entities": {"product_name": "mmq_syariah"}
    },
    {
        "text": "Apakah MMQ Syariah memberikan porsi kepemilikan bertahap pada nasabah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "mmq_syariah"}
    },
    {
        "text": "Apakah bisa menggunakan MMQ Syariah untuk ruko dan rukan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "mmq_syariah"}
    },
    {
        "text": "MMQ Syariah itu pembiayaan dengan akad kepemilikan bertahap ya?",
        "intent": "product_inquiry",
        "entities": {"product_name": "mmq_syariah"}
    },
    {
        "text": "Apa itu pembiayaan Murabahah Modal Kerja?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_modal_kerja"}
    },
    {
        "text": "Bisa dijelaskan produk Murabahah Modal Kerja dari Bank Nagari?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_modal_kerja"}
    },
    {
        "text": "Murabahah Modal Kerja itu termasuk pembiayaan jenis apa?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_modal_kerja"}
    },
    {
        "text": "Apakah Murabahah Modal Kerja menggunakan prinsip syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_modal_kerja"}
    },
    {
        "text": "Apakah akad yang digunakan dalam pembiayaan ini adalah Murabahah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_modal_kerja"}
    },
    {
        "text": "Siapa saja yang bisa mengajukan Murabahah Modal Kerja?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_modal_kerja"}
    },
    {
        "text": "Apakah badan usaha boleh mengajukan Murabahah Modal Kerja?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_modal_kerja"}
    },
    {
        "text": "Apakah pembiayaan ini bisa untuk usaha informal tanpa izin usaha?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_modal_kerja"}
    },
    {
        "text": "Berapa maksimal plafon untuk usaha informal pada Murabahah Modal Kerja?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_modal_kerja"}
    },
    {
        "text": "Berapa lama jangka waktu pembiayaan Murabahah Modal Kerja bisa diberikan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_modal_kerja"}
    },
    {
        "text": "Apakah tenor Murabahah Modal Kerja bisa sampai 60 bulan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_modal_kerja"}
    },
    {
        "text": "Apa saja manfaat dari pembiayaan Murabahah Modal Kerja ini?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_modal_kerja"}
    },
    {
        "text": "Apakah produk ini cocok untuk ekspansi usaha?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_modal_kerja"}
    },
    {
        "text": "Bisakah pembiayaan Murabahah Modal Kerja digunakan untuk operasional harian?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_modal_kerja"}
    },
    {
        "text": "Apakah plafon pembiayaan disesuaikan dengan kebutuhan usaha?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_modal_kerja"}
    },
    {
        "text": "Dokumen apa saja yang perlu disiapkan untuk ajukan Murabahah Modal Kerja?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_modal_kerja"}
    },
    {
        "text": "Apakah saya perlu fotokopi KTP dan KK untuk mengajukan Murabahah Modal Kerja?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_modal_kerja"}
    },
    {
        "text": "Apakah pas foto dibutuhkan saat mengajukan Murabahah Modal Kerja?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_modal_kerja"}
    },
    {
        "text": "Apakah NPWP wajib disertakan dalam pengajuan Murabahah Modal Kerja?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_modal_kerja"}
    },
    {
        "text": "Apakah laporan keuangan usaha harus dilampirkan untuk Murabahah Modal Kerja?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_modal_kerja"}
    },
    {
        "text": "Untuk badan usaha, apakah harus menyertakan anggaran dasar saat pengajuan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_modal_kerja"}
    },
    {
        "text": "Apa tujuan utama dari pembiayaan Murabahah Modal Kerja?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_modal_kerja"}
    },
    {
        "text": "Apakah Murabahah Modal Kerja bisa digunakan oleh pelaku UMKM?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_modal_kerja"}
    },
    {
        "text": "Saya punya usaha kecil tanpa izin, apakah bisa ajukan Murabahah Modal Kerja?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_modal_kerja"}
    },
    {
        "text": "Apa keunggulan Murabahah Modal Kerja dibanding pembiayaan konvensional?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_modal_kerja"}
    },
    {
        "text": "Apakah pembiayaan ini berdasarkan prinsip jual beli dalam Islam?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_modal_kerja"}
    },
    {
        "text": "Apakah Murabahah Modal Kerja tersedia di semua kantor Bank Nagari?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_modal_kerja"}
    },
    {
        "text": "Berapa pas foto yang dibutuhkan untuk pembiayaan Murabahah Modal Kerja?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_modal_kerja"}
    },
    {
        "text": "Kalau saya belum punya izin usaha, apakah tetap bisa ajukan Murabahah Modal Kerja?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_modal_kerja"}
    },
    {
        "text": "Saya sedang butuh tambahan modal, apakah bisa ajukan Murabahah Modal Kerja?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_modal_kerja"}
    },
    {
        "text": "Apa itu pembiayaan Murabahah Investasi?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_investasi"}
    },
    {
        "text": "Bisa dijelaskan produk Murabahah Investasi dari Bank Nagari?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_investasi"}
    },
    {
        "text": "Apakah Murabahah Investasi menggunakan prinsip syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_investasi"}
    },
    {
        "text": "Akad apa yang digunakan dalam Murabahah Investasi?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_investasi"}
    },
    {
        "text": "Murabahah Investasi cocok untuk kebutuhan seperti apa?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_investasi"}
    },
    {
        "text": "Apakah produk ini bisa digunakan untuk pembiayaan jangka panjang?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_investasi"}
    },
    {
        "text": "Berapa jangka waktu pembiayaan pada Murabahah Investasi?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_investasi"}
    },
    {
        "text": "Apakah tenor Murabahah Investasi bisa sampai 10 tahun?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_investasi"}
    },
    {
        "text": "Siapa saja yang bisa mengajukan Murabahah Investasi?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_investasi"}
    },
    {
        "text": "Apakah instansi pemerintah juga bisa mendapatkan Murabahah Investasi?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_investasi"}
    },
    {
        "text": "Apakah usaha informal bisa menggunakan pembiayaan Murabahah Investasi?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_investasi"}
    },
    {
        "text": "Berapa plafon maksimal untuk usaha informal dalam Murabahah Investasi?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_investasi"}
    },
    {
        "text": "Apakah plafon Murabahah Investasi bisa menyesuaikan kebutuhan investasi usaha?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_investasi"}
    },
    {
        "text": "Apa saja keunggulan dari Murabahah Investasi?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_investasi"}
    },
    {
        "text": "Apa bedanya Murabahah Investasi dengan Murabahah Modal Kerja?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_investasi"}
    },
    {
        "text": "Apa manfaat Murabahah Investasi bagi pelaku UMKM?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_investasi"}
    },
    {
        "text": "Apakah pembiayaan ini bisa digunakan untuk ekspansi bisnis jangka panjang?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_investasi"}
    },
    {
        "text": "Apa saja syarat untuk mengajukan Murabahah Investasi?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_investasi"}
    },
    {
        "text": "Apakah saya perlu isi formulir permohonan untuk ajukan Murabahah Investasi?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_investasi"}
    },
    {
        "text": "Dokumen identitas apa yang dibutuhkan untuk Murabahah Investasi?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_investasi"}
    },
    {
        "text": "Apakah KTP atau Paspor bisa digunakan untuk pengajuan Murabahah Investasi?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_investasi"}
    },
    {
        "text": "Perlu pas foto juga gak untuk pengajuan Murabahah Investasi?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_investasi"}
    },
    {
        "text": "Apakah NPWP wajib untuk ajukan Murabahah Investasi?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_investasi"}
    },
    {
        "text": "Saya punya badan usaha, apa saya perlu melampirkan anggaran dasar juga?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_investasi"}
    },
    {
        "text": "Apakah laporan keuangan wajib disiapkan untuk Murabahah Investasi?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_investasi"}
    },
    {
        "text": "Apakah pembiayaan ini tersedia untuk sektor formal dan informal?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_investasi"}
    },
    {
        "text": "Kalau usaha saya belum punya izin, plafon maksimalnya berapa di Murabahah Investasi?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_investasi"}
    },
    {
        "text": "Saya ingin membiayai proyek usaha, apakah bisa gunakan Murabahah Investasi?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_investasi"}
    },
    {
        "text": "Apakah saya bisa gunakan Murabahah Investasi untuk beli mesin pabrik?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_investasi"}
    },
    {
        "text": "Apakah Murabahah Investasi cocok untuk usaha jangka menengah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_investasi"}
    },
    {
        "text": "Kalau saya dari instansi pemerintah, bisa gak ajukan Murabahah Investasi?",
        "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_investasi"}
    },
    {
        "text": "Apa itu pembiayaan Modal Kerja Kontraktor?",
        "intent": "product_inquiry",
        "entities": {"product_name": "modal_kerja_kontraktor"}
    },
    {
        "text": "Saya ingin tahu tentang produk Modal Kerja Kontraktor dari Bank Nagari.",
        "intent": "product_inquiry",
        "entities": {"product_name": "modal_kerja_kontraktor"}
    },
    {
        "text": "Apakah Modal Kerja Kontraktor menggunakan prinsip syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "modal_kerja_kontraktor"}
    },
    {
        "text": "Jenis akad apa yang digunakan untuk Modal Kerja Kontraktor?",
        "intent": "product_inquiry",
        "entities": {"product_name": "modal_kerja_kontraktor"}
    },
    {
        "text": "Apa saja proyek yang bisa didanai oleh pembiayaan Modal Kerja Kontraktor?",
        "intent": "product_inquiry",
        "entities": {"product_name": "modal_kerja_kontraktor"}
    },
    {
        "text": "Apakah pembiayaan ini bisa digunakan untuk pengadaan barang?",
        "intent": "product_inquiry",
        "entities": {"product_name": "modal_kerja_kontraktor"}
    },
    {
        "text": "Bisa digunakan untuk proyek konstruksi jalan juga?",
        "intent": "product_inquiry",
        "entities": {"product_name": "modal_kerja_kontraktor"}
    },
    {
        "text": "Modal Kerja Kontraktor diperuntukkan untuk siapa?",
        "intent": "product_inquiry",
        "entities": {"product_name": "modal_kerja_kontraktor"}
    },
    {
        "text": "Apa saja syarat untuk mengajukan Modal Kerja Kontraktor?",
        "intent": "product_inquiry",
        "entities": {"product_name": "modal_kerja_kontraktor"}
    },
    {
        "text": "Apakah saya perlu menyertakan kontrak proyek atau SPK saat mengajukan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "modal_kerja_kontraktor"}
    },
    {
        "text": "Butuh persetujuan dari Bouwheer juga ya?",
        "intent": "product_inquiry",
        "entities": {"product_name": "modal_kerja_kontraktor"}
    },
    {
        "text": "Apa dokumen legalitas yang dibutuhkan untuk pembiayaan kontraktor ini?",
        "intent": "product_inquiry",
        "entities": {"product_name": "modal_kerja_kontraktor"}
    },
    {
        "text": "Apakah harus melampirkan laporan keuangan perusahaan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "modal_kerja_kontraktor"}
    },
    {
        "text": "Berapa plafon pembiayaan yang bisa diberikan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "modal_kerja_kontraktor"}
    },
    {
        "text": "Apakah saya bisa mengajukan tanpa agunan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "modal_kerja_kontraktor"}
    },
    {
        "text": "Kalau tanpa agunan, maksimal plafon berapa ya?",
        "intent": "product_inquiry",
        "entities": {"product_name": "modal_kerja_kontraktor"}
    },
    {
        "text": "Apa syarat dana sendiri untuk pengajuan Modal Kerja Kontraktor?",
        "intent": "product_inquiry",
        "entities": {"product_name": "modal_kerja_kontraktor"}
    },
    {
        "text": "Berapa persen dana pribadi yang dibutuhkan kalau pakai agunan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "modal_kerja_kontraktor"}
    },
    {
        "text": "Kalau tanpa agunan, saya harus siapkan dana pribadi berapa persen?",
        "intent": "product_inquiry",
        "entities": {"product_name": "modal_kerja_kontraktor"}
    },
    {
        "text": "Apakah plafon disesuaikan dengan nilai kontrak proyek?",
        "intent": "product_inquiry",
        "entities": {"product_name": "modal_kerja_kontraktor"}
    },
    {
        "text": "Apa saja komponen yang dikurangi dari nilai kontrak untuk menentukan plafon?",
        "intent": "product_inquiry",
        "entities": {"product_name": "modal_kerja_kontraktor"}
    },
    {
        "text": "Berapa lama jangka waktu pembiayaan Modal Kerja Kontraktor?",
        "intent": "product_inquiry",
        "entities": {"product_name": "modal_kerja_kontraktor"}
    },
    {
        "text": "Jangka waktunya disesuaikan dengan kontrak proyek ya?",
        "intent": "product_inquiry",
        "entities": {"product_name": "modal_kerja_kontraktor"}
    },
    {
        "text": "Apakah produk ini cocok untuk proyek konstruksi skala kecil?",
        "intent": "product_inquiry",
        "entities": {"product_name": "modal_kerja_kontraktor"}
    },
    {
        "text": "Bisa dipakai untuk pengadaan barang oleh instansi pemerintah juga?",
        "intent": "product_inquiry",
        "entities": {"product_name": "modal_kerja_kontraktor"}
    },
    {
        "text": "Apakah rekening giro perusahaan juga harus dilampirkan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "modal_kerja_kontraktor"}
    },
    {
        "text": "Modal Kerja Kontraktor termasuk dalam pembiayaan syariah apa?",
        "intent": "product_inquiry",
        "entities": {"product_name": "modal_kerja_kontraktor"}
    },
    {
        "text": "Kalau saya kontraktor pengadaan alat berat, apakah bisa pakai produk ini?",
        "intent": "product_inquiry",
        "entities": {"product_name": "modal_kerja_kontraktor"}
    },
    {
        "text": "Bisa digunakan untuk proyek pembangunan gedung perkantoran?",
        "intent": "product_inquiry",
        "entities": {"product_name": "modal_kerja_kontraktor"}
    },
    {
        "text": "Saya kontraktor jalan tol, bisa pakai Modal Kerja Kontraktor Bank Nagari?",
        "intent": "product_inquiry",
        "entities": {"product_name": "modal_kerja_kontraktor"}
    },
    {
        "text": "Apa itu produk Giro iB di Bank Nagari?",
        "intent": "product_inquiry",
        "entities": {"product_name": "giro_ib"}
    },
    {
        "text": "Bisa jelaskan tentang rekening Giro iB?",
        "intent": "product_inquiry",
        "entities": {"product_name": "giro_ib"}
    },
    {
        "text": "Apakah Giro iB menggunakan prinsip syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "giro_ib"}
    },
    {
        "text": "Akad apa yang digunakan dalam Giro iB?",
        "intent": "product_inquiry",
        "entities": {"product_name": "giro_ib"}
    },
    {
        "text": "Bisa pilih akad Wadiah atau Mudharabah untuk Giro iB?",
        "intent": "product_inquiry",
        "entities": {"product_name": "giro_ib"}
    },
    {
        "text": "Apa keunggulan Giro iB dibandingkan tabungan biasa?",
        "intent": "product_inquiry",
        "entities": {"product_name": "giro_ib"}
    },
    {
        "text": "Apa manfaat dari membuka rekening Giro iB?",
        "intent": "product_inquiry",
        "entities": {"product_name": "giro_ib"}
    },
    {
        "text": "Bagaimana cara penarikan dana di Giro iB?",
        "intent": "product_inquiry",
        "entities": {"product_name": "giro_ib"}
    },
    {
        "text": "Bisa tarik dana Giro iB lewat cek atau bilyet giro?",
        "intent": "product_inquiry",
        "entities": {"product_name": "giro_ib"}
    },
    {
        "text": "Apakah Giro iB bisa dipakai untuk transfer antar rekening?",
        "intent": "product_inquiry",
        "entities": {"product_name": "giro_ib"}
    },
    {
        "text": "Apakah Giro iB bisa untuk perusahaan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "giro_ib"}
    },
    {
        "text": "Apakah nasabah perorangan juga bisa buka rekening Giro iB?",
        "intent": "product_inquiry",
        "entities": {"product_name": "giro_ib"}
    },
    {
        "text": "Apa saja syarat membuka Giro iB?",
        "intent": "product_inquiry",
        "entities": {"product_name": "giro_ib"}
    },
    {
        "text": "Apakah wajib menyerahkan NPWP untuk Giro iB?",
        "intent": "product_inquiry",
        "entities": {"product_name": "giro_ib"}
    },
    {
        "text": "Giro iB wajib punya setoran awal berapa ya?",
        "intent": "product_inquiry",
        "entities": {"product_name": "giro_ib"}
    },
    {
        "text": "Berapa minimal saldo yang harus dijaga di Giro iB?",
        "intent": "product_inquiry",
        "entities": {"product_name": "giro_ib"}
    },
    {
        "text": "Giro iB cocok digunakan untuk apa saja?",
        "intent": "product_inquiry",
        "entities": {"product_name": "giro_ib"}
    },
    {
        "text": "Apakah bisa menggunakan Giro iB untuk transaksi rutin perusahaan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "giro_ib"}
    },
    {
        "text": "Apa yang dimaksud dengan instrumen pembayaran di Giro iB?",
        "intent": "product_inquiry",
        "entities": {"product_name": "giro_ib"}
    },
    {
        "text": "Apakah pemindahbukuan bisa dilakukan dari rekening Giro iB?",
        "intent": "product_inquiry",
        "entities": {"product_name": "giro_ib"}
    },
    {
        "text": "Saya tidak punya NPWP, apakah tetap bisa buka Giro iB?",
        "intent": "product_inquiry",
        "entities": {"product_name": "giro_ib"}
    },
    {
        "text": "Apa kegunaan bilyet giro dalam produk Giro iB?",
        "intent": "product_inquiry",
        "entities": {"product_name": "giro_ib"}
    },
    {
        "text": "Apakah rekening Giro iB bisa digunakan untuk transaksi besar?",
        "intent": "product_inquiry",
        "entities": {"product_name": "giro_ib"}
    },
    {
        "text": "Apa dokumen identitas yang perlu dilampirkan untuk Giro iB?",
        "intent": "product_inquiry",
        "entities": {"product_name": "giro_ib"}
    },
    {
        "text": "Jika saya terdaftar di Daftar Hitam BI, apakah bisa buka Giro iB?",
        "intent": "product_inquiry",
        "entities": {"product_name": "giro_ib"}
    },
    {
        "text": "Giro iB tersedia di seluruh cabang Bank Nagari?",
        "intent": "product_inquiry",
        "entities": {"product_name": "giro_ib"}
    },
    {
        "text": "Apakah Giro iB memberikan bagi hasil?",
        "intent": "product_inquiry",
        "entities": {"product_name": "giro_ib"}
    },
    {
        "text": "Jika memilih akad Wadiah, apakah tetap dapat manfaat dari Giro iB?",
        "intent": "product_inquiry",
        "entities": {"product_name": "giro_ib"}
    },
    {
        "text": "Untuk membuka Giro iB, apa saja langkah awalnya?",
        "intent": "product_inquiry",
        "entities": {"product_name": "giro_ib"}
    },
    {
        "text": "Cek dan bilyet giro Giro iB bisa digunakan di mana saja?",
        "intent": "product_inquiry",
        "entities": {"product_name": "giro_ib"}
    },
    {
        "text": "Berapa nominal minimal untuk membuka Giro iB?",
        "intent": "product_inquiry",
        "entities": {"product_name": "giro_ib"}
    },
    {
        "text": "Apa itu layanan Gadai Emas iB di Bank Nagari?",
        "intent": "product_inquiry",
        "entities": {"product_name": "gadai_emas_ib"}
    },
    {
        "text": "Gadai Emas iB itu seperti apa sistem kerjanya?",
        "intent": "product_inquiry",
        "entities": {"product_name": "gadai_emas_ib"}
    },
    {
        "text": "Gadai Emas iB bisa digunakan untuk keperluan apa saja?",
        "intent": "product_inquiry",
        "entities": {"product_name": "gadai_emas_ib"}
    },
    {
        "text": "Apa keuntungan utama dari layanan Gadai Emas iB?",
        "intent": "product_inquiry",
        "entities": {"product_name": "gadai_emas_ib"}
    },
    {
        "text": "Apakah Gadai Emas iB menggunakan prinsip syariah?",
        "intent": "product_inquiry",
        "entities": {"product_name": "gadai_emas_ib"}
    },
    {
        "text": "Akad apa saja yang digunakan dalam Gadai Emas iB?",
        "intent": "product_inquiry",
        "entities": {"product_name": "gadai_emas_ib"}
    },
    {
        "text": "Apakah Gadai Emas iB menggunakan akad Rahn?",
        "intent": "product_inquiry",
        "entities": {"product_name": "gadai_emas_ib"}
    },
    {
        "text": "Apa itu akad Ijarah dalam konteks Gadai Emas iB?",
        "intent": "product_inquiry",
        "entities": {"product_name": "gadai_emas_ib"}
    },
    {
        "text": "Apa fungsi akad Qardh pada Gadai Emas iB?",
        "intent": "product_inquiry",
        "entities": {"product_name": "gadai_emas_ib"}
    },
    {
        "text": "Apakah layanan Gadai Emas iB cocok untuk kebutuhan usaha?",
        "intent": "product_inquiry",
        "entities": {"product_name": "gadai_emas_ib"}
    },
    {
        "text": "Bagaimana proses pengajuan Gadai Emas iB di Bank Nagari?",
        "intent": "product_inquiry",
        "entities": {"product_name": "gadai_emas_ib"}
    },
    {
        "text": "Apa saja dokumen yang diperlukan untuk Gadai Emas iB?",
        "intent": "product_inquiry",
        "entities": {"product_name": "gadai_emas_ib"}
    },
    {
        "text": "Apakah perlu NPWP untuk mengajukan Gadai Emas iB?",
        "intent": "product_inquiry",
        "entities": {"product_name": "gadai_emas_ib"}
    },
    {
        "text": "Apakah harus buka tabungan dulu sebelum Gadai Emas iB?",
        "intent": "product_inquiry",
        "entities": {"product_name": "gadai_emas_ib"}
    },
    {
        "text": "Jenis emas seperti apa yang bisa dijadikan jaminan Gadai Emas iB?",
        "intent": "product_inquiry",
        "entities": {"product_name": "gadai_emas_ib"}
    },
    {
        "text": "Bisa pakai emas batangan untuk Gadai Emas iB?",
        "intent": "product_inquiry",
        "entities": {"product_name": "gadai_emas_ib"}
    },
    {
        "text": "Berapa maksimal pembiayaan dari Gadai Emas iB?",
        "intent": "product_inquiry",
        "entities": {"product_name": "gadai_emas_ib"}
    },
    {
        "text": "Gadai Emas iB bisa mendapatkan pembiayaan sampai berapa persen dari nilai emas?",
        "intent": "product_inquiry",
        "entities": {"product_name": "gadai_emas_ib"}
    },
    {
        "text": "Apa biaya administrasi dari layanan Gadai Emas iB?",
        "intent": "product_inquiry",
        "entities": {"product_name": "gadai_emas_ib"}
    },
    {
        "text": "Berapa biaya pemeliharaan bulanan di Gadai Emas iB?",
        "intent": "product_inquiry",
        "entities": {"product_name": "gadai_emas_ib"}
    },
    {
        "text": "Berapa lama jangka waktu pembiayaan Gadai Emas iB?",
        "intent": "product_inquiry",
        "entities": {"product_name": "gadai_emas_ib"}
    },
    {
        "text": "Apakah pembiayaan Gadai Emas iB bisa diperpanjang?",
        "intent": "product_inquiry",
        "entities": {"product_name": "gadai_emas_ib"}
    },
    {
        "text": "Bisa digadai ulang jika belum bisa menebus emas pada Gadai Emas iB?",
        "intent": "product_inquiry",
        "entities": {"product_name": "gadai_emas_ib"}
    },
    {
        "text": "Apakah layanan Gadai Emas iB bisa diajukan oleh siapa saja?",
        "intent": "product_inquiry",
        "entities": {"product_name": "gadai_emas_ib"}
    },
    {
        "text": "Saya punya emas, bagaimana cara mendapat dana cepat lewat Gadai Emas iB?",
        "intent": "product_inquiry",
        "entities": {"product_name": "gadai_emas_ib"}
    },
    {
        "text": "Apakah bisa pakai Gadai Emas iB untuk biaya sekolah anak?",
        "intent": "product_inquiry",
        "entities": {"product_name": "gadai_emas_ib"}
    },
    {
        "text": "Apa saja bukti pendukung yang dibutuhkan untuk Gadai Emas iB?",
        "intent": "product_inquiry",
        "entities": {"product_name": "gadai_emas_ib"}
    },
    {
        "text": "Gadai Emas iB bisa digunakan untuk modal usaha kecil?",
        "intent": "product_inquiry",
        "entities": {"product_name": "gadai_emas_ib"}
    },
    {
        "text": "Berapa biaya total jika saya menggadaikan 10 gram emas lewat Gadai Emas iB?",
        "intent": "product_inquiry",
        "entities": {"product_name": "gadai_emas_ib"}
    },
    {
        "text": "Apakah Gadai Emas iB hanya untuk emas atau bisa barang lain?",
        "intent": "product_inquiry",
        "entities": {"product_name": "gadai_emas_ib"}
    },

    # Produk KPR FLPP Syariah
    {"text": "Apa itu KPR FLPP Syariah?", "intent": "product_inquiry",
        "entities": {"product_name": "kpr_flpp_syariah"}},
    {"text": "Apa yang dimaksud dengan KPR FLPP Syariah?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp_syariah"}},
    {"text": "KPR FLPP Syariah itu apa sih?", "intent": "product_inquiry",
        "entities": {"product_name": "kpr_flpp_syariah"}},
    {"text": "Bisa jelaskan lebih lanjut tentang KPR FLPP Syariah?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp_syariah"}},
    {"text": "Apa tujuan utama dari KPR FLPP Syariah?", "intent": "product_inquiry",
        "entities": {"product_name": "kpr_flpp_syariah"}},
    {"text": "Apa saja manfaat yang diberikan oleh KPR FLPP Syariah?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp_syariah"}},
    {"text": "Bagaimana cara kerja KPR FLPP Syariah?", "intent": "product_inquiry",
        "entities": {"product_name": "kpr_flpp_syariah"}},
    {"text": "KPR FLPP Syariah, siapa saja yang dapat mengaksesnya?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp_syariah"}},
    {"text": "Apa saja keuntungan memiliki KPR FLPP Syariah?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp_syariah"}},

    {"text": "Apa keuntungan dari KPR FLPP Syariah?", "intent": "product_inquiry",
        "entities": {"product_name": "kpr_flpp_syariah"}},
    {"text": "Apa saja keuntungan dari KPR FLPP Syariah?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp_syariah"}},
    {"text": "Keuntungan apa saja yang ditawarkan oleh KPR FLPP Syariah?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp_syariah"}},
    {"text": "Apa manfaat utama dari KPR FLPP Syariah?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp_syariah"}},
    {"text": "KPR FLPP Syariah, apa keuntungan bagi pembeli rumah?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp_syariah"}},
    {"text": "Apa yang membedakan keuntungan KPR FLPP Syariah dengan KPR biasa?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp_syariah"}},
    {"text": "Keuntungan jangka panjang apa yang bisa didapat dari KPR FLPP Syariah?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp_syariah"}},
    {"text": "Apa saja benefit yang didapatkan dengan memilih KPR FLPP Syariah?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp_syariah"}},

    {"text": "Apa syarat KPR FLPP Syariah?", "intent": "product_inquiry",
        "entities": {"product_name": "kpr_flpp_syariah"}},
    {"text": "Apa syarat untuk mendapatkan KPR FLPP Syariah?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp_syariah"}},
    {"text": "Syarat apa yang harus dipenuhi untuk mendapatkan KPR FLPP Syariah?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp_syariah"}},
    {"text": "Apa saja persyaratan yang perlu dipenuhi untuk mengajukan KPR FLPP Syariah?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp_syariah"}},
    {"text": "KPR FLPP Syariah, apa saja ketentuan yang harus dipenuhi?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp_syariah"}},
    {"text": "Apa persyaratan umum untuk mengajukan KPR FLPP Syariah?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp_syariah"}},
    {"text": "Syarat KPR FLPP Syariah apa yang perlu diketahui calon nasabah?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp_syariah"}},
    {"text": "Untuk mengajukan KPR FLPP Syariah, apa saja dokumen yang diperlukan?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp_syariah"}},
    {"text": "Apa saja syarat administratif yang harus dipenuhi untuk KPR FLPP Syariah?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp_syariah"}},

    # Produk Griya Madani
    {"text": "Apa itu Griya Madani?", "intent": "product_inquiry",
        "entities": {"product_name": "griya_madani"}},
    {"text": "Apa yang dimaksud dengan Griya Madani?",
        "intent": "product_inquiry", "entities": {"product_name": "griya_madani"}},
    {"text": "Griya Madani itu apa sih?", "intent": "product_inquiry",
        "entities": {"product_name": "griya_madani"}},
    {"text": "Bisa jelaskan lebih lanjut tentang Griya Madani?",
        "intent": "product_inquiry", "entities": {"product_name": "griya_madani"}},
    {"text": "Apa tujuan utama dari Griya Madani?", "intent": "product_inquiry",
        "entities": {"product_name": "griya_madani"}},
    {"text": "Apa saja manfaat yang diberikan oleh Griya Madani?",
        "intent": "product_inquiry", "entities": {"product_name": "griya_madani"}},
    {"text": "Bagaimana cara kerja Griya Madani?", "intent": "product_inquiry",
        "entities": {"product_name": "griya_madani"}},
    {"text": "Griya Madani, siapa saja yang dapat mengaksesnya?",
        "intent": "product_inquiry", "entities": {"product_name": "griya_madani"}},
    {"text": "Apa saja keuntungan memiliki Griya Madani?",
        "intent": "product_inquiry", "entities": {"product_name": "griya_madani"}},

    {"text": "Apa saja keuntungan dari Griya Madani?",
        "intent": "product_inquiry", "entities": {"product_name": "griya_madani"}},
    {"text": "Apa saja keuntungan dari Griya Madani?",
        "intent": "product_inquiry", "entities": {"product_name": "griya_madani"}},
    {"text": "Keuntungan apa saja yang ditawarkan oleh Griya Madani?",
        "intent": "product_inquiry", "entities": {"product_name": "griya_madani"}},
    {"text": "Apa manfaat utama dari Griya Madani?",
        "intent": "product_inquiry", "entities": {"product_name": "griya_madani"}},
    {"text": "Griya Madani, apa keuntungan bagi pembeli rumah?",
        "intent": "product_inquiry", "entities": {"product_name": "griya_madani"}},
    {"text": "Apa yang membedakan keuntungan Griya Madani dengan produk sejenis?",
        "intent": "product_inquiry", "entities": {"product_name": "griya_madani"}},
    {"text": "Keuntungan jangka panjang apa yang bisa didapat dari Griya Madani?",
        "intent": "product_inquiry", "entities": {"product_name": "griya_madani"}},
    {"text": "Apa saja benefit yang didapatkan dengan memilih Griya Madani?",
        "intent": "product_inquiry", "entities": {"product_name": "griya_madani"}},

    {"text": "Apa syarat Griya Madani?", "intent": "product_inquiry",
        "entities": {"product_name": "griya_madani"}},
    {"text": "Apa syarat untuk mendapatkan Griya Madani?",
        "intent": "product_inquiry", "entities": {"product_name": "griya_madani"}},
    {"text": "Syarat apa yang harus dipenuhi untuk mendapatkan Griya Madani?",
        "intent": "product_inquiry", "entities": {"product_name": "griya_madani"}},
    {"text": "Apa saja persyaratan yang perlu dipenuhi untuk mengajukan Griya Madani?",
        "intent": "product_inquiry", "entities": {"product_name": "griya_madani"}},
    {"text": "Griya Madani, apa saja ketentuan yang harus dipenuhi?",
        "intent": "product_inquiry", "entities": {"product_name": "griya_madani"}},
    {"text": "Apa persyaratan umum untuk mengajukan Griya Madani?",
        "intent": "product_inquiry", "entities": {"product_name": "griya_madani"}},
    {"text": "Syarat Griya Madani apa yang perlu diketahui calon nasabah?",
        "intent": "product_inquiry", "entities": {"product_name": "griya_madani"}},
    {"text": "Untuk mengajukan Griya Madani, apa saja dokumen yang diperlukan?",
        "intent": "product_inquiry", "entities": {"product_name": "griya_madani"}},
    {"text": "Apa saja syarat administratif yang harus dipenuhi untuk Griya Madani?",
        "intent": "product_inquiry", "entities": {"product_name": "griya_madani"}},

    # Produk Murabahah Plus
    {"text": "Apa itu Murabahah Plus?", "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_plus"}},
    {"text": "Apa yang dimaksud dengan Murabahah Plus?",
        "intent": "product_inquiry", "entities": {"product_name": "murabahah_plus"}},
    {"text": "Murabahah Plus itu apa sih?", "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_plus"}},
    {"text": "Bisa jelaskan lebih lanjut tentang Murabahah Plus?",
        "intent": "product_inquiry", "entities": {"product_name": "murabahah_plus"}},
    {"text": "Apa tujuan utama dari Murabahah Plus?", "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_plus"}},
    {"text": "Apa saja manfaat yang diberikan oleh Murabahah Plus?",
        "intent": "product_inquiry", "entities": {"product_name": "murabahah_plus"}},
    {"text": "Bagaimana cara kerja Murabahah Plus?", "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_plus"}},
    {"text": "Murabahah Plus, siapa saja yang dapat mengaksesnya?",
        "intent": "product_inquiry", "entities": {"product_name": "murabahah_plus"}},
    {"text": "Apa saja keuntungan memiliki Murabahah Plus?",
        "intent": "product_inquiry", "entities": {"product_name": "murabahah_plus"}},

    {"text": "Apa saja keuntungan dari Murabahah Plus?",
        "intent": "product_inquiry", "entities": {"product_name": "murabahah_plus"}},
    {"text": "Apa saja keuntungan dari Murabahah Plus?",
        "intent": "product_inquiry", "entities": {"product_name": "murabahah_plus"}},
    {"text": "Keuntungan apa saja yang ditawarkan oleh Murabahah Plus?",
        "intent": "product_inquiry", "entities": {"product_name": "murabahah_plus"}},
    {"text": "Apa manfaat utama dari Murabahah Plus?",
        "intent": "product_inquiry", "entities": {"product_name": "murabahah_plus"}},
    {"text": "Murabahah Plus, apa keuntungan bagi pengguna?",
        "intent": "product_inquiry", "entities": {"product_name": "murabahah_plus"}},
    {"text": "Apa yang membedakan keuntungan Murabahah Plus dengan produk lain?",
        "intent": "product_inquiry", "entities": {"product_name": "murabahah_plus"}},
    {"text": "Keuntungan jangka panjang apa yang bisa didapat dari Murabahah Plus?",
        "intent": "product_inquiry", "entities": {"product_name": "murabahah_plus"}},
    {"text": "Apa saja benefit yang didapatkan dengan memilih Murabahah Plus?",
        "intent": "product_inquiry", "entities": {"product_name": "murabahah_plus"}},

    {"text": "Apa syarat Murabahah Plus?", "intent": "product_inquiry",
        "entities": {"product_name": "murabahah_plus"}},
    {"text": "Apa syarat untuk mendapatkan Murabahah Plus?",
        "intent": "product_inquiry", "entities": {"product_name": "murabahah_plus"}},
    {"text": "Syarat apa yang harus dipenuhi untuk mendapatkan Murabahah Plus?",
        "intent": "product_inquiry", "entities": {"product_name": "murabahah_plus"}},
    {"text": "Apa saja persyaratan yang perlu dipenuhi untuk mengajukan Murabahah Plus?",
        "intent": "product_inquiry", "entities": {"product_name": "murabahah_plus"}},
    {"text": "Murabahah Plus, apa saja ketentuan yang harus dipenuhi?",
        "intent": "product_inquiry", "entities": {"product_name": "murabahah_plus"}},
    {"text": "Apa persyaratan umum untuk mengajukan Murabahah Plus?",
        "intent": "product_inquiry", "entities": {"product_name": "murabahah_plus"}},
    {"text": "Syarat Murabahah Plus apa yang perlu diketahui calon nasabah?",
        "intent": "product_inquiry", "entities": {"product_name": "murabahah_plus"}},
    {"text": "Untuk mengajukan Murabahah Plus, apa saja dokumen yang diperlukan?",
        "intent": "product_inquiry", "entities": {"product_name": "murabahah_plus"}},
    {"text": "Apa saja syarat administratif yang harus dipenuhi untuk Murabahah Plus?",
        "intent": "product_inquiry", "entities": {"product_name": "murabahah_plus"}},

    # Produk Deposito Mudharabah
    {"text": "Apa itu Deposito Mudharabah?", "intent": "product_inquiry",
        "entities": {"product_name": "deposito_mudharabah"}},
    {"text": "Apa yang dimaksud dengan Deposito Mudharabah?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito_mudharabah"}},
    {"text": "Deposito Mudharabah itu apa sih?", "intent": "product_inquiry",
        "entities": {"product_name": "deposito_mudharabah"}},
    {"text": "Bisa jelaskan lebih lanjut tentang Deposito Mudharabah?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito_mudharabah"}},
    {"text": "Apa tujuan utama dari Deposito Mudharabah?", "intent": "product_inquiry",
        "entities": {"product_name": "deposito_mudharabah"}},
    {"text": "Apa saja manfaat yang diberikan oleh Deposito Mudharabah?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito_mudharabah"}},
    {"text": "Bagaimana cara kerja Deposito Mudharabah?", "intent": "product_inquiry",
        "entities": {"product_name": "deposito_mudharabah"}},
    {"text": "Deposito Mudharabah, siapa saja yang dapat mengaksesnya?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito_mudharabah"}},
    {"text": "Apa saja keuntungan memiliki Deposito Mudharabah?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito_mudharabah"}},

    {"text": "Apa saja keuntungan dari Deposito Mudharabah?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito_mudharabah"}},
    {"text": "Apa saja keuntungan dari Deposito Mudharabah?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito_mudharabah"}},
    {"text": "Keuntungan apa saja yang ditawarkan oleh Deposito Mudharabah?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito_mudharabah"}},
    {"text": "Apa manfaat utama dari Deposito Mudharabah?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito_mudharabah"}},
    {"text": "Deposito Mudharabah, apa keuntungan bagi nasabah?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito_mudharabah"}},
    {"text": "Apa yang membedakan keuntungan Deposito Mudharabah dengan produk lainnya?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito_mudharabah"}},
    {"text": "Keuntungan jangka panjang apa yang bisa didapat dari Deposito Mudharabah?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito_mudharabah"}},
    {"text": "Apa saja benefit yang didapatkan dengan memilih Deposito Mudharabah?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito_mudharabah"}},

    {"text": "Apa syarat Deposito Mudharabah?", "intent": "product_inquiry",
        "entities": {"product_name": "deposito_mudharabah"}},
    {"text": "Apa syarat untuk membuka Deposito Mudharabah?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito_mudharabah"}},
    {"text": "Syarat apa yang harus dipenuhi untuk membuka Deposito Mudharabah?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito_mudharabah"}},
    {"text": "Apa saja persyaratan yang perlu dipenuhi untuk membuka Deposito Mudharabah?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito_mudharabah"}},
    {"text": "Deposito Mudharabah, apa saja ketentuan yang harus dipenuhi?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito_mudharabah"}},
    {"text": "Apa persyaratan umum untuk membuka Deposito Mudharabah?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito_mudharabah"}},
    {"text": "Syarat Deposito Mudharabah apa yang perlu diketahui calon nasabah?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito_mudharabah"}},
    {"text": "Untuk membuka Deposito Mudharabah, apa saja dokumen yang diperlukan?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito_mudharabah"}},
    {"text": "Apa saja syarat administratif yang harus dipenuhi untuk Deposito Mudharabah?",
        "intent": "product_inquiry", "entities": {"product_name": "deposito_mudharabah"}},

    # Produk BI FAST
    {"text": "Apa itu BI FAST?", "intent": "product_inquiry",
        "entities": {"product_name": "bi_fast"}},
    {"text": "Apa yang dimaksud dengan BI FAST?",
        "intent": "product_inquiry", "entities": {"product_name": "bi_fast"}},
    {"text": "BI FAST itu apa sih?", "intent": "product_inquiry",
        "entities": {"product_name": "bi_fast"}},
    {"text": "Bisa jelaskan lebih lanjut tentang BI FAST?",
        "intent": "product_inquiry", "entities": {"product_name": "bi_fast"}},
    {"text": "Apa tujuan utama dari BI FAST?", "intent": "product_inquiry",
        "entities": {"product_name": "bi_fast"}},
    {"text": "Apa saja manfaat yang diberikan oleh BI FAST?",
        "intent": "product_inquiry", "entities": {"product_name": "bi_fast"}},
    {"text": "Bagaimana cara kerja BI FAST?", "intent": "product_inquiry",
        "entities": {"product_name": "bi_fast"}},
    {"text": "BI FAST, siapa saja yang dapat mengaksesnya?",
        "intent": "product_inquiry", "entities": {"product_name": "bi_fast"}},
    {"text": "Apa saja keuntungan menggunakan BI FAST?",
        "intent": "product_inquiry", "entities": {"product_name": "bi_fast"}},

    {"text": "Apa keuntungan menggunakan BI FAST?",
        "intent": "product_inquiry", "entities": {"product_name": "bi_fast"}},
    {"text": "Apa keuntungan menggunakan BI FAST?",
        "intent": "product_inquiry", "entities": {"product_name": "bi_fast"}},
    {"text": "Keuntungan apa saja yang ditawarkan oleh BI FAST?",
        "intent": "product_inquiry", "entities": {"product_name": "bi_fast"}},
    {"text": "Apa manfaat utama dari BI FAST?", "intent": "product_inquiry",
        "entities": {"product_name": "bi_fast"}},
    {"text": "BI FAST, apa keuntungan bagi penggunanya?",
        "intent": "product_inquiry", "entities": {"product_name": "bi_fast"}},
    {"text": "Apa yang membedakan keuntungan BI FAST dengan layanan transfer lainnya?",
        "intent": "product_inquiry", "entities": {"product_name": "bi_fast"}},
    {"text": "Keuntungan jangka panjang apa yang bisa didapat dari BI FAST?",
        "intent": "product_inquiry", "entities": {"product_name": "bi_fast"}},
    {"text": "Apa saja benefit yang didapatkan dengan memilih BI FAST?",
        "intent": "product_inquiry", "entities": {"product_name": "bi_fast"}},

    {"text": "Berapa limit transaksi BI FAST?", "intent": "product_inquiry",
        "entities": {"product_name": "bi_fast"}},
    {"text": "Berapa limit transaksi yang dapat dilakukan melalui BI FAST?",
        "intent": "product_inquiry", "entities": {"product_name": "bi_fast"}},
    {"text": "Limit transaksi BI FAST berapa sih?",
        "intent": "product_inquiry", "entities": {"product_name": "bi_fast"}},
    {"text": "Apa batasan transaksi yang diberlakukan oleh BI FAST?",
        "intent": "product_inquiry", "entities": {"product_name": "bi_fast"}},
    {"text": "Berapa maksimal transaksi yang bisa dilakukan dengan BI FAST?",
        "intent": "product_inquiry", "entities": {"product_name": "bi_fast"}},
    {"text": "Apa saja ketentuan terkait limit transaksi pada BI FAST?",
        "intent": "product_inquiry", "entities": {"product_name": "bi_fast"}},
    {"text": "Untuk transaksi melalui BI FAST, berapa jumlah maksimal yang dapat ditransfer?",
        "intent": "product_inquiry", "entities": {"product_name": "bi_fast"}},
    {"text": "BI FAST memiliki batasan transaksi, berapa batasannya?",
        "intent": "product_inquiry", "entities": {"product_name": "bi_fast"}},

    # Produk Safe Deposit Box
    {"text": "Apa itu Safe Deposit Box?", "intent": "product_inquiry",
        "entities": {"product_name": "safe_deposit_box"}},
    {"text": "Apa yang dimaksud dengan Safe Deposit Box?",
        "intent": "product_inquiry", "entities": {"product_name": "safe_deposit_box"}},
    {"text": "Safe Deposit Box itu apa sih?", "intent": "product_inquiry",
        "entities": {"product_name": "safe_deposit_box"}},
    {"text": "Bisa jelaskan lebih lanjut tentang Safe Deposit Box?",
        "intent": "product_inquiry", "entities": {"product_name": "safe_deposit_box"}},
    {"text": "Apa tujuan utama dari Safe Deposit Box?", "intent": "product_inquiry",
        "entities": {"product_name": "safe_deposit_box"}},
    {"text": "Apa saja manfaat yang diberikan oleh Safe Deposit Box?",
        "intent": "product_inquiry", "entities": {"product_name": "safe_deposit_box"}},
    {"text": "Bagaimana cara kerja Safe Deposit Box?", "intent": "product_inquiry",
        "entities": {"product_name": "safe_deposit_box"}},
    {"text": "Safe Deposit Box, siapa saja yang dapat mengaksesnya?",
        "intent": "product_inquiry", "entities": {"product_name": "safe_deposit_box"}},
    {"text": "Apa saja keuntungan memiliki Safe Deposit Box?",
        "intent": "product_inquiry", "entities": {"product_name": "safe_deposit_box"}},

    {"text": "Apa syarat untuk sewa Safe Deposit Box untuk individu?",
        "intent": "product_inquiry", "entities": {"product_name": "safe_deposit_box"}},
    {"text": "Apa syarat untuk menyewa Safe Deposit Box untuk individu?",
        "intent": "product_inquiry", "entities": {"product_name": "safe_deposit_box"}},
    {"text": "Syarat apa saja yang harus dipenuhi untuk menyewa Safe Deposit Box bagi individu?",
        "intent": "product_inquiry", "entities": {"product_name": "safe_deposit_box"}},
    {"text": "Untuk individu, apa saja persyaratan sewa Safe Deposit Box?",
        "intent": "product_inquiry", "entities": {"product_name": "safe_deposit_box"}},
    {"text": "Apa saja ketentuan untuk menyewa Safe Deposit Box bagi individu?",
        "intent": "product_inquiry", "entities": {"product_name": "safe_deposit_box"}},
    {"text": "Apa saja persyaratan sewa Safe Deposit Box untuk individu?",
        "intent": "product_inquiry", "entities": {"product_name": "safe_deposit_box"}},

    {"text": "Apa syarat Safe Deposit Box untuk perusahaan?",
        "intent": "product_inquiry", "entities": {"product_name": "safe_deposit_box"}},
    {"text": "Apa syarat yang harus dipenuhi untuk perusahaan yang ingin menyewa Safe Deposit Box?",
        "intent": "product_inquiry", "entities": {"product_name": "safe_deposit_box"}},
    {"text": "Syarat apa saja yang diperlukan untuk perusahaan dalam menyewa Safe Deposit Box?",
        "intent": "product_inquiry", "entities": {"product_name": "safe_deposit_box"}},
    {"text": "Untuk perusahaan, apa saja persyaratan dalam menyewa Safe Deposit Box?",
        "intent": "product_inquiry", "entities": {"product_name": "safe_deposit_box"}},
    {"text": "Apa ketentuan yang berlaku untuk perusahaan yang ingin menyewa Safe Deposit Box?",
        "intent": "product_inquiry", "entities": {"product_name": "safe_deposit_box"}},

    {"text": "Apa syarat Safe Deposit Box untuk instansi pemerintah?",
        "intent": "product_inquiry", "entities": {"product_name": "safe_deposit_box"}},
    {"text": "Apa saja syarat untuk menyewa Safe Deposit Box untuk instansi pemerintah?",
        "intent": "product_inquiry", "entities": {"product_name": "safe_deposit_box"}},
    {"text": "Apa persyaratan untuk instansi pemerintah yang ingin menyewa Safe Deposit Box?",
        "intent": "product_inquiry", "entities": {"product_name": "safe_deposit_box"}},
    {"text": "Syarat apa saja yang diperlukan oleh instansi pemerintah untuk menyewa Safe Deposit Box?",
        "intent": "product_inquiry", "entities": {"product_name": "safe_deposit_box"}},
    {"text": "Apa saja ketentuan bagi instansi pemerintah yang ingin menyewa Safe Deposit Box?",
        "intent": "product_inquiry", "entities": {"product_name": "safe_deposit_box"}},
    {"text": "Apa saja persyaratan untuk sewa Safe Deposit Box untuk instansi pemerintah?",
        "intent": "product_inquiry", "entities": {"product_name": "safe_deposit_box"}},

    # Produk Western Union
    {"text": "Apa itu Western Union?", "intent": "product_inquiry",
        "entities": {"product_name": "western_union"}},
    {"text": "Apa yang dimaksud dengan Western Union?",
        "intent": "product_inquiry", "entities": {"product_name": "western_union"}},
    {"text": "Western Union itu apa sih?", "intent": "product_inquiry",
        "entities": {"product_name": "western_union"}},
    {"text": "Bisa jelaskan lebih lanjut tentang Western Union?",
        "intent": "product_inquiry", "entities": {"product_name": "western_union"}},
    {"text": "Apa tujuan utama dari Western Union?", "intent": "product_inquiry",
        "entities": {"product_name": "western_union"}},
    {"text": "Apa saja manfaat yang diberikan oleh Western Union?",
        "intent": "product_inquiry", "entities": {"product_name": "western_union"}},
    {"text": "Bagaimana cara kerja Western Union?", "intent": "product_inquiry",
        "entities": {"product_name": "western_union"}},
    {"text": "Western Union, siapa saja yang dapat mengaksesnya?",
        "intent": "product_inquiry", "entities": {"product_name": "western_union"}},

    {"text": "Apa keuntungan dari Western Union?", "intent": "product_inquiry",
        "entities": {"product_name": "western_union"}},
    {"text": "Apa saja keuntungan menggunakan Western Union?",
        "intent": "product_inquiry", "entities": {"product_name": "western_union"}},
    {"text": "Keuntungan apa saja yang ditawarkan oleh Western Union?",
        "intent": "product_inquiry", "entities": {"product_name": "western_union"}},
    {"text": "Apa manfaat utama dari menggunakan Western Union?",
        "intent": "product_inquiry", "entities": {"product_name": "western_union"}},
    {"text": "Western Union, apa keuntungan bagi pengirim dan penerima?",
        "intent": "product_inquiry", "entities": {"product_name": "western_union"}},
    {"text": "Apa yang membedakan keuntungan Western Union dengan layanan pengiriman uang lainnya?",
        "intent": "product_inquiry", "entities": {"product_name": "western_union"}},
    {"text": "Keuntungan jangka panjang apa yang bisa didapat dari menggunakan Western Union?",
        "intent": "product_inquiry", "entities": {"product_name": "western_union"}},
    {"text": "Apa saja benefit yang didapatkan dengan memilih Western Union?",
        "intent": "product_inquiry", "entities": {"product_name": "western_union"}},

    # Produk Nagari Mobile Banking
    {"text": "Apa itu Nagari Mobile Banking?", "intent": "product_inquiry",
        "entities": {"product_name": "nagari_mobile_banking"}},
    {"text": "Apa yang dimaksud dengan Nagari Mobile Banking?",
        "intent": "product_inquiry", "entities": {"product_name": "nagari_mobile_banking"}},
    {"text": "Nagari Mobile Banking itu apa sih?", "intent": "product_inquiry",
        "entities": {"product_name": "nagari_mobile_banking"}},
    {"text": "Bisa jelaskan lebih lanjut tentang Nagari Mobile Banking?",
        "intent": "product_inquiry", "entities": {"product_name": "nagari_mobile_banking"}},
    {"text": "Apa tujuan utama dari Nagari Mobile Banking?", "intent": "product_inquiry",
        "entities": {"product_name": "nagari_mobile_banking"}},
    {"text": "Apa saja manfaat yang diberikan oleh Nagari Mobile Banking?",
        "intent": "product_inquiry", "entities": {"product_name": "nagari_mobile_banking"}},
    {"text": "Bagaimana cara kerja Nagari Mobile Banking?", "intent": "product_inquiry",
        "entities": {"product_name": "nagari_mobile_banking"}},
    {"text": "Nagari Mobile Banking, siapa saja yang dapat mengaksesnya?",
        "intent": "product_inquiry", "entities": {"product_name": "nagari_mobile_banking"}},
    {"text": "Apa saja keuntungan memiliki Nagari Mobile Banking?",
        "intent": "product_inquiry", "entities": {"product_name": "nagari_mobile_banking"}},

    {"text": "Apa saja menu di Nagari Mobile Banking?", "intent": "product_inquiry",
        "entities": {"product_name": "nagari_mobile_banking"}},
    {"text": "Apa saja menu yang tersedia di Nagari Mobile Banking?",
        "intent": "product_inquiry", "entities": {"product_name": "nagari_mobile_banking"}},
    {"text": "Menu apa saja yang bisa diakses di Nagari Mobile Banking?",
        "intent": "product_inquiry", "entities": {"product_name": "nagari_mobile_banking"}},
    {"text": "Apa saja pilihan menu di Nagari Mobile Banking?",
        "intent": "product_inquiry", "entities": {"product_name": "nagari_mobile_banking"}},
    {"text": "Menu utama apa saja yang tersedia di Nagari Mobile Banking?",
        "intent": "product_inquiry", "entities": {"product_name": "nagari_mobile_banking"}},
    {"text": "Apa saja fitur menu yang ada di Nagari Mobile Banking?",
        "intent": "product_inquiry", "entities": {"product_name": "nagari_mobile_banking"}},
    {"text": "Apa saja layanan yang bisa diakses melalui menu Nagari Mobile Banking?",
        "intent": "product_inquiry", "entities": {"product_name": "nagari_mobile_banking"}},
    {"text": "Menu apa saja yang bisa membantu transaksi di Nagari Mobile Banking?",
        "intent": "product_inquiry", "entities": {"product_name": "nagari_mobile_banking"}},
    {"text": "Nagari Mobile Banking, apa saja menu transaksi yang bisa dilakukan?",
        "intent": "product_inquiry", "entities": {"product_name": "nagari_mobile_banking"}},

    {"text": "Apa fitur dari Nagari Mobile Banking?", "intent": "product_inquiry",
        "entities": {"product_name": "nagari_mobile_banking"}},
    {"text": "Apa saja fitur yang ada di Nagari Mobile Banking?",
        "intent": "product_inquiry", "entities": {"product_name": "nagari_mobile_banking"}},
    {"text": "Fitur-fitur apa saja yang disediakan oleh Nagari Mobile Banking?",
        "intent": "product_inquiry", "entities": {"product_name": "nagari_mobile_banking"}},
    {"text": "Apa saja fitur unggulan Nagari Mobile Banking?",
        "intent": "product_inquiry", "entities": {"product_name": "nagari_mobile_banking"}},
    {"text": "Bagaimana cara menggunakan fitur di Nagari Mobile Banking?",
        "intent": "product_inquiry", "entities": {"product_name": "nagari_mobile_banking"}},
    {"text": "Fitur apa yang paling sering digunakan di Nagari Mobile Banking?",
        "intent": "product_inquiry", "entities": {"product_name": "nagari_mobile_banking"}},
    {"text": "Apa kelebihan fitur Nagari Mobile Banking dibandingkan dengan aplikasi sejenis?",
        "intent": "product_inquiry", "entities": {"product_name": "nagari_mobile_banking"}},
    {"text": "Apa manfaat utama dari fitur-fitur Nagari Mobile Banking?",
        "intent": "product_inquiry", "entities": {"product_name": "nagari_mobile_banking"}},
    {"text": "Apa saja fitur transaksi yang ada di Nagari Mobile Banking?",
        "intent": "product_inquiry", "entities": {"product_name": "nagari_mobile_banking"}},

    # Produk Nagari Auto Debet
    {"text": "Apa itu layanan Auto Debet?", "intent": "product_inquiry",
        "entities": {"product_name": "nagari_auto_debet"}},
    {"text": "Apa yang dimaksud dengan layanan Auto Debet?",
        "intent": "product_inquiry", "entities": {"product_name": "nagari_auto_debet"}},
    {"text": "Layanan Auto Debet itu apa sih?", "intent": "product_inquiry",
        "entities": {"product_name": "nagari_auto_debet"}},
    {"text": "Bisa jelaskan lebih lanjut tentang layanan Auto Debet?",
        "intent": "product_inquiry", "entities": {"product_name": "nagari_auto_debet"}},
    {"text": "Apa tujuan utama dari layanan Auto Debet?",
        "intent": "product_inquiry", "entities": {"product_name": "nagari_auto_debet"}},
    {"text": "Apa saja manfaat yang diberikan oleh layanan Auto Debet?",
        "intent": "product_inquiry", "entities": {"product_name": "nagari_auto_debet"}},
    {"text": "Bagaimana cara kerja layanan Auto Debet?", "intent": "product_inquiry",
        "entities": {"product_name": "nagari_auto_debet"}},
    {"text": "Layanan Auto Debet, siapa saja yang dapat mengaksesnya?",
        "intent": "product_inquiry", "entities": {"product_name": "nagari_auto_debet"}},
    {"text": "Apa saja keuntungan menggunakan layanan Auto Debet?",
        "intent": "product_inquiry", "entities": {"product_name": "nagari_auto_debet"}},

    {"text": "Apa fitur dari layanan Auto Debet?", "intent": "product_inquiry",
        "entities": {"product_name": "nagari_auto_debet"}},
    {"text": "Apa saja fitur yang ada di layanan Auto Debet?",
        "intent": "product_inquiry", "entities": {"product_name": "nagari_auto_debet"}},
    {"text": "Fitur apa saja yang disediakan oleh layanan Auto Debet?",
        "intent": "product_inquiry", "entities": {"product_name": "nagari_auto_debet"}},
    {"text": "Apa saja fitur unggulan layanan Auto Debet?",
        "intent": "product_inquiry", "entities": {"product_name": "nagari_auto_debet"}},
    {"text": "Bagaimana cara menggunakan fitur layanan Auto Debet?",
        "intent": "product_inquiry", "entities": {"product_name": "nagari_auto_debet"}},
    {"text": "Apa manfaat utama dari fitur layanan Auto Debet?",
        "intent": "product_inquiry", "entities": {"product_name": "nagari_auto_debet"}},
    {"text": "Apa kelebihan fitur layanan Auto Debet dibandingkan dengan metode pembayaran lainnya?",
        "intent": "product_inquiry", "entities": {"product_name": "nagari_auto_debet"}},
    {"text": "Apa fitur-fitur utama dari layanan Auto Debet yang harus diketahui?",
        "intent": "product_inquiry", "entities": {"product_name": "nagari_auto_debet"}},
    {"text": "Apa saja fitur yang membuat layanan Auto Debet lebih efisien?",
        "intent": "product_inquiry", "entities": {"product_name": "nagari_auto_debet"}},

    # Produk QRIS Nagari Mobile Banking
    {"text": "Bagaimana cara membayar dengan QRIS di Nagari Mobile Banking?",
        "intent": "product_inquiry", "entities": {"product_name": "qris_nagari"}},
    {"text": "Bagaimana cara melakukan pembayaran menggunakan QRIS di Nagari Mobile Banking?",
        "intent": "product_inquiry", "entities": {"product_name": "qris_nagari"}},
    {"text": "Apa langkah-langkah untuk membayar dengan QRIS di Nagari Mobile Banking?",
        "intent": "product_inquiry", "entities": {"product_name": "qris_nagari"}},
    {"text": "Bagaimana cara bayar menggunakan QRIS di Nagari Mobile Banking?",
        "intent": "product_inquiry", "entities": {"product_name": "qris_nagari"}},
    {"text": "Bisakah Anda jelaskan cara melakukan pembayaran QRIS di Nagari Mobile Banking?",
        "intent": "product_inquiry", "entities": {"product_name": "qris_nagari"}},
    {"text": "Langkah-langkah apa saja yang harus dilakukan untuk membayar menggunakan QRIS di Nagari Mobile Banking?",
        "intent": "product_inquiry", "entities": {"product_name": "qris_nagari"}},
    {"text": "Bagaimana cara mudah membayar dengan QRIS melalui aplikasi Nagari Mobile Banking?",
        "intent": "product_inquiry", "entities": {"product_name": "qris_nagari"}},
    {"text": "Apa saja tahapan yang perlu dilakukan untuk membayar menggunakan QRIS di Nagari Mobile Banking?",
        "intent": "product_inquiry", "entities": {"product_name": "qris_nagari"}},
    {"text": "Cara apa yang harus dilakukan untuk melakukan pembayaran QRIS di Nagari Mobile Banking?",
        "intent": "product_inquiry", "entities": {"product_name": "qris_nagari"}},

    {"text": "Bagaimana cara transfer dengan QRIS?",
        "intent": "product_inquiry", "entities": {"product_name": "qris_nagari"}},
    {"text": "Bagaimana cara transfer menggunakan QRIS di Nagari Mobile Banking?",
        "intent": "product_inquiry", "entities": {"product_name": "qris_nagari"}},
    {"text": "Apa langkah-langkah untuk melakukan transfer dengan QRIS di Nagari Mobile Banking?",
        "intent": "product_inquiry", "entities": {"product_name": "qris_nagari"}},
    {"text": "Bagaimana cara transfer uang lewat QRIS di Nagari Mobile Banking?",
        "intent": "product_inquiry", "entities": {"product_name": "qris_nagari"}},
    {"text": "Bisakah Anda jelaskan cara melakukan transfer dengan QRIS melalui Nagari Mobile Banking?",
        "intent": "product_inquiry", "entities": {"product_name": "qris_nagari"}},
    {"text": "Langkah-langkah apa yang perlu dilakukan untuk transfer menggunakan QRIS di Nagari Mobile Banking?",
        "intent": "product_inquiry", "entities": {"product_name": "qris_nagari"}},
    {"text": "Bagaimana cara mudah transfer uang dengan QRIS di Nagari Mobile Banking?",
        "intent": "product_inquiry", "entities": {"product_name": "qris_nagari"}},
    {"text": "Apa saja tahapan yang harus dilakukan untuk transfer dengan QRIS di Nagari Mobile Banking?",
        "intent": "product_inquiry", "entities": {"product_name": "qris_nagari"}},
    {"text": "Cara apa yang perlu dilakukan untuk melakukan transfer menggunakan QRIS di Nagari Mobile Banking?",
        "intent": "product_inquiry", "entities": {"product_name": "qris_nagari"}},

    # Produk Laku Pandai
    {"text": "Apa itu Laku Pandai?", "intent": "product_inquiry",
        "entities": {"product_name": "laku_pandai"}},
    {"text": "Apa yang dimaksud dengan Laku Pandai?",
        "intent": "product_inquiry", "entities": {"product_name": "laku_pandai"}},
    {"text": "Laku Pandai itu apa sih?", "intent": "product_inquiry",
        "entities": {"product_name": "laku_pandai"}},
    {"text": "Bisa jelaskan lebih lanjut tentang Laku Pandai?",
        "intent": "product_inquiry", "entities": {"product_name": "laku_pandai"}},
    {"text": "Apa tujuan utama dari Laku Pandai?", "intent": "product_inquiry",
        "entities": {"product_name": "laku_pandai"}},
    {"text": "Apa saja manfaat yang diberikan oleh Laku Pandai?",
        "intent": "product_inquiry", "entities": {"product_name": "laku_pandai"}},
    {"text": "Bagaimana cara kerja Laku Pandai?", "intent": "product_inquiry",
        "entities": {"product_name": "laku_pandai"}},
    {"text": "Laku Pandai, siapa saja yang dapat mengaksesnya?",
        "intent": "product_inquiry", "entities": {"product_name": "laku_pandai"}},
    {"text": "Apa saja keuntungan menggunakan Laku Pandai?",
        "intent": "product_inquiry", "entities": {"product_name": "laku_pandai"}},

    {"text": "Apa syarat menjadi agen Laku Pandai?",
        "intent": "product_inquiry", "entities": {"product_name": "laku_pandai"}},
    {"text": "Apa syarat untuk menjadi agen Laku Pandai?",
        "intent": "product_inquiry", "entities": {"product_name": "laku_pandai"}},
    {"text": "Apa saja persyaratan untuk menjadi agen Laku Pandai?",
        "intent": "product_inquiry", "entities": {"product_name": "laku_pandai"}},
    {"text": "Siapa saja yang bisa menjadi agen Laku Pandai?",
        "intent": "product_inquiry", "entities": {"product_name": "laku_pandai"}},
    {"text": "Apa saja ketentuan untuk menjadi agen Laku Pandai?",
        "intent": "product_inquiry", "entities": {"product_name": "laku_pandai"}},
    {"text": "Bagaimana cara menjadi agen Laku Pandai?",
        "intent": "product_inquiry", "entities": {"product_name": "laku_pandai"}},
    {"text": "Syarat apa saja yang dibutuhkan untuk menjadi agen Laku Pandai?",
        "intent": "product_inquiry", "entities": {"product_name": "laku_pandai"}},
    {"text": "Apa saja dokumen yang diperlukan untuk menjadi agen Laku Pandai?",
        "intent": "product_inquiry", "entities": {"product_name": "laku_pandai"}},
    {"text": "Apa saja kriteria yang harus dipenuhi untuk menjadi agen Laku Pandai?",
        "intent": "product_inquiry", "entities": {"product_name": "laku_pandai"}},

    # Produk Ollin by Nagari
    {"text": "Apa itu Ollin by Nagari?", "intent": "product_inquiry",
        "entities": {"product_name": "ollin_by_nagari"}},
    {"text": "Apa yang dimaksud dengan Ollin by Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "ollin_by_nagari"}},
    {"text": "Ollin by Nagari itu apa sih?", "intent": "product_inquiry",
        "entities": {"product_name": "ollin_by_nagari"}},
    {"text": "Bisa jelaskan lebih lanjut tentang Ollin by Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "ollin_by_nagari"}},
    {"text": "Apa tujuan utama dari Ollin by Nagari?", "intent": "product_inquiry",
        "entities": {"product_name": "ollin_by_nagari"}},
    {"text": "Apa saja manfaat yang diberikan oleh Ollin by Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "ollin_by_nagari"}},
    {"text": "Bagaimana cara kerja Ollin by Nagari?", "intent": "product_inquiry",
        "entities": {"product_name": "ollin_by_nagari"}},
    {"text": "Ollin by Nagari, siapa saja yang dapat mengaksesnya?",
        "intent": "product_inquiry", "entities": {"product_name": "ollin_by_nagari"}},
    {"text": "Apa saja keuntungan menggunakan Ollin by Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "ollin_by_nagari"}},

    {"text": "Apa fitur Ollin by Nagari?", "intent": "product_inquiry",
        "entities": {"product_name": "ollin_by_nagari"}},
    {"text": "Apa saja fitur yang ada di Ollin by Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "ollin_by_nagari"}},
    {"text": "Fitur apa saja yang disediakan oleh Ollin by Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "ollin_by_nagari"}},
    {"text": "Apa saja fitur unggulan Ollin by Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "ollin_by_nagari"}},
    {"text": "Bagaimana cara menggunakan fitur Ollin by Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "ollin_by_nagari"}},
    {"text": "Apa manfaat utama dari fitur Ollin by Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "ollin_by_nagari"}},
    {"text": "Apa kelebihan fitur Ollin by Nagari dibandingkan dengan aplikasi sejenis?",
        "intent": "product_inquiry", "entities": {"product_name": "ollin_by_nagari"}},
    {"text": "Apa fitur-fitur utama dari Ollin by Nagari yang harus diketahui?",
        "intent": "product_inquiry", "entities": {"product_name": "ollin_by_nagari"}},
    {"text": "Apa saja fitur yang membuat Ollin by Nagari lebih efisien?",
        "intent": "product_inquiry", "entities": {"product_name": "ollin_by_nagari"}},

    {"text": "Bagaimana cara mendaftar Ollin by Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "ollin_by_nagari"}},
    {"text": "Bagaimana cara mendaftar Ollin by Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "ollin_by_nagari"}},
    {"text": "Apa langkah-langkah untuk mendaftar di Ollin by Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "ollin_by_nagari"}},
    {"text": "Bagaimana cara melakukan registrasi di Ollin by Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "ollin_by_nagari"}},
    {"text": "Apa yang harus dilakukan untuk mendaftar Ollin by Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "ollin_by_nagari"}},
    {"text": "Langkah apa saja yang perlu diikuti untuk mendaftar Ollin by Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "ollin_by_nagari"}},
    {"text": "Apa saja persyaratan untuk mendaftar di Ollin by Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "ollin_by_nagari"}},
    {"text": "Bagaimana cara cepat mendaftar Ollin by Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "ollin_by_nagari"}},
    {"text": "Apa yang perlu disiapkan untuk mendaftar Ollin by Nagari?",
        "intent": "product_inquiry", "entities": {"product_name": "ollin_by_nagari"}},

    {
        "intent": "product_inquiry",
        "text": "Apa itu layanan APN dari Bank Nagari dan bagaimana cara menggunakannya di luar negeri?",
        "entities": {"product_name": "apn"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya ingin tarik tunai di Malaysia, apakah kartu ATM Bank Nagari bisa digunakan lewat APN?",
        "entities": {"product_name": "apn"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah layanan APN Bank Nagari bisa digunakan untuk mengecek saldo di Thailand?",
        "entities": {"product_name": "apn"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apa saja negara yang mendukung transaksi kartu debit Bank Nagari melalui jaringan APN?",
        "entities": {"product_name": "apn"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bagaimana prosedur aktivasi layanan APN di aplikasi Ollin?",
        "entities": {"product_name": "apn"}
    },
    {
        "intent": "product_inquiry",
        "text": "Berapa biaya tarik tunai di luar negeri dengan APN?",
        "entities": {"product_name": "apn"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya mau cek saldo rekening Bank Nagari di Korea, apakah bisa dengan APN?",
        "entities": {"product_name": "apn"}
    },
    {
        "intent": "product_inquiry",
        "text": "Layanan APN bisa digunakan di ATM negara mana saja?",
        "entities": {"product_name": "apn"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah Bank Nagari menyediakan fitur untuk transaksi internasional seperti APN?",
        "entities": {"product_name": "apn"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apa saja langkah-langkah untuk aktivasi kartu ATM luar negeri lewat Ollin?",
        "entities": {"product_name": "apn"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bisakah saya tarik tunai di Korea Selatan dengan ATM Bank Nagari?",
        "entities": {"product_name": "apn"}
    },
    {
        "intent": "product_inquiry",
        "text": "ATM bank mana di Thailand yang bisa digunakan dengan APN?",
        "entities": {"product_name": "apn"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya nasabah Bank Nagari, ingin mengaktifkan kartu ATM agar bisa dipakai di luar negeri. Bagaimana caranya?",
        "entities": {"product_name": "apn"}
    },
    {
        "intent": "product_inquiry",
        "text": "Kalau saya tarik uang di Malaysia pakai APN, kena biaya berapa?",
        "entities": {"product_name": "apn"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apa yang dimaksud dengan fitur APN dan manfaatnya bagi nasabah Bank Nagari?",
        "entities": {"product_name": "apn"}
    },
    {
        "intent": "product_inquiry",
        "text": "Dimana saya bisa menggunakan ATM Bank Nagari di luar negeri melalui jaringan APN?",
        "entities": {"product_name": "apn"}
    },
    {
        "intent": "product_inquiry",
        "text": "Berapa biaya cek saldo dengan layanan APN di luar negeri?",
        "entities": {"product_name": "apn"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah Citi Bank di Korea Selatan mendukung kartu Bank Nagari lewat APN?",
        "entities": {"product_name": "apn"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya ingin tahu apakah kartu ATM Bank Nagari bisa digunakan di Kasikornbank Thailand?",
        "entities": {"product_name": "apn"}
    },
    {
        "intent": "product_inquiry",
        "text": "ATM mana saja di Malaysia yang kompatibel dengan kartu APN Bank Nagari?",
        "entities": {"product_name": "apn"}
    },
    {
        "intent": "product_inquiry",
        "text": "Setelah aktivasi APN, apa saja transaksi yang bisa dilakukan di luar negeri?",
        "entities": {"product_name": "apn"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah Maybank di Malaysia bisa menerima transaksi dari kartu debit Bank Nagari lewat APN?",
        "entities": {"product_name": "apn"}
    },
    {
        "intent": "product_inquiry",
        "text": "Aktivasi fitur APN melalui aplikasi Ollin dimulai dari menu mana ya?",
        "entities": {"product_name": "apn"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bisakah saya cek saldo rekening di ATM Thailand lewat APN?",
        "entities": {"product_name": "apn"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya tidak menemukan pilihan aktivasi APN di Ollin, apa langkah-langkah lengkapnya?",
        "entities": {"product_name": "apn"}
    },
    {
        "intent": "product_inquiry",
        "text": "Adakah biaya tambahan jika saya melakukan penarikan tunai di luar negeri dengan kartu Bank Nagari?",
        "entities": {"product_name": "apn"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya ingin tahu cara aktivasi kartu ATM luar negeri di aplikasi Ollin by Nagari.",
        "entities": {"product_name": "apn"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bank Nagari punya fitur ATM luar negeri lewat APN? Tolong dijelaskan.",
        "entities": {"product_name": "apn"}
    },
    {
        "intent": "product_inquiry",
        "text": "Kalau saya pakai ATM di Korea, apakah bisa tarik tunai dan cek saldo dengan APN?",
        "entities": {"product_name": "apn"}
    },
    {
        "intent": "product_inquiry",
        "text": "Transaksi lewat APN di Indonesia, Malaysia, Thailand, dan Korea apa saja yang bisa dilakukan?",
        "entities": {"product_name": "apn"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya mau ke Thailand, apakah bisa gunakan kartu Bank Nagari di Krungthai Bank lewat APN?",
        "entities": {"product_name": "apn"}
    },

    {
        "intent": "product_inquiry",
        "text": "Apa itu layanan N-KISS dari Bank Nagari dan bagaimana cara kerjanya?",
        "entities": {"product_name": "n_kiss_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya ingin tahu fungsi dari aplikasi N-KISS di Bank Nagari.",
        "entities": {"product_name": "n_kiss_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah di N-KISS saya bisa melihat jadwal praktik dokter?",
        "entities": {"product_name": "n_kiss_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bisa tidak saya booking nomor antrian di klinik lewat aplikasi N-KISS?",
        "entities": {"product_name": "n_kiss_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Dimana saya bisa menemukan menu N-KISS di aplikasi Bank Nagari?",
        "entities": {"product_name": "n_kiss_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Langkah-langkah penggunaan N-KISS secara online lewat Ollin itu bagaimana ya?",
        "entities": {"product_name": "n_kiss_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bagaimana cara membuat janji dengan dokter melalui N-KISS?",
        "entities": {"product_name": "n_kiss_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Kalau saya datang langsung ke klinik, apa alur penggunaan N-KISS yang harus saya ikuti?",
        "entities": {"product_name": "n_kiss_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apa saja fitur utama dari aplikasi N-KISS di Bank Nagari?",
        "entities": {"product_name": "n_kiss_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya ingin tahu apakah bisa bayar layanan klinik lewat N-KISS langsung?",
        "entities": {"product_name": "n_kiss_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah bisa mencari lokasi klinik terdekat menggunakan aplikasi N-KISS?",
        "entities": {"product_name": "n_kiss_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apa saja langkah saat saya registrasi di N-KISS secara online?",
        "entities": {"product_name": "n_kiss_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Fitur pemesanan dokter di aplikasi N-KISS bagaimana cara kerjanya?",
        "entities": {"product_name": "n_kiss_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya ingin buat janji pemeriksaan via N-KISS, apa yang harus saya lakukan?",
        "entities": {"product_name": "n_kiss_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah pembayaran di N-KISS bisa dilakukan melalui channel Bank Nagari langsung?",
        "entities": {"product_name": "n_kiss_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apa perbedaan alur penggunaan N-KISS secara online dan di klinik langsung?",
        "entities": {"product_name": "n_kiss_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Kalau saya tidak punya aplikasi Ollin, apakah tetap bisa gunakan N-KISS di klinik?",
        "entities": {"product_name": "n_kiss_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah saya bisa input data pasien melalui aplikasi N-KISS?",
        "entities": {"product_name": "n_kiss_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "N-KISS itu aplikasi untuk layanan klinik ya? Bagaimana cara mengaksesnya?",
        "entities": {"product_name": "n_kiss_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah saya bisa konsultasi dengan dokter setelah booking lewat N-KISS?",
        "entities": {"product_name": "n_kiss_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saat mendaftar via admin klinik, apakah sistemnya masih tetap menggunakan N-KISS?",
        "entities": {"product_name": "n_kiss_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Langkah terakhir saat menggunakan N-KISS apa langsung ke pembayaran?",
        "entities": {"product_name": "n_kiss_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah menu multilink di Ollin mencakup akses ke layanan N-KISS?",
        "entities": {"product_name": "n_kiss_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya sudah install Ollin, bagaimana cara cari N-KISS di dalamnya?",
        "entities": {"product_name": "n_kiss_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya ingin tahu semua fitur di aplikasi N-KISS yang bisa saya gunakan.",
        "entities": {"product_name": "n_kiss_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah bisa langsung datang ke klinik lalu mendaftar via admin untuk pakai N-KISS?",
        "entities": {"product_name": "n_kiss_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah data pasien harus diisi secara manual saat booking di N-KISS?",
        "entities": {"product_name": "n_kiss_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Kalau mau bayar biaya pemeriksaan setelah konsultasi dokter di N-KISS, bisa pakai Bank Nagari langsung?",
        "entities": {"product_name": "n_kiss_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya butuh panduan lengkap alur registrasi dan booking layanan N-KISS.",
        "entities": {"product_name": "n_kiss_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Aplikasi N-KISS bisa bantu temukan klinik terdekat ya? Bagaimana caranya?",
        "entities": {"product_name": "n_kiss_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Kalau pakai N-KISS untuk booking dokter, bisa langsung tentukan jadwal pemeriksaan juga?",
        "entities": {"product_name": "n_kiss_bank_nagari"}
    },

    {
        "intent": "product_inquiry",
        "text": "Apa itu aplikasi Nagari Digital Masjid dari Bank Nagari?",
        "entities": {"product_name": "nagari_digital_masjid"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya ingin tahu fungsi utama dari aplikasi Nagari Digital Masjid.",
        "entities": {"product_name": "nagari_digital_masjid"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah aplikasi Nagari Digital Masjid mendukung infaq digital?",
        "entities": {"product_name": "nagari_digital_masjid"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bisa tidak saya mencari lokasi musholla terdekat lewat aplikasi Nagari Digital Masjid?",
        "entities": {"product_name": "nagari_digital_masjid"}
    },
    {
        "intent": "product_inquiry",
        "text": "Fitur apa saja yang tersedia di dalam aplikasi Nagari Digital Masjid?",
        "entities": {"product_name": "nagari_digital_masjid"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah aplikasi Nagari Digital Masjid memberikan update tentang kegiatan masjid?",
        "entities": {"product_name": "nagari_digital_masjid"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya ingin tahu apakah jadwal sholat tersedia di aplikasi Nagari Digital Masjid.",
        "entities": {"product_name": "nagari_digital_masjid"}
    },
    {
        "intent": "product_inquiry",
        "text": "Dimana saya bisa mendownload aplikasi Nagari Digital Masjid?",
        "entities": {"product_name": "nagari_digital_masjid"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah Nagari Digital Masjid bisa digunakan untuk infaq menggunakan QRIS?",
        "entities": {"product_name": "nagari_digital_masjid"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah aplikasi Nagari Digital Masjid menampilkan foto dan profil masjid?",
        "entities": {"product_name": "nagari_digital_masjid"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya ingin melihat jadwal sholat harian lewat aplikasi Bank Nagari, bisa?",
        "entities": {"product_name": "nagari_digital_masjid"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah di Nagari Digital Masjid bisa lihat kegiatan masjid secara berkala?",
        "entities": {"product_name": "nagari_digital_masjid"}
    },
    {
        "intent": "product_inquiry",
        "text": "Nagari Digital Masjid itu aplikasi seperti apa?",
        "entities": {"product_name": "nagari_digital_masjid"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bisa tidak saya gunakan GPS untuk cari musholla lewat Nagari Digital Masjid?",
        "entities": {"product_name": "nagari_digital_masjid"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah aplikasi Nagari Digital Masjid bisa membantu saya berdonasi ke masjid?",
        "entities": {"product_name": "nagari_digital_masjid"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bagaimana cara mengetahui profil sebuah masjid dari aplikasi Bank Nagari?",
        "entities": {"product_name": "nagari_digital_masjid"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya ingin lihat kegiatan mingguan masjid. Apakah bisa lewat Nagari Digital Masjid?",
        "entities": {"product_name": "nagari_digital_masjid"}
    },
    {
        "intent": "product_inquiry",
        "text": "Kalau ingin melihat foto-foto musholla, apakah bisa lewat Nagari Digital Masjid?",
        "entities": {"product_name": "nagari_digital_masjid"}
    },
    {
        "intent": "product_inquiry",
        "text": "Di mana saya bisa mendapatkan aplikasi Nagari Digital Masjid?",
        "entities": {"product_name": "nagari_digital_masjid"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah Bank Nagari menyediakan aplikasi khusus untuk informasi kegiatan masjid?",
        "entities": {"product_name": "nagari_digital_masjid"}
    },
    {
        "intent": "product_inquiry",
        "text": "Nagari Digital Masjid tersedia di Play Store atau App Store?",
        "entities": {"product_name": "nagari_digital_masjid"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apa manfaat menggunakan Nagari Digital Masjid dari Bank Nagari?",
        "entities": {"product_name": "nagari_digital_masjid"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya sedang mencari informasi tentang masjid. Apakah aplikasi Bank Nagari bisa membantu?",
        "entities": {"product_name": "nagari_digital_masjid"}
    },
    {
        "intent": "product_inquiry",
        "text": "Fitur QRIS di Nagari Digital Masjid untuk infaq itu bagaimana cara pakainya?",
        "entities": {"product_name": "nagari_digital_masjid"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah ada fitur pencarian masjid berbasis lokasi di Nagari Digital Masjid?",
        "entities": {"product_name": "nagari_digital_masjid"}
    },
    {
        "intent": "product_inquiry",
        "text": "Kalau saya ingin tahu jadwal adzan dan sholat, bisa lihat di Nagari Digital Masjid?",
        "entities": {"product_name": "nagari_digital_masjid"}
    },
    {
        "intent": "product_inquiry",
        "text": "Aplikasi apa dari Bank Nagari yang bisa bantu saya menemukan masjid?",
        "entities": {"product_name": "nagari_digital_masjid"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya ingin infak ke masjid secara digital, apakah Nagari Digital Masjid mendukung?",
        "entities": {"product_name": "nagari_digital_masjid"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apa saja kelebihan aplikasi Nagari Digital Masjid dibanding aplikasi lainnya?",
        "entities": {"product_name": "nagari_digital_masjid"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya ingin mengetahui detail masjid tertentu lewat HP, bisa pakai Nagari Digital Masjid?",
        "entities": {"product_name": "nagari_digital_masjid"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah fitur di Nagari Digital Masjid hanya untuk informasi atau juga bisa transaksi?",
        "entities": {"product_name": "nagari_digital_masjid"}
    },

    {
        "intent": "product_inquiry",
        "text": "Apa itu layanan TPE dari Bank Nagari?",
        "entities": {"product_name": "tpe_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya ingin tahu fungsi utama Terminal Perbankan Elektronik Bank Nagari.",
        "entities": {"product_name": "tpe_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apa saja jenis mesin yang tersedia dalam layanan TPE Bank Nagari?",
        "entities": {"product_name": "tpe_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah TPE Bank Nagari punya mesin CRM untuk tarik dan setor tunai?",
        "entities": {"product_name": "tpe_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Fitur apa saja yang ditawarkan oleh TPE Bank Nagari?",
        "entities": {"product_name": "tpe_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah saya bisa buka rekening lewat TPE Bank Nagari?",
        "entities": {"product_name": "tpe_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Kalau saya sudah jadi nasabah, bisa buka rekening baru lewat TPE Bank Nagari?",
        "entities": {"product_name": "tpe_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah saya bisa ganti kartu ATM lewat layanan TPE Bank Nagari?",
        "entities": {"product_name": "tpe_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "TPE Bank Nagari beroperasi jam berapa saja?",
        "entities": {"product_name": "tpe_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah TPE Bank Nagari buka setiap hari?",
        "entities": {"product_name": "tpe_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Kalau kartu ATM saya kadaluarsa, apakah bisa diganti gratis lewat TPE?",
        "entities": {"product_name": "tpe_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah semua nasabah bisa upgrade kartu ATM lewat TPE Bank Nagari?",
        "entities": {"product_name": "tpe_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apa saja jenis kartu ATM yang bisa diganti melalui TPE Bank Nagari?",
        "entities": {"product_name": "tpe_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Berapa biaya penggantian kartu ATM lewat TPE Bank Nagari?",
        "entities": {"product_name": "tpe_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah kartu ATM diberikan langsung saat pembukaan rekening di TPE?",
        "entities": {"product_name": "tpe_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Buku tabungan saya bisa diambil di mana setelah buka rekening lewat TPE Bank Nagari?",
        "entities": {"product_name": "tpe_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apa saja syarat pembukaan rekening di TPE Bank Nagari bagi calon nasabah?",
        "entities": {"product_name": "tpe_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya WNI berusia 20 tahun, apakah bisa buka rekening di TPE Bank Nagari?",
        "entities": {"product_name": "tpe_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Berapa setoran awal minimum untuk buka tabungan di TPE Bank Nagari?",
        "entities": {"product_name": "tpe_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Tabungan apa yang tersedia jika buka rekening melalui TPE Bank Nagari?",
        "entities": {"product_name": "tpe_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bagaimana proses setor tunai di mesin CRM Bank Nagari?",
        "entities": {"product_name": "tpe_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bisakah saya melakukan transaksi tanpa bantuan teller lewat TPE Bank Nagari?",
        "entities": {"product_name": "tpe_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Jika saya kehilangan kartu ATM, apakah bisa langsung ganti di TPE Bank Nagari?",
        "entities": {"product_name": "tpe_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Untuk ganti kartu ATM karena upgrade, biayanya berapa di TPE?",
        "entities": {"product_name": "tpe_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah saya perlu membawa kartu ATM lama saat ingin menggantinya di TPE?",
        "entities": {"product_name": "tpe_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Kalau saya nasabah lama, boleh tidak buka rekening baru di TPE Bank Nagari?",
        "entities": {"product_name": "tpe_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Kapan waktu yang tepat untuk datang ke TPE Bank Nagari agar bisa buka rekening?",
        "entities": {"product_name": "tpe_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Setoran selanjutnya setelah pembukaan rekening bisa dilakukan lewat mana saja?",
        "entities": {"product_name": "tpe_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah ada biaya admin bulanan untuk rekening yang dibuka di TPE Bank Nagari?",
        "entities": {"product_name": "tpe_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Jenis tabungan apa yang tersedia saat buka rekening di mesin TPE?",
        "entities": {"product_name": "tpe_bank_nagari"}
    },
    {
        "intent": "product_inquiry",
        "text": "Jika saya lupa bawa e-KTP, apakah tetap bisa buka rekening di TPE Bank Nagari?",
        "entities": {"product_name": "tpe_bank_nagari"}
    },

    {
        "intent": "product_inquiry",
        "text": "Apa itu Nagari Card dari Bank Nagari?",
        "entities": {"product_name": "nagari_card"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya ingin tahu kegunaan Nagari Card.",
        "entities": {"product_name": "nagari_card"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah Nagari Card bisa langsung digunakan tanpa aktivasi?",
        "entities": {"product_name": "nagari_card"}
    },
    {
        "intent": "product_inquiry",
        "text": "Nagari Card bisa digunakan di mana saja?",
        "entities": {"product_name": "nagari_card"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bisa kah saya memakai Nagari Card di tol dan parkir?",
        "entities": {"product_name": "nagari_card"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah kartu ini bisa digunakan untuk bayar di mini market seperti Indomaret atau Alfamart?",
        "entities": {"product_name": "nagari_card"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bagaimana cara melakukan top up saldo Nagari Card?",
        "entities": {"product_name": "nagari_card"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya ingin tahu di mana saja saya bisa isi saldo kartu Nagari.",
        "entities": {"product_name": "nagari_card"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah top up Nagari Card bisa dilakukan lewat aplikasi e-commerce?",
        "entities": {"product_name": "nagari_card"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya pengguna Tokopedia, bisa top up Nagari Card di sana?",
        "entities": {"product_name": "nagari_card"}
    },
    {
        "intent": "product_inquiry",
        "text": "Berapa minimal top up Nagari Card?",
        "entities": {"product_name": "nagari_card"}
    },
    {
        "intent": "product_inquiry",
        "text": "Berapa batas maksimum saldo yang bisa disimpan di Nagari Card?",
        "entities": {"product_name": "nagari_card"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah ada batas maksimal top up bulanan untuk Nagari Card?",
        "entities": {"product_name": "nagari_card"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya bukan nasabah Bank Nagari, apakah tetap bisa punya Nagari Card?",
        "entities": {"product_name": "nagari_card"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah Nagari Card hanya untuk nasabah saja?",
        "entities": {"product_name": "nagari_card"}
    },
    {
        "intent": "product_inquiry",
        "text": "Kalau kartu saya hilang, apakah bisa diblokir atau diganti?",
        "entities": {"product_name": "nagari_card"}
    },
    {
        "intent": "product_inquiry",
        "text": "Siapa yang bertanggung jawab kalau Nagari Card rusak atau disalahgunakan?",
        "entities": {"product_name": "nagari_card"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bagaimana cara mengembalikan sisa saldo jika saya tidak ingin memakai Nagari Card lagi?",
        "entities": {"product_name": "nagari_card"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah bisa menyerahkan kartu untuk tarik saldo yang tersisa?",
        "entities": {"product_name": "nagari_card"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah kartu Nagari Card pakai PIN saat transaksi?",
        "entities": {"product_name": "nagari_card"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apa transaksi dengan Nagari Card cukup tapping saja?",
        "entities": {"product_name": "nagari_card"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bagaimana cara cek saldo Nagari Card?",
        "entities": {"product_name": "nagari_card"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah saldo Nagari Card bisa nol?",
        "entities": {"product_name": "nagari_card"}
    },
    {
        "intent": "product_inquiry",
        "text": "Berapa saldo minimum yang wajib ada di Nagari Card?",
        "entities": {"product_name": "nagari_card"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah informasi mengenai Nagari Card bisa berubah sewaktu-waktu?",
        "entities": {"product_name": "nagari_card"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah Bank Nagari sering mengubah ketentuan penggunaan Nagari Card?",
        "entities": {"product_name": "nagari_card"}
    },
    {
        "intent": "product_inquiry",
        "text": "Kalau saya ingin berhenti memakai Nagari Card, apakah ada proses khusus?",
        "entities": {"product_name": "nagari_card"}
    },
    {
        "intent": "product_inquiry",
        "text": "Nagari Card termasuk jenis e-money bukan?",
        "entities": {"product_name": "nagari_card"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah Nagari Card bisa digunakan di merchant QRIS?",
        "entities": {"product_name": "nagari_card"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah transaksi dengan Nagari Card butuh tanda tangan?",
        "entities": {"product_name": "nagari_card"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bisakah saya menggunakan Nagari Card untuk bayar parkir bandara?",
        "entities": {"product_name": "nagari_card"}
    },

    {
        "intent": "product_inquiry",
        "text": "Apa itu kartu ATM atau debit giro dari Bank Nagari?",
        "entities": {"product_name": "kartu_atm_debit_giro"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya ingin tahu kegunaan dari kartu ATM giro Bank Nagari.",
        "entities": {"product_name": "kartu_atm_debit_giro"}
    },
    {
        "intent": "product_inquiry",
        "text": "Jenis kartu ATM giro apa saja yang tersedia di Bank Nagari?",
        "entities": {"product_name": "kartu_atm_debit_giro"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apa perbedaan kartu ATM giro Reguler dan Diamond?",
        "entities": {"product_name": "kartu_atm_debit_giro"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya ingin tahu limit transaksi kartu ATM giro Diamond.",
        "entities": {"product_name": "kartu_atm_debit_giro"}
    },
    {
        "intent": "product_inquiry",
        "text": "Berapa limit tarik tunai kartu ATM giro jenis reguler?",
        "entities": {"product_name": "kartu_atm_debit_giro"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah bisa setor tunai dengan kartu ATM giro Bank Nagari?",
        "entities": {"product_name": "kartu_atm_debit_giro"}
    },
    {
        "intent": "product_inquiry",
        "text": "Berapa maksimal transfer antar rekening dengan kartu giro Diamond?",
        "entities": {"product_name": "kartu_atm_debit_giro"}
    },
    {
        "intent": "product_inquiry",
        "text": "Kalau saya pakai kartu reguler, berapa maksimal transfer ke rekening lain di ATM?",
        "entities": {"product_name": "kartu_atm_debit_giro"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah kartu ATM giro bisa digunakan untuk belanja di EDC?",
        "entities": {"product_name": "kartu_atm_debit_giro"}
    },
    {
        "intent": "product_inquiry",
        "text": "Berapa maksimal belanja EDC dengan kartu Diamond?",
        "entities": {"product_name": "kartu_atm_debit_giro"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah limit transfer antar bank berbeda untuk jenis kartu reguler dan diamond?",
        "entities": {"product_name": "kartu_atm_debit_giro"}
    },
    {
        "intent": "product_inquiry",
        "text": "Berapa batas minimal dan maksimal transfer HVT dengan kartu ATM giro?",
        "entities": {"product_name": "kartu_atm_debit_giro"}
    },
    {
        "intent": "product_inquiry",
        "text": "Kartu debit giro ini bisa digunakan untuk transaksi di ATM dan EDC kan?",
        "entities": {"product_name": "kartu_atm_debit_giro"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah PIN kartu ATM giro sama dengan kartu debit tabungan?",
        "entities": {"product_name": "kartu_atm_debit_giro"}
    },
    {
        "intent": "product_inquiry",
        "text": "Limit pembayaran melalui ATM/CRM untuk kartu Diamond berapa ya?",
        "entities": {"product_name": "kartu_atm_debit_giro"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya ingin tahu apakah kartu debit giro instan dan biasa itu berbeda?",
        "entities": {"product_name": "kartu_atm_debit_giro"}
    },
    {
        "intent": "product_inquiry",
        "text": "Siapa saja yang bisa mendapatkan kartu ATM giro dari Bank Nagari?",
        "entities": {"product_name": "kartu_atm_debit_giro"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah nasabah baru giro bisa langsung memiliki kartu ATM giro?",
        "entities": {"product_name": "kartu_atm_debit_giro"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah wajib bawa bukti rekening giro untuk bisa mendapatkan kartu ini?",
        "entities": {"product_name": "kartu_atm_debit_giro"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya ingin tahu syarat untuk mendapatkan kartu ATM giro Bank Nagari.",
        "entities": {"product_name": "kartu_atm_debit_giro"}
    },
    {
        "intent": "product_inquiry",
        "text": "Kartu ini mendukung pembayaran dan pembelian ya?",
        "entities": {"product_name": "kartu_atm_debit_giro"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bisakah saya transfer ke bank lain pakai kartu giro Diamond?",
        "entities": {"product_name": "kartu_atm_debit_giro"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apa saja jenis transaksi yang didukung oleh kartu debit giro?",
        "entities": {"product_name": "kartu_atm_debit_giro"}
    },
    {
        "intent": "product_inquiry",
        "text": "Berapa rekening yang bisa dikaitkan dengan kartu Reguler?",
        "entities": {"product_name": "kartu_atm_debit_giro"}
    },
    {
        "intent": "product_inquiry",
        "text": "Kalau pakai kartu Diamond, bisa dikaitkan ke berapa rekening?",
        "entities": {"product_name": "kartu_atm_debit_giro"}
    },
    {
        "intent": "product_inquiry",
        "text": "Limit transaksi antar bank di NCM Personal untuk kartu ATM giro berapa?",
        "entities": {"product_name": "kartu_atm_debit_giro"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah ada batas transfer berbeda untuk NCM Corporate Pemda?",
        "entities": {"product_name": "kartu_atm_debit_giro"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya tertarik dengan kartu ATM giro, bisa jelaskan detail transaksinya?",
        "entities": {"product_name": "kartu_atm_debit_giro"}
    },
    {
        "intent": "product_inquiry",
        "text": "Fasilitas kartu ATM giro lebih unggul dari kartu debit biasa, benar?",
        "entities": {"product_name": "kartu_atm_debit_giro"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah transaksi pakai kartu ini bisa unlimited di NCM Personal?",
        "entities": {"product_name": "kartu_atm_debit_giro"}
    },

    {
        "intent": "product_inquiry",
        "text": "Berapa batas limit transaksi untuk kartu ATM Bank Nagari?",
        "entities": {"product_name": "limit_kartu_atm_debit"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya ingin tahu limit tarik tunai harian kartu debit Bank Nagari.",
        "entities": {"product_name": "limit_kartu_atm_debit"}
    },
    {
        "intent": "product_inquiry",
        "text": "Berapa maksimal tarik tunai di ATM untuk kartu Platinum?",
        "entities": {"product_name": "limit_kartu_atm_debit"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah limit setor tunai CRM berbeda antar jenis kartu?",
        "entities": {"product_name": "limit_kartu_atm_debit"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya pakai kartu Silver, berapa limit setor tunainya?",
        "entities": {"product_name": "limit_kartu_atm_debit"}
    },
    {
        "intent": "product_inquiry",
        "text": "Limit transfer antar rekening dengan kartu Gold berapa?",
        "entities": {"product_name": "limit_kartu_atm_debit"}
    },
    {
        "intent": "product_inquiry",
        "text": "Kalau saya pakai kartu Reguler, maksimal transfer ke sesama Bank Nagari berapa?",
        "entities": {"product_name": "limit_kartu_atm_debit"}
    },
    {
        "intent": "product_inquiry",
        "text": "Berapa batas transfer ke bank lain dengan kartu ATM Platinum?",
        "entities": {"product_name": "limit_kartu_atm_debit"}
    },
    {
        "intent": "product_inquiry",
        "text": "Limit transfer antar bank untuk kartu Silver apakah sama dengan Gold?",
        "entities": {"product_name": "limit_kartu_atm_debit"}
    },
    {
        "intent": "product_inquiry",
        "text": "Transfer HVT di NCM Personal bisa sampai berapa juta rupiah?",
        "entities": {"product_name": "limit_kartu_atm_debit"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya ingin tahu batas transfer HVT NCM Corporate.",
        "entities": {"product_name": "limit_kartu_atm_debit"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah transfer HVT untuk Pemda ada batasan tertentu?",
        "entities": {"product_name": "limit_kartu_atm_debit"}
    },
    {
        "intent": "product_inquiry",
        "text": "Limit maksimal SKN RTGS untuk NCM Corporate berapa ya?",
        "entities": {"product_name": "limit_kartu_atm_debit"}
    },
    {
        "intent": "product_inquiry",
        "text": "Berapa minimal dan maksimal transaksi RTGS?",
        "entities": {"product_name": "limit_kartu_atm_debit"}
    },
    {
        "intent": "product_inquiry",
        "text": "Untuk pembayaran dan pembelian, kartu Platinum bisa sampai berapa?",
        "entities": {"product_name": "limit_kartu_atm_debit"}
    },
    {
        "intent": "product_inquiry",
        "text": "Limit transaksi pembelian di kartu ATM Silver Bank Nagari berapa?",
        "entities": {"product_name": "limit_kartu_atm_debit"}
    },
    {
        "intent": "product_inquiry",
        "text": "Kalau pakai kartu Gold, maksimal pembelian harian di ATM berapa?",
        "entities": {"product_name": "limit_kartu_atm_debit"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah transaksi belanja EDC semua kartu dibatasi sama?",
        "entities": {"product_name": "limit_kartu_atm_debit"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya pakai kartu debit Reguler, berapa batas belanja via EDC?",
        "entities": {"product_name": "limit_kartu_atm_debit"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bisa dijelaskan berapa maksimal korelasi rekening untuk masing-masing kartu?",
        "entities": {"product_name": "limit_kartu_atm_debit"}
    },
    {
        "intent": "product_inquiry",
        "text": "Kartu Platinum bisa dikaitkan ke berapa rekening?",
        "entities": {"product_name": "limit_kartu_atm_debit"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya pakai kartu ATM Gold, hanya bisa satu rekening ya?",
        "entities": {"product_name": "limit_kartu_atm_debit"}
    },
    {
        "intent": "product_inquiry",
        "text": "Limit top up atau transfer bulanan kartu ATM Bank Nagari ada berapa?",
        "entities": {"product_name": "limit_kartu_atm_debit"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah NCM Personal punya batas transfer antar rekening?",
        "entities": {"product_name": "limit_kartu_atm_debit"}
    },
    {
        "intent": "product_inquiry",
        "text": "NCM Corporate bisa transfer antar rekening tanpa batas?",
        "entities": {"product_name": "limit_kartu_atm_debit"}
    },
    {
        "intent": "product_inquiry",
        "text": "Ada catatan khusus tentang limit kartu untuk Pemda?",
        "entities": {"product_name": "limit_kartu_atm_debit"}
    },
    {
        "intent": "product_inquiry",
        "text": "Transaksi antar bank di NCM Corporate apakah dibatasi?",
        "entities": {"product_name": "limit_kartu_atm_debit"}
    },
    {
        "intent": "product_inquiry",
        "text": "Kapan terakhir kali limit kartu ATM Bank Nagari diperbarui?",
        "entities": {"product_name": "limit_kartu_atm_debit"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah informasi limit ini berlaku mulai Januari 2022?",
        "entities": {"product_name": "limit_kartu_atm_debit"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya ingin tahu detail semua jenis kartu ATM dan limitnya.",
        "entities": {"product_name": "limit_kartu_atm_debit"}
    },

    {
        "intent": "product_inquiry",
        "text": "Apa itu layanan Nagari Portal Payment dari Bank Nagari?",
        "entities": {"product_name": "nagari_portal_payment"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bisa jelaskan fungsi utama dari sistem Nagari Portal Payment?",
        "entities": {"product_name": "nagari_portal_payment"}
    },
    {
        "intent": "product_inquiry",
        "text": "NPP itu digunakan untuk siapa saja ya?",
        "entities": {"product_name": "nagari_portal_payment"}
    },
    {
        "intent": "product_inquiry",
        "text": "Nagari Portal Payment ditujukan untuk mitra bank yang seperti apa?",
        "entities": {"product_name": "nagari_portal_payment"}
    },
    {
        "intent": "product_inquiry",
        "text": "Kalau saya mitra bank dan punya tagihan, apa bisa menggunakan Nagari Portal Payment?",
        "entities": {"product_name": "nagari_portal_payment"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah saya harus punya sistem sendiri untuk kelola tagihan kalau pakai NPP?",
        "entities": {"product_name": "nagari_portal_payment"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bagaimana proses data tagihan dimasukkan ke sistem NPP?",
        "entities": {"product_name": "nagari_portal_payment"}
    },
    {
        "intent": "product_inquiry",
        "text": "Data tagihan di Nagari Portal Payment diimpor secara manual atau otomatis?",
        "entities": {"product_name": "nagari_portal_payment"}
    },
    {
        "intent": "product_inquiry",
        "text": "Setelah tagihan dimasukkan ke NPP, nasabah bisa bayar di mana saja?",
        "entities": {"product_name": "nagari_portal_payment"}
    },
    {
        "intent": "product_inquiry",
        "text": "Nagari Portal Payment bisa menerima pembayaran dari seluruh channel Bank Nagari?",
        "entities": {"product_name": "nagari_portal_payment"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apa keunggulan dari sistem NPP untuk mitra Bank Nagari?",
        "entities": {"product_name": "nagari_portal_payment"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya ingin tahu fitur yang ditawarkan oleh Nagari Portal Payment.",
        "entities": {"product_name": "nagari_portal_payment"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah NPP punya fitur pengelolaan data pembayaran juga?",
        "entities": {"product_name": "nagari_portal_payment"}
    },
    {
        "intent": "product_inquiry",
        "text": "Fitur-fitur apa saja yang dimiliki oleh sistem NPP?",
        "entities": {"product_name": "nagari_portal_payment"}
    },
    {
        "intent": "product_inquiry",
        "text": "Dengan NPP, mitra bank bisa kelola tagihan dan pembayaran secara efisien?",
        "entities": {"product_name": "nagari_portal_payment"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya ingin tahu manfaat utama dari Nagari Portal Payment.",
        "entities": {"product_name": "nagari_portal_payment"}
    },
    {
        "intent": "product_inquiry",
        "text": "Nagari Portal Payment bisa digunakan untuk layanan pembayaran apa saja?",
        "entities": {"product_name": "nagari_portal_payment"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah sistem NPP cocok untuk institusi pendidikan yang ingin tagih iuran?",
        "entities": {"product_name": "nagari_portal_payment"}
    },
    {
        "intent": "product_inquiry",
        "text": "Kalau institusi saya tidak punya sistem tagihan, bisa tetap pakai NPP?",
        "entities": {"product_name": "nagari_portal_payment"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah Bank Nagari bantu mengelola data pembayaran mitra melalui NPP?",
        "entities": {"product_name": "nagari_portal_payment"}
    },
    {
        "intent": "product_inquiry",
        "text": "NPP itu sistem internal atau berbasis online?",
        "entities": {"product_name": "nagari_portal_payment"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bisakah saya memantau status pembayaran tagihan di NPP?",
        "entities": {"product_name": "nagari_portal_payment"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bagaimana cara mengakses atau mendaftar sebagai mitra NPP?",
        "entities": {"product_name": "nagari_portal_payment"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah pengguna perlu pelatihan untuk menggunakan Nagari Portal Payment?",
        "entities": {"product_name": "nagari_portal_payment"}
    },
    {
        "intent": "product_inquiry",
        "text": "Berapa lama proses integrasi data tagihan ke NPP?",
        "entities": {"product_name": "nagari_portal_payment"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apa saja delivery channel Bank Nagari yang bisa digunakan untuk bayar tagihan di NPP?",
        "entities": {"product_name": "nagari_portal_payment"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya pengguna Ollin, bisa bayar tagihan dari NPP juga?",
        "entities": {"product_name": "nagari_portal_payment"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah sistem ini bisa digunakan untuk tagihan air dan listrik?",
        "entities": {"product_name": "nagari_portal_payment"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apa saja jenis data pembayaran yang dapat dikelola oleh Nagari Portal Payment?",
        "entities": {"product_name": "nagari_portal_payment"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah tagihan dari koperasi atau lembaga kecil bisa masuk ke sistem NPP?",
        "entities": {"product_name": "nagari_portal_payment"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bagaimana cara kerja sistem pembayaran melalui NPP ini secara keseluruhan?",
        "entities": {"product_name": "nagari_portal_payment"}
    },

    {
        "intent": "product_inquiry",
        "text": "Apa itu Nagari Virtual Account dari Bank Nagari?",
        "entities": {"product_name": "nagari_virtual_account"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bisa dijelaskan fungsi utama dari layanan Nagari Virtual Account?",
        "entities": {"product_name": "nagari_virtual_account"}
    },
    {
        "intent": "product_inquiry",
        "text": "Nagari Virtual Account itu produk seperti apa ya?",
        "entities": {"product_name": "nagari_virtual_account"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya ingin tahu fitur dan manfaat dari Nagari Virtual Account.",
        "entities": {"product_name": "nagari_virtual_account"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apa tujuan dibuatnya Nagari Virtual Account ini?",
        "entities": {"product_name": "nagari_virtual_account"}
    },
    {
        "intent": "product_inquiry",
        "text": "Untuk apa kegunaan nomor virtual account di layanan ini?",
        "entities": {"product_name": "nagari_virtual_account"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah Nagari Virtual Account digunakan sebagai identitas mitra bisnis?",
        "entities": {"product_name": "nagari_virtual_account"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apa manfaat dari mencantumkan nomor virtual account sebagai identitas pelanggan?",
        "entities": {"product_name": "nagari_virtual_account"}
    },
    {
        "intent": "product_inquiry",
        "text": "Layanan virtual account ini bisa digunakan oleh siapa saja?",
        "entities": {"product_name": "nagari_virtual_account"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah produk ini cocok untuk perorangan juga atau hanya untuk perusahaan?",
        "entities": {"product_name": "nagari_virtual_account"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah pemerintah daerah juga bisa menggunakan Nagari Virtual Account?",
        "entities": {"product_name": "nagari_virtual_account"}
    },
    {
        "intent": "product_inquiry",
        "text": "Siapa saja pengguna yang disasar oleh layanan Nagari Virtual Account ini?",
        "entities": {"product_name": "nagari_virtual_account"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya ingin tahu bagaimana Nagari Virtual Account membantu mengelola arus kas masuk.",
        "entities": {"product_name": "nagari_virtual_account"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apa benar Nagari Virtual Account dapat mengidentifikasi transaksi masuk dengan lebih akurat?",
        "entities": {"product_name": "nagari_virtual_account"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apa keuntungan utama bagi perusahaan yang menggunakan virtual account ini?",
        "entities": {"product_name": "nagari_virtual_account"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya ingin tahu cara kerja virtual account di Bank Nagari.",
        "entities": {"product_name": "nagari_virtual_account"}
    },
    {
        "intent": "product_inquiry",
        "text": "Dengan adanya Nagari Virtual Account, apakah pelanggan bisa punya ID transaksi unik?",
        "entities": {"product_name": "nagari_virtual_account"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah nomor virtual account bisa membedakan transaksi antar pelanggan?",
        "entities": {"product_name": "nagari_virtual_account"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah setiap pelanggan akan memiliki nomor virtual account tersendiri?",
        "entities": {"product_name": "nagari_virtual_account"}
    },
    {
        "intent": "product_inquiry",
        "text": "Adakah contoh penggunaan Nagari Virtual Account dalam sistem pembayaran pelanggan?",
        "entities": {"product_name": "nagari_virtual_account"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya ingin tahu bagaimana virtual account ini membantu pengelolaan keuangan perusahaan.",
        "entities": {"product_name": "nagari_virtual_account"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah virtual account ini bisa terhubung dengan sistem keuangan internal perusahaan?",
        "entities": {"product_name": "nagari_virtual_account"}
    },
    {
        "intent": "product_inquiry",
        "text": "Layanan ini membantu rekonsiliasi pembayaran perusahaan nggak?",
        "entities": {"product_name": "nagari_virtual_account"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah ada fitur real-time tracking transaksi untuk virtual account?",
        "entities": {"product_name": "nagari_virtual_account"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bank Nagari punya solusi virtual account seperti bank besar lainnya?",
        "entities": {"product_name": "nagari_virtual_account"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah saya harus menjadi nasabah bisnis dulu untuk bisa pakai virtual account?",
        "entities": {"product_name": "nagari_virtual_account"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah virtual account ini bisa diintegrasikan ke sistem pembayaran online?",
        "entities": {"product_name": "nagari_virtual_account"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya penasaran, apakah virtual account Bank Nagari mendukung pembayaran otomatis?",
        "entities": {"product_name": "nagari_virtual_account"}
    },
    {
        "intent": "product_inquiry",
        "text": "Ada biaya tambahan nggak untuk pakai layanan Nagari Virtual Account ini?",
        "entities": {"product_name": "nagari_virtual_account"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bagaimana saya bisa mendaftar untuk mendapatkan Nagari Virtual Account?",
        "entities": {"product_name": "nagari_virtual_account"}
    },

    {
        "intent": "product_inquiry",
        "text": "Apa itu layanan Host to Host SP2D Online dari Bank Nagari?",
        "entities": {"product_name": "host_to_host_sp2d_online"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bisa jelaskan bagaimana sistem Host to Host SP2D Online bekerja?",
        "entities": {"product_name": "host_to_host_sp2d_online"}
    },
    {
        "intent": "product_inquiry",
        "text": "SP2D Online Host to Host itu apa fungsinya ya?",
        "entities": {"product_name": "host_to_host_sp2d_online"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah layanan Host to Host SP2D Online ini menggantikan proses manual pencairan dana?",
        "entities": {"product_name": "host_to_host_sp2d_online"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bagaimana Host to Host SP2D Online membantu proses pencairan SP2D?",
        "entities": {"product_name": "host_to_host_sp2d_online"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah Host to Host SP2D bisa mempercepat pencairan dana SP2D?",
        "entities": {"product_name": "host_to_host_sp2d_online"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah dokumen fisik masih diperlukan dalam sistem Host to Host SP2D?",
        "entities": {"product_name": "host_to_host_sp2d_online"}
    },
    {
        "intent": "product_inquiry",
        "text": "Layanan ini terhubung ke sistem Pemda secara langsung ya?",
        "entities": {"product_name": "host_to_host_sp2d_online"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apa keuntungan menggunakan Host to Host SP2D Online dibanding manual?",
        "entities": {"product_name": "host_to_host_sp2d_online"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah SP2D online ini mengurangi risiko kesalahan pencairan dana?",
        "entities": {"product_name": "host_to_host_sp2d_online"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bagaimana sistem ini mengurangi risiko selisih bayar di bank?",
        "entities": {"product_name": "host_to_host_sp2d_online"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah pencairan SP2D sekarang bisa dipastikan tepat waktu dengan layanan ini?",
        "entities": {"product_name": "host_to_host_sp2d_online"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah pemerintah bisa pantau SP2D real-time dengan Host to Host?",
        "entities": {"product_name": "host_to_host_sp2d_online"}
    },
    {
        "intent": "product_inquiry",
        "text": "Layanan ini bisa dilihat progress SP2D-nya secara langsung ya?",
        "entities": {"product_name": "host_to_host_sp2d_online"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apa saja kelebihan dari layanan SP2D Online Host to Host ini?",
        "entities": {"product_name": "host_to_host_sp2d_online"}
    },
    {
        "intent": "product_inquiry",
        "text": "Pemerintah daerah mana saja yang sudah bekerja sama dengan layanan ini?",
        "entities": {"product_name": "host_to_host_sp2d_online"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah Pemprov Sumbar sudah menggunakan Host to Host SP2D?",
        "entities": {"product_name": "host_to_host_sp2d_online"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah Pemerintah Kabupaten Agam termasuk mitra SP2D Online ini?",
        "entities": {"product_name": "host_to_host_sp2d_online"}
    },
    {
        "intent": "product_inquiry",
        "text": "Kota Padang termasuk yang sudah implementasi Host to Host SP2D ya?",
        "entities": {"product_name": "host_to_host_sp2d_online"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah Kabupaten Pesisir Selatan sudah menggunakan Host to Host SP2D?",
        "entities": {"product_name": "host_to_host_sp2d_online"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah layanan ini tersedia untuk semua pemerintah daerah di Sumatera Barat?",
        "entities": {"product_name": "host_to_host_sp2d_online"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah mitra layanan SP2D Online bisa bertambah dari luar Sumbar?",
        "entities": {"product_name": "host_to_host_sp2d_online"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah layanan ini bisa digunakan oleh instansi pemerintah pusat juga?",
        "entities": {"product_name": "host_to_host_sp2d_online"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bagaimana prosedur untuk integrasi sistem SP2D Pemda dengan Bank Nagari?",
        "entities": {"product_name": "host_to_host_sp2d_online"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya ingin tahu cara kerja layanan Host to Host SP2D Online secara teknis.",
        "entities": {"product_name": "host_to_host_sp2d_online"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah sistem Host to Host ini aman untuk pencairan dana SP2D?",
        "entities": {"product_name": "host_to_host_sp2d_online"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah layanan SP2D Online ini sudah berjalan secara penuh?",
        "entities": {"product_name": "host_to_host_sp2d_online"}
    },
    {
        "intent": "product_inquiry",
        "text": "Ada biaya tambahan untuk integrasi layanan Host to Host SP2D ini?",
        "entities": {"product_name": "host_to_host_sp2d_online"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah fitur real-time pada Host to Host bisa diakses dari dashboard pemda?",
        "entities": {"product_name": "host_to_host_sp2d_online"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya tertarik untuk tahu bagaimana implementasi SP2D Online di lapangan.",
        "entities": {"product_name": "host_to_host_sp2d_online"}
    },

    {
        "intent": "product_inquiry",
        "text": "Apa itu layanan SMS Banking Bank Nagari?",
        "entities": {"product_name": "sms_banking"}
    },
    {
        "intent": "product_inquiry",
        "text": "SMS Banking Nagari itu fungsinya untuk apa ya?",
        "entities": {"product_name": "sms_banking"}
    },
    {
        "intent": "product_inquiry",
        "text": "Jelaskan layanan SMS Banking dari Bank Nagari.",
        "entities": {"product_name": "sms_banking"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya ingin tahu apa yang bisa dilakukan dengan SMS Banking.",
        "entities": {"product_name": "sms_banking"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apa saja fitur yang tersedia dalam layanan SMS Banking?",
        "entities": {"product_name": "sms_banking"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bisa cek saldo pakai SMS Banking Bank Nagari?",
        "entities": {"product_name": "sms_banking"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah bisa transfer uang lewat SMS Banking?",
        "entities": {"product_name": "sms_banking"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bisa lihat mutasi rekening melalui SMS Banking?",
        "entities": {"product_name": "sms_banking"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apa itu fitur inquiry statement di SMS Banking?",
        "entities": {"product_name": "sms_banking"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apa saja jenis transaksi yang bisa dilakukan lewat SMS Banking?",
        "entities": {"product_name": "sms_banking"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bagaimana cara mendaftar SMS Banking Bank Nagari?",
        "entities": {"product_name": "sms_banking"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apa syarat untuk bisa menggunakan SMS Banking?",
        "entities": {"product_name": "sms_banking"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah harus punya ATM Bank Nagari untuk daftar SMS Banking?",
        "entities": {"product_name": "sms_banking"}
    },
    {
        "intent": "product_inquiry",
        "text": "Di mana saya bisa daftar SMS Banking?",
        "entities": {"product_name": "sms_banking"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bisa daftar SMS Banking lewat aplikasi Ollin?",
        "entities": {"product_name": "sms_banking"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah layanan SMS Banking tersedia untuk semua nasabah?",
        "entities": {"product_name": "sms_banking"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah rekening perusahaan bisa pakai SMS Banking?",
        "entities": {"product_name": "sms_banking"}
    },
    {
        "intent": "product_inquiry",
        "text": "Perlu aplikasi khusus tidak untuk SMS Banking?",
        "entities": {"product_name": "sms_banking"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah SMS Banking pakai pulsa atau internet?",
        "entities": {"product_name": "sms_banking"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apa bedanya SMS Banking dengan Mobile Banking?",
        "entities": {"product_name": "sms_banking"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah transaksi di SMS Banking dikenakan biaya?",
        "entities": {"product_name": "sms_banking"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya punya rekening di Bank Nagari, apakah otomatis bisa pakai SMS Banking?",
        "entities": {"product_name": "sms_banking"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apa saja informasi yang bisa diakses dari SMS Banking?",
        "entities": {"product_name": "sms_banking"}
    },
    {
        "intent": "product_inquiry",
        "text": "SMS Banking mendukung transfer ke bank lain juga tidak?",
        "entities": {"product_name": "sms_banking"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah SMS Banking bisa digunakan di semua jenis handphone?",
        "entities": {"product_name": "sms_banking"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah layanan SMS Banking aktif 24 jam?",
        "entities": {"product_name": "sms_banking"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah transaksi SMS Banking aman?",
        "entities": {"product_name": "sms_banking"}
    },
    {
        "intent": "product_inquiry",
        "text": "Butuh sinyal atau jaringan tertentu untuk pakai SMS Banking?",
        "entities": {"product_name": "sms_banking"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah SMS Banking bisa digunakan di luar negeri?",
        "entities": {"product_name": "sms_banking"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bisa ubah nomor HP SMS Banking setelah daftar?",
        "entities": {"product_name": "sms_banking"}
    },

    {
        "intent": "product_inquiry",
        "text": "Apa itu layanan Nagari Cash Management dari Bank Nagari?",
        "entities": {"product_name": "nagari_cash_management"}
    },
    {
        "intent": "product_inquiry",
        "text": "Jelaskan NCM dari Bank Nagari.",
        "entities": {"product_name": "nagari_cash_management"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apa saja yang bisa dilakukan melalui Nagari Cash Management?",
        "entities": {"product_name": "nagari_cash_management"}
    },
    {
        "intent": "product_inquiry",
        "text": "Fitur apa saja yang tersedia di NCM Bank Nagari?",
        "entities": {"product_name": "nagari_cash_management"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah NCM bisa untuk melihat saldo dan informasi deposito?",
        "entities": {"product_name": "nagari_cash_management"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah bisa melakukan transfer antar bank lewat layanan NCM?",
        "entities": {"product_name": "nagari_cash_management"}
    },
    {
        "intent": "product_inquiry",
        "text": "NCM Bank Nagari mendukung transfer antar rekening?",
        "entities": {"product_name": "nagari_cash_management"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah saya bisa mengakses cek dan bilyet giro lewat Nagari Cash Management?",
        "entities": {"product_name": "nagari_cash_management"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bisa digunakan untuk apa saja layanan Nagari Cash Management?",
        "entities": {"product_name": "nagari_cash_management"}
    },
    {
        "intent": "product_inquiry",
        "text": "Fitur payroll tersedia juga di NCM?",
        "entities": {"product_name": "nagari_cash_management"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bisakah saya melakukan pembayaran tagihan lewat NCM?",
        "entities": {"product_name": "nagari_cash_management"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apa itu fitur multi biller dalam layanan NCM?",
        "entities": {"product_name": "nagari_cash_management"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah nasabah perorangan bisa menggunakan Nagari Cash Management?",
        "entities": {"product_name": "nagari_cash_management"}
    },
    {
        "intent": "product_inquiry",
        "text": "Saya bukan perusahaan, apakah tetap bisa pakai NCM?",
        "entities": {"product_name": "nagari_cash_management"}
    },
    {
        "intent": "product_inquiry",
        "text": "Untuk siapa saja layanan NCM ini ditujukan?",
        "entities": {"product_name": "nagari_cash_management"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah NCM hanya untuk nasabah corporate?",
        "entities": {"product_name": "nagari_cash_management"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah perorangan bisa akses fitur NCM yang lengkap seperti perusahaan?",
        "entities": {"product_name": "nagari_cash_management"}
    },
    {
        "intent": "product_inquiry",
        "text": "NCM itu aplikasi atau berbasis web?",
        "entities": {"product_name": "nagari_cash_management"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apa keuntungan menggunakan layanan NCM untuk perusahaan?",
        "entities": {"product_name": "nagari_cash_management"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah saya bisa melihat rekap pengeluaran cek/BG lewat NCM?",
        "entities": {"product_name": "nagari_cash_management"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apa perbedaan NCM Personal dan Corporate?",
        "entities": {"product_name": "nagari_cash_management"}
    },
    {
        "intent": "product_inquiry",
        "text": "NCM mendukung transaksi digital apa saja?",
        "entities": {"product_name": "nagari_cash_management"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah layanan NCM real-time atau batch processing?",
        "entities": {"product_name": "nagari_cash_management"}
    },
    {
        "intent": "product_inquiry",
        "text": "NCM Bank Nagari bisa digunakan untuk transaksi 24 jam?",
        "entities": {"product_name": "nagari_cash_management"}
    },
    {
        "intent": "product_inquiry",
        "text": "Adakah fitur pelaporan transaksi keuangan di NCM?",
        "entities": {"product_name": "nagari_cash_management"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apa saja kemudahan yang ditawarkan oleh Nagari Cash Management?",
        "entities": {"product_name": "nagari_cash_management"}
    },
    {
        "intent": "product_inquiry",
        "text": "Bisakah NCM digunakan di mobile phone?",
        "entities": {"product_name": "nagari_cash_management"}
    },
    {
        "intent": "product_inquiry",
        "text": "Nagari Cash Management cocok digunakan untuk jenis usaha apa saja?",
        "entities": {"product_name": "nagari_cash_management"}
    },
    {
        "intent": "product_inquiry",
        "text": "Apakah NCM aman digunakan untuk transaksi besar?",
        "entities": {"product_name": "nagari_cash_management"}
    },
    {
        "intent": "product_inquiry",
        "text": "Ada pelatihan atau panduan khusus untuk pengguna baru NCM?",
        "entities": {"product_name": "nagari_cash_management"}
    },

    # Produk KCU Simamak
    {"text": "Apa itu KCU Simamak?", "intent": "product_inquiry",
        "entities": {"product_name": "kcu_simamak"}},
    {"text": "Apa yang dimaksud dengan KCU Simamak?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_simamak"}},
    {"text": "KCU Simamak itu apa sih?", "intent": "product_inquiry",
        "entities": {"product_name": "kcu_simamak"}},
    {"text": "Bisa jelaskan lebih lanjut tentang KCU Simamak?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_simamak"}},
    {"text": "Apa tujuan utama dari KCU Simamak?", "intent": "product_inquiry",
        "entities": {"product_name": "kcu_simamak"}},
    {"text": "Apa saja manfaat yang diberikan oleh KCU Simamak?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_simamak"}},
    {"text": "Bagaimana cara kerja KCU Simamak?", "intent": "product_inquiry",
        "entities": {"product_name": "kcu_simamak"}},
    {"text": "KCU Simamak, siapa saja yang dapat mengaksesnya?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_simamak"}},
    {"text": "Apa saja keuntungan menggunakan KCU Simamak?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_simamak"}},

    {"text": "Apa keuntungan dari KCU Simamak?", "intent": "product_inquiry",
        "entities": {"product_name": "kcu_simamak"}},
    {"text": "Apa keuntungan utama dari KCU Simamak?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_simamak"}},
    {"text": "Apa saja manfaat yang diberikan oleh KCU Simamak?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_simamak"}},
    {"text": "Kenapa memilih KCU Simamak? Apa saja keuntungannya?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_simamak"}},
    {"text": "Apa saja keuntungan dari bergabung dengan KCU Simamak?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_simamak"}},
    {"text": "Bagaimana KCU Simamak memberikan manfaat bagi anggotanya?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_simamak"}},
    {"text": "Apa keuntungan finansial yang didapat dari KCU Simamak?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_simamak"}},
    {"text": "Apa saja benefit yang bisa didapatkan dari KCU Simamak?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_simamak"}},
    {"text": "Apa keuntungan utama yang ditawarkan oleh KCU Simamak?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_simamak"}},

    {"text": "Apa saja syarat KCU Simamak?", "intent": "product_inquiry",
        "entities": {"product_name": "kcu_simamak"}},
    {"text": "Apa saja syarat untuk bergabung dengan KCU Simamak?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_simamak"}},
    {"text": "Apa persyaratan untuk menjadi anggota KCU Simamak?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_simamak"}},
    {"text": "Syarat apa saja yang diperlukan untuk membuka akun di KCU Simamak?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_simamak"}},
    {"text": "Apa saja ketentuan untuk bisa bergabung dengan KCU Simamak?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_simamak"}},
    {"text": "Bagaimana cara memenuhi syarat untuk KCU Simamak?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_simamak"}},
    {"text": "Apa saja dokumen yang diperlukan untuk bergabung dengan KCU Simamak?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_simamak"}},
    {"text": "Apa saja syarat yang harus dipenuhi untuk menjadi anggota KCU Simamak?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_simamak"}},
    {"text": "Apa saja persyaratan umum untuk KCU Simamak?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_simamak"}},

    # Produk KKB
    {"text": "Apa itu KKB?", "intent": "product_inquiry",
        "entities": {"product_name": "kkb"}},
    {"text": "Apa yang dimaksud dengan KKB?",
        "intent": "product_inquiry", "entities": {"product_name": "kkb"}},
    {"text": "KKB itu apa sih?", "intent": "product_inquiry",
        "entities": {"product_name": "kkb"}},
    {"text": "Bisa jelaskan lebih lanjut tentang KKB?",
        "intent": "product_inquiry", "entities": {"product_name": "kkb"}},
    {"text": "Apa tujuan utama dari KKB?", "intent": "product_inquiry",
        "entities": {"product_name": "kkb"}},
    {"text": "Apa saja manfaat yang diberikan oleh KKB?",
        "intent": "product_inquiry", "entities": {"product_name": "kkb"}},
    {"text": "Bagaimana cara kerja KKB?", "intent": "product_inquiry",
        "entities": {"product_name": "kkb"}},
    {"text": "KKB, siapa saja yang bisa mengajukan?",
        "intent": "product_inquiry", "entities": {"product_name": "kkb"}},
    {"text": "Apa saja keuntungan menggunakan KKB?",
        "intent": "product_inquiry", "entities": {"product_name": "kkb"}},

    {"text": "Apa keuntungan dari KKB?", "intent": "product_inquiry",
        "entities": {"product_name": "kkb"}},
    {"text": "Apa keuntungan utama dari KKB?",
        "intent": "product_inquiry", "entities": {"product_name": "kkb"}},
    {"text": "Apa saja keuntungan yang bisa didapatkan dari KKB?",
        "intent": "product_inquiry", "entities": {"product_name": "kkb"}},
    {"text": "Kenapa memilih KKB? Apa saja manfaatnya?",
        "intent": "product_inquiry", "entities": {"product_name": "kkb"}},
    {"text": "Apa saja keuntungan dari memiliki KKB?",
        "intent": "product_inquiry", "entities": {"product_name": "kkb"}},
    {"text": "Bagaimana KKB memberikan keuntungan bagi peminjam?",
        "intent": "product_inquiry", "entities": {"product_name": "kkb"}},
    {"text": "Apa keuntungan finansial yang didapat dari KKB?",
        "intent": "product_inquiry", "entities": {"product_name": "kkb"}},
    {"text": "Apa saja manfaat yang bisa didapatkan dengan KKB?",
        "intent": "product_inquiry", "entities": {"product_name": "kkb"}},
    {"text": "Apa keuntungan yang akan Anda dapatkan jika memilih KKB?",
        "intent": "product_inquiry", "entities": {"product_name": "kkb"}},

    {"text": "Apa saja syarat KKB?", "intent": "product_inquiry",
        "entities": {"product_name": "kkb"}},
    {"text": "Apa syarat untuk mengajukan KKB?",
        "intent": "product_inquiry", "entities": {"product_name": "kkb"}},
    {"text": "Apa saja persyaratan untuk mengajukan KKB?",
        "intent": "product_inquiry", "entities": {"product_name": "kkb"}},
    {"text": "Syarat apa saja yang diperlukan untuk mendapatkan KKB?",
        "intent": "product_inquiry", "entities": {"product_name": "kkb"}},
    {"text": "Apa saja ketentuan yang perlu dipenuhi untuk KKB?",
        "intent": "product_inquiry", "entities": {"product_name": "kkb"}},
    {"text": "Bagaimana cara memenuhi syarat untuk mengajukan KKB?",
        "intent": "product_inquiry", "entities": {"product_name": "kkb"}},
    {"text": "Apa saja dokumen yang diperlukan untuk mengajukan KKB?",
        "intent": "product_inquiry", "entities": {"product_name": "kkb"}},
    {"text": "Apa saja syarat yang harus dipenuhi untuk mengajukan KKB?",
        "intent": "product_inquiry", "entities": {"product_name": "kkb"}},
    {"text": "Apa persyaratan utama untuk mengajukan KKB?",
        "intent": "product_inquiry", "entities": {"product_name": "kkb"}},

    # Produk KPR FLPP
    {"text": "Apa itu KPR FLPP?", "intent": "product_inquiry",
        "entities": {"product_name": "kpr_flpp"}},
    {"text": "Apa yang dimaksud dengan KPR FLPP?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp"}},
    {"text": "KPR FLPP itu apa sih?", "intent": "product_inquiry",
        "entities": {"product_name": "kpr_flpp"}},
    {"text": "Bisa jelaskan lebih lanjut tentang KPR FLPP?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp"}},
    {"text": "Apa tujuan utama dari KPR FLPP?", "intent": "product_inquiry",
        "entities": {"product_name": "kpr_flpp"}},
    {"text": "Apa saja manfaat yang diberikan oleh KPR FLPP?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp"}},
    {"text": "Bagaimana cara kerja KPR FLPP?", "intent": "product_inquiry",
        "entities": {"product_name": "kpr_flpp"}},
    {"text": "KPR FLPP, siapa saja yang bisa mengajukan?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp"}},
    {"text": "Apa saja keuntungan menggunakan KPR FLPP?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp"}},

    {"text": "Apa saja keuntungan dari KPR FLPP?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp"}},
    {"text": "Apa keuntungan utama dari KPR FLPP?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp"}},
    {"text": "Apa saja keuntungan yang bisa didapatkan dari KPR FLPP?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp"}},
    {"text": "Kenapa memilih KPR FLPP? Apa saja manfaatnya?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp"}},
    {"text": "Apa saja keuntungan dari memiliki KPR FLPP?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp"}},
    {"text": "Bagaimana KPR FLPP memberikan keuntungan bagi peminjam?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp"}},
    {"text": "Apa keuntungan finansial yang didapat dari KPR FLPP?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp"}},
    {"text": "Apa saja manfaat yang bisa didapatkan dengan KPR FLPP?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp"}},
    {"text": "Apa keuntungan yang akan Anda dapatkan jika memilih KPR FLPP?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp"}},

    {"text": "Apa syarat untuk KPR FLPP?", "intent": "product_inquiry",
        "entities": {"product_name": "kpr_flpp"}},
    {"text": "Apa syarat untuk mengajukan KPR FLPP?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp"}},
    {"text": "Apa saja persyaratan untuk mengajukan KPR FLPP?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp"}},
    {"text": "Syarat apa saja yang diperlukan untuk mendapatkan KPR FLPP?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp"}},
    {"text": "Apa saja ketentuan yang perlu dipenuhi untuk KPR FLPP?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp"}},
    {"text": "Bagaimana cara memenuhi syarat untuk mengajukan KPR FLPP?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp"}},
    {"text": "Apa saja dokumen yang diperlukan untuk mengajukan KPR FLPP?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp"}},
    {"text": "Apa saja syarat yang harus dipenuhi untuk mengajukan KPR FLPP?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp"}},
    {"text": "Apa persyaratan utama untuk mengajukan KPR FLPP?",
        "intent": "product_inquiry", "entities": {"product_name": "kpr_flpp"}},

    {
        "text": "Apa itu Kredit Cicilan Uang Umum dari Bank Nagari?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_umum"}
    },
    {
        "text": "KCU Umum di Bank Nagari itu kegunaannya untuk apa ya?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_umum"}
    },
    {
        "text": "Siapa saja yang bisa mengajukan KCU Umum di Bank Nagari?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_umum"}
    },
    {
        "text": "Apakah KCU Umum bisa diajukan oleh pegawai BUMN?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_umum"}
    },
    {
        "text": "Apakah anggota TNI juga bisa menggunakan fasilitas KCU Umum?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_umum"}
    },
    {
        "text": "Kredit KCU Umum cocok untuk kebutuhan konsumtif apa saja?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_umum"}
    },
    {
        "text": "Berapa lama tenor kredit yang tersedia di KCU Umum?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_umum"}
    },
    {
        "text": "Apakah jangka waktu KCU Umum bisa sampai 20 tahun?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_umum"}
    },
    {
        "text": "Berapa besar plafon kredit yang ditawarkan dalam program KCU Umum?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_umum"}
    },
    {
        "text": "Bagaimana cara menentukan plafon kredit untuk KCU Umum?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_umum"}
    },
    {
        "text": "Apakah penghasilan bulanan mempengaruhi jumlah kredit di KCU Umum?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_umum"}
    },
    {
        "text": "Bagaimana sistem bunga yang digunakan di produk KCU Umum?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_umum"}
    },
    {
        "text": "Apa saja jenis suku bunga dalam KCU Umum Bank Nagari?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_umum"}
    },
    {
        "text": "Apakah KCU Umum menggunakan bunga flat atau anuitas?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_umum"}
    },
    {
        "text": "Bagaimana sistem sliding bunga pada KCU Umum?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_umum"}
    },
    {
        "text": "Apakah biaya pengajuan KCU Umum tergolong ringan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_umum"}
    },
    {
        "text": "Apa saja syarat untuk bisa mengajukan KCU Umum?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_umum"}
    },
    {
        "text": "Dokumen apa yang harus dilengkapi untuk mengajukan KCU Umum?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_umum"}
    },
    {
        "text": "Apakah saya perlu menyertakan SK Pengangkatan saat ajukan KCU Umum?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_umum"}
    },
    {
        "text": "Apakah slip gaji terbaru wajib dilampirkan untuk KCU Umum?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_umum"}
    },
    {
        "text": "Kartu Taspen diperlukan untuk syarat KCU Umum?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_umum"}
    },
    {
        "text": "Perlu surat kuasa potong gaji juga ya untuk KCU Umum?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_umum"}
    },
    {
        "text": "Apakah pemohon harus mengisi aplikasi kredit untuk KCU Umum?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_umum"}
    },
    {
        "text": "Saya PNS, apakah bisa mengajukan KCU Umum tanpa agunan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_umum"}
    },
    {
        "text": "Kapan saya perlu menyertakan agunan untuk KCU Umum?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_umum"}
    },
    {
        "text": "Apakah pegawai BUMD bisa mendapatkan KCU Umum?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_umum"}
    },
    {
        "text": "Apa yang membedakan KCU Umum dengan pinjaman pribadi biasa?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_umum"}
    },
    {
        "text": "Berapa maksimal kredit yang bisa saya ajukan lewat KCU Umum?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_umum"}
    },
    {
        "text": "Apa saja kelebihan dari KCU Umum Bank Nagari dibanding produk serupa?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_umum"}
    },
    {
        "text": "Saya butuh kredit konsumtif, apakah KCU Umum bisa jadi solusi?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_umum"}
    },
    {
        "text": "Apakah KCU Umum cocok untuk pegawai aktif dan pensiunan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_umum"}
    },
    {
        "text": "Apa saja ketentuan penting yang berlaku pada program KCU Umum ini?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_umum"}
    },
    {
        "text": "Jika saya memenuhi semua syarat, berapa lama proses KCU Umum disetujui?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_umum"}
    },

    # Produk KCU Pensiunan Pegawai
    {"text": "Apa itu KCU Pensiunan Pegawai?", "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pensiunan_pegawai"}},
    {"text": "Apa yang dimaksud dengan KCU Pensiunan Pegawai?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_pensiunan_pegawai"}},
    {"text": "KCU Pensiunan Pegawai itu apa sih?", "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pensiunan_pegawai"}},
    {"text": "Bisa jelaskan lebih lanjut tentang KCU Pensiunan Pegawai?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_pensiunan_pegawai"}},
    {"text": "Apa tujuan utama dari KCU Pensiunan Pegawai?", "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pensiunan_pegawai"}},
    {"text": "Apa saja manfaat yang diberikan oleh KCU Pensiunan Pegawai?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_pensiunan_pegawai"}},
    {"text": "Bagaimana cara kerja KCU Pensiunan Pegawai?", "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pensiunan_pegawai"}},
    {"text": "KCU Pensiunan Pegawai, siapa saja yang bisa mengaksesnya?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_pensiunan_pegawai"}},
    {"text": "Apa saja keuntungan menggunakan KCU Pensiunan Pegawai?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_pensiunan_pegawai"}},

    {"text": "Apa keuntungan dari KCU Pensiunan Pegawai?", "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pensiunan_pegawai"}},
    {"text": "Apa keuntungan utama dari KCU Pensiunan Pegawai?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_pensiunan_pegawai"}},
    {"text": "Apa saja keuntungan yang bisa didapatkan dari KCU Pensiunan Pegawai?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_pensiunan_pegawai"}},
    {"text": "Kenapa memilih KCU Pensiunan Pegawai? Apa saja manfaatnya?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_pensiunan_pegawai"}},
    {"text": "Apa saja keuntungan dari bergabung dengan KCU Pensiunan Pegawai?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_pensiunan_pegawai"}},
    {"text": "Bagaimana KCU Pensiunan Pegawai memberikan manfaat bagi anggotanya?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_pensiunan_pegawai"}},
    {"text": "Apa keuntungan finansial yang didapat dari KCU Pensiunan Pegawai?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_pensiunan_pegawai"}},
    {"text": "Apa saja benefit yang bisa didapatkan dari KCU Pensiunan Pegawai?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_pensiunan_pegawai"}},
    {"text": "Apa keuntungan utama yang ditawarkan oleh KCU Pensiunan Pegawai?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_pensiunan_pegawai"}},

    {"text": "Apa syarat untuk KCU Pensiunan Pegawai?", "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pensiunan_pegawai"}},
    {"text": "Apa saja syarat untuk bergabung dengan KCU Pensiunan Pegawai?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_pensiunan_pegawai"}},
    {"text": "Apa persyaratan untuk menjadi anggota KCU Pensiunan Pegawai?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_pensiunan_pegawai"}},
    {"text": "Syarat apa saja yang diperlukan untuk membuka akun di KCU Pensiunan Pegawai?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_pensiunan_pegawai"}},
    {"text": "Apa saja ketentuan untuk bisa bergabung dengan KCU Pensiunan Pegawai?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_pensiunan_pegawai"}},
    {"text": "Bagaimana cara memenuhi syarat untuk KCU Pensiunan Pegawai?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_pensiunan_pegawai"}},
    {"text": "Apa saja dokumen yang diperlukan untuk bergabung dengan KCU Pensiunan Pegawai?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_pensiunan_pegawai"}},
    {"text": "Apa saja syarat yang harus dipenuhi untuk menjadi anggota KCU Pensiunan Pegawai?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_pensiunan_pegawai"}},
    {"text": "Apa saja persyaratan umum untuk KCU Pensiunan Pegawai?",
        "intent": "product_inquiry", "entities": {"product_name": "kcu_pensiunan_pegawai"}},

    {
        "text": "Apa itu produk KCU untuk Pegawai Swasta di Bank Nagari?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pegawai_swasta"}
    },
    {
        "text": "Bisa dijelaskan tentang kredit cicilan uang untuk pegawai swasta?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pegawai_swasta"}
    },
    {
        "text": "Siapa saja yang bisa mengajukan KCU Pegawai Swasta?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pegawai_swasta"}
    },
    {
        "text": "Apakah pegawai outsourcing di Bank Nagari bisa ambil KCU ini?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pegawai_swasta"}
    },
    {
        "text": "Apakah pegawai tetap yayasan bisa mengajukan kredit konsumtif ini?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pegawai_swasta"}
    },
    {
        "text": "KCU untuk pegawai swasta ini bisa digunakan untuk keperluan apa saja?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pegawai_swasta"}
    },
    {
        "text": "Apakah pembiayaan ini hanya untuk kebutuhan konsumsi pribadi?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pegawai_swasta"}
    },
    {
        "text": "Berapa lama tenor pinjaman maksimal untuk KCU Pegawai Swasta?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pegawai_swasta"}
    },
    {
        "text": "Apakah kredit ini bisa diambil hingga 10 tahun lamanya?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pegawai_swasta"}
    },
    {
        "text": "Berapa usia maksimal debitur saat kredit KCU ini berakhir?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pegawai_swasta"}
    },
    {
        "text": "Apakah saya masih bisa mengajukan KCU jika usia saya sekarang 52 tahun?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pegawai_swasta"}
    },
    {
        "text": "Bagaimana ketentuan bunga di KCU untuk pegawai swasta?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pegawai_swasta"}
    },
    {
        "text": "Berapa besar suku bunga kredit KCU Pegawai Swasta?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pegawai_swasta"}
    },
    {
        "text": "Apakah biaya pinjaman dalam program KCU ini tergolong ringan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pegawai_swasta"}
    },
    {
        "text": "Apakah pinjaman ini wajib diasuransikan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pegawai_swasta"}
    },
    {
        "text": "Apakah ada asuransi selama masa pinjaman KCU Pegawai Swasta?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pegawai_swasta"}
    },
    {
        "text": "Salah satu syaratnya adalah gaji harus dibayarkan lewat Bank Nagari ya?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pegawai_swasta"}
    },
    {
        "text": "Apakah gaji harus masuk ke rekening Bank Nagari agar bisa ambil KCU ini?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pegawai_swasta"}
    },
    {
        "text": "Apa saja syarat dokumen untuk ajukan KCU Pegawai Swasta?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pegawai_swasta"}
    },
    {
        "text": "Apa perlu NPWP dan slip gaji untuk KCU Pegawai Swasta?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pegawai_swasta"}
    },
    {
        "text": "Apakah saya perlu menyerahkan SK dari perusahaan untuk pinjaman ini?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pegawai_swasta"}
    },
    {
        "text": "Bagaimana dengan persyaratan agunan, apakah selalu diwajibkan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pegawai_swasta"}
    },
    {
        "text": "Jika agunan diminta, dokumen apa saja yang harus saya lampirkan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pegawai_swasta"}
    },
    {
        "text": "Perlu isi surat kuasa potong gaji juga untuk produk ini?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pegawai_swasta"}
    },
    {
        "text": "Apakah perlu surat kuasa pendebetan rekening juga?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pegawai_swasta"}
    },
    {
        "text": "Saya punya tabungan Bank Nagari, apakah bisa digunakan untuk proses KCU ini?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pegawai_swasta"}
    },
    {
        "text": "Kalau saya pegawai tetap swasta, berapa besar plafon kredit yang bisa saya ajukan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pegawai_swasta"}
    },
    {
        "text": "Kredit ini bisa untuk beli barang kebutuhan rumah tangga juga kan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pegawai_swasta"}
    },
    {
        "text": "Produk KCU Pegawai Swasta ini dikhususkan untuk konsumtif saja, bukan usaha ya?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pegawai_swasta"}
    },
    {
        "text": "Adakah ketentuan dari perusahaan atau yayasan agar pegawainya bisa ambil KCU?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pegawai_swasta"}
    },
    {
        "text": "Jika usia saya sudah 54, apakah masih bisa ajukan KCU untuk pegawai swasta?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pegawai_swasta"}
    },
    {
        "text": "Saya outsourcing di Bank Nagari, apakah bisa mengajukan pinjaman ini?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pegawai_swasta"}
    },
    {
        "text": "Berapa lama proses pengajuan KCU Pegawai Swasta biasanya disetujui?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kcu_pegawai_swasta"}
    },
    {
        "text": "Apa itu layanan Kredit Jaminan Deposito atau KJD dari Bank Nagari?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kjd"}
    },
    {
        "text": "Bisa jelaskan KJD itu produk apa ya?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kjd"}
    },
    {
        "text": "Kalau saya punya deposito di Bank Nagari, bisa dapat pinjaman KJD?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kjd"}
    },
    {
        "text": "Apakah KJD hanya untuk nasabah yang punya deposito saja?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kjd"}
    },
    {
        "text": "Siapa saja yang boleh mengajukan Kredit Jaminan Deposito ini?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kjd"}
    },
    {
        "text": "Apakah instansi pemerintah juga bisa mengambil fasilitas KJD?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kjd"}
    },
    {
        "text": "Saya pemilik badan usaha, boleh ajukan KJD di Bank Nagari?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kjd"}
    },
    {
        "text": "Untuk apa saja pinjaman KJD ini bisa digunakan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kjd"}
    },
    {
        "text": "Apakah KJD bisa digunakan untuk pembiayaan jangka pendek?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kjd"}
    },
    {
        "text": "Berapa maksimal pinjaman yang bisa saya ajukan lewat KJD?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kjd"}
    },
    {
        "text": "Berapa persen dari deposito saya bisa dijadikan pinjaman KJD?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kjd"}
    },
    {
        "text": "Apakah plafon KJD bisa mencapai 90 persen dari nilai deposito?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kjd"}
    },
    {
        "text": "Berapa lama tenor atau jangka waktu untuk KJD?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kjd"}
    },
    {
        "text": "Apakah jangka waktu KJD mengikuti masa jatuh tempo depositonya?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kjd"}
    },
    {
        "text": "Berapa suku bunga yang dikenakan pada KJD?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kjd"}
    },
    {
        "text": "Apakah suku bunga KJD tergolong kompetitif?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kjd"}
    },
    {
        "text": "Benarkah KJD tidak dikenakan biaya provisi?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kjd"}
    },
    {
        "text": "Kalau ajukan KJD, apakah ada biaya administrasi atau provisi?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kjd"}
    },
    {
        "text": "Apakah proses pengajuan KJD memerlukan waktu lama?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kjd"}
    },
    {
        "text": "Apakah pengajuan pinjaman KJD cepat dan mudah prosesnya?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kjd"}
    },
    {
        "text": "Dokumen apa saja yang perlu saya siapkan untuk KJD?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kjd"}
    },
    {
        "text": "Apa saya harus mengisi aplikasi kredit untuk ajukan KJD?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kjd"}
    },
    {
        "text": "Apakah saya perlu menyerahkan bilyet deposito asli untuk KJD?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kjd"}
    },
    {
        "text": "Apakah harus menyertakan fotokopi KTP dan NPWP saat ajukan KJD?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kjd"}
    },
    {
        "text": "Untuk plafon besar di KJD, apakah NPWP wajib diserahkan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kjd"}
    },
    {
        "text": "Kalau saya hanya punya deposito kecil, tetap bisa ajukan KJD?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kjd"}
    },
    {
        "text": "Saya ingin pinjam tanpa agunan, tapi punya deposito. Bisa pakai KJD?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kjd"}
    },
    {
        "text": "Produk KJD ini bisa membantu saya memenuhi kebutuhan mendesak?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kjd"}
    },
    {
        "text": "Adakah batasan jenis kebutuhan untuk pinjaman dari KJD?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kjd"}
    },
    {
        "text": "Bagaimana cara mengajukan KJD kalau saya pemilik perusahaan?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kjd"}
    },
    {
        "text": "Jika deposito atas nama perusahaan, apakah tetap bisa ajukan KJD?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kjd"}
    },
    {
        "text": "Saya PNS dan punya deposito, bisa ambil KJD untuk keperluan pribadi?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kjd"}
    },
    {
        "text": "Bolehkah deposito digunakan sebagai jaminan pinjaman di Bank Nagari?",
        "intent": "product_inquiry",
        "entities": {"product_name": "kjd"}
    },

    # Promo EDC Cashback
    {
        "text": "Apa itu promo EDC cashback Bank Nagari?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "promo_edc_cashback", "info_type": "description"}
    },
    {
        "text": "Bisa jelasin EDC cashback itu prmo apa?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "promo_edc_cashback", "info_type": "description"}
    },
    {
        "text": "EDC cashback itu gunanya buat apa sih?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "promo_edc_cashback", "info_type": "description"}
    },
    {
        "text": "Promo EDC cashback ini penjelasannya gimana?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "promo_edc_cashback", "info_type": "description"}
    },

    {
        "text": "Promo EDC cashback berlaku sampai kapan?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "promo_edc_cashback", "info_type": "periode"}
    },
    {
        "text": "Kapan periode promo EDC cashback dimulai?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "promo_edc_cashback", "info_type": "periode"}
    },
    {
        "text": "Tanggal berakhir promo EDC cashback?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "promo_edc_cashback", "info_type": "periode"}
    },
    {
        "text": "Masa berlaku promo EDC cashback bank nagari?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "promo_edc_cashback", "info_type": "periode"}
    },

    {
        "text": "Keuntungan ikut promo EDC cashback apa aja?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "promo_edc_cashback", "info_type": "benefits"}
    },
    {
        "text": "Benefit EDC cashback itu apa sih?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "promo_edc_cashback", "info_type": "benefits"}
    },
    {
        "text": "Apa saja yang didapat dari promo EDC cashback?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "promo_edc_cashback", "info_type": "benefits"}
    },
    {
        "text": "EDC cashback ini kasih cashback berapa?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "promo_edc_cashback", "info_type": "benefits"}
    },

    {
        "text": "Syarat ikut promo EDC cashback apa aja?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "promo_edc_cashback", "info_type": "requirements"}
    },
    {
        "text": "Persyaratan biar bisa dapet cashback EDC?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "promo_edc_cashback", "info_type": "requirements"}
    },
    {
        "text": "EDC cashback ini berlaku untuk siapa aja?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "promo_edc_cashback", "info_type": "requirements"}
    },
    {
        "text": "Minimal belanja buat promo EDC cashback berapa?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "promo_edc_cashback", "info_type": "requirements"}
    },

    {
        "text": "Apa aja jenis program di promo EDC cashback?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "promo_edc_cashback", "info_type": "programs"}
    },
    {
        "text": "Jelaskan daftar program EDC cashback Bank Nagari",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "promo_edc_cashback", "info_type": "programs"}
    },
    {
        "text": "EDC cashback ada kategori program apa aja sih?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "promo_edc_cashback", "info_type": "programs"}
    },
    {
        "text": "Kasih tau promo EDC Market itu termasuk apa di program cashback?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "promo_edc_cashback", "info_type": "programs"}
    },

    {
        "text": "prmo EDC cashbak bank nagri itu apa?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "promo_edc_cashback", "info_type": "description"}
    },
    {
        "text": "Keungtungn ikut promo edc cb ini apa aja?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "promo_edc_cashback", "info_type": "benefits"}
    },
    {
        "text": "Batas waktu prmo EDC cash back ini kapan?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "promo_edc_cashback", "info_type": "periode"}
    },
    {
        "text": "Gimana cara ikut EDC cashback?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "promo_edc_cashback", "info_type": "requirements"}
    },
    {
        "text": "Kategori program edc cashback ada berapa?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "promo_edc_cashback", "info_type": "programs"}
    },
    {
        "text": "Apa semua transaksi bisa dapet promo EDC cashback?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "promo_edc_cashback", "info_type": "requirements"}
    },
    {
        "text": "Bisa jelasin semua kategori EDC cashback?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "promo_edc_cashback", "info_type": "programs"}
    },

    # Promo Nagari Merdeka
    {
        "text": "Apa itu promo Nagari Merdeka?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "nagari_merdeka", "info_type": "description"}
    },
    {
        "text": "Bisa jelasin promo nagari merdeka hut 80 thn 2025?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "nagari_merdeka", "info_type": "description"}
    },
    {
        "text": "Nagari merdeka ini maksudnya promo apa?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "nagari_merdeka", "info_type": "description"}
    },
    {
        "text": "Promo nagari merdeka itu acara apa sih?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "nagari_merdeka", "info_type": "description"}
    },

    {
        "text": "Promo Nagari Merdeka berlaku dari kapan sampai kapan?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "nagari_merdeka", "info_type": "periode"}
    },
    {
        "text": "Tanggal promo nagari merdeka dimulai?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "nagari_merdeka", "info_type": "periode"}
    },
    {
        "text": "Sampai kapan promo nagari merdeka bisa diikuti?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "nagari_merdeka", "info_type": "periode"}
    },
    {
        "text": "Masa berlaku promo nagari merdeka bank nagari?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "nagari_merdeka", "info_type": "periode"}
    },

    {
        "text": "Apa keuntungan ikut promo nagari merdeka?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "nagari_merdeka", "info_type": "benefits"}
    },
    {
        "text": "Benefit nagari merdeka itu apa saja?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "nagari_merdeka", "info_type": "benefits"}
    },
    {
        "text": "Kalau ikut promo nagari merdeka dapat apa?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "nagari_merdeka", "info_type": "benefits"}
    },
    {
        "text": "Promo ini kasih reward berapa maksimal?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "nagari_merdeka", "info_type": "benefits"}
    },

    {
        "text": "Syarat ikut promo nagari merdeka apa aja?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "nagari_merdeka", "info_type": "requirements"}
    },
    {
        "text": "Persyaratan promo nagari merdeka untuk siapa?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "nagari_merdeka", "info_type": "requirements"}
    },
    {
        "text": "Siapa yang bisa ikut promo nagari merdeka?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "nagari_merdeka", "info_type": "requirements"}
    },
    {
        "text": "Promo nagari merdeka ini berlaku untuk pengajuan apa aja?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "nagari_merdeka", "info_type": "requirements"}
    },

    {
        "text": "nagari merdeka itu prmo apa sih?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "nagari_merdeka", "info_type": "description"}
    },
    {
        "text": "Keuntungn ikut nagari merdeka itu apa aja?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "nagari_merdeka", "info_type": "benefits"}
    },
    {
        "text": "Batas waktu prmo nagari merdeka kapan?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "nagari_merdeka", "info_type": "periode"}
    },
    {
        "text": "Gimana cara ikut promo nagari merdeka?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "nagari_merdeka", "info_type": "requirements"}
    },
    {
        "text": "Siapa aja yg boleh daftar promo nagari merdeka?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "nagari_merdeka", "info_type": "requirements"}
    },
    {
        "text": "Promo nagari merdeka itu rewardnya apa?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "nagari_merdeka", "info_type": "benefits"}
    },
    {
        "text": "Maksimal hadiah promo nagari merdeka brapa?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "nagari_merdeka", "info_type": "benefits"}
    },
    {
        "text": "Periode promo nagari merdeka kapan sj?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "nagari_merdeka", "info_type": "periode"}
    },
    {
        "text": "Apakah pensiunan bisa ikut promo nagari merdeka?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "nagari_merdeka", "info_type": "requirements"}
    },
    {
        "text": "Promo nagari merdeka ini untuk top up bisa?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "nagari_merdeka", "info_type": "requirements"}
    },

    # Promo Sikoci Cuan
    {
        "text": "Apa itu promo sikoci cuan?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "sikoci_cuan", "info_type": "description"}
    },
    {
        "text": "Bisa jelasin promo sikoci cuan bank nagari?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "sikoci_cuan", "info_type": "description"}
    },
    {
        "text": "Sikoci cuan ini promo apa sih?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "sikoci_cuan", "info_type": "description"}
    },
    {
        "text": "Promo sikoci cuan itu apa maksudnya?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "sikoci_cuan", "info_type": "description"}
    },

    {
        "text": "Promo sikoci cuan berlaku sampai kapan?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "sikoci_cuan", "info_type": "periode"}
    },
    {
        "text": "Batas akhir promo sikoci cuan kapan?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "sikoci_cuan", "info_type": "periode"}
    },
    {
        "text": "Masa berlaku promo sikoci cuan bank nagari?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "sikoci_cuan", "info_type": "periode"}
    },
    {
        "text": "Promo sikoci cuan dimulai dari kapan?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "sikoci_cuan", "info_type": "periode"}
    },

    {
        "text": "Apa keuntungan ikut promo sikoci cuan?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "sikoci_cuan", "info_type": "benefits"}
    },
    {
        "text": "Benefit promo sikoci cuan apa aja?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "sikoci_cuan", "info_type": "benefits"}
    },
    {
        "text": "Hadiah promo sikoci cuan apa saja?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "sikoci_cuan", "info_type": "benefits"}
    },
    {
        "text": "Kalau ikut sikoci cuan dapat hadiah apa?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "sikoci_cuan", "info_type": "benefits"}
    },

    {
        "text": "Syarat ikut promo sikoci cuan apa aja?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "sikoci_cuan", "info_type": "requirements"}
    },
    {
        "text": "Persyaratan ikut promo sikoci cuan?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "sikoci_cuan", "info_type": "requirements"}
    },
    {
        "text": "Jangka waktu tabungan untuk promo sikoci cuan?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "sikoci_cuan", "info_type": "requirements"}
    },
    {
        "text": "Promo sikoci cuan pencairan tabungannya kapan?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "sikoci_cuan", "info_type": "requirements"}
    },

    {
        "text": "skoci cuan itu promo apaan?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "sikoci_cuan", "info_type": "description"}
    },
    {
        "text": "Keuntungn promo skoci cuan apa?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "sikoci_cuan", "info_type": "benefits"}
    },
    {
        "text": "Batas waktu prmo sikoci cuan?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "sikoci_cuan", "info_type": "periode"}
    },
    {
        "text": "Cara ikut promo sikoci cuan gimana?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "sikoci_cuan", "info_type": "requirements"}
    },
    {
        "text": "syarat ikut skoci cuan apa aj?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "sikoci_cuan", "info_type": "requirements"}
    },
    {
        "text": "Hadiah promo skoci cuan apa?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "sikoci_cuan", "info_type": "benefits"}
    },
    {
        "text": "Promo skoci cuan berlaku smpe kapan?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "sikoci_cuan", "info_type": "periode"}
    },
    {
        "text": "Apakah tabungan 3 bulan bisa ikut promo sikoci cuan?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "sikoci_cuan", "info_type": "requirements"}
    },
    {
        "text": "Promo sikoci cuan ini bisa 6 bulan tabungan?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "sikoci_cuan", "info_type": "requirements"}
    },
    {
        "text": "Hadiah langsung promo sikoci cuan berapa nilainya?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "sikoci_cuan", "info_type": "benefits"}
    },

    # Promo Gebyar Hadiah Tabungan
    {
        "text": "Apa itu promo gebyar hadiah tabungan?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "gebyar_hadiah_tabungan", "info_type": "description"}
    },
    {
        "text": "Bisa jelasin promo gebyar hadiah tabungan bank nagari?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "gebyar_hadiah_tabungan", "info_type": "description"}
    },
    {
        "text": "Gebyar hadiah tabungan itu promo apa?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "gebyar_hadiah_tabungan", "info_type": "description"}
    },
    {
        "text": "Jelaskan program undian gebyar hadiah tabungan!",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "gebyar_hadiah_tabungan", "info_type": "description"}
    },

    {
        "text": "Apa saja hadiah gebyar hadiah tabungan?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "gebyar_hadiah_tabungan", "info_type": "hadiah"}
    },
    {
        "text": "Hadiah utama promo gebyar hadiah tabungan apa?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "gebyar_hadiah_tabungan", "info_type": "hadiah"}
    },
    {
        "text": "Kalau ikut gebyar hadiah tabungan dapat apa?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "gebyar_hadiah_tabungan", "info_type": "hadiah"}
    },
    {
        "text": "List hadiah promo gebyar hadiah tabungan",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "gebyar_hadiah_tabungan", "info_type": "hadiah"}
    },

    {
        "text": "Syarat ikut gebyar hadiah tabungan apa aja?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "gebyar_hadiah_tabungan", "info_type": "requirements"}
    },
    {
        "text": "Persyaratan untuk ikut undian gebyar hadiah tabungan?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "gebyar_hadiah_tabungan", "info_type": "requirements"}
    },
    {
        "text": "Minimal saldo untuk ikut gebyar hadiah tabungan berapa?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "gebyar_hadiah_tabungan", "info_type": "requirements"}
    },
    {
        "text": "Tabungan apa yang bisa ikut gebyar hadiah tabungan?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "gebyar_hadiah_tabungan", "info_type": "requirements"}
    },

    {
        "text": "ghbt itu promo apaan?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "gebyar_hadiah_tabungan", "info_type": "description"}
    },
    {
        "text": "List hadiah GHBT",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "gebyar_hadiah_tabungan", "info_type": "hadiah"}
    },
    {
        "text": "Apa aja hadiah GHBT bank nagari?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "gebyar_hadiah_tabungan", "info_type": "hadiah"}
    },
    {
        "text": "Hadiah utama GHBT apa?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "gebyar_hadiah_tabungan", "info_type": "hadiah"}
    },
    {
        "text": "syarat ikut GHBT apa aj?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "gebyar_hadiah_tabungan", "info_type": "requirements"}
    },
    {
        "text": "Berap saldo minimal untuk GHBT?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "gebyar_hadiah_tabungan", "info_type": "requirements"}
    },
    {
        "text": "GHBT berlaku untuk tabungan apa aja?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "gebyar_hadiah_tabungan", "info_type": "requirements"}
    },

    {
        "text": "Apa it gebyar hadiah tabungan?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "gebyar_hadiah_tabungan", "info_type": "description"}
    },
    {
        "text": "Hadia promo gebyar tabungan?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "gebyar_hadiah_tabungan", "info_type": "hadiah"}
    },
    {
        "text": "Brp minimal saldo gebyar tabungan?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "gebyar_hadiah_tabungan", "info_type": "requirements"}
    },
    {
        "text": "GHBT itu undian apa?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "gebyar_hadiah_tabungan", "info_type": "description"}
    },
    {
        "text": "Apakah GHBT butuh saldo 1 juta?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "gebyar_hadiah_tabungan", "info_type": "requirements"}
    },
    {
        "text": "GHBT punya hadiah fortuner ya?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "gebyar_hadiah_tabungan", "info_type": "hadiah"}
    },
    {
        "text": "Apakah GHBT ada hadiah umroh?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "gebyar_hadiah_tabungan", "info_type": "hadiah"}
    },

    # Promo KPR Berhadiah Langsung
    {
        "text": "Apa itu program KPR berhadiah langsung?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "kpr_berhadiah_langsung", "info_type": "description"}
    },
    {
        "text": "Jelaskan promo KPR berhadiah langsung bank nagari!",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "kpr_berhadiah_langsung", "info_type": "description"}
    },
    {
        "text": "KPR berhadiah langsung itu apa sih?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "kpr_berhadiah_langsung", "info_type": "description"}
    },
    {
        "text": "Program NGM berhadiah langsung itu gimana?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "kpr_berhadiah_langsung", "info_type": "description"}
    },

    {
        "text": "Apa keuntungan KPR berhadiah langsung?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "kpr_berhadiah_langsung", "info_type": "benefits"}
    },
    {
        "text": "Hadiah apa saja di KPR berhadiah langsung?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "kpr_berhadiah_langsung", "info_type": "benefits"}
    },
    {
        "text": "Kalau ikut KPR berhadiah langsung dapat apa?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "kpr_berhadiah_langsung", "info_type": "benefits"}
    },
    {
        "text": "List hadiah promo KPR NGM berhadiah langsung",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "kpr_berhadiah_langsung", "info_type": "benefits"}
    },

    {
        "text": "Syarat ikut KPR berhadiah langsung apa saja?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "kpr_berhadiah_langsung", "info_type": "requirements"}
    },
    {
        "text": "Persyaratan program KPR NGM berhadiah langsung?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "kpr_berhadiah_langsung", "info_type": "requirements"}
    },
    {
        "text": "Minimal kredit untuk ikut KPR berhadiah langsung berapa?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "kpr_berhadiah_langsung", "info_type": "requirements"}
    },
    {
        "text": "KPR berhadiah langsung berlaku untuk pembelian apa saja?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "kpr_berhadiah_langsung", "info_type": "requirements"}
    },

    {
        "text": "kpr hadiah langsung itu promo apa?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "kpr_berhadiah_langsung", "info_type": "description"}
    },
    {
        "text": "List hadiah kpr hadiah langsung",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "kpr_berhadiah_langsung", "info_type": "benefits"}
    },
    {
        "text": "Dapet apa aja klo ikut kpr hadiah langsung?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "kpr_berhadiah_langsung", "info_type": "benefits"}
    },
    {
        "text": "syarat ikut kpr hadiah langsung apa aj?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "kpr_berhadiah_langsung", "info_type": "requirements"}
    },
    {
        "text": "berapa minimal kredit kpr hadiah langsung?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "kpr_berhadiah_langsung", "info_type": "requirements"}
    },
    {
        "text": "kpr hadiah langsung untuk rumah saja?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "kpr_berhadiah_langsung", "info_type": "requirements"}
    },

    {
        "text": "Apa it kpr hadiah lngsung?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "kpr_berhadiah_langsung", "info_type": "description"}
    },
    {
        "text": "Hadiah promo kpr lngsung?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "kpr_berhadiah_langsung", "info_type": "benefits"}
    },
    {
        "text": "Brp minimal kredit kpr lngsung?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "kpr_berhadiah_langsung", "info_type": "requirements"}
    },
    {
        "text": "kpr hadiah langsung itu peralatan rumah tangga ya?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "kpr_berhadiah_langsung", "info_type": "benefits"}
    },
    {
        "text": "apakah kpr hadiah langsung berlaku untuk renovasi?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "kpr_berhadiah_langsung", "info_type": "requirements"}
    },
    {
        "text": "promo kpr hadiah langsung sampe kapan?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "kpr_berhadiah_langsung", "info_type": "description"}
    },
    {
        "text": "pajak hadiah kpr langsung sudah termasuk?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "kpr_berhadiah_langsung", "info_type": "benefits"}
    },

    # Promo Hangout Weekend Ollin
    {
        "text": "Apa itu promo Hangout Weekend Ollin?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "hangout_weekend_ollin", "info_type": "description"}
    },
    {
        "text": "Jelaskan promo QRISperience Hangout Weekend Ollin!",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "hangout_weekend_ollin", "info_type": "description"}
    },
    {
        "text": "Hangout weekend ollin itu apaan sih?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "hangout_weekend_ollin", "info_type": "description"}
    },
    {
        "text": "QRIS Ollin weekend itu program apa?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "hangout_weekend_ollin", "info_type": "description"}
    },

    {
        "text": "Apa keuntungan hangout weekend ollin?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "hangout_weekend_ollin", "info_type": "benefits"}
    },
    {
        "text": "Berapa cashback hangout weekend ollin?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "hangout_weekend_ollin", "info_type": "benefits"}
    },
    {
        "text": "Kalau ikut promo hangout weekend ollin dapat apa?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "hangout_weekend_ollin", "info_type": "benefits"}
    },
    {
        "text": "List benefit promo hangout weekend ollin",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "hangout_weekend_ollin", "info_type": "benefits"}
    },

    {
        "text": "Syarat ikut hangout weekend ollin apa saja?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "hangout_weekend_ollin", "info_type": "requirements"}
    },
    {
        "text": "Persyaratan promo QRIS hangout weekend ollin?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "hangout_weekend_ollin", "info_type": "requirements"}
    },
    {
        "text": "Minimal transaksi untuk hangout weekend ollin berapa?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "hangout_weekend_ollin", "info_type": "requirements"}
    },
    {
        "text": "Hangout weekend ollin berlaku untuk pembayaran apa saja?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "hangout_weekend_ollin", "info_type": "requirements"}
    },

    {
        "text": "Merchant hangout weekend ollin ada di mana?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "hangout_weekend_ollin", "info_type": "merchants"}
    },
    {
        "text": "Daftar resto/cafe untuk promo hangout weekend ollin",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "hangout_weekend_ollin", "info_type": "merchants"}
    },
    {
        "text": "Lokasi hangout weekend ollin ada di mana aja?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "hangout_weekend_ollin", "info_type": "merchants"}
    },
    {
        "text": "Toko mana yang ikut promo hangout weekend ollin?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "hangout_weekend_ollin", "info_type": "merchants"}
    },

    {
        "text": "hangout ollin itu promo ap?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "hangout_weekend_ollin", "info_type": "description"}
    },
    {
        "text": "cashback hangout ollin brp?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "hangout_weekend_ollin", "info_type": "benefits"}
    },
    {
        "text": "syarat promo hangout ollin ap aj?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "hangout_weekend_ollin", "info_type": "requirements"}
    },
    {
        "text": "merchant promo ollin dmna aja?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "hangout_weekend_ollin", "info_type": "merchants"}
    },

    {
        "text": "Apa it hangout weknd ollin?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "hangout_weekend_ollin", "info_type": "description"}
    },
    {
        "text": "Hadiah promo hangout weknd ollin?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "hangout_weekend_ollin", "info_type": "benefits"}
    },
    {
        "text": "brp min trsaksi hangout ollin?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "hangout_weekend_ollin", "info_type": "requirements"}
    },
    {
        "text": "merchant hangout weknd ollin lengkapnya?",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "hangout_weekend_ollin", "info_type": "merchants"}
    },
    {
        "text": "link merchant promo hangout ollin",
        "intent": "promo_inquiry",
        "entities": {"promo_name": "hangout_weekend_ollin", "info_type": "merchants"}
    },

    # Intent Lokasi ATM
    {
        "text": "Dimana lokasi cabang Alahan Panjang?",
        "intent": "branch_inquiry",
        "entities": [
            {
                "entity": "branch_name",
                "value": "alahan panjang",
                "start": 20,
                "end": 3
            }
        ]
    },
    {
        "text": "Alamat cabang Alahan Panjang di mana?",
        "intent": "branch_inquiry",
        "entities": [
            {
                "entity": "branch_name",
                "value": "alahan panjang",
                "start": 13,
                "end": 2
            }
        ]
    },
    {
        "text": "Dimana alamat cabang Alahan Panjang?",
        "intent": "branch_inquiry",
        "entities": [
            {
                "entity": "branch_name",
                "value": "alahan panjang",
                "start": 21,
                "end": 3
            }
        ]
    },
    {
        "text": "Cabang Alahan Panjang berada di mana?",
        "intent": "branch_inquiry",
        "entities": [
            {
                "entity": "branch_name",
                "value": "alahan panjang",
                "start": 7,
                "end": 2
            }
        ]
    },
    {
        "text": "Dimana tepatnya lokasi cabang Alahan Panjang?",
        "intent": "branch_inquiry",
        "entities": [
            {
                "entity": "branch_name",
                "value": "alahan panjang",
                "start": 31,
                "end": 4
            }
        ]
    },
    {
        "text": "Apa alamat lengkap cabang Alahan Panjang?",
        "intent": "branch_inquiry",
        "entities": [
            {
                "entity": "branch_name",
                "value": "alahan panjang",
                "start": 26,
                "end": 4
            }
        ]
    },
    {
        "text": "Cabang Alahan Panjang itu terletak di mana?",
        "intent": "branch_inquiry",
        "entities": [
            {
                "entity": "branch_name",
                "value": "alahan panjang",
                "start": 7,
                "end": 2
            }
        ]
    },
    {
        "text": "Dimana lokasi cabang Bandung?",
        "intent": "branch_inquiry",
        "entities": [
            {
                "entity": "branch_name",
                "value": "bandung",
                "start": 20,
                "end": 2
            }
        ]
    },
    {
        "text": "Alamat cabang Bandung apa?",
        "intent": "branch_inquiry",
        "entities": [
            {
                "entity": "branch_name",
                "value": "bandung",
                "start": 13,
                "end": 2
            }
        ]
    },
    {
        "text": "Dimana alamat cabang Bandung?",
        "intent": "branch_inquiry",
        "entities": [
            {
                "entity": "branch_name",
                "value": "bandung",
                "start": 21,
                "end": 2
            }
        ]
    },
    {
        "text": "Cabang Bandung berada di mana?",
        "intent": "branch_inquiry",
        "entities": [
            {
                "entity": "branch_name",
                "value": "bandung",
                "start": 7,
                "end": 1
            }
        ]
    },
    {
        "text": "Dimana tepatnya lokasi cabang Bandung?",
        "intent": "branch_inquiry",
        "entities": [
            {
                "entity": "branch_name",
                "value": "bandung",
                "start": 31,
                "end": 3
            }
        ]
    },
    {
        "text": "Apa alamat lengkap cabang Bandung?",
        "intent": "branch_inquiry",
        "entities": [
            {
                "entity": "branch_name",
                "value": "bandung",
                "start": 26,
                "end": 3
            }
        ]
    },
    {
        "text": "Cabang Bandung itu terletak di mana?",
        "intent": "branch_inquiry",
        "entities": [
            {
                "entity": "branch_name",
                "value": "bandung",
                "start": 7,
                "end": 1
            }
        ]
    },

    {
        "text": "Dimana lokasi cabang Batusangkar?",
        "intent": "branch_inquiry",
        "entities": [
            {"entity": "branch_name", "value": "batusangkar", "start": 20, "end": 31}
        ]
},
    {
        "text": "Alamat cabang Batusangkar dimana?",
        "intent": "branch_inquiry",
        "entities": [
            {"entity": "branch_name", "value": "batusangkar", "start": 13, "end": 24}
        ]
},
    {
        "text": "Dimana alamat cabang Batusangkar?",
        "intent": "branch_inquiry",
        "entities": [
            {"entity": "branch_name", "value": "batusangkar", "start": 21, "end": 32}
        ]
},
    {
        "text": "Cabang Batusangkar berada di lokasi mana?",
        "intent": "branch_inquiry",
        "entities": [
            {"entity": "branch_name", "value": "batusangkar", "start": 7, "end": 18}
        ]
},
    {
        "text": "Di mana lokasi cabang Batusangkar yang tepat?",
        "intent": "branch_inquiry",
        "entities": [
            {"entity": "branch_name", "value": "batusangkar", "start": 24, "end": 35}
        ]
},
    {
        "text": "Bisa kasih tahu alamat cabang Batusangkar?",
        "intent": "branch_inquiry",
        "entities": [
            {"entity": "branch_name", "value": "batusangkar", "start": 31, "end": 42}
        ]
},
    {
        "text": "Dimana tepatnya cabang Batusangkar berada?",
        "intent": "branch_inquiry",
        "entities": [
            {"entity": "branch_name", "value": "batusangkar", "start": 20, "end": 31}
        ]
},
    {
        "text": "Dimana lokasi cabang Bukittinggi?",
        "intent": "branch_inquiry",
        "entities": [
            {"entity": "branch_name", "value": "bukittinggi", "start": 20, "end": 31}
        ]
},
    {
        "text": "Dimana alamat cabang Bukittinggi?",
        "intent": "branch_inquiry",
        "entities": [
            {"entity": "branch_name", "value": "bukittinggi", "start": 21, "end": 32}
        ]
},
    {
        "text": "Cabang Bukittinggi berada di mana?",
        "intent": "branch_inquiry",
        "entities": [
            {"entity": "branch_name", "value": "bukittinggi", "start": 7, "end": 18}
        ]
},
    {
        "text": "Dimana lokasi cabang Bukittinggi yang tepat?",
        "intent": "branch_inquiry",
        "entities": [
            {"entity": "branch_name", "value": "bukittinggi", "start": 20, "end": 31}
        ]
},
    {
        "text": "Bisa beri tahu alamat cabang Bukittinggi?",
        "intent": "branch_inquiry",
        "entities": [
            {"entity": "branch_name", "value": "bukittinggi", "start": 33, "end": 44}
        ]
},
    {
        "text": "Di mana cabang Bukittinggi terletak?",
        "intent": "branch_inquiry",
        "entities": [
            {"entity": "branch_name", "value": "bukittinggi", "start": 10, "end": 21}
        ]
},
    {
        "text": "Alamat cabang Bukittinggi?",
        "intent": "branch_inquiry",
        "entities": [
            {"entity": "branch_name", "value": "bukittinggi", "start": 13, "end": 24}
        ]
},
    {
        "text": "Dimana lokasi cabang Jakarta?",
        "intent": "branch_inquiry",
        "entities": [
            {"entity": "branch_name", "value": "jakarta", "start": 20, "end": 27}
        ]
},
    {
        "text": "Apa alamat cabang Jakarta?",
        "intent": "branch_inquiry",
        "entities": [
            {"entity": "branch_name", "value": "jakarta", "start": 21, "end": 28}
        ]
},
    {
        "text": "Dimana alamat cabang Jakarta?",
        "intent": "branch_inquiry",
        "entities": [
            {"entity": "branch_name", "value": "jakarta", "start": 21, "end": 28}
        ]
},
    {
        "text": "Cabang Jakarta terletak di mana?",
        "intent": "branch_inquiry",
        "entities": [
            {"entity": "branch_name", "value": "jakarta", "start": 7, "end": 14}
        ]
},
    {
        "text": "Lokasi cabang Jakarta ada di mana?",
        "intent": "branch_inquiry",
        "entities": [
            {"entity": "branch_name", "value": "jakarta", "start": 14, "end": 21}
        ]
},
    {
        "text": "Di mana cabang Jakarta bisa ditemukan?",
        "intent": "branch_inquiry",
        "entities": [
            {"entity": "branch_name", "value": "jakarta", "start": 10, "end": 17}
        ]
},
    {
        "text": "Apa alamat cabang Jakarta?",
        "intent": "branch_inquiry",
        "entities": [
            {"entity": "branch_name", "value": "jakarta", "start": 21, "end": 28}
        ]
},
    {
        "text": "Dimana lokasi cabang Koto Baru?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "koto baru", "start": 20, "end": 29}]
    },
{
        "text": "Alamat cabang Koto Baru apa?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "koto baru", "start": 13, "end": 22}]
    },
{
        "text": "Dimana alamat cabang Koto Baru?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "koto baru", "start": 21, "end": 30}]
    },
{
        "text": "Cabang Koto Baru berada di mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "koto baru", "start": 7, "end": 16}]
    },
{
        "text": "Lokasi cabang Koto Baru ada di mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "koto baru", "start": 14, "end": 23}]
    },
{
        "text": "Di mana tepatnya cabang Koto Baru?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "koto baru", "start": 24, "end": 33}]
    },
{
        "text": "Apa alamat cabang Koto Baru?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "koto baru", "start": 21, "end": 30}]
    },

 {
        "text": "Dimana lokasi cabang Lintau?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "lintau", "start": 20, "end": 26}]
    },
{
        "text": "Alamat cabang Lintau apa?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "lintau", "start": 13, "end": 19}]
    },
{
        "text": "Dimana alamat cabang Lintau?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "lintau", "start": 21, "end": 27}]
    },
{
        "text": "Cabang Lintau terletak di mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "lintau", "start": 7, "end": 13}]
    },
{
        "text": "Lokasi cabang Lintau itu ada di mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "lintau", "start": 14, "end": 20}]
    },
{
        "text": "Di mana lokasi cabang Lintau yang tepat?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "lintau", "start": 24, "end": 30}]
    },
{
        "text": "Apa alamat lengkap cabang Lintau?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "lintau", "start": 27, "end": 33}]
    },

 {
        "text": "Dimana lokasi cabang Lubuk Alung?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "lubuk alung", "start": 20, "end": 31}]
    },
{
        "text": "Alamat cabang Lubuk Alung?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "lubuk alung", "start": 13, "end": 24}]
    },
{
        "text": "Dimana alamat cabang Lubuk Alung?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "lubuk alung", "start": 21, "end": 32}]
    },
{
        "text": "Cabang Lubuk Alung berada di mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "lubuk alung", "start": 7, "end": 18}]
    },
{
        "text": "Lokasi cabang Lubuk Alung itu di mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "lubuk alung", "start": 14, "end": 25}]
    },
{
        "text": "Di mana cabang Lubuk Alung terletak?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "lubuk alung", "start": 10, "end": 21}]
    },
{
        "text": "Apa alamat cabang Lubuk Alung?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "lubuk alung", "start": 21, "end": 32}]
    },

 {
        "text": "Dimana lokasi cabang Lubuk Basung?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "lubuk basung", "start": 20, "end": 33}]
    },
{
        "text": "Alamat cabang Lubuk Basung apa?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "lubuk basung", "start": 13, "end": 26}]
    },
{
        "text": "Dimana alamat cabang Lubuk Basung?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "lubuk basung", "start": 21, "end": 34}]
    },
{
        "text": "Cabang Lubuk Basung terletak di mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "lubuk basung", "start": 7, "end": 20}]
    },
{
        "text": "Lokasi cabang Lubuk Basung itu ada di mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "lubuk basung", "start": 14, "end": 27}]
    },
{
        "text": "Di mana lokasi cabang Lubuk Basung yang tepat?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "lubuk basung", "start": 24, "end": 37}]
    },
{
        "text": "Apa alamat cabang Lubuk Basung?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "lubuk basung", "start": 21, "end": 34}]
    },

 {
        "text": "Dimana lokasi cabang Lubuk Gadang?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "lubuk gadang", "start": 20, "end": 33}]
    },
{
        "text": "Apa alamat cabang Lubuk Gadang?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "lubuk gadang", "start": 21, "end": 34}]
    },
{
        "text": "Dimana alamat cabang Lubuk Gadang?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "lubuk gadang", "start": 21, "end": 34}]
    },
{
        "text": "Cabang Lubuk Gadang berada di mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "lubuk gadang", "start": 7, "end": 20}]
    },
{
        "text": "Lokasi cabang Lubuk Gadang itu di mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "lubuk gadang", "start": 14, "end": 27}]
    },
{
        "text": "Di mana tepatnya cabang Lubuk Gadang?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "lubuk gadang", "start": 24, "end": 37}]
    },
{
        "text": "Apa alamat cabang Lubuk Gadang?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "lubuk gadang", "start": 21, "end": 34}]
    },

 {
        "text": "Dimana lokasi cabang Lubuk Sikaping?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "lubuk sikaping", "start": 20, "end": 35}]
    },
{
        "text": "Alamat cabang Lubuk Sikaping apa?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "lubuk sikaping", "start": 13, "end": 28}]
    },
{
        "text": "Dimana alamat cabang Lubuk Sikaping?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "lubuk sikaping", "start": 21, "end": 36}]
    },
{
        "text": "Cabang Lubuk Sikaping terletak di mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "lubuk sikaping", "start": 7, "end": 22}]
    },
{
        "text": "Lokasi cabang Lubuk Sikaping itu ada di mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "lubuk sikaping", "start": 14, "end": 29}]
    },
{
        "text": "Di mana tepatnya cabang Lubuk Sikaping?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "lubuk sikaping", "start": 24, "end": 39}]
    },
{
        "text": "Apa alamat cabang Lubuk Sikaping?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "lubuk sikaping", "start": 21, "end": 36}]
    },
{
        "text": "Dimana lokasi cabang Matraman Jakarta?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "matraman jakarta", "start": 20, "end": 37}]
    },
{
        "text": "Alamat cabang Matraman Jakarta apa?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "matraman jakarta", "start": 13, "end": 30}]
    },
{
        "text": "Dimana alamat cabang Matraman Jakarta?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "matraman jakarta", "start": 21, "end": 38}]
    },
{
        "text": "Cabang Matraman Jakarta terletak di mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "matraman jakarta", "start": 7, "end": 24}]
    },
{
        "text": "Lokasi cabang Matraman Jakarta itu ada di mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "matraman jakarta", "start": 14, "end": 31}]
    },
{
        "text": "Di mana lokasi cabang Matraman Jakarta?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "matraman jakarta", "start": 24, "end": 41}]
    },
{
        "text": "Apa alamat cabang Matraman Jakarta?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "matraman jakarta", "start": 21, "end": 38}]
    },

 {
        "text": "Dimana lokasi cabang Mentawai?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "mentawai", "start": 20, "end": 28}]
    },
{
        "text": "Alamat cabang Mentawai apa?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "mentawai", "start": 13, "end": 21}]
    },
{
        "text": "Dimana alamat cabang Mentawai?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "mentawai", "start": 21, "end": 29}]
    },
{
        "text": "Cabang Mentawai terletak di mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "mentawai", "start": 7, "end": 15}]
    },
{
        "text": "Lokasi cabang Mentawai itu ada di mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "mentawai", "start": 14, "end": 22}]
    },
{
        "text": "Di mana tepatnya cabang Mentawai?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "mentawai", "start": 24, "end": 32}]
    },
{
        "text": "Apa alamat cabang Mentawai?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "mentawai", "start": 21, "end": 29}]
    },

 {
        "text": "Dimana lokasi cabang Muara Labuh?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "muara labuh", "start": 20, "end": 32}]
    },
{
        "text": "Alamat cabang Muara Labuh apa?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "muara labuh", "start": 13, "end": 25}]
    },
{
        "text": "Di mana cabang Muara Labuh berada?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "muara labuh", "start": 13, "end": 25}]
    },
{
        "text": "Lokasi cabang Muara Labuh itu di mana ya?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "muara labuh", "start": 14, "end": 26}]
    },
{
        "text": "Bisa kasih tahu alamat cabang Muara Labuh?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "muara labuh", "start": 33, "end": 45}]
    },
{
        "text": "Dimanakah cabang Muara Labuh terletak?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "muara labuh", "start": 12, "end": 24}]
    },
{
        "text": "Cabang Muara Labuh ada di mana ya?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "muara labuh", "start": 7, "end": 19}]
    },

 {
        "text": "Dimana lokasi cabang Padang Panjang?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "padang panjang", "start": 20, "end": 34}]
    },
{
        "text": "Alamat cabang Padang Panjang apa?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "padang panjang", "start": 13, "end": 27}]
    },
{
        "text": "Di mana cabang Padang Panjang berada?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "padang panjang", "start": 13, "end": 27}]
    },
{
        "text": "Lokasi cabang Padang Panjang ada di mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "padang panjang", "start": 14, "end": 28}]
    },
{
        "text": "Bisa kasih tahu alamat cabang Padang Panjang?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "padang panjang", "start": 33, "end": 47}]
    },
{
        "text": "Di mana lokasi cabang Padang Panjang?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "padang panjang", "start": 24, "end": 38}]
    },
{
        "text": "Cabang Padang Panjang terletak di mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "padang panjang", "start": 7, "end": 21}]
    },

 {
        "text": "Dimana lokasi cabang Painan?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "painan", "start": 20, "end": 26}]
    },
{
        "text": "Alamat cabang Painan apa?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "painan", "start": 13, "end": 19}]
    },
{
        "text": "Di mana cabang Painan berada?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "painan", "start": 13, "end": 19}]
    },
{
        "text": "Lokasi cabang Painan itu ada di mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "painan", "start": 14, "end": 20}]
    },
{
        "text": "Bisa beri tahu alamat cabang Painan?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "painan", "start": 33, "end": 39}]
    },
{
        "text": "Dimanakah cabang Painan terletak?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "painan", "start": 12, "end": 18}]
    },
{
        "text": "Cabang Painan ada di lokasi mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "painan", "start": 7, "end": 13}]
    },

 {
        "text": "Dimana lokasi cabang Pangkalan?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "pangkalan", "start": 20, "end": 29}]
    },
{
        "text": "Apa alamat cabang Pangkalan?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "pangkalan", "start": 21, "end": 30}]
    },
{
        "text": "Di mana cabang Pangkalan berada?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "pangkalan", "start": 13, "end": 22}]
    },
{
        "text": "Lokasi cabang Pangkalan itu di mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "pangkalan", "start": 14, "end": 23}]
    },
{
        "text": "Bisa kasih tahu alamat cabang Pangkalan?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "pangkalan", "start": 33, "end": 42}]
    },
{
        "text": "Dimana tepatnya cabang Pangkalan terletak?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "pangkalan", "start": 21, "end": 30}]
    },
{
        "text": "Cabang Pangkalan ada di mana ya?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "pangkalan", "start": 7, "end": 16}]
    },

 {
        "text": "Dimana lokasi cabang Pariaman?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "pariaman", "start": 20, "end": 28}]
    },
{
        "text": "Alamat cabang Pariaman apa?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "pariaman", "start": 13, "end": 21}]
    },
{
        "text": "Di mana cabang Pariaman berada?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "pariaman", "start": 13, "end": 21}]
    },
{
        "text": "Lokasi cabang Pariaman itu ada di mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "pariaman", "start": 14, "end": 22}]
    },
{
        "text": "Bisa beri tahu alamat cabang Pariaman?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "pariaman", "start": 33, "end": 41}]
    },
{
        "text": "Dimana tepatnya cabang Pariaman terletak?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "pariaman", "start": 21, "end": 29}]
    },
{
        "text": "Cabang Pariaman ada di lokasi mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "pariaman", "start": 7, "end": 15}]
    },

 {
        "text": "Dimana lokasi cabang Pasar Raya Padang?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "pasar raya padang", "start": 20, "end": 37}]
    },
{
        "text": "Apa alamat cabang Pasar Raya Padang?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "pasar raya padang", "start": 21, "end": 38}]
    },
{
        "text": "Di mana tepatnya cabang Pasar Raya Padang?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "pasar raya padang", "start": 24, "end": 41}]
    },
{
        "text": "Lokasi cabang Pasar Raya Padang ada di mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "pasar raya padang", "start": 14, "end": 31}]
    },
{
        "text": "Dimana alamat cabang Pasar Raya Padang?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "pasar raya padang", "start": 21, "end": 38}]
    },
{
        "text": "Bisa informasikan lokasi cabang Pasar Raya Padang?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "pasar raya padang", "start": 35, "end": 52}]
    },
{
        "text": "Di mana letak cabang Pasar Raya Padang?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "pasar raya padang", "start": 20, "end": 37}]
    },

 {
        "text": "Dimana lokasi cabang Payakumbuh?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "payakumbuh", "start": 20, "end": 30}]
    },
{
        "text": "Apa alamat cabang Payakumbuh?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "payakumbuh", "start": 21, "end": 31}]
    },
{
        "text": "Di mana cabang Payakumbuh berada?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "payakumbuh", "start": 13, "end": 23}]
    },
{
        "text": "Lokasi cabang Payakumbuh itu di mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "payakumbuh", "start": 14, "end": 24}]
    },
{
        "text": "Bisa beri tahu alamat cabang Payakumbuh?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "payakumbuh", "start": 33, "end": 43}]
    },
{
        "text": "Dimana tepatnya cabang Payakumbuh terletak?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "payakumbuh", "start": 21, "end": 31}]
    },
{
        "text": "Cabang Payakumbuh ada di daerah mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "payakumbuh", "start": 7, "end": 17}]
    },

 {
        "text": "Dimana lokasi cabang Pekanbaru?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "pekanbaru", "start": 20, "end": 29}]
    },
{
        "text": "Alamat cabang Pekanbaru apa?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "pekanbaru", "start": 13, "end": 22}]
    },
{
        "text": "Di mana cabang Pekanbaru berada?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "pekanbaru", "start": 13, "end": 22}]
    },
{
        "text": "Lokasi cabang Pekanbaru itu ada di mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "pekanbaru", "start": 14, "end": 23}]
    },
{
        "text": "Bisa beri tahu alamat cabang Pekanbaru?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "pekanbaru", "start": 33, "end": 42}]
    },
{
        "text": "Dimana tepatnya cabang Pekanbaru terletak?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "pekanbaru", "start": 21, "end": 30}]
    },
{
        "text": "Cabang Pekanbaru ada di lokasi mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "pekanbaru", "start": 7, "end": 16}]
    },

 {
        "text": "Dimana lokasi cabang Pulau Punjung?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "pulau punjung", "start": 20, "end": 34}]
    },
{
        "text": "Apa alamat cabang Pulau Punjung?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "pulau punjung", "start": 21, "end": 35}]
    },
{
        "text": "Cabang Pulau Punjung terletak di mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "pulau punjung", "start": 7, "end": 21}]
    },
{
        "text": "Di mana bisa ditemukan cabang Pulau Punjung?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "pulau punjung", "start": 31, "end": 45}]
    },
{
        "text": "Lokasi cabang Pulau Punjung itu dimana ya?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "pulau punjung", "start": 14, "end": 28}]
    },
{
        "text": "Dimana alamat cabang Pulau Punjung berada?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "pulau punjung", "start": 21, "end": 35}]
    },
{
        "text": "Ada di mana sih cabang Pulau Punjung?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "pulau punjung", "start": 21, "end": 35}]
    },

 {
        "text": "Dimana lokasi cabang Sawahlunto?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "sawahlunto", "start": 20, "end": 30}]
    },
{
        "text": "Alamat cabang Sawahlunto apa?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "sawahlunto", "start": 13, "end": 23}]
    },
{
        "text": "Di mana lokasi cabang Sawahlunto?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "sawahlunto", "start": 24, "end": 34}]
    },
{
        "text": "Dimana tepatnya cabang Sawahlunto berada?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "sawahlunto", "start": 21, "end": 31}]
    },
{
        "text": "Cabang Sawahlunto itu letaknya di mana ya?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "sawahlunto", "start": 7, "end": 17}]
    },
{
        "text": "Di mana alamat cabang Sawahlunto?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "sawahlunto", "start": 24, "end": 34}]
    },
{
        "text": "Lokasi cabang Sawahlunto ada di daerah mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "sawahlunto", "start": 14, "end": 24}]
    },

 {
        "text": "Dimana lokasi cabang Sijunjung?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "sijunjung", "start": 20, "end": 29}]
    },
{
        "text": "Apa alamat cabang Sijunjung?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "sijunjung", "start": 21, "end": 30}]
    },
{
        "text": "Di mana lokasi cabang Sijunjung berada?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "sijunjung", "start": 24, "end": 33}]
    },
{
        "text": "Cabang Sijunjung terletak di daerah mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "sijunjung", "start": 7, "end": 16}]
    },
{
        "text": "Tolong beri tahu alamat cabang Sijunjung?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "sijunjung", "start": 32, "end": 41}]
    },
{
        "text": "Dimana tepatnya lokasi cabang Sijunjung?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "sijunjung", "start": 31, "end": 40}]
    },
{
        "text": "Lokasi cabang Sijunjung itu ada di mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "sijunjung", "start": 14, "end": 23}]
    },

 {
        "text": "Dimana lokasi cabang Simpang Empat?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "simpang empat", "start": 20, "end": 34}]
    },
{
        "text": "Alamat cabang Simpang Empat?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "simpang empat", "start": 13, "end": 27}]
    },
{
        "text": "Di mana cabang Simpang Empat berada?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "simpang empat", "start": 13, "end": 27}]
    },
{
        "text": "Lokasi cabang Simpang Empat itu ada di mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "simpang empat", "start": 14, "end": 28}]
    },
{
        "text": "Bisa beri tahu alamat cabang Simpang Empat?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "simpang empat", "start": 33, "end": 47}]
    },
{
        "text": "Dimana tepatnya cabang Simpang Empat terletak?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "simpang empat", "start": 21, "end": 35}]
    },
{
        "text": "Cabang Simpang Empat ada di lokasi mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "simpang empat", "start": 7, "end": 21}]
    },

 {
        "text": "Dimana lokasi cabang Siteba?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "siteba", "start": 20, "end": 26}]
    },
{
        "text": "Apa alamat cabang Siteba?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "siteba", "start": 21, "end": 27}]
    },
{
        "text": "Di mana cabang Siteba berada?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "siteba", "start": 13, "end": 19}]
    },
{
        "text": "Lokasi cabang Siteba itu ada di mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "siteba", "start": 14, "end": 20}]
    },
{
        "text": "Tolong beri tahu alamat cabang Siteba?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "siteba", "start": 32, "end": 38}]
    },
{
        "text": "Dimana tepatnya cabang Siteba terletak?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "siteba", "start": 21, "end": 27}]
    },
{
        "text": "Cabang Siteba ada di daerah mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "siteba", "start": 7, "end": 13}]
    },

 {
        "text": "Dimana lokasi cabang Solok?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "solok", "start": 20, "end": 25}]
    },
{
        "text": "Apa alamat cabang Solok?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "solok", "start": 21, "end": 26}]
    },
{
        "text": "Di mana cabang Solok berada?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "solok", "start": 13, "end": 18}]
    },
{
        "text": "Lokasi cabang Solok itu ada di mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "solok", "start": 14, "end": 19}]
    },
{
        "text": "Tolong informasikan alamat cabang Solok?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "solok", "start": 35, "end": 40}]
    },
{
        "text": "Dimana tepatnya lokasi cabang Solok?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "solok", "start": 31, "end": 36}]
    },
{
        "text": "Cabang Solok terletak di daerah mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "solok", "start": 7, "end": 12}]
    },

 {
        "text": "Dimana lokasi cabang Syariah Padang?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "syariah padang", "start": 20, "end": 35}]
    },
{
        "text": "Alamat cabang Syariah Padang apa?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "syariah padang", "start": 13, "end": 28}]
    },
{
        "text": "Di mana cabang Syariah Padang berada?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "syariah padang", "start": 13, "end": 28}]
    },
{
        "text": "Lokasi cabang Syariah Padang itu ada di mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "syariah padang", "start": 14, "end": 29}]
    },
{
        "text": "Tolong beri tahu alamat cabang Syariah Padang?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "syariah padang", "start": 32, "end": 47}]
    },
{
        "text": "Dimana tepatnya cabang Syariah Padang terletak?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "syariah padang", "start": 21, "end": 36}]
    },
{
        "text": "Cabang Syariah Padang ada di daerah mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "syariah padang", "start": 7, "end": 22}]
    },

 {
        "text": "Dimana lokasi cabang Syariah Payakumbuh?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "syariah payakumbuh", "start": 20, "end": 39}]
    },
{
        "text": "Alamat cabang Syariah Payakumbuh apa?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "syariah payakumbuh", "start": 13, "end": 32}]
    },
{
        "text": "Di mana cabang Syariah Payakumbuh berada?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "syariah payakumbuh", "start": 13, "end": 32}]
    },
{
        "text": "Lokasi cabang Syariah Payakumbuh itu ada di mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "syariah payakumbuh", "start": 14, "end": 33}]
    },
{
        "text": "Tolong informasikan alamat cabang Syariah Payakumbuh?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "syariah payakumbuh", "start": 35, "end": 54}]
    },
{
        "text": "Dimana tepatnya cabang Syariah Payakumbuh terletak?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "syariah payakumbuh", "start": 21, "end": 40}]
    },
{
        "text": "Cabang Syariah Payakumbuh terletak di daerah mana?",
        "intent": "branch_inquiry",
        "entities": [{"entity": "branch_name", "value": "syariah payakumbuh", "start": 7, "end": 26}]
    },

 {
        "text": "Dimana lokasi cabang Syariah Solok?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "syariah_solok"}
    },
    {
        "text": "Apa alamat cabang Syariah Solok?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "syariah_solok"}
    },
    {
        "text": "Di mana cabang Syariah Solok berada?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "syariah_solok"}
    },
    {
        "text": "Lokasi cabang Syariah Solok itu ada di mana?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "syariah_solok"}
    },
    {
        "text": "Tolong beri tahu alamat cabang Syariah Solok?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "syariah_solok"}
    },
    {
        "text": "Dimana tepatnya cabang Syariah Solok terletak?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "syariah_solok"}
    },
    {
        "text": "Cabang Syariah Solok terletak di daerah mana?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "syariah_solok"}
    },

    {
        "text": "Dimana lokasi cabang Tapan?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "tapan"}
    },
    {
        "text": "Apa alamat cabang Tapan?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "tapan"}
    },
    {
        "text": "Di mana cabang Tapan berada?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "tapan"}
    },
    {
        "text": "Lokasi cabang Tapan itu ada di mana?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "tapan"}
    },
    {
        "text": "Tolong informasikan alamat cabang Tapan?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "tapan"}
    },
    {
        "text": "Dimana tepatnya cabang Tapan terletak?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "tapan"}
    },
    {
        "text": "Cabang Tapan terletak di daerah mana?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "tapan"}
    },

    {
        "text": "Dimana lokasi cabang Tapus?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "tapus"}
    },
    {
        "text": "Apa alamat cabang Tapus?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "tapus"}
    },
    {
        "text": "Di mana cabang Tapus berada?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "tapus"}
    },
    {
        "text": "Lokasi cabang Tapus itu ada di mana?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "tapus"}
    },
    {
        "text": "Tolong beri tahu alamat cabang Tapus?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "tapus"}
    },
    {
        "text": "Dimana tepatnya cabang Tapus terletak?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "tapus"}
    },
    {
        "text": "Cabang Tapus ada di daerah mana?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "tapus"}
    },

    {
        "text": "Dimana lokasi cabang Ujung Gading?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "ujung_gading"}
    },
    {
        "text": "Apa alamat cabang Ujung Gading?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "ujung_gading"}
    },
    {
        "text": "Di mana cabang Ujung Gading berada?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "ujung_gading"}
    },
    {
        "text": "Lokasi cabang Ujung Gading itu ada di mana?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "ujung_gading"}
    },
    {
        "text": "Tolong informasikan alamat cabang Ujung Gading?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "ujung_gading"}
    },
    {
        "text": "Dimana tepatnya cabang Ujung Gading terletak?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "ujung_gading"}
    },
    {
        "text": "Cabang Ujung Gading ada di daerah mana?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "ujung_gading"}
    },

    {
        "text": "Dimana lokasi cabang Utama Padang?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "utama_padang"}
    },
    {
        "text": "Apa alamat cabang Utama Padang?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "utama_padang"}
    },
    {
        "text": "Di mana cabang Utama Padang berada?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "utama_padang"}
    },
    {
        "text": "Lokasi cabang Utama Padang itu ada di mana?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "utama_padang"}
    },
    {
        "text": "Tolong informasikan alamat cabang Utama Padang?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "utama_padang"}
    },
    {
        "text": "Dimana tepatnya cabang Utama Padang terletak?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "utama_padang"}
    },
    {
        "text": "Cabang Utama Padang ada di daerah mana?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "utama_padang"}
    },

    {
        "text": "Dimana lokasi Kantor Pusat?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "kantor_pusat"}
    },
    {
        "text": "Apa alamat Kantor Pusat Bank Nagari?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "kantor_pusat"}
    },
    {
        "text": "Di mana lokasi Kantor Pusat berada?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "kantor_pusat"}
    },
    {
        "text": "Lokasi Kantor Pusat itu ada di mana?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "kantor_pusat"}
    },
    {
        "text": "Tolong beri tahu alamat Kantor Pusat?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "kantor_pusat"}
    },
    {
        "text": "Dimana tepatnya Kantor Pusat terletak?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "kantor_pusat"}
    },
    {
        "text": "Kantor Pusat berada di daerah mana?",
        "intent": "branch_inquiry",
        "entities": {"branch_name": "kantor_pusat"}
    },

    {
        "text": "Di mana lokasi Capem A. Yani Pekanbaru?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "a_yani_pekanbaru"}
    },
    {
        "text": "Alamat Capem A. Yani Pekanbaru?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "a_yani_pekanbaru"}
    },
    {
        "text": "Tolong beri tahu lokasi Capem A. Yani Pekanbaru?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "a_yani_pekanbaru"}
    },
    {
        "text": "Dimana alamat Capem A. Yani Pekanbaru berada?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "a_yani_pekanbaru"}
    },
    {
        "text": "Capem A. Yani Pekanbaru ada di mana?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "a_yani_pekanbaru"}
    },
    {
        "text": "Di mana tepatnya Capem A. Yani Pekanbaru?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "a_yani_pekanbaru"}
    },
    {
        "text": "Lokasi Capem A. Yani Pekanbaru berada di mana?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "a_yani_pekanbaru"}
    },

    {
        "text": "Di mana lokasi Capem Air Haji?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "air_haji"}
    },
    {
        "text": "Alamat Capem Air Haji?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "air_haji"}
    },
    {
        "text": "Tolong beri tahu lokasi Capem Air Haji?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "air_haji"}
    },
    {
        "text": "Dimana alamat Capem Air Haji berada?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "air_haji"}
    },
    {
        "text": "Capem Air Haji ada di mana?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "air_haji"}
    },
    {
        "text": "Di mana tepatnya Capem Air Haji?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "air_haji"}
    },
    {
        "text": "Lokasi Capem Air Haji berada di mana?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "air_haji"}
    },

    {
        "text": "Di mana lokasi Capem Arosuka?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "arosuka"}
    },
    {
        "text": "Alamat Capem Arosuka?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "arosuka"}
    },
    {
        "text": "Tolong beri tahu saya di mana lokasi Capem Arosuka?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "arosuka"}
    },
    {
        "text": "Dimana alamat Capem Arosuka?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "arosuka"}
    },
    {
        "text": "Capem Arosuka itu lokasinya di mana?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "arosuka"}
    },
    {
        "text": "Bisa informasikan lokasi Capem Arosuka?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "arosuka"}
    },
    {
        "text": "Di mana tepatnya Capem Arosuka berada?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "arosuka"}
    },

    {
        "text": "Di mana lokasi Capem Aur Kuning Bukittinggi?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "aur_kuning_bukittinggi"}
    },
    {
        "text": "Alamat Capem Aur Kuning Bukittinggi?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "aur_kuning_bukittinggi"}
    },
    {
        "text": "Tolong beri tahu saya dimana lokasi Capem Aur Kuning Bukittinggi?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "aur_kuning_bukittinggi"}
    },
    {
        "text": "Dimana alamat Capem Aur Kuning Bukittinggi?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "aur_kuning_bukittinggi"}
    },
    {
        "text": "Capem Aur Kuning Bukittinggi itu lokasinya di mana?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "aur_kuning_bukittinggi"}
    },
    {
        "text": "Bisa informasikan lokasi Capem Aur Kuning Bukittinggi?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "aur_kuning_bukittinggi"}
    },
    {
        "text": "Di mana tepatnya Capem Aur Kuning di Bukittinggi?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "aur_kuning_bukittinggi"}
    },

    {
        "text": "Di mana lokasi Capem Bandar Buat?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "bandar_buat"}
    },
    {
        "text": "Alamat Capem Bandar Buat?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "bandar_buat"}
    },
    {
        "text": "Tolong beri tahu lokasi Capem Bandar Buat?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "bandar_buat"}
    },
    {
        "text": "Dimana tepatnya alamat Capem Bandar Buat?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "bandar_buat"}
    },
    {
        "text": "Capem Bandar Buat itu ada di mana ya?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "bandar_buat"}
    },
    {
        "text": "Bisa informasikan di mana letak Capem Bandar Buat?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "bandar_buat"}
    },
    {
        "text": "Di mana posisi Capem Bandar Buat?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "bandar_buat"}
    },

    {
        "text": "Di mana lokasi Capem Bawan?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "bawan"}
    },
    {
        "text": "Alamat Capem Bawan?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "bawan"}
    },
    {
        "text": "Di mana letak Capem Bawan?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "bawan"}
    },
    {
        "text": "Tolong informasikan alamat Capem Bawan?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "bawan"}
    },
    {
        "text": "Capem Bawan itu berlokasi di mana ya?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "bawan"}
    },
    {
        "text": "Di mana tempat Capem Bawan berada?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "bawan"}
    },
    {
        "text": "Dimana tepatnya lokasi Capem Bawan?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "bawan"}
    },

    {
        "text": "Di mana lokasi Capem By Pass Padang?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "by_pass_padang"}
    },
    {
        "text": "Alamat Capem By Pass Padang?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "by_pass_padang"}
    },
    {
        "text": "Tolong beri tahu lokasi Capem By Pass Padang?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "by_pass_padang"}
    },
    {
        "text": "Di mana letak Capem By Pass Padang?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "by_pass_padang"}
    },
    {
        "text": "Dimana alamat Capem By Pass Padang?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "by_pass_padang"}
    },
    {
        "text": "Capem By Pass Padang ada di mana?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "by_pass_padang"}
    },
    {
        "text": "Bisa informasikan lokasi Capem By Pass Padang?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "by_pass_padang"}
    },

    {
        "text": "Di mana lokasi Capem Cipulir Jakarta?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "cipulir_jakarta"}
    },
    {
        "text": "Alamat Capem Cipulir Jakarta?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "cipulir_jakarta"}
    },
    {
        "text": "Dimana saya bisa menemukan Capem Cipulir Jakarta?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "cipulir_jakarta"}
    },
    {
        "text": "Capem Cipulir Jakarta berada di mana?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "cipulir_jakarta"}
    },
    {
        "text": "Tolong beri tahu lokasi Capem Cipulir Jakarta?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "cipulir_jakarta"}
    },
    {
        "text": "Alamat Capem Cipulir Jakarta di mana?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "cipulir_jakarta"}
    },
    {
        "text": "Capem Cipulir Jakarta ada di mana tepatnya?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "cipulir_jakarta"}
    },

    {
        "text": "Di mana lokasi Capem Dangung-Dangung?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "dangung_dangung"}
    },
    {
        "text": "Alamat Capem Dangung-Dangung?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "dangung_dangung"}
    },
    {
        "text": "Dimana tepatnya lokasi Capem Dangung-Dangung?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "dangung_dangung"}
    },
    {
        "text": "Capem Dangung-Dangung berada di mana?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "dangung_dangung"}
    },
    {
        "text": "Tolong informasikan alamat Capem Dangung-Dangung?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "dangung_dangung"}
    },
    {
        "text": "Di mana saya bisa menemukan Capem Dangung-Dangung?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "dangung_dangung"}
    },
    {
        "text": "Dimana lokasi tepatnya untuk Capem Dangung-Dangung?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "dangung_dangung"}
    },

    {
        "text": "Di mana lokasi Capem Indarung Padang?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "indarung_padang"}
    },
    {
        "text": "Alamat Capem Indarung Padang?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "indarung_padang"}
    },
    {
        "text": "Dimana saya bisa menemukan Capem Indarung Padang?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "indarung_padang"}
    },
    {
        "text": "Tolong beritahukan alamat Capem Indarung Padang?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "indarung_padang"}
    },
    {
        "text": "Capem Indarung Padang letaknya di mana?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "indarung_padang"}
    },
    {
        "text": "Dimana lokasi Capem Indarung di Padang?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "indarung_padang"}
    },
    {
        "text": "Di alamat mana Capem Indarung Padang berada?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "indarung_padang"}
    },

    {
        "text": "Di mana lokasi Capem Kambang?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "kambang"}
    },
    {
        "text": "Alamat Capem Kambang?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "kambang"}
    },
    {
        "text": "Dimana saya dapat menemukan Capem Kambang?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "kambang"}
    },
    {
        "text": "Tolong informasikan lokasi Capem Kambang?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "kambang"}
    },
    {
        "text": "Capem Kambang ada di mana ya?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "kambang"}
    },
    {
        "text": "Di mana tempat Capem Kambang berada?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "kambang"}
    },
    {
        "text": "Lokasi Capem Kambang itu di mana?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "kambang"}
    },

    {
        "text": "Di mana lokasi Capem Kantor Gubernur Sumbar?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "kantor_gubernur_sumbar"}
    },
    {
        "text": "Alamat Capem Kantor Gubernur Sumbar?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "kantor_gubernur_sumbar"}
    },
    {
        "text": "Dimana saya bisa menemukan Capem Kantor Gubernur Sumbar?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "kantor_gubernur_sumbar"}
    },
    {
        "text": "Tolong beri informasi mengenai lokasi Capem Kantor Gubernur Sumbar?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "kantor_gubernur_sumbar"}
    },
    {
        "text": "Capem Kantor Gubernur Sumbar berada di mana ya?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "kantor_gubernur_sumbar"}
    },
    {
        "text": "Lokasi Capem Kantor Gubernur Sumbar ada di mana?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "kantor_gubernur_sumbar"}
    },
    {
        "text": "Dimana tepatnya Capem Kantor Gubernur Sumbar berada?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "kantor_gubernur_sumbar"}
    },

    {
        "text": "Di mana lokasi Capem Kinali?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "kinali"}
    },
    {
        "text": "Alamat Capem Kinali?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "kinali"}
    },
    {
        "text": "Dimana saya dapat menemukan Capem Kinali?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "kinali"}
    },
    {
        "text": "Tolong beritahu lokasi Capem Kinali?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "kinali"}
    },
    {
        "text": "Capem Kinali terletak di mana?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "kinali"}
    },
    {
        "text": "Di mana lokasi tepat Capem Kinali?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "kinali"}
    },
    {
        "text": "Capem Kinali ada di mana ya?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "kinali"}
    },

    {
        "text": "Di mana lokasi Capem Kramat Jati Jakarta?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "kramat_jati_jakarta"}
    },
    {
        "text": "Alamat Capem Kramat Jati Jakarta?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "kramat_jati_jakarta"}
    },
    {
        "text": "Dimana lokasi Capem Kramat Jati di Jakarta?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "kramat_jati_jakarta"}
    },
    {
        "text": "Tolong beri tahu alamat Capem Kramat Jati Jakarta?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "kramat_jati_jakarta"}
    },
    {
        "text": "Capem Kramat Jati Jakarta ada di mana?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "kramat_jati_jakarta"}
    },
    {
        "text": "Dimana tepatnya Capem Kramat Jati Jakarta berada?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "kramat_jati_jakarta"}
    },
    {
        "text": "Di daerah mana Capem Kramat Jati Jakarta?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "kramat_jati_jakarta"}
    },

    {
        "text": "Di mana lokasi Capem Lubuk Buaya?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "lubuk_buaya"}
    },
    {
        "text": "Alamat Capem Lubuk Buaya?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "lubuk_buaya"}
    },
    {
        "text": "Dimana Capem Lubuk Buaya berada?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "lubuk_buaya"}
    },
    {
        "text": "Tolong beri tahu alamat Capem Lubuk Buaya?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "lubuk_buaya"}
    },
    {
        "text": "Capem Lubuk Buaya itu ada di mana?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "lubuk_buaya"}
    },
    {
        "text": "Dimana letak Capem Lubuk Buaya?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "lubuk_buaya"}
    },
    {
        "text": "Di mana tepatnya Capem Lubuk Buaya?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "lubuk_buaya"}
    },

    {
        "text": "Di mana lokasi Capem Nangka Pekanbaru?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "nangka_pekanbaru"}
    },
    {
        "text": "Alamat Capem Nangka Pekanbaru?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "nangka_pekanbaru"}
    },
    {
        "text": "Dimana Capem Nangka di Pekanbaru?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "nangka_pekanbaru"}
    },
    {
        "text": "Tolong beritahu saya alamat Capem Nangka Pekanbaru?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "nangka_pekanbaru"}
    },
    {
        "text": "Capem Nangka Pekanbaru itu terletak di mana?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "nangka_pekanbaru"}
    },
    {
        "text": "Dimana tepatnya lokasi Capem Nangka Pekanbaru?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "nangka_pekanbaru"}
    },
    {
        "text": "Bisa sebutkan lokasi Capem Nangka di Pekanbaru?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "nangka_pekanbaru"}
    },

    {
        "text": "Di mana lokasi Capem Niaga Padang?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "niaga_padang"}
    },
    {
        "text": "Alamat Capem Niaga Padang?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "niaga_padang"}
    },
    {
        "text": "Dimana lokasi Capem Niaga di Padang?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "niaga_padang"}
    },
    {
        "text": "Tolong informasikan alamat Capem Niaga Padang?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "niaga_padang"}
    },
    {
        "text": "Capem Niaga Padang berada di mana?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "niaga_padang"}
    },
    {
        "text": "Lokasi Capem Niaga Padang itu di mana tepatnya?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "niaga_padang"}
    },
    {
        "text": "Dimana saya bisa menemukan Capem Niaga Padang?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "niaga_padang"}
    },

    {
        "text": "Di mana lokasi Capem Padang Luar Bukittinggi?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "padang_luar_bukittinggi"}
    },
    {
        "text": "Alamat Capem Padang Luar Bukittinggi?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "padang_luar_bukittinggi"}
    },
    {
        "text": "Dimana lokasi Capem Padang Luar yang ada di Bukittinggi?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "padang_luar_bukittinggi"}
    },
    {
        "text": "Tolong beri tahu alamat Capem Padang Luar Bukittinggi?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "padang_luar_bukittinggi"}
    },
    {
        "text": "Capem Padang Luar Bukittinggi berada di mana ya?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "padang_luar_bukittinggi"}
    },
    {
        "text": "Dimana tepatnya Capem Padang Luar Bukittinggi?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "padang_luar_bukittinggi"}
    },
    {
        "text": "Lokasi Capem Padang Luar Bukittinggi ada di mana?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "padang_luar_bukittinggi"}
    },

    {
        "text": "Di mana lokasi Capem Pasar Bawah Bukittinggi?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "pasar_bawah_bukittinggi"}
    },
    {
        "text": "Alamat Capem Pasar Bawah Bukittinggi?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "pasar_bawah_bukittinggi"}
    },
    {
        "text": "Dimana lokasi Capem Pasar Bawah yang ada di Bukittinggi?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "pasar_bawah_bukittinggi"}
    },
    {
        "text": "Tolong beri tahu alamat Capem Pasar Bawah Bukittinggi?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "pasar_bawah_bukittinggi"}
    },
    {
        "text": "Capem Pasar Bawah Bukittinggi berada di mana ya?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "pasar_bawah_bukittinggi"}
    },
    {
        "text": "Dimana tepatnya Capem Pasar Bawah Bukittinggi?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "pasar_bawah_bukittinggi"}
    },
    {
        "text": "Lokasi Capem Pasar Bawah Bukittinggi ada di mana?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "pasar_bawah_bukittinggi"}
    },

    {
        "text": "Di mana lokasi Capem Pasar Belimbing?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "pasar_belimbing"}
    },
    {
        "text": "Alamat Capem Pasar Belimbing?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "pasar_belimbing"}
    },
    {
        "text": "Dimana Capem Pasar Belimbing berada?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "pasar_belimbing"}
    },
    {
        "text": "Tolong beri tahu lokasi Capem Pasar Belimbing?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "pasar_belimbing"}
    },
    {
        "text": "Capem Pasar Belimbing terletak di mana?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "pasar_belimbing"}
    },
    {
        "text": "Di lokasi mana Capem Pasar Belimbing?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "pasar_belimbing"}
    },
    {
        "text": "Lokasi Capem Pasar Belimbing di mana ya?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "pasar_belimbing"}
    },

    {
        "text": "Di mana lokasi Capem Pasar Ibuh?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "pasar_ibuh"}
    },
    {
        "text": "Alamat Capem Pasar Ibuh?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "pasar_ibuh"}
    },
    {
        "text": "Dimana Capem Pasar Ibuh berada?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "pasar_ibuh"}
    },
    {
        "text": "Tolong beri tahu saya lokasi Capem Pasar Ibuh?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "pasar_ibuh"}
    },
    {
        "text": "Di mana tepatnya Capem Pasar Ibuh?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "pasar_ibuh"}
    },
    {
        "text": "Capem Pasar Ibuh berada di lokasi mana?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "pasar_ibuh"}
    },
    {
        "text": "Lokasi Capem Pasar Ibuh di mana?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "pasar_ibuh"}
    },

    {
        "text": "Di mana lokasi Capem Pasar Koto Agung?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "pasar_koto_agung"}
    },
    {
        "text": "Alamat Capem Pasar Koto Agung?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "pasar_koto_agung"}
    },
    {
        "text": "Capem Pasar Koto Agung ada di mana ya?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "pasar_koto_agung"}
    },
    {
        "text": "Bisa kasih tahu lokasi Capem Pasar Koto Agung?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "pasar_koto_agung"}
    },
    {
        "text": "Saya ingin tahu di mana letak Capem Pasar Koto Agung.",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "pasar_koto_agung"}
    },
    {
        "text": "Tolong infokan alamat Capem Pasar Koto Agung.",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "pasar_koto_agung"}
    },
    {
        "text": "Dimana saya bisa menemukan Capem Pasar Koto Agung?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "pasar_koto_agung"}
    },

    {
        "text": "Di mana lokasi Capem Pasar Sijunjung?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "pasar_sijunjung"}
    },
    {
        "text": "Alamat Capem Pasar Sijunjung?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "pasar_sijunjung"}
    },
    {
        "text": "Capem Pasar Sijunjung itu lokasinya di mana ya?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "pasar_sijunjung"}
    },
    {
        "text": "Bisa bantu info alamat Capem Pasar Sijunjung?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "pasar_sijunjung"}
    },
    {
        "text": "Saya mau tahu letak Capem Pasar Sijunjung di mana.",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "pasar_sijunjung"}
    },
    {
        "text": "Tolong kasih tahu lokasi Capem Pasar Sijunjung.",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "pasar_sijunjung"}
    },
    {
        "text": "Dimana saya bisa menemukan Capem Pasar Sijunjung?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "pasar_sijunjung"}
    },

    {
        "text": "Di mana lokasi Capem Ranah Batahan?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "ranah_batahan"}
    },
    {
        "text": "Alamat Capem Ranah Batahan?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "ranah_batahan"}
    },
    {
        "text": "Apakah kamu tahu di mana Capem Ranah Batahan berada?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "ranah_batahan"}
    },
    {
        "text": "Capem Ranah Batahan itu terletak di daerah mana, ya?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "ranah_batahan"}
    },
    {
        "text": "Saya sedang mencari lokasi Capem Ranah Batahan, bisa bantu?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "ranah_batahan"}
    },
    {
        "text": "Tahu nggak, Capem Ranah Batahan itu di mana posisinya?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "ranah_batahan"}
    },
    {
        "text": "Boleh info lokasi lengkap Capem Ranah Batahan?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "ranah_batahan"}
    },

    {
        "text": "Di mana lokasi Capem RSUP Dr. M. Djamil?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "rsup_dr_m_djamil"}
    },
    {
        "text": "Alamat Capem RSUP Dr. M. Djamil?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "rsup_dr_m_djamil"}
    },
    {
        "text": "Capem RSUP Dr. M. Djamil itu beralamat di mana ya?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "rsup_dr_m_djamil"}
    },
    {
        "text": "Saya ingin mengetahui posisi Capem RSUP Dr. M. Djamil, bisa bantu?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "rsup_dr_m_djamil"}
    },
    {
        "text": "Tolong arahkan saya ke Capem RSUP Dr. M. Djamil, letaknya di mana?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "rsup_dr_m_djamil"}
    },
    {
        "text": "Di daerah mana saya bisa menemukan Capem RSUP Dr. M. Djamil?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "rsup_dr_m_djamil"}
    },
    {
        "text": "Bisa diinformasikan letak Capem RSUP Dr. M. Djamil secara detail?",
        "intent": "capem_inquiry",
        "entities": {"capem_name": "rsup_dr_m_djamil"}
    },

    {"text": "Di mana lokasi Capem Siberut?", "intent": "capem_inquiry",
        "entities": {"capem_name": "siberut"}},
    {"text": "Alamat Capem Siberut?", "intent": "capem_inquiry",
        "entities": {"capem_name": "siberut"}},
    {"text": "Bisa beritahu saya Capem Siberut itu berada di mana?",
        "intent": "capem_inquiry", "entities": {"capem_name": "siberut"}},
    {"text": "Saya sedang cari alamat Capem Siberut, ada infonya?",
        "intent": "capem_inquiry", "entities": {"capem_name": "siberut"}},
    {"text": "Tahu nggak lokasi Capem Siberut yang paling dekat?",
        "intent": "capem_inquiry", "entities": {"capem_name": "siberut"}},
    {"text": "Capem Siberut itu letaknya di wilayah mana?",
        "intent": "capem_inquiry", "entities": {"capem_name": "siberut"}},
    {"text": "Kalau mau ke Capem Siberut, harus ke mana ya?",
        "intent": "capem_inquiry", "entities": {"capem_name": "siberut"}},

    {"text": "Di mana lokasi Capem Sicincin?", "intent": "capem_inquiry",
        "entities": {"capem_name": "sicincin"}},
    {"text": "Alamat Capem Sicincin?", "intent": "capem_inquiry",
        "entities": {"capem_name": "sicincin"}},
    {"text": "Capem Sicincin itu ada di sebelah mana, ya?",
        "intent": "capem_inquiry", "entities": {"capem_name": "sicincin"}},
    {"text": "Mohon informasi letak Capem Sicincin, di mana tepatnya?",
        "intent": "capem_inquiry", "entities": {"capem_name": "sicincin"}},
    {"text": "Saya perlu petunjuk arah ke Capem Sicincin, bisa bantu?",
        "intent": "capem_inquiry", "entities": {"capem_name": "sicincin"}},
    {"text": "Di wilayah mana Capem Sicincin beroperasi?",
        "intent": "capem_inquiry", "entities": {"capem_name": "sicincin"}},
    {"text": "Tolong kasih info lokasi Capem Sicincin secara lengkap.",
        "intent": "capem_inquiry", "entities": {"capem_name": "sicincin"}},

    {"text": "Di mana lokasi Capem Silaut?", "intent": "capem_inquiry",
        "entities": {"capem_name": "silaut"}},
    {"text": "Alamat Capem Silaut?", "intent": "capem_inquiry",
        "entities": {"capem_name": "silaut"}},
    {"text": "Kamu tahu nggak Capem Silaut itu letaknya di mana?",
        "intent": "capem_inquiry", "entities": {"capem_name": "silaut"}},
    {"text": "Saya butuh info lokasi Capem Silaut, bisa dibantu?",
        "intent": "capem_inquiry", "entities": {"capem_name": "silaut"}},
    {"text": "Capem Silaut itu berada di area mana ya?",
        "intent": "capem_inquiry", "entities": {"capem_name": "silaut"}},
    {"text": "Boleh tanya, Capem Silaut itu posisinya di mana?",
        "intent": "capem_inquiry", "entities": {"capem_name": "silaut"}},
    {"text": "Dimanakah alamat lengkap dari Capem Silaut?",
        "intent": "capem_inquiry", "entities": {"capem_name": "silaut"}},

    {"text": "Di mana lokasi Capem Simpang Haru?", "intent": "capem_inquiry",
        "entities": {"capem_name": "simpang_haru"}},
    {"text": "Alamat Capem Simpang Haru?", "intent": "capem_inquiry",
     "entities": {"capem_name": "simpang_haru"}},
    {"text": "Capem Simpang Haru terletak di mana ya, bisa bantu?",
     "intent": "capem_inquiry", "entities": {"capem_name": "simpang_haru"}},
    {"text": "Saya ingin mencari Capem Simpang Haru, lokasinya di mana?",
     "intent": "capem_inquiry", "entities": {"capem_name": "simpang_haru"}},
    {"text": "Boleh tahu posisi Capem Simpang Haru itu di mana?",
     "intent": "capem_inquiry", "entities": {"capem_name": "simpang_haru"}},
    {"text": "Capem Simpang Haru itu berada di area mana, ya?",
     "intent": "capem_inquiry", "entities": {"capem_name": "simpang_haru"}},
    {"text": "Tolong beri info alamat Capem Simpang Haru.",
     "intent": "capem_inquiry", "entities": {"capem_name": "simpang_haru"}},

    {"text": "Di mana lokasi Capem Sungai Limau?", "intent": "capem_inquiry",
     "entities": {"capem_name": "sungai_limau"}},
    {"text": "Alamat Capem Sungai Limau?", "intent": "capem_inquiry",
     "entities": {"capem_name": "sungai_limau"}},
    {"text": "Capem Sungai Limau itu adanya di mana, ya?",
     "intent": "capem_inquiry", "entities": {"capem_name": "sungai_limau"}},
    {"text": "Saya ingin tahu lokasi pasti Capem Sungai Limau.",
     "intent": "capem_inquiry", "entities": {"capem_name": "sungai_limau"}},
    {"text": "Bisa bantu tunjukkan di mana letak Capem Sungai Limau?",
     "intent": "capem_inquiry", "entities": {"capem_name": "sungai_limau"}},
    {"text": "Capem Sungai Limau itu terletak di daerah mana?",
     "intent": "capem_inquiry", "entities": {"capem_name": "sungai_limau"}},
    {"text": "Mohon informasi alamat Capem Sungai Limau, ada?",
     "intent": "capem_inquiry", "entities": {"capem_name": "sungai_limau"}},

    {"text": "Di mana lokasi Capem Sungai Rumbai?", "intent": "capem_inquiry",
     "entities": {"capem_name": "sungai_rumbai"}},
    {"text": "Alamat Capem Sungai Rumbai?", "intent": "capem_inquiry",
     "entities": {"capem_name": "sungai_rumbai"}},
    {"text": "Bisa kasih tahu saya di mana Capem Sungai Rumbai berada?",
     "intent": "capem_inquiry", "entities": {"capem_name": "sungai_rumbai"}},
    {"text": "Saya lagi cari Capem Sungai Rumbai, tahu lokasinya?",
     "intent": "capem_inquiry", "entities": {"capem_name": "sungai_rumbai"}},
    {"text": "Capem Sungai Rumbai itu posisinya di mana ya?",
     "intent": "capem_inquiry", "entities": {"capem_name": "sungai_rumbai"}},
    {"text": "Di kawasan mana Capem Sungai Rumbai bisa ditemukan?",
     "intent": "capem_inquiry", "entities": {"capem_name": "sungai_rumbai"}},
    {"text": "Tolong infokan lokasi Capem Sungai Rumbai secara jelas.",
     "intent": "capem_inquiry", "entities": {"capem_name": "sungai_rumbai"}},

    {"text": "Di mana lokasi Capem Sungai Tambang?", "intent": "capem_inquiry",
     "entities": {"capem_name": "sungai_tambang"}},
    {"text": "Alamat Capem Sungai Tambang?", "intent": "capem_inquiry",
     "entities": {"capem_name": "sungai_tambang"}},
    {"text": "Capem Sungai Tambang itu terletak di mana ya?",
     "intent": "capem_inquiry", "entities": {"capem_name": "sungai_tambang"}},
    {"text": "Saya mau tahu alamat lengkap Capem Sungai Tambang, bisa tolong?",
     "intent": "capem_inquiry", "entities": {"capem_name": "sungai_tambang"}},
    {"text": "Bisa jelaskan lokasi Capem Sungai Tambang?",
     "intent": "capem_inquiry", "entities": {"capem_name": "sungai_tambang"}},
    {"text": "Dimana saya dapat menemukan Capem Sungai Tambang?",
     "intent": "capem_inquiry", "entities": {"capem_name": "sungai_tambang"}},
    {"text": "Tolong info posisi Capem Sungai Tambang secara detail.",
     "intent": "capem_inquiry", "entities": {"capem_name": "sungai_tambang"}},

    {"text": "Di mana lokasi Capem Syariah Bukittinggi?",
     "intent": "capem_inquiry", "entities": {"capem_name": "syariah_bukittinggi"}},
    {"text": "Alamat Capem Syariah Bukittinggi?", "intent": "capem_inquiry",
     "entities": {"capem_name": "syariah_bukittinggi"}},
    {"text": "Capem Syariah Bukittinggi itu berada di mana, ya?",
     "intent": "capem_inquiry", "entities": {"capem_name": "syariah_bukittinggi"}},
    {"text": "Bisa kasih tahu saya alamat Capem Syariah Bukittinggi?",
     "intent": "capem_inquiry", "entities": {"capem_name": "syariah_bukittinggi"}},
    {"text": "Saya ingin mengetahui lokasi Capem Syariah Bukittinggi.",
     "intent": "capem_inquiry", "entities": {"capem_name": "syariah_bukittinggi"}},
    {"text": "Tolong infokan posisi Capem Syariah Bukittinggi secara lengkap.",
     "intent": "capem_inquiry", "entities": {"capem_name": "syariah_bukittinggi"}},
    {"text": "Di mana saya bisa menemukan Capem Syariah Bukittinggi?",
     "intent": "capem_inquiry", "entities": {"capem_name": "syariah_bukittinggi"}},

    {"text": "Di mana lokasi Capem Syariah Dharmasraya?",
     "intent": "capem_inquiry", "entities": {"capem_name": "syariah_dharmasraya"}},
    {"text": "Alamat Capem Syariah Dharmasraya?", "intent": "capem_inquiry",
     "entities": {"capem_name": "syariah_dharmasraya"}},
    {"text": "Capem Syariah Dharmasraya terletak di mana, ya?",
     "intent": "capem_inquiry", "entities": {"capem_name": "syariah_dharmasraya"}},
    {"text": "Bisa tolong beri tahu alamat Capem Syariah Dharmasraya?",
     "intent": "capem_inquiry", "entities": {"capem_name": "syariah_dharmasraya"}},
    {"text": "Saya mau cari lokasi Capem Syariah Dharmasraya, di mana ya?",
     "intent": "capem_inquiry", "entities": {"capem_name": "syariah_dharmasraya"}},
    {"text": "Tolong infokan posisi Capem Syariah Dharmasraya dengan jelas.",
     "intent": "capem_inquiry", "entities": {"capem_name": "syariah_dharmasraya"}},
    {"text": "Di mana saya dapat menemukan Capem Syariah Dharmasraya?",
     "intent": "capem_inquiry", "entities": {"capem_name": "syariah_dharmasraya"}},

    {"text": "Di mana lokasi Capem Syariah Padang Panjang?",
     "intent": "capem_inquiry", "entities": {"capem_name": "syariah_padang_panjang"}},
    {"text": "Alamat Capem Syariah Padang Panjang?", "intent": "capem_inquiry",
     "entities": {"capem_name": "syariah_padang_panjang"}},
    {"text": "Capem Syariah Padang Panjang itu terletak di mana?",
     "intent": "capem_inquiry", "entities": {"capem_name": "syariah_padang_panjang"}},
    {"text": "Bisa beri tahu saya alamat Capem Syariah Padang Panjang?",
     "intent": "capem_inquiry", "entities": {"capem_name": "syariah_padang_panjang"}},
    {"text": "Saya ingin mengetahui posisi Capem Syariah Padang Panjang.",
     "intent": "capem_inquiry", "entities": {"capem_name": "syariah_padang_panjang"}},
    {"text": "Tolong infokan lokasi Capem Syariah Padang Panjang secara lengkap.",
     "intent": "capem_inquiry", "entities": {"capem_name": "syariah_padang_panjang"}},
    {"text": "Dimana saya bisa menemukan Capem Syariah Padang Panjang?",
     "intent": "capem_inquiry", "entities": {"capem_name": "syariah_padang_panjang"}},

    {"text": "Di mana lokasi Capem Syariah Pariaman?",
        "intent": "capem_inquiry", "entities": {"capem_name": "syariah_pariaman"}},
    {"text": "Alamat Capem Syariah Pariaman?", "intent": "capem_inquiry",
        "entities": {"capem_name": "syariah_pariaman"}},
    {"text": "Capem Syariah Pariaman itu berada di mana, ya?",
        "intent": "capem_inquiry", "entities": {"capem_name": "syariah_pariaman"}},
    {"text": "Tolong beritahu saya alamat Capem Syariah Pariaman.",
        "intent": "capem_inquiry", "entities": {"capem_name": "syariah_pariaman"}},
    {"text": "Saya ingin tahu lokasi Capem Syariah Pariaman, bisa bantu?",
        "intent": "capem_inquiry", "entities": {"capem_name": "syariah_pariaman"}},
    {"text": "Di mana persisnya Capem Syariah Pariaman berada?",
        "intent": "capem_inquiry", "entities": {"capem_name": "syariah_pariaman"}},
    {"text": "Bisa infokan letak Capem Syariah Pariaman?",
        "intent": "capem_inquiry", "entities": {"capem_name": "syariah_pariaman"}},

    {"text": "Di mana lokasi Capem Syariah Simpang Empat?",
        "intent": "capem_inquiry", "entities": {"capem_name": "syariah_simpang_empat"}},
    {"text": "Alamat Capem Syariah Simpang Empat?", "intent": "capem_inquiry",
        "entities": {"capem_name": "syariah_simpang_empat"}},
    {"text": "Capem Syariah Simpang Empat itu posisinya di mana, ya?",
        "intent": "capem_inquiry", "entities": {"capem_name": "syariah_simpang_empat"}},
    {"text": "Saya mau tahu alamat Capem Syariah Simpang Empat, bisa bantu?",
        "intent": "capem_inquiry", "entities": {"capem_name": "syariah_simpang_empat"}},
    {"text": "Tolong beritahu saya lokasi Capem Syariah Simpang Empat.",
        "intent": "capem_inquiry", "entities": {"capem_name": "syariah_simpang_empat"}},
    {"text": "Dimana tepatnya Capem Syariah Simpang Empat berada?",
        "intent": "capem_inquiry", "entities": {"capem_name": "syariah_simpang_empat"}},
    {"text": "Bisa kasih info lokasi lengkap Capem Syariah Simpang Empat?",
        "intent": "capem_inquiry", "entities": {"capem_name": "syariah_simpang_empat"}},

    {"text": "Di mana lokasi Capem Talawi?", "intent": "capem_inquiry",
        "entities": {"capem_name": "talawi"}},
    {"text": "Alamat Capem Talawi?", "intent": "capem_inquiry",
        "entities": {"capem_name": "talawi"}},
    {"text": "Capem Talawi itu berada di mana, ya?",
        "intent": "capem_inquiry", "entities": {"capem_name": "talawi"}},
    {"text": "Tolong beritahu saya alamat Capem Talawi.",
        "intent": "capem_inquiry", "entities": {"capem_name": "talawi"}},
    {"text": "Saya mau tahu lokasi Capem Talawi, bisa bantu?",
        "intent": "capem_inquiry", "entities": {"capem_name": "talawi"}},
    {"text": "Di mana persisnya Capem Talawi berada?",
        "intent": "capem_inquiry", "entities": {"capem_name": "talawi"}},
    {"text": "Bisa infokan letak Capem Talawi?",
        "intent": "capem_inquiry", "entities": {"capem_name": "talawi"}},

    {"text": "Di mana lokasi Capem Tanah Abang Jakarta?",
        "intent": "capem_inquiry", "entities": {"capem_name": "tanah_abang_jakarta"}},
    {"text": "Alamat Capem Tanah Abang Jakarta?", "intent": "capem_inquiry",
     "entities": {"capem_name": "tanah_abang_jakarta"}},
    {"text": "Capem Tanah Abang Jakarta itu terletak di mana?",
     "intent": "capem_inquiry", "entities": {"capem_name": "tanah_abang_jakarta"}},
    {"text": "Bisa kasih tahu saya alamat Capem Tanah Abang Jakarta?",
     "intent": "capem_inquiry", "entities": {"capem_name": "tanah_abang_jakarta"}},
    {"text": "Saya ingin mengetahui posisi Capem Tanah Abang Jakarta.",
     "intent": "capem_inquiry", "entities": {"capem_name": "tanah_abang_jakarta"}},
    {"text": "Tolong infokan lokasi Capem Tanah Abang Jakarta secara lengkap.",
     "intent": "capem_inquiry", "entities": {"capem_name": "tanah_abang_jakarta"}},
    {"text": "Di mana saya bisa menemukan Capem Tanah Abang Jakarta?",
     "intent": "capem_inquiry", "entities": {"capem_name": "tanah_abang_jakarta"}},

    {"text": "Di mana lokasi Capem Tarusan?", "intent": "capem_inquiry",
     "entities": {"capem_name": "tarusan"}},
    {"text": "Alamat Capem Tarusan?", "intent": "capem_inquiry",
     "entities": {"capem_name": "tarusan"}},
    {"text": "Capem Tarusan itu ada di mana, ya?",
     "intent": "capem_inquiry", "entities": {"capem_name": "tarusan"}},
    {"text": "Bisa tolong beri tahu alamat Capem Tarusan?",
     "intent": "capem_inquiry", "entities": {"capem_name": "tarusan"}},
    {"text": "Saya ingin tahu lokasi Capem Tarusan, bisa bantu?",
     "intent": "capem_inquiry", "entities": {"capem_name": "tarusan"}},
    {"text": "Tolong infokan posisi Capem Tarusan dengan jelas.",
     "intent": "capem_inquiry", "entities": {"capem_name": "tarusan"}},
    {"text": "Di mana saya dapat menemukan Capem Tarusan?",
     "intent": "capem_inquiry", "entities": {"capem_name": "tarusan"}},

    {"text": "Di mana lokasi Capem Tigo Nagari?", "intent": "capem_inquiry",
     "entities": {"capem_name": "tigo_nagari"}},
    {"text": "Alamat Capem Tigo Nagari?", "intent": "capem_inquiry",
     "entities": {"capem_name": "tigo_nagari"}},
    {"text": "Capem Tigo Nagari itu berada di mana, ya?",
     "intent": "capem_inquiry", "entities": {"capem_name": "tigo_nagari"}},
    {"text": "Bisa beritahu saya alamat Capem Tigo Nagari?",
     "intent": "capem_inquiry", "entities": {"capem_name": "tigo_nagari"}},
    {"text": "Saya ingin tahu lokasi Capem Tigo Nagari, bisa bantu?",
     "intent": "capem_inquiry", "entities": {"capem_name": "tigo_nagari"}},
    {"text": "Tolong infokan posisi Capem Tigo Nagari dengan jelas.",
     "intent": "capem_inquiry", "entities": {"capem_name": "tigo_nagari"}},
    {"text": "Di mana saya dapat menemukan Capem Tigo Nagari?",
     "intent": "capem_inquiry", "entities": {"capem_name": "tigo_nagari"}},

    {"text": "Di mana lokasi Capem Ulak Karang?", "intent": "capem_inquiry",
     "entities": {"capem_name": "ulak_karang"}},
    {"text": "Alamat Capem Ulak Karang?", "intent": "capem_inquiry",
     "entities": {"capem_name": "ulak_karang"}},
    {"text": "Capem Ulak Karang itu ada di mana, ya?",
     "intent": "capem_inquiry", "entities": {"capem_name": "ulak_karang"}},
    {"text": "Bisa kasih tahu alamat Capem Ulak Karang?",
     "intent": "capem_inquiry", "entities": {"capem_name": "ulak_karang"}},
    {"text": "Saya ingin mengetahui lokasi Capem Ulak Karang, bisa bantu?",
     "intent": "capem_inquiry", "entities": {"capem_name": "ulak_karang"}},
    {"text": "Tolong infokan posisi Capem Ulak Karang secara lengkap.",
     "intent": "capem_inquiry", "entities": {"capem_name": "ulak_karang"}},
    {"text": "Di mana saya bisa menemukan Capem Ulak Karang?",
     "intent": "capem_inquiry", "entities": {"capem_name": "ulak_karang"}},

    {"text": "Di mana lokasi Capem Universitas Bung Hatta?",
     "intent": "capem_inquiry", "entities": {"capem_name": "universitas_bung_hatta"}},
    {"text": "Alamat Capem Universitas Bung Hatta?", "intent": "capem_inquiry",
     "entities": {"capem_name": "universitas_bung_hatta"}},
    {"text": "Capem Universitas Bung Hatta itu terletak di mana?",
     "intent": "capem_inquiry", "entities": {"capem_name": "universitas_bung_hatta"}},
    {"text": "Bisa beri tahu saya alamat Capem Universitas Bung Hatta?",
     "intent": "capem_inquiry", "entities": {"capem_name": "universitas_bung_hatta"}},
    {"text": "Saya ingin mengetahui posisi Capem Universitas Bung Hatta.",
     "intent": "capem_inquiry", "entities": {"capem_name": "universitas_bung_hatta"}},
    {"text": "Tolong infokan lokasi Capem Universitas Bung Hatta secara lengkap.",
     "intent": "capem_inquiry", "entities": {"capem_name": "universitas_bung_hatta"}},
    {"text": "Di mana saya bisa menemukan Capem Universitas Bung Hatta?",
     "intent": "capem_inquiry", "entities": {"capem_name": "universitas_bung_hatta"}},

    {"text": "Di mana lokasi Kantor Kas Alai Padang?",
        "intent": "branch_kas_inquiry", "entities": {"branch_kas_name": "alai_padang"}},
    {"text": "Alamat Kantor Kas Alai Padang?", "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "alai_padang"}},
    {"text": "Kantor Kas Alai Padang berada di mana?",
        "intent": "branch_kas_inquiry", "entities": {"branch_kas_name": "alai_padang"}},
    {"text": "Dimanakah lokasi dari Kantor Kas Alai Padang?",
        "intent": "branch_kas_inquiry", "entities": {"branch_kas_name": "alai_padang"}},
    {"text": "Tolong informasikan alamat Kantor Kas Alai Padang!",
        "intent": "branch_kas_inquiry", "entities": {"branch_kas_name": "alai_padang"}},
    {"text": "Saya ingin tahu di mana Kantor Kas Alai Padang berada?",
        "intent": "branch_kas_inquiry", "entities": {"branch_kas_name": "alai_padang"}},
    {"text": "Lokasi Kantor Kas Alai Padang itu di mana ya?",
        "intent": "branch_kas_inquiry", "entities": {"branch_kas_name": "alai_padang"}},

    {"text": "Di mana lokasi Kantor Kas Balaikota Bukittinggi?",
        "intent": "branch_kas_inquiry", "entities": {"branch_kas_name": "balaikota_bukittinggi"}},
    {"text": "Alamat Kantor Kas Balaikota Bukittinggi?", "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "balaikota_bukittinggi"}},
    {"text": "Kantor Kas Balaikota Bukittinggi letaknya di mana?",
        "intent": "branch_kas_inquiry", "entities": {"branch_kas_name": "balaikota_bukittinggi"}},
    {"text": "Dimana lokasi Kantor Kas di Balaikota Bukittinggi?",
        "intent": "branch_kas_inquiry", "entities": {"branch_kas_name": "balaikota_bukittinggi"}},
    {"text": "Tolong beri tahu di mana alamat Kantor Kas Balaikota Bukittinggi?",
        "intent": "branch_kas_inquiry", "entities": {"branch_kas_name": "balaikota_bukittinggi"}},
    {"text": "Saya ingin tahu di mana tepatnya Kantor Kas Balaikota Bukittinggi?",
        "intent": "branch_kas_inquiry", "entities": {"branch_kas_name": "balaikota_bukittinggi"}},
    {"text": "Lokasi dari Kantor Kas Balaikota Bukittinggi itu di mana?",
        "intent": "branch_kas_inquiry", "entities": {"branch_kas_name": "balaikota_bukittinggi"}},

    {"text": "Di mana lokasi Kantor Kas Balaikota Padang?",
        "intent": "branch_kas_inquiry", "entities": {"branch_kas_name": "balaikota_padang"}},
    {"text": "Alamat Kantor Kas Balaikota Padang?", "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "balaikota_padang"}},
    {"text": "Kantor Kas Balaikota Padang ada di mana ya?",
        "intent": "branch_kas_inquiry", "entities": {"branch_kas_name": "balaikota_padang"}},
    {"text": "Lokasi Kantor Kas di Balaikota Padang itu di mana?",
        "intent": "branch_kas_inquiry", "entities": {"branch_kas_name": "balaikota_padang"}},
    {"text": "Di mana alamat Kantor Kas Balaikota Padang?",
        "intent": "branch_kas_inquiry", "entities": {"branch_kas_name": "balaikota_padang"}},
    {"text": "Tolong beritahu saya di mana letak Kantor Kas Balaikota Padang?",
        "intent": "branch_kas_inquiry", "entities": {"branch_kas_name": "balaikota_padang"}},
    {"text": "Saya ingin tahu lokasi dari Kantor Kas Balaikota Padang, di mana ya?",
        "intent": "branch_kas_inquiry", "entities": {"branch_kas_name": "balaikota_padang"}},

    {"text": "Di mana lokasi Kantor Kas Balaikota Pariaman?",
        "intent": "branch_kas_inquiry", "entities": {"branch_kas_name": "balaikota_pariaman"}},
    {"text": "Alamat Kantor Kas Balaikota Pariaman?", "intent": "branch_kas_inquiry",
     "entities": {"branch_kas_name": "balaikota_pariaman"}},
    {"text": "Kantor Kas Balaikota Pariaman itu berada di mana?",
     "intent": "branch_kas_inquiry", "entities": {"branch_kas_name": "balaikota_pariaman"}},
    {"text": "Bisa beri tahu saya di mana letak Kantor Kas Balaikota Pariaman?",
     "intent": "branch_kas_inquiry", "entities": {"branch_kas_name": "balaikota_pariaman"}},
    {"text": "Lokasi dari Kantor Kas Balaikota Pariaman ada di mana ya?",
     "intent": "branch_kas_inquiry", "entities": {"branch_kas_name": "balaikota_pariaman"}},
    {"text": "Di kawasan mana saya bisa menemukan Kantor Kas Balaikota Pariaman?",
     "intent": "branch_kas_inquiry", "entities": {"branch_kas_name": "balaikota_pariaman"}},
    {"text": "Tolong informasikan di mana Kantor Kas Balaikota Pariaman berada?",
     "intent": "branch_kas_inquiry", "entities": {"branch_kas_name": "balaikota_pariaman"}},

    {"text": "Di mana lokasi Kantor Kas Bandara Internasional Minangkabau?",
     "intent": "branch_kas_inquiry", "entities": {"branch_kas_name": "bandara_internasional_minangkabau"}},
    {"text": "Alamat Kantor Kas Bandara Internasional Minangkabau?", "intent": "branch_kas_inquiry",
     "entities": {"branch_kas_name": "bandara_internasional_minangkabau"}},
    {"text": "Kantor Kas Bandara Internasional Minangkabau ada di mana?", "intent": "branch_kas_inquiry",
     "entities": {"branch_kas_name": "bandara_internasional_minangkabau"}},
    {"text": "Di mana saya bisa menemukan Kantor Kas di Bandara Internasional Minangkabau?",
     "intent": "branch_kas_inquiry", "entities": {"branch_kas_name": "bandara_internasional_minangkabau"}},
    {"text": "Lokasi Kantor Kas di Bandara Internasional Minangkabau itu di mana?",
     "intent": "branch_kas_inquiry", "entities": {"branch_kas_name": "bandara_internasional_minangkabau"}},
    {"text": "Tolong beri tahu saya di mana letak Kantor Kas Bandara Internasional Minangkabau?",
     "intent": "branch_kas_inquiry", "entities": {"branch_kas_name": "bandara_internasional_minangkabau"}},
    {"text": "Apakah Anda tahu di mana Kantor Kas yang ada di Bandara Internasional Minangkabau?",
     "intent": "branch_kas_inquiry", "entities": {"branch_kas_name": "bandara_internasional_minangkabau"}},

    {"text": "Di mana lokasi Kantor Kas Dispenda Sumatera Barat?",
     "intent": "branch_kas_inquiry", "entities": {"branch_kas_name": "dispenda_sumatera_barat"}},
    {"text": "Alamat Kantor Kas Dispenda Sumatera Barat?", "intent": "branch_kas_inquiry",
     "entities": {"branch_kas_name": "dispenda_sumatera_barat"}},
    {"text": "Kantor Kas Dispenda Sumatera Barat ada di mana ya?",
     "intent": "branch_kas_inquiry", "entities": {"branch_kas_name": "dispenda_sumatera_barat"}},
    {"text": "Di mana tepatnya alamat Kantor Kas Dispenda Sumatera Barat?",
     "intent": "branch_kas_inquiry", "entities": {"branch_kas_name": "dispenda_sumatera_barat"}},
    {"text": "Saya ingin tahu lokasi Kantor Kas Dispenda Sumatera Barat, di mana ya?",
     "intent": "branch_kas_inquiry", "entities": {"branch_kas_name": "dispenda_sumatera_barat"}},
    {"text": "Lokasi Kantor Kas Dispenda di Sumatera Barat itu di mana?",
     "intent": "branch_kas_inquiry", "entities": {"branch_kas_name": "dispenda_sumatera_barat"}},
    {"text": "Bisa beri tahu saya di mana letak Kantor Kas Dispenda Sumatera Barat?",
     "intent": "branch_kas_inquiry", "entities": {"branch_kas_name": "dispenda_sumatera_barat"}},

    {
        "text": "Di mana lokasi Kantor Kas DPKAD Bukittinggi?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "DPKAD Bukittinggi"}
    },
    {
        "text": "Alamat Kantor Kas DPKAD Bukittinggi?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "DPKAD Bukittinggi"}
    },
    {
        "text": "Di kawasan mana saya bisa menemukan Kantor Kas DPKAD Bukittinggi?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "DPKAD Bukittinggi"}
    },
    {
        "text": "Lokasi Kantor Kas DPKAD Bukittinggi itu ada di mana ya?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "DPKAD Bukittinggi"}
    },
    {
        "text": "Tolong beri tahu saya di mana letak Kantor Kas DPKAD di Bukittinggi?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "DPKAD Bukittinggi"}
    },
    {
        "text": "Kantor Kas DPKAD Bukittinggi itu terletak di mana?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "DPKAD Bukittinggi"}
    },
    {
        "text": "Dimana alamat Kantor Kas DPKAD Bukittinggi berada?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "DPKAD Bukittinggi"}
    },

    {
        "text": "Di mana lokasi Kantor Kas IAIN Imam Bonjol Padang?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "IAIN Imam Bonjol Padang"}
    },
    {
        "text": "Alamat Kantor Kas IAIN Imam Bonjol Padang?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "IAIN Imam Bonjol Padang"}
    },
    {
        "text": "Kantor Kas IAIN Imam Bonjol Padang berada di mana?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "IAIN Imam Bonjol Padang"}
    },
    {
        "text": "Di mana alamat Kantor Kas IAIN Imam Bonjol Padang?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "IAIN Imam Bonjol Padang"}
    },
    {
        "text": "Tolong informasikan lokasi Kantor Kas IAIN Imam Bonjol di Padang?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "IAIN Imam Bonjol Padang"}
    },
    {
        "text": "Saya ingin tahu di mana Kantor Kas IAIN Imam Bonjol Padang?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "IAIN Imam Bonjol Padang"}
    },
    {
        "text": "Lokasi Kantor Kas IAIN Imam Bonjol Padang itu di mana ya?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "IAIN Imam Bonjol Padang"}
    },

    {
        "text": "Di mana lokasi Kantor Kas Jalan Samudera?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Jalan Samudera"}
    },
    {
        "text": "Alamat Kantor Kas Jalan Samudera?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Jalan Samudera"}
    },
    {
        "text": "Kantor Kas di Jalan Samudera itu letaknya di mana?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Jalan Samudera"}
    },
    {
        "text": "Dimana saya bisa menemukan Kantor Kas yang ada di Jalan Samudera?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Jalan Samudera"}
    },
    {
        "text": "Lokasi Kantor Kas di Jalan Samudera itu di mana ya?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Jalan Samudera"}
    },
    {
        "text": "Apakah Anda tahu alamat Kantor Kas di Jalan Samudera?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Jalan Samudera"}
    },
    {
        "text": "Saya ingin tahu di mana Kantor Kas yang terletak di Jalan Samudera?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Jalan Samudera"}
    },

    {
        "text": "Di mana lokasi Kantor Kas Balaikota Padang Panjang?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Balaikota Padang Panjang"}
    },
    {
        "text": "Alamat Kantor Kas Balaikota Padang Panjang?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Balaikota Padang Panjang"}
    },
    {
        "text": "Kantor Kas di Balaikota Padang Panjang itu berada di mana?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Balaikota Padang Panjang"}
    },
    {
        "text": "Di mana saya bisa menemukan Kantor Kas Balaikota Padang Panjang?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Balaikota Padang Panjang"}
    },
    {
        "text": "Lokasi Kantor Kas Balaikota Padang Panjang itu ada di mana?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Balaikota Padang Panjang"}
    },
    {
        "text": "Tolong beritahu saya di mana letak Kantor Kas Balaikota Padang Panjang?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Balaikota Padang Panjang"}
    },
    {
        "text": "Saya ingin tahu lokasi Kantor Kas di Balaikota Padang Panjang, di mana ya?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Balaikota Padang Panjang"}
    },

    {
        "text": "Di mana lokasi Kantor Kas Kantor Bupati Limapuluh Kota?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Bupati Limapuluh Kota"}
    },
    {
        "text": "Alamat Kantor Kas Kantor Bupati Limapuluh Kota?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Bupati Limapuluh Kota"}
    },
    {
        "text": "Kantor Kas Kantor Bupati Limapuluh Kota itu di mana ya?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Bupati Limapuluh Kota"}
    },
    {
        "text": "Lokasi Kantor Kas yang ada di Kantor Bupati Limapuluh Kota itu di mana?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Bupati Limapuluh Kota"}
    },
    {
        "text": "Dimana tepatnya saya bisa menemukan Kantor Kas Kantor Bupati Limapuluh Kota?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Bupati Limapuluh Kota"}
    },
    {
        "text": "Apakah Anda tahu di mana alamat Kantor Kas di Kantor Bupati Limapuluh Kota?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Bupati Limapuluh Kota"}
    },
    {
        "text": "Tolong beri tahu saya di mana letak Kantor Kas di Kantor Bupati Limapuluh Kota?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Bupati Limapuluh Kota"}
    },

    {
        "text": "Di mana lokasi Kantor Kas Kantor Bupati Pariaman?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Bupati Pariaman"}
    },
    {
        "text": "Alamat Kantor Kas Kantor Bupati Pariaman?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Bupati Pariaman"}
    },
    {
        "text": "Kantor Kas di Kantor Bupati Pariaman itu terletak di mana?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Bupati Pariaman"}
    },
    {
        "text": "Dimana lokasi Kantor Kas Kantor Bupati Pariaman ya?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Bupati Pariaman"}
    },
    {
        "text": "Tolong informasikan saya, di mana Kantor Kas Kantor Bupati Pariaman berada?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Bupati Pariaman"}
    },
    {
        "text": "Saya ingin tahu lokasi Kantor Kas yang ada di Kantor Bupati Pariaman, di mana?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Bupati Pariaman"}
    },
    {
        "text": "Apakah Anda tahu di mana letak Kantor Kas Kantor Bupati Pariaman?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Bupati Pariaman"}
    },

    {
        "text": "Di mana lokasi Kantor Kas Kantor Bupati Pasaman Barat?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Bupati Pasaman Barat"}
    },
    {
        "text": "Alamat Kantor Kas Kantor Bupati Pasaman Barat?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Bupati Pasaman Barat"}
    },
    {
        "text": "Kantor Kas yang ada di Kantor Bupati Pasaman Barat itu di mana?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Bupati Pasaman Barat"}
    },
    {
        "text": "Saya ingin tahu, di mana lokasi Kantor Kas Kantor Bupati Pasaman Barat?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Bupati Pasaman Barat"}
    },
    {
        "text": "Dimana alamat Kantor Kas Kantor Bupati Pasaman Barat ya?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Bupati Pasaman Barat"}
    },
    {
        "text": "Lokasi Kantor Kas yang berada di Kantor Bupati Pasaman Barat itu ada di mana?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Bupati Pasaman Barat"}
    },
    {
        "text": "Tolong beri tahu saya di mana tepatnya Kantor Kas Kantor Bupati Pasaman Barat?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Bupati Pasaman Barat"}
    },

    {
        "text": "Di mana lokasi Kantor Kas Kantor Bupati Solok Selatan?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Bupati Solok Selatan"}
    },
    {
        "text": "Alamat Kantor Kas Kantor Bupati Solok Selatan?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Bupati Solok Selatan"}
    },
    {
        "text": "Kantor Kas Kantor Bupati Solok Selatan itu ada di mana ya?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Bupati Solok Selatan"}
    },
    {
        "text": "Dimana saya bisa menemukan Kantor Kas yang berada di Kantor Bupati Solok Selatan?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Bupati Solok Selatan"}
    },
    {
        "text": "Tolong beri tahu di mana lokasi Kantor Kas di Kantor Bupati Solok Selatan?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Bupati Solok Selatan"}
    },
    {
        "text": "Apakah Kantor Kas di Kantor Bupati Solok Selatan itu letaknya di mana?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Bupati Solok Selatan"}
    },
    {
        "text": "Saya ingin tahu, di mana alamat Kantor Kas Kantor Bupati Solok Selatan?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Bupati Solok Selatan"}
    },

    {
        "text": "Di mana lokasi Kantor Kas Kantor Bupati Tanah Datar?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Bupati Tanah Datar"}
    },
    {
        "text": "Alamat Kantor Kas Kantor Bupati Tanah Datar?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Bupati Tanah Datar"}
    },
    {
        "text": "Kantor Kas yang berada di Kantor Bupati Tanah Datar itu letaknya di mana?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Bupati Tanah Datar"}
    },
    {
        "text": "Dimana alamat Kantor Kas Kantor Bupati Tanah Datar ya?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Bupati Tanah Datar"}
    },
    {
        "text": "Saya ingin tahu, di mana lokasi Kantor Kas Kantor Bupati Tanah Datar?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Bupati Tanah Datar"}
    },
    {
        "text": "Tolong informasikan saya, di mana letak Kantor Kas di Kantor Bupati Tanah Datar?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Bupati Tanah Datar"}
    },
    {
        "text": "Lokasi Kantor Kas di Kantor Bupati Tanah Datar itu ada di mana ya?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Bupati Tanah Datar"}
    },

    {
        "text": "Di mana lokasi Kantor Kas Kantor Walikota Sawahlunto?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Walikota Sawahlunto"}
    },
    {
        "text": "Alamat Kantor Kas Kantor Walikota Sawahlunto?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Walikota Sawahlunto"}
    },
    {
        "text": "Kantor Kas Kantor Walikota Sawahlunto itu ada di mana ya?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Walikota Sawahlunto"}
    },
    {
        "text": "Di mana saya bisa menemukan Kantor Kas di Kantor Walikota Sawahlunto?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Walikota Sawahlunto"}
    },
    {
        "text": "Lokasi Kantor Kas di Kantor Walikota Sawahlunto itu terletak di mana?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Walikota Sawahlunto"}
    },
    {
        "text": "Apakah Anda tahu di mana alamat Kantor Kas Kantor Walikota Sawahlunto?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Walikota Sawahlunto"}
    },
    {
        "text": "Tolong beri tahu saya, di mana letak Kantor Kas Kantor Walikota Sawahlunto?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Kantor Walikota Sawahlunto"}
    },

    {
        "text": "Di mana lokasi Kantor Kas Panti?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Panti"}
    },
    {
        "text": "Alamat Kantor Kas Panti?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Panti"}
    },
    {
        "text": "Kantor Kas Panti itu ada di mana ya?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Panti"}
    },
    {
        "text": "Dimana alamat Kantor Kas Panti?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Panti"}
    },
    {
        "text": "Lokasi Kantor Kas Panti itu terletak di mana?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Panti"}
    },
    {
        "text": "Tolong beri tahu saya di mana letak Kantor Kas Panti?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Panti"}
    },
    {
        "text": "Saya ingin tahu, di mana lokasi Kantor Kas Panti?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Panti"}
    },

    {
        "text": "Di mana lokasi Kantor Kas Parit Malintang?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Parit Malintang"}
    },
    {
        "text": "Alamat Kantor Kas Parit Malintang?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Parit Malintang"}
    },
    {
        "text": "Kantor Kas Parit Malintang itu terletak di mana?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Parit Malintang"}
    },
    {
        "text": "Di mana saya bisa menemukan Kantor Kas Parit Malintang?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Parit Malintang"}
    },
    {
        "text": "Lokasi Kantor Kas Parit Malintang itu di mana ya?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Parit Malintang"}
    },
    {
        "text": "Tolong beri tahu saya, di mana alamat Kantor Kas Parit Malintang?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Parit Malintang"}
    },
    {
        "text": "Saya ingin tahu, di mana lokasi Kantor Kas Parit Malintang berada?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Parit Malintang"}
    },

    {
        "text": "Di mana lokasi Kantor Kas Pasar Baru Bandung?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Pasar Baru Bandung"}
    },
    {
        "text": "Alamat Kantor Kas Pasar Baru Bandung?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Pasar Baru Bandung"}
    },
    {
        "text": "Kantor Kas Pasar Baru Bandung itu ada di mana?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Pasar Baru Bandung"}
    },
    {
        "text": "Dimana letak Kantor Kas yang berada di Pasar Baru Bandung?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Pasar Baru Bandung"}
    },
    {
        "text": "Lokasi Kantor Kas Pasar Baru Bandung itu di mana ya?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Pasar Baru Bandung"}
    },
    {
        "text": "Tolong informasikan saya, di mana Kantor Kas Pasar Baru Bandung berada?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Pasar Baru Bandung"}
    },
    {
        "text": "Apakah Anda tahu lokasi Kantor Kas Pasar Baru Bandung?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Pasar Baru Bandung"}
    },

    {
        "text": "Di mana lokasi Kantor Kas Pasar Baru Padang?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Pasar Baru Padang"}
    },
    {
        "text": "Alamat Kantor Kas Pasar Baru Padang?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Pasar Baru Padang"}
    },
    {
        "text": "Kantor Kas Pasar Baru Padang itu berada di mana ya?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Pasar Baru Padang"}
    },
    {
        "text": "Dimana alamat Kantor Kas yang ada di Pasar Baru Padang?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Pasar Baru Padang"}
    },
    {
        "text": "Lokasi Kantor Kas Pasar Baru Padang itu terletak di mana?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Pasar Baru Padang"}
    },
    {
        "text": "Tolong beri tahu saya di mana Kantor Kas Pasar Baru Padang?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Pasar Baru Padang"}
    },
    {
        "text": "Saya ingin tahu, di mana letak Kantor Kas Pasar Baru Padang?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Pasar Baru Padang"}
    },

    {
        "text": "Di mana lokasi Kantor Kas Pasar Raya Padang?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Pasar Raya Padang"}
    },
    {
        "text": "Alamat Kantor Kas Pasar Raya Padang?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Pasar Raya Padang"}
    },
    {
        "text": "Kantor Kas Pasar Raya Padang itu berada di mana ya?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Pasar Raya Padang"}
    },
    {
        "text": "Dimana lokasi Kantor Kas yang ada di Pasar Raya Padang?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Pasar Raya Padang"}
    },
    {
        "text": "Lokasi Kantor Kas Pasar Raya Padang itu di mana?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Pasar Raya Padang"}
    },
    {
        "text": "Tolong informasikan saya, di mana Kantor Kas Pasar Raya Padang?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Pasar Raya Padang"}
    },
    {
        "text": "Apakah Anda tahu di mana alamat Kantor Kas Pasar Raya Padang?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Pasar Raya Padang"}
    },

    {
        "text": "Di mana lokasi Kantor Kas Pasar Raya Solok?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Pasar Raya Solok"}
    },
    {
        "text": "Alamat Kantor Kas Pasar Raya Solok?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Pasar Raya Solok"}
    },
    {
        "text": "Bisa kasih tahu alamat Kantor Kas Pasar Raya Solok?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Pasar Raya Solok"}
    },
    {
        "text": "Saya ingin tahu di mana letak Kantor Kas Pasar Raya Solok.",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Pasar Raya Solok"}
    },
    {
        "text": "Di Solok, Kantor Kas Pasar Raya itu berada di mana ya?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Pasar Raya Solok"}
    },
    {
        "text": "Alamat lengkap Kantor Kas Pasar Raya Solok di mana?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Pasar Raya Solok"}
    },
    {
        "text": "Tolong informasikan lokasi dari Kantor Kas Pasar Raya Solok.",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Pasar Raya Solok"}
    },

    {
        "text": "Di mana lokasi Kantor Kas RSUD Achmad Muchtar?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "RSUD Achmad Muchtar"}
    },
    {
        "text": "Alamat Kantor Kas RSUD Achmad Muchtar?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "RSUD Achmad Muchtar"}
    },
    {
        "text": "Bisa bantu info alamat Kantor Kas RSUD Achmad Muchtar?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "RSUD Achmad Muchtar"}
    },
    {
        "text": "Saya ingin tahu letak Kantor Kas RSUD Achmad Muchtar.",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "RSUD Achmad Muchtar"}
    },
    {
        "text": "Lokasi Kantor Kas di RSUD Achmad Muchtar ada di mana ya?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "RSUD Achmad Muchtar"}
    },
    {
        "text": "Tolong beri tahu di mana posisi Kantor Kas RSUD Achmad Muchtar.",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "RSUD Achmad Muchtar"}
    },
    {
        "text": "Alamat lengkap Kantor Kas di RSUD Achmad Muchtar itu di mana?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "RSUD Achmad Muchtar"}
    },

    {
        "text": "Di mana lokasi Kantor Kas RSUD Adnan WD?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "RSUD Adnan WD"}
    },
    {
        "text": "Alamat Kantor Kas RSUD Adnan WD?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "RSUD Adnan WD"}
    },
    {
        "text": "Dimana saya bisa menemukan Kantor Kas di RSUD Adnan WD?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "RSUD Adnan WD"}
    },
    {
        "text": "Apakah kamu tahu lokasi Kantor Kas RSUD Adnan WD?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "RSUD Adnan WD"}
    },
    {
        "text": "Kantor Kas RSUD Adnan WD terletak di area mana?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "RSUD Adnan WD"}
    },
    {
        "text": "Mohon info posisi Kantor Kas yang ada di RSUD Adnan WD.",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "RSUD Adnan WD"}
    },
    {
        "text": "RSUD Adnan WD punya Kantor Kas di bagian mana ya?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "RSUD Adnan WD"}
    },

    {
        "text": "Di mana lokasi Kantor Kas RSUD Padang Panjang?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "RSUD Padang Panjang"}
    },
    {
        "text": "Alamat Kantor Kas RSUD Padang Panjang?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "RSUD Padang Panjang"}
    },
    {
        "text": "Kantor Kas yang berada di RSUD Padang Panjang itu ada di bagian mana?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "RSUD Padang Panjang"}
    },
    {
        "text": "Saya butuh petunjuk lokasi Kantor Kas di RSUD Padang Panjang.",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "RSUD Padang Panjang"}
    },
    {
        "text": "Bisa dijelaskan di mana Kantor Kas RSUD Padang Panjang berada?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "RSUD Padang Panjang"}
    },
    {
        "text": "Tolong arahkan saya ke lokasi Kantor Kas RSUD Padang Panjang.",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "RSUD Padang Panjang"}
    },
    {
        "text": "Letak Kantor Kas di lingkungan RSUD Padang Panjang itu di mana ya?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "RSUD Padang Panjang"}
    },

    {
        "text": "Di mana lokasi Kantor Kas RSUD Sijunjung?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "RSUD Sijunjung"}
    },
    {
        "text": "Alamat Kantor Kas RSUD Sijunjung?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "RSUD Sijunjung"}
    },
    {
        "text": "Apa kamu tahu di mana saya bisa menemukan Kantor Kas di RSUD Sijunjung?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "RSUD Sijunjung"}
    },
    {
        "text": "Saya mencari Kantor Kas di RSUD Sijunjung, letaknya di mana ya?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "RSUD Sijunjung"}
    },
    {
        "text": "Di area RSUD Sijunjung, Kantor Kas-nya ada di mana?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "RSUD Sijunjung"}
    },
    {
        "text": "Mohon arah lokasi Kantor Kas RSUD Sijunjung.",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "RSUD Sijunjung"}
    },
    {
        "text": "Lokasi persis Kantor Kas yang ada di RSUD Sijunjung itu di mana, ya?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "RSUD Sijunjung"}
    },

    {
        "text": "Di mana lokasi Kantor Kas RSUP P3SN Bukittinggi?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "RSUP P3SN Bukittinggi"}
    },
    {
        "text": "Alamat Kantor Kas RSUP P3SN Bukittinggi?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "RSUP P3SN Bukittinggi"}
    },
    {
        "text": "Di kawasan RSUP P3SN Bukittinggi, Kantor Kas-nya ada di mana?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "RSUP P3SN Bukittinggi"}
    },
    {
        "text": "Saya ingin mencari Kantor Kas di RSUP P3SN Bukittinggi, bisa bantu tunjukkan lokasinya?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "RSUP P3SN Bukittinggi"}
    },
    {
        "text": "Apakah kamu bisa beri tahu posisi Kantor Kas RSUP P3SN Bukittinggi?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "RSUP P3SN Bukittinggi"}
    },
    {
        "text": "Letak Kantor Kas yang berada di RSUP P3SN Bukittinggi itu di mana persisnya?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "RSUP P3SN Bukittinggi"}
    },
    {
        "text": "Saya butuh informasi lokasi Kantor Kas yang ada di RSUP P3SN Bukittinggi.",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "RSUP P3SN Bukittinggi"}
    },

    {
        "text": "Di mana lokasi Kantor Kas Semen Padang Hospital?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Semen Padang Hospital"}
    },
    {
        "text": "Alamat Kantor Kas Semen Padang Hospital?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Semen Padang Hospital"}
    },
    {
        "text": "Kantor Kas yang berada di Semen Padang Hospital berlokasi di mana ya?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Semen Padang Hospital"}
    },
    {
        "text": "Bisa diinformasikan posisi Kantor Kas di area Semen Padang Hospital?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Semen Padang Hospital"}
    },
    {
        "text": "Saya sedang mencari Kantor Kas di Semen Padang Hospital, letaknya di mana?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Semen Padang Hospital"}
    },
    {
        "text": "Tahu nggak lokasi Kantor Kas yang ada di Semen Padang Hospital?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Semen Padang Hospital"}
    },
    {
        "text": "Ada yang tahu di mana Kantor Kas Semen Padang Hospital berada?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Semen Padang Hospital"}
    },

    {
        "text": "Di mana lokasi Kantor Kas Simpang Tiga?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Simpang Tiga"}
    },
    {
        "text": "Alamat Kantor Kas Simpang Tiga?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Simpang Tiga"}
    },
    {
        "text": "Apakah kamu bisa menunjukkan di mana Kantor Kas Simpang Tiga berada?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Simpang Tiga"}
    },
    {
        "text": "Saya perlu tahu posisi Kantor Kas di Simpang Tiga, bisa bantu?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Simpang Tiga"}
    },
    {
        "text": "Letak persis Kantor Kas Simpang Tiga itu di jalan mana ya?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Simpang Tiga"}
    },
    {
        "text": "Di Simpang Tiga, Kantor Kas-nya terletak di sebelah mana?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Simpang Tiga"}
    },
    {
        "text": "Ada info lokasi Kantor Kas yang berada di daerah Simpang Tiga?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Simpang Tiga"}
    },

    {
        "text": "Di mana lokasi Kantor Kas Syariah R.S. Yarsi Ibnu Sina?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Syariah R.S. Yarsi Ibnu Sina"}
    },
    {
        "text": "Alamat Kantor Kas Syariah R.S. Yarsi Ibnu Sina?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Syariah R.S. Yarsi Ibnu Sina"}
    },
    {
        "text": "Di mana letak Kantor Kas Syariah di R.S. Yarsi Ibnu Sina?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Syariah R.S. Yarsi Ibnu Sina"}
    },
    {
        "text": "Tolong beri tahu saya posisi Kantor Kas Syariah di RS Yarsi Ibnu Sina.",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Syariah R.S. Yarsi Ibnu Sina"}
    },
    {
        "text": "Kantor Kas Syariah yang ada di RS Yarsi Ibnu Sina itu di mana ya?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Syariah R.S. Yarsi Ibnu Sina"}
    },
    {
        "text": "Apakah lokasi Kantor Kas Syariah di RS Yarsi Ibnu Sina sudah diketahui?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Syariah R.S. Yarsi Ibnu Sina"}
    },
    {
        "text": "Saya mencari Kantor Kas Syariah di RS Yarsi Ibnu Sina, bisa kasih tahu di mana tempatnya?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Syariah R.S. Yarsi Ibnu Sina"}
    },

    {
        "text": "Di mana lokasi Kantor Kas Tabing?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Tabing"}
    },
    {
        "text": "Alamat Kantor Kas Tabing?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Tabing"}
    },
    {
        "text": "Kantor Kas Tabing ada di daerah mana ya?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Tabing"}
    },
    {
        "text": "Tolong informasikan lokasi Kantor Kas di Tabing.",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Tabing"}
    },
    {
        "text": "Di Tabing, Kantor Kas-nya terletak di mana?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Tabing"}
    },
    {
        "text": "Saya butuh tahu di mana letak Kantor Kas Tabing.",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Tabing"}
    },
    {
        "text": "Lokasi Kantor Kas Tabing itu ada di sebelah mana ya?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Tabing"}
    },

    {
        "text": "Di mana lokasi Kantor Kas Teluk Bayur?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Teluk Bayur"}
    },
    {
        "text": "Alamat Kantor Kas Teluk Bayur?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Teluk Bayur"}
    },
    {
        "text": "Di sekitar Teluk Bayur, Kantor Kas-nya berada di mana ya?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Teluk Bayur"}
    },
    {
        "text": "Kantor Kas Teluk Bayur itu letaknya di mana, ya?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Teluk Bayur"}
    },
    {
        "text": "Bisa kasih tahu di mana saya bisa menemukan Kantor Kas di Teluk Bayur?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Teluk Bayur"}
    },
    {
        "text": "Saya mencari alamat Kantor Kas yang ada di Teluk Bayur, ada info?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Teluk Bayur"}
    },
    {
        "text": "Lokasi tepat Kantor Kas Teluk Bayur itu di mana ya?",
        "intent": "branch_kas_inquiry",
        "entities": {"branch_kas_name": "Teluk Bayur"}
    },

    {
        "text": "Lokasi ATM-2 di Bank Nagari Cabang Utama Padang di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "ATM-2 Cabang Utama Padang"}
    },
    {
        "text": "Di mana ATM-2 di Kantor Bank Nagari Cabang Utama Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "ATM-2 Cabang Utama Padang"}
    },
    {
        "text": "Bisa beri tahu saya alamat ATM-2 di Cabang Utama Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "ATM-2 Cabang Utama Padang"}
    },
    {
        "text": "Tolong beritahu saya lokasi ATM 2 di Bank Nagari Cabang Utama Padang",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "ATM-2 Cabang Utama Padang"}
    },

    {
        "text": "Lokasi ATM-3 di Kantor Bank Nagari Cabang Utama Padang di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "ATM-3 Cabang Utama Padang"}
    },
    {
        "text": "Dimana letak ATM-3 di Bank Nagari Cabang Utama Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "ATM-3 Cabang Utama Padang"}
    },
    {
        "text": "Apa alamat ATM-3 di Cabang Utama Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "ATM-3 Cabang Utama Padang"}
    },
    {
        "text": "Di mana saya bisa menemukan ATM 3 di Kantor Bank Nagari Utama Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "ATM-3 Cabang Utama Padang"}
    },

    {
        "text": "Lokasi ATM-4 di Kantor Bank Nagari Cabang Utama Padang di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "ATM-4 Cabang Utama Padang"}
    },
    {
        "text": "Tolong sebutkan lokasi ATM-4 di Bank Nagari Cabang Utama Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "ATM-4 Cabang Utama Padang"}
    },
    {
        "text": "Apa alamat ATM-4 di Cabang Utama Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "ATM-4 Cabang Utama Padang"}
    },
    {
        "text": "Di mana letak ATM-4 di Kantor Bank Nagari Cabang Utama Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "ATM-4 Cabang Utama Padang"}
    },

    {
        "text": "Di mana lokasi ATM di SJS Plaza Lapai Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "SJS Plaza Lapai Padang"}
    },
    {
        "text": "Alamat ATM di SJS Plaza Lapai Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "SJS Plaza Lapai Padang"}
    },
    {
        "text": "ATM di SJS Plaza Lapai Padang itu ada di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "SJS Plaza Lapai Padang"}
    },
    {
        "text": "Di SJS Plaza Lapai Padang, ATM-nya terletak di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "SJS Plaza Lapai Padang"}
    },
    {
        "text": "Tolong beri tahu saya lokasi ATM yang ada di SJS Plaza Lapai Padang.",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "SJS Plaza Lapai Padang"}
    },
    {
        "text": "Saya ingin tahu di mana ATM di area SJS Plaza Lapai Padang berada.",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "SJS Plaza Lapai Padang"}
    },
    {
        "text": "Lokasi ATM yang ada di SJS Plaza Lapai Padang itu ada di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "SJS Plaza Lapai Padang"}
    },

    {
        "text": "Di mana lokasi ATM di Tee Box ATM Center?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Tee Box ATM Center"}
    },
    {
        "text": "Alamat ATM di Tee Box ATM Center?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Tee Box ATM Center"}
    },
    {
        "text": "Tolong beri tahu lokasi ATM yang ada di Tee Box ATM Center?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Tee Box ATM Center"}
    },
    {
        "text": "Lokasi ATM di Tee Box ATM Center itu ada di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Tee Box ATM Center"}
    },
    {
        "text": "Di Tee Box ATM Center, posisi ATM-nya di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Tee Box ATM Center"}
    },
    {
        "text": "Saya butuh informasi tentang lokasi ATM di Tee Box ATM Center, bisa bantu?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Tee Box ATM Center"}
    },
    {
        "text": "Tahu nggak di mana tempat ATM yang ada di Tee Box ATM Center?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Tee Box ATM Center"}
    },

    {
        "text": "Di mana lokasi ATM di Komplek RSU Islam Siti Rahmah Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek RSU Islam Siti Rahmah Padang"}
    },
    {
        "text": "Alamat ATM di Komplek RSU Islam Siti Rahmah Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek RSU Islam Siti Rahmah Padang"}
    },
    {
        "text": "Posisi ATM di Komplek RSU Islam Siti Rahmah Padang itu ada di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek RSU Islam Siti Rahmah Padang"}
    },
    {
        "text": "Lokasi ATM yang ada di Komplek RSU Islam Siti Rahmah Padang, bisa dijelaskan?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek RSU Islam Siti Rahmah Padang"}
    },
    {
        "text": "Tolong beri tahu saya di mana ATM di Komplek RSU Islam Siti Rahmah Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek RSU Islam Siti Rahmah Padang"}
    },
    {
        "text": "Di Komplek RSU Islam Siti Rahmah Padang, lokasi ATM-nya ada di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek RSU Islam Siti Rahmah Padang"}
    },
    {
        "text": "ATM di Komplek RSU Islam Siti Rahmah Padang itu terletak di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek RSU Islam Siti Rahmah Padang"}
    },

    {
        "text": "Di mana lokasi ATM di Basko Grand Mall Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Basko Grand Mall Padang"}
    },
    {
        "text": "Alamat ATM di Basko Grand Mall Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Basko Grand Mall Padang"}
    },
    {
        "text": "Tahu nggak di mana posisi ATM yang ada di Basko Grand Mall Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Basko Grand Mall Padang"}
    },
    {
        "text": "Lokasi ATM di Basko Grand Mall Padang ada di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Basko Grand Mall Padang"}
    },
    {
        "text": "Di Basko Grand Mall Padang, ATM-nya terletak di bagian mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Basko Grand Mall Padang"}
    },
    {
        "text": "Bisa beri tahu saya di mana ATM di Basko Grand Mall Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Basko Grand Mall Padang"}
    },
    {
        "text": "Saya butuh info lokasi ATM di Basko Grand Mall Padang, di mana tempatnya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Basko Grand Mall Padang"}
    },

    {
        "text": "Di mana lokasi ATM di SPBU Sabral Bahir?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "SPBU Sabral Bahir"}
    },
    {
        "text": "Alamat ATM di SPBU Sabral Bahir?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "SPBU Sabral Bahir"}
    },
    {
        "text": "Tolong informasikan di mana saya bisa menemukan ATM di SPBU Sabral Bahir?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "SPBU Sabral Bahir"}
    },
    {
        "text": "ATM di SPBU Sabral Bahir itu posisinya ada di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "SPBU Sabral Bahir"}
    },
    {
        "text": "Di sekitar SPBU Sabral Bahir, lokasi ATM-nya ada di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "SPBU Sabral Bahir"}
    },
    {
        "text": "Saya butuh petunjuk lokasi ATM di SPBU Sabral Bahir, bisa bantu?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "SPBU Sabral Bahir"}
    },
    {
        "text": "Ada yang tahu di mana ATM di SPBU Sabral Bahir berada?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "SPBU Sabral Bahir"}
    },

    {
        "text": "Di mana lokasi ATM di Komplek PT. Semen Padang Indarung?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek PT. Semen Padang Indarung"}
    },
    {
        "text": "Alamat ATM di Komplek PT. Semen Padang Indarung?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek PT. Semen Padang Indarung"}
    },
    {
        "text": "Lokasi ATM yang ada di Komplek PT. Semen Padang Indarung itu di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek PT. Semen Padang Indarung"}
    },
    {
        "text": "Saya sedang mencari ATM di Komplek PT. Semen Padang Indarung, ada info?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek PT. Semen Padang Indarung"}
    },
    {
        "text": "Tahu nggak di mana letak ATM di Komplek PT. Semen Padang Indarung?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek PT. Semen Padang Indarung"}
    },
    {
        "text": "Bisa beri tahu saya lokasi ATM yang ada di Komplek PT. Semen Padang Indarung?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek PT. Semen Padang Indarung"}
    },
    {
        "text": "Di area Komplek PT. Semen Padang Indarung, ATM-nya ada di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek PT. Semen Padang Indarung"}
    },

    {
        "text": "Dimana lokasi ATM di Komplek Kantor Gubernur Sumbar (ATM-1)?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek Kantor Gubernur Sumbar ATM-1"}
    },
    {
        "text": "Tolong beritahu lokasi ATM di Komplek Gubernur Sumbar (ATM-1)?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek Kantor Gubernur Sumbar ATM-1"}
    },
    {
        "text": "Alamat ATM di Komplek Kantor Gubernur Sumbar (ATM-1) apa ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek Kantor Gubernur Sumbar ATM-1"}
    },
    {
        "text": "Di mana letak ATM 1 di Komplek Kantor Gubernur Sumbar?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek Kantor Gubernur Sumbar ATM-1"}
    },

    {
        "text": "Lokasi ATM-2 di Komplek Kantor Gubernur Sumbar di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek Kantor Gubernur Sumbar ATM-2"}
    },
    {
        "text": "Di mana saya bisa menemukan ATM-2 di Komplek Kantor Gubernur Sumbar?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek Kantor Gubernur Sumbar ATM-2"}
    },
    {
        "text": "Tolong sebutkan alamat ATM-2 di Komplek Kantor Gubernur Sumbar?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek Kantor Gubernur Sumbar ATM-2"}
    },
    {
        "text": "Dimana letak ATM 2 di Komplek Kantor Gubernur Sumbar?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek Kantor Gubernur Sumbar ATM-2"}
    },

    {
        "text": "Di mana lokasi ATM di Komplek Universitas Negeri Padang (ATM-1)?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Universitas Negeri Padang ATM-1"}
    },
    {
        "text": "Dimana letak ATM-1 di Universitas Negeri Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Universitas Negeri Padang ATM-1"}
    },
    {
        "text": "Apa alamat ATM-1 di Kampus Universitas Negeri Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Universitas Negeri Padang ATM-1"}
    },
    {
        "text": "Di mana lokasi ATM 1 di Universitas Negeri Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Universitas Negeri Padang ATM-1"}
    },

    {
        "text": "Dimana letak ATM-2 di Universitas Negeri Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Universitas Negeri Padang ATM-2"}
    },
    {
        "text": "Alamat ATM-2 di Universitas Negeri Padang apa?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Universitas Negeri Padang ATM-2"}
    },
    {
        "text": "Di mana lokasi ATM-2 di Universitas Negeri Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Universitas Negeri Padang ATM-2"}
    },
    {
        "text": "Apa alamat ATM 2 di Universitas Negeri Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Universitas Negeri Padang ATM-2"}
    },

    {
        "text": "Dimana lokasi ATM-3 di Komplek Universitas Negeri Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Universitas Negeri Padang ATM-3"}
    },
    {
        "text": "Apa alamat ATM-3 di Universitas Negeri Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Universitas Negeri Padang ATM-3"}
    },
    {
        "text": "Di mana ATM 3 di Universitas Negeri Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Universitas Negeri Padang ATM-3"}
    },

    {
        "text": "Di mana lokasi ATM di Rektorat Universitas Andalas?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Rektorat Universitas Andalas"}
    },
    {
        "text": "Alamat ATM di Rektorat Universitas Andalas?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Rektorat Universitas Andalas"}
    },
    {
        "text": "Lokasi ATM yang ada di Rektorat Universitas Andalas itu di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Rektorat Universitas Andalas"}
    },
    {
        "text": "Saya ingin tahu posisi ATM di Rektorat Universitas Andalas, bisa bantu?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Rektorat Universitas Andalas"}
    },
    {
        "text": "Di Rektorat Universitas Andalas, ATM-nya ada di bagian mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Rektorat Universitas Andalas"}
    },
    {
        "text": "Tolong beri tahu saya di mana lokasi ATM di Rektorat Universitas Andalas.",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Rektorat Universitas Andalas"}
    },
    {
        "text": "Di area Rektorat Universitas Andalas, ATM-nya terletak di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Rektorat Universitas Andalas"}
    },

    {
        "text": "Di mana lokasi ATM di Komplek Universitas Bung Hatta?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek Universitas Bung Hatta"}
    },
    {
        "text": "Alamat ATM di Komplek Universitas Bung Hatta?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek Universitas Bung Hatta"}
    },
    {
        "text": "Lokasi ATM di Komplek Universitas Bung Hatta itu ada di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek Universitas Bung Hatta"}
    },
    {
        "text": "Tahu nggak di mana posisi ATM di Komplek Universitas Bung Hatta?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek Universitas Bung Hatta"}
    },
    {
        "text": "Saya butuh informasi lokasi ATM di Komplek Universitas Bung Hatta, di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek Universitas Bung Hatta"}
    },
    {
        "text": "Di Komplek Universitas Bung Hatta, ATM-nya ada di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek Universitas Bung Hatta"}
    },
    {
        "text": "Di area Komplek Universitas Bung Hatta, di mana saya bisa menemukan ATM?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek Universitas Bung Hatta"}
    },
    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Capem Niaga?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem Niaga"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Capem Niaga?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem Niaga"}
    },
    {
        "text": "Posisi ATM di Kantor Bank Nagari Capem Niaga itu ada di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem Niaga"}
    },
    {
        "text": "Lokasi ATM yang berada di Kantor Bank Nagari Capem Niaga itu di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem Niaga"}
    },
    {
        "text": "Di sekitar Kantor Bank Nagari Capem Niaga, posisi ATM-nya ada di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem Niaga"}
    },
    {
        "text": "Saya mencari ATM di Kantor Bank Nagari Capem Niaga, bisa kasih tahu lokasi?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem Niaga"}
    },
    {
        "text": "Tolong beri tahu saya di mana letak ATM yang ada di Kantor Bank Nagari Capem Niaga?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem Niaga"}
    },

    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Kas Pasar Baru Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Kas Pasar Baru Padang"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Kas Pasar Baru Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Kas Pasar Baru Padang"}
    },
    {
        "text": "Lokasi ATM di Kantor Bank Nagari Kas Pasar Baru Padang itu ada di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Kas Pasar Baru Padang"}
    },
    {
        "text": "Saya butuh tahu di mana letak ATM di Kantor Bank Nagari Kas Pasar Baru Padang.",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Kas Pasar Baru Padang"}
    },
    {
        "text": "Tolong beri tahu saya posisi ATM di Kantor Bank Nagari Kas Pasar Baru Padang.",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Kas Pasar Baru Padang"}
    },
    {
        "text": "Di sekitar Kantor Bank Nagari Kas Pasar Baru Padang, ATM-nya ada di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Kas Pasar Baru Padang"}
    },
    {
        "text": "Di Kantor Bank Nagari Kas Pasar Baru Padang, di mana saya bisa menemukan ATM?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Kas Pasar Baru Padang"}
    },

    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Cabang Mentawai?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Mentawai"}
    },
    {
        "text": "Alamat ATM Kantor Bank Nagari Cabang Mentawai?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Mentawai"}
    },
    {
        "text": "Tolong beri tahu saya di mana ATM di Kantor Bank Nagari Cabang Mentawai?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Mentawai"}
    },
    {
        "text": "Lokasi ATM di Kantor Bank Nagari Cabang Mentawai itu ada di bagian mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Mentawai"}
    },
    {
        "text": "Di sekitar Kantor Bank Nagari Cabang Mentawai, ATM-nya ada di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Mentawai"}
    },
    {
        "text": "Di Kantor Bank Nagari Cabang Mentawai, di mana saya bisa menemukan ATM?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Mentawai"}
    },
    {
        "text": "Saya ingin tahu lokasi ATM di Kantor Bank Nagari Cabang Mentawai, ada info?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Mentawai"}
    },

    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Cabang Tapus?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Tapus"}
    },
    {
        "text": "Alamat ATM Kantor Bank Nagari Cabang Tapus?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Tapus"}
    },
    {
        "text": "Lokasi ATM di Kantor Bank Nagari Cabang Tapus itu ada di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Tapus"}
    },
    {
        "text": "Saya mencari ATM di Kantor Bank Nagari Cabang Tapus, bisa beri tahu di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Tapus"}
    },
    {
        "text": "Di Kantor Bank Nagari Cabang Tapus, ATM-nya terletak di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Tapus"}
    },
    {
        "text": "Tolong beri informasi mengenai lokasi ATM di Kantor Bank Nagari Cabang Tapus.",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Tapus"}
    },
    {
        "text": "Di area Kantor Bank Nagari Cabang Tapus, di mana ATM-nya berada?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Tapus"}
    },

    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Cabang Alahan Panjang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Alahan Panjang"}
    },
    {
        "text": "Alamat ATM Kantor Bank Nagari Cabang Alahan Panjang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Alahan Panjang"}
    },
    {
        "text": "Lokasi ATM di Kantor Bank Nagari Cabang Alahan Panjang itu ada di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Alahan Panjang"}
    },
    {
        "text": "Saya butuh informasi tentang lokasi ATM di Kantor Bank Nagari Cabang Alahan Panjang, bisa bantu?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Alahan Panjang"}
    },
    {
        "text": "Di sekitar Kantor Bank Nagari Cabang Alahan Panjang, posisi ATM-nya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Alahan Panjang"}
    },
    {
        "text": "Tahu nggak di mana letak ATM di Kantor Bank Nagari Cabang Alahan Panjang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Alahan Panjang"}
    },
    {
        "text": "Di Kantor Bank Nagari Cabang Alahan Panjang, di mana saya bisa menemukan ATM?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Alahan Panjang"}
    },

    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Capem Cipulir Jakarta?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem Cipulir Jakarta"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Capem Cipulir Jakarta?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem Cipulir Jakarta"}
    },
    {
        "text": "Di Kantor Bank Nagari Capem Cipulir Jakarta, lokasi ATM-nya di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem Cipulir Jakarta"}
    },
    {
        "text": "Lokasi ATM yang ada di Kantor Bank Nagari Capem Cipulir Jakarta itu di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem Cipulir Jakarta"}
    },
    {
        "text": "Bisa beri tahu saya di mana ATM di Kantor Bank Nagari Capem Cipulir Jakarta?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem Cipulir Jakarta"}
    },
    {
        "text": "Posisi ATM di Kantor Bank Nagari Capem Cipulir Jakarta itu ada di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem Cipulir Jakarta"}
    },
    {
        "text": "Di sekitar Kantor Bank Nagari Capem Cipulir Jakarta, di mana saya bisa menemukan ATM?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem Cipulir Jakarta"}
    },

    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Cabang Jakarta?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Jakarta"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Cabang Jakarta?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Jakarta"}
    },
    {
        "text": "Lokasi ATM di Kantor Bank Nagari Cabang Jakarta itu ada di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Jakarta"}
    },
    {
        "text": "Di Kantor Bank Nagari Cabang Jakarta, ATM-nya terletak di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Jakarta"}
    },
    {
        "text": "Bisa beri tahu saya lokasi ATM di Kantor Bank Nagari Cabang Jakarta?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Jakarta"}
    },
    {
        "text": "Di sekitar Kantor Bank Nagari Cabang Jakarta, posisi ATM-nya ada di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Jakarta"}
    },
    {
        "text": "Saya ingin tahu di mana ATM di Kantor Bank Nagari Cabang Jakarta, bisa bantu?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Jakarta"}
    },

    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Capem Tanah Abang Jakarta?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem Tanah Abang Jakarta"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Capem Tanah Abang Jakarta?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem Tanah Abang Jakarta"}
    },
    {
        "text": "Tolong beri tahu saya di mana posisi ATM di Kantor Bank Nagari Capem Tanah Abang Jakarta?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem Tanah Abang Jakarta"}
    },
    {
        "text": "Lokasi ATM yang ada di Kantor Bank Nagari Capem Tanah Abang Jakarta itu di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem Tanah Abang Jakarta"}
    },
    {
        "text": "Di sekitar Kantor Bank Nagari Capem Tanah Abang Jakarta, ATM-nya ada di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem Tanah Abang Jakarta"}
    },
    {
        "text": "Saya mencari ATM di Kantor Bank Nagari Capem Tanah Abang Jakarta, bisa kasih tahu di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem Tanah Abang Jakarta"}
    },
    {
        "text": "ATM di Kantor Bank Nagari Capem Tanah Abang Jakarta itu letaknya di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem Tanah Abang Jakarta"}
    },

    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Capem Kramat Jati Jakarta?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem Kramat Jati Jakarta"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Capem Kramat Jati Jakarta?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem Kramat Jati Jakarta"}
    },
    {
        "text": "Lokasi ATM di Kantor Bank Nagari Capem Kramat Jati Jakarta ada di bagian mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem Kramat Jati Jakarta"}
    },
    {
        "text": "Bisa beri tahu saya di mana ATM di Kantor Bank Nagari Capem Kramat Jati Jakarta?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem Kramat Jati Jakarta"}
    },
    {
        "text": "Di Kantor Bank Nagari Capem Kramat Jati Jakarta, posisi ATM-nya terletak di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem Kramat Jati Jakarta"}
    },
    {
        "text": "Saya ingin tahu letak ATM di Kantor Bank Nagari Capem Kramat Jati Jakarta, di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem Kramat Jati Jakarta"}
    },
    {
        "text": "Di sekitar Kantor Bank Nagari Capem Kramat Jati Jakarta, ATM-nya ada di lokasi mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem Kramat Jati Jakarta"}
    },

    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Cabang Pekanbaru?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Pekanbaru"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Cabang Pekanbaru?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Pekanbaru"}
    },
    {
        "text": "Lokasi ATM di Kantor Bank Nagari Cabang Pekanbaru ada di mana, ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Pekanbaru"}
    },
    {
        "text": "Tahu nggak di mana letak ATM di Kantor Bank Nagari Cabang Pekanbaru?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Pekanbaru"}
    },
    {
        "text": "Saya butuh informasi lokasi ATM di Kantor Bank Nagari Cabang Pekanbaru, bisa kasih tahu?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Pekanbaru"}
    },
    {
        "text": "Posisi ATM di Kantor Bank Nagari Cabang Pekanbaru itu ada di mana, ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Pekanbaru"}
    },
    {
        "text": "Di Kantor Bank Nagari Cabang Pekanbaru, di mana saya bisa menemukan ATM?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Pekanbaru"}
    },

    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Capem A. Yani Pekanbaru?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem A. Yani Pekanbaru"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Capem A. Yani Pekanbaru?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem A. Yani Pekanbaru"}
    },
    {
        "text": "Kira-kira di mana saya bisa menemukan ATM di Kantor Bank Nagari Capem A. Yani Pekanbaru?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem A. Yani Pekanbaru"}
    },
    {
        "text": "Lokasi ATM di Kantor Bank Nagari Capem A. Yani Pekanbaru ada di sudut mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem A. Yani Pekanbaru"}
    },
    {
        "text": "ATM di Kantor Bank Nagari Capem A. Yani Pekanbaru posisinya di bagian mana, ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem A. Yani Pekanbaru"}
    },
    {
        "text": "Bisa bantu saya cari ATM di Kantor Bank Nagari Capem A. Yani Pekanbaru? Di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem A. Yani Pekanbaru"}
    },
    {
        "text": "Saya ingin tahu lokasi ATM di Kantor Bank Nagari Capem A. Yani Pekanbaru, ada info di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem A. Yani Pekanbaru"}
    },

    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Capem Nangka Pekanbaru?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem Nangka Pekanbaru"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Capem Nangka Pekanbaru?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem Nangka Pekanbaru"}
    },
    {
        "text": "Lokasi ATM di Kantor Bank Nagari Capem Nangka Pekanbaru itu ada di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem Nangka Pekanbaru"}
    },
    {
        "text": "Di sekitar Kantor Bank Nagari Capem Nangka Pekanbaru, ATM-nya berada di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem Nangka Pekanbaru"}
    },
    {
        "text": "Bisa bantu beri tahu saya lokasi ATM di Kantor Bank Nagari Capem Nangka Pekanbaru?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem Nangka Pekanbaru"}
    },
    {
        "text": "Di mana letak ATM yang ada di Kantor Bank Nagari Capem Nangka Pekanbaru?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem Nangka Pekanbaru"}
    },
    {
        "text": "Saya lagi cari ATM di Kantor Bank Nagari Capem Nangka Pekanbaru, di mana ya letaknya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Capem Nangka Pekanbaru"}
    },

    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Cabang Bandung?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Bandung"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Cabang Bandung?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Bandung"}
    },
    {
        "text": "Tahu nggak di mana saya bisa menemukan ATM di Kantor Bank Nagari Cabang Bandung?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Bandung"}
    },
    {
        "text": "Di Kantor Bank Nagari Cabang Bandung, posisi ATM-nya ada di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Bandung"}
    },
    {
        "text": "Lokasi ATM di Kantor Bank Nagari Cabang Bandung itu ada di sudut mana, ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Bandung"}
    },
    {
        "text": "Di sekitar Kantor Bank Nagari Cabang Bandung, ATM-nya di mana, ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Bandung"}
    },
    {
        "text": "Di Kantor Bank Nagari Cabang Bandung, ATM-nya ada di tempat yang mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Cabang Bandung"}
    },

    {
        "text": "Di mana lokasi ATM di Komplek Pasar Baru Bandung?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek Pasar Baru Bandung"}
    },
    {
        "text": "Alamat ATM di Komplek Pasar Baru Bandung?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek Pasar Baru Bandung"}
    },
    {
        "text": "Lokasi ATM di Komplek Pasar Baru Bandung itu ada di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek Pasar Baru Bandung"}
    },
    {
        "text": "Di sekitar Komplek Pasar Baru Bandung, ATM-nya terletak di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek Pasar Baru Bandung"}
    },
    {
        "text": "Di Komplek Pasar Baru Bandung, posisi ATM-nya ada di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek Pasar Baru Bandung"}
    },
    {
        "text": "Tahu nggak di mana letak ATM di Komplek Pasar Baru Bandung?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek Pasar Baru Bandung"}
    },
    {
        "text": "ATM di Komplek Pasar Baru Bandung itu ada di bagian mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Komplek Pasar Baru Bandung"}
    },

    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Syariah Cabang Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Syariah Cabang Padang"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Syariah Cabang Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Syariah Cabang Padang"}
    },
    {
        "text": "Lokasi ATM di Kantor Bank Nagari Syariah Cabang Padang ada di mana, ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Syariah Cabang Padang"}
    },
    {
        "text": "Di sekitar Kantor Bank Nagari Syariah Cabang Padang, posisi ATM-nya ada di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Syariah Cabang Padang"}
    },
    {
        "text": "Tahu nggak di mana letak ATM di Kantor Bank Nagari Syariah Cabang Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Syariah Cabang Padang"}
    },
    {
        "text": "Di Kantor Bank Nagari Syariah Cabang Padang, di mana saya bisa menemukan ATM?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Syariah Cabang Padang"}
    },
    {
        "text": "Posisi ATM di Kantor Bank Nagari Syariah Cabang Padang itu ada di mana, ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "Kantor Bank Nagari Syariah Cabang Padang"}
    },

    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Capem Dangung Dangung?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_dangung_dangung"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Capem Dangung Dangung?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_dangung_dangung"}
    },
    {
        "text": "Lokasi ATM di Kantor Bank Nagari Capem Dangung Dangung itu ada di mana, ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_dangung_dangung"}
    },
    {
        "text": "Di sekitar Kantor Bank Nagari Capem Dangung Dangung, posisi ATM-nya ada di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_dangung_dangung"}
    },
    {
        "text": "Tahu nggak di mana letak ATM di Kantor Bank Nagari Capem Dangung Dangung?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_dangung_dangung"}
    },
    {
        "text": "Di Kantor Bank Nagari Capem Dangung Dangung, di mana saya bisa menemukan ATM?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_dangung_dangung"}
    },
    {
        "text": "ATM di Kantor Bank Nagari Capem Dangung Dangung itu posisinya ada di bagian mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_dangung_dangung"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Cabang Payakumbuh (ATM-1)?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "atm_1_cabang_payakumbuh"}
    },
    {
        "text": "Lokasi ATM-1 di Bank Nagari Cabang Payakumbuh di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "atm_1_cabang_payakumbuh"}
    },
    {
        "text": "Apa lokasi ATM-1 di Kantor Bank Nagari Cabang Payakumbuh?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "atm_1_cabang_payakumbuh"}
    },
    {
        "text": "Di mana ATM 1 di Bank Nagari Cabang Payakumbuh?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "atm_1_cabang_payakumbuh"}
    },
    {
        "text": "Dimana lokasi ATM-2 di Kantor Bank Nagari Cabang Payakumbuh?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "atm_2_cabang_payakumbuh"}
    },
    {
        "text": "Lokasi ATM-2 di Kantor Bank Nagari Cabang Payakumbuh itu ada di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "atm_2_cabang_payakumbuh"}
    },
    {
        "text": "Saya ingin tahu di mana ATM-2 yang ada di Kantor Bank Nagari Cabang Payakumbuh.",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "atm_2_cabang_payakumbuh"}
    },
    {
        "text": "Di Kantor Bank Nagari Cabang Payakumbuh, ATM-2-nya terletak di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "atm_2_cabang_payakumbuh"}
    },
    {
        "text": "Di sekitar Kantor Bank Nagari Cabang Payakumbuh, ATM-2 itu posisinya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "atm_2_cabang_payakumbuh"}
    },
    {
        "text": "Bisa dijelaskan di mana ATM-2 di Kantor Bank Nagari Cabang Payakumbuh berada?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "atm_2_cabang_payakumbuh"}
    },
    {
        "text": "Apa alamat ATM-2 di Bank Nagari Cabang Payakumbuh?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "atm_2_cabang_payakumbuh"}
    },

    {
        "text": "Di mana lokasi ATM di Komplek Kantor Bupati Lima Puluh Kota?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "komplek_kantor_bupati_lima_puluh_kota"}
    },
    {
        "text": "Alamat ATM di Komplek Kantor Bupati Lima Puluh Kota?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "komplek_kantor_bupati_lima_puluh_kota"}
    },
    {
        "text": "Lokasi ATM di Komplek Kantor Bupati Lima Puluh Kota ada di mana, ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "komplek_kantor_bupati_lima_puluh_kota"}
    },
    {
        "text": "Di sekitar Komplek Kantor Bupati Lima Puluh Kota, ATM-nya di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "komplek_kantor_bupati_lima_puluh_kota"}
    },
    {
        "text": "Tahu nggak di mana saya bisa menemukan ATM di Komplek Kantor Bupati Lima Puluh Kota?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "komplek_kantor_bupati_lima_puluh_kota"}
    },
    {
        "text": "Saya lagi cari ATM di Komplek Kantor Bupati Lima Puluh Kota, di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "komplek_kantor_bupati_lima_puluh_kota"}
    },
    {
        "text": "ATM di Komplek Kantor Bupati Lima Puluh Kota itu ada di mana ya posisinya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "komplek_kantor_bupati_lima_puluh_kota"}
    },

    {
        "text": "Di mana lokasi ATM di RSUD Dr. Adnan WD Payakumbuh?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsud_dr_adnan_wd_payakumbuh"}
    },
    {
        "text": "Alamat ATM di RSUD Dr. Adnan WD Payakumbuh?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsud_dr_adnan_wd_payakumbuh"}
    },
    {
        "text": "Ada yang tahu di mana ATM di RSUD Dr. Adnan WD Payakumbuh?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsud_dr_adnan_wd_payakumbuh"}
    },
    {
        "text": "Posisi ATM di RSUD Dr. Adnan WD Payakumbuh itu ada di bagian mana, ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsud_dr_adnan_wd_payakumbuh"}
    },
    {
        "text": "Saya sedang mencari ATM di RSUD Dr. Adnan WD Payakumbuh, di mana ya letaknya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsud_dr_adnan_wd_payakumbuh"}
    },
    {
        "text": "Di sekitar RSUD Dr. Adnan WD Payakumbuh, di mana bisa ditemukan ATM?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsud_dr_adnan_wd_payakumbuh"}
    },
    {
        "text": "Lokasi ATM yang ada di RSUD Dr. Adnan WD Payakumbuh, ada di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsud_dr_adnan_wd_payakumbuh"}
    },

    {
        "text": "Dimana letak ATM-1 di Kantor Bank Nagari Cabang Bukittinggi?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "atm_1_cabang_bukittinggi"}
    },
    {
        "text": "Lokasi ATM-1 di Bank Nagari Cabang Bukittinggi di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "atm_1_cabang_bukittinggi"}
    },
    {
        "text": "Apa alamat ATM 1 di Cabang Bukittinggi?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "atm_1_cabang_bukittinggi"}
    },

    {
        "text": "Dimana lokasi ATM-2 di Kantor Bank Nagari Cabang Bukittinggi?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "atm_2_cabang_bukittinggi"}
    },
    {
        "text": "Apa alamat ATM-2 di Cabang Bukittinggi?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "atm_2_cabang_bukittinggi"}
    },
    {
        "text": "Di mana ATM 2 di Bank Nagari Cabang Bukittinggi?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "atm_2_cabang_bukittinggi"}
    },

    {
        "text": "Di mana lokasi ATM di Komplek Kantor Balaikota Bukittinggi?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "komplek_kantor_balaikota_bukittinggi"}
    },
    {
        "text": "Alamat ATM di Komplek Kantor Balaikota Bukittinggi?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "komplek_kantor_balaikota_bukittinggi"}
    },
    {
        "text": "ATM di Komplek Kantor Balaikota Bukittinggi itu letaknya di mana, ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "komplek_kantor_balaikota_bukittinggi"}
    },
    {
        "text": "Saya lagi cari ATM di Komplek Kantor Balaikota Bukittinggi, ada yang tahu lokasinya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "komplek_kantor_balaikota_bukittinggi"}
    },
    {
        "text": "Di sekitar Komplek Kantor Balaikota Bukittinggi, di mana posisi ATM-nya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "komplek_kantor_balaikota_bukittinggi"}
    },
    {
        "text": "Letak ATM di Komplek Kantor Balaikota Bukittinggi ada di mana ya, bisa kasih tahu?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "komplek_kantor_balaikota_bukittinggi"}
    },
    {
        "text": "Posisi ATM yang ada di Komplek Kantor Balaikota Bukittinggi itu di mana, ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "komplek_kantor_balaikota_bukittinggi"}
    },

    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Capem Pasar Bawah?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_pasar_bawah"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Capem Pasar Bawah?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_pasar_bawah"}
    },
    {
        "text": "Tahu nggak di mana lokasi ATM di Kantor Bank Nagari Capem Pasar Bawah?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_pasar_bawah"}
    },
    {
        "text": "Di Kantor Bank Nagari Capem Pasar Bawah, posisi ATM-nya ada di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_pasar_bawah"}
    },
    {
        "text": "Saya lagi cari ATM di Kantor Bank Nagari Capem Pasar Bawah, di mana ya letaknya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_pasar_bawah"}
    },
    {
        "text": "Di sekitar Kantor Bank Nagari Capem Pasar Bawah, di mana saya bisa temukan ATM?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_pasar_bawah"}
    },
    {
        "text": "Lokasi ATM di Kantor Bank Nagari Capem Pasar Bawah itu ada di mana, ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_pasar_bawah"}
    },

    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Capem Aur Kuning?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_aur_kuning"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Capem Aur Kuning?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_aur_kuning"}
    },
    {
        "text": "Lokasi ATM di Kantor Bank Nagari Capem Aur Kuning itu ada di mana, ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_aur_kuning"}
    },
    {
        "text": "Di sekitar Kantor Bank Nagari Capem Aur Kuning, posisi ATM-nya ada di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_aur_kuning"}
    },
    {
        "text": "Tahu nggak di mana saya bisa menemukan ATM di Kantor Bank Nagari Capem Aur Kuning?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_aur_kuning"}
    },
    {
        "text": "Saya sedang mencari ATM di Kantor Bank Nagari Capem Aur Kuning, di mana ya letaknya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_aur_kuning"}
    },
    {
        "text": "Posisi ATM di Kantor Bank Nagari Capem Aur Kuning itu di bagian mana, ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_aur_kuning"}
    },

    {
        "text": "Di mana lokasi ATM di RSUD Achmad Muchtar Bukittinggi?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsud_achmad_muchtar_bukittinggi"}
    },
    {
        "text": "Alamat ATM di RSUD Achmad Muchtar Bukittinggi?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsud_achmad_muchtar_bukittinggi"}
    },
    {
        "text": "Lokasi ATM di RSUD Achmad Muchtar Bukittinggi itu ada di mana, ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsud_achmad_muchtar_bukittinggi"}
    },
    {
        "text": "Di RSUD Achmad Muchtar Bukittinggi, posisi ATM-nya ada di bagian mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsud_achmad_muchtar_bukittinggi"}
    },
    {
        "text": "Saya ingin tahu, di mana letak ATM di RSUD Achmad Muchtar Bukittinggi?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsud_achmad_muchtar_bukittinggi"}
    },
    {
        "text": "Di sekitar RSUD Achmad Muchtar Bukittinggi, di mana saya bisa menemukan ATM?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsud_achmad_muchtar_bukittinggi"}
    },
    {
        "text": "ATM di RSUD Achmad Muchtar Bukittinggi itu ada di mana ya, bisa kasih tahu?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsud_achmad_muchtar_bukittinggi"}
    },

    {
        "text": "Di mana lokasi ATM di RSUP P3SN Bukittinggi?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsup_p3sn_bukittinggi"}
    },
    {
        "text": "Alamat ATM di RSUP P3SN Bukittinggi?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsup_p3sn_bukittinggi"}
    },
    {
        "text": "Tahu di mana letak ATM di RSUP P3SN Bukittinggi?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsup_p3sn_bukittinggi"}
    },
    {
        "text": "Di RSUP P3SN Bukittinggi, di mana saya bisa menemukan ATM?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsup_p3sn_bukittinggi"}
    },
    {
        "text": "Lokasi ATM di RSUP P3SN Bukittinggi itu ada di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsup_p3sn_bukittinggi"}
    },
    {
        "text": "Posisi ATM di RSUP P3SN Bukittinggi itu di bagian mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsup_p3sn_bukittinggi"}
    },
    {
        "text": "Dimana ya lokasi ATM yang ada di RSUP P3SN Bukittinggi?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsup_p3sn_bukittinggi"}
    },

    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Capem Padang Luar?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_padang_luar"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Capem Padang Luar?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_padang_luar"}
    },
    {
        "text": "Di mana letak mesin ATM yang ada di Kantor Bank Nagari Capem Padang Luar?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_padang_luar"}
    },
    {
        "text": "Ada ATM di sekitar Kantor Bank Nagari Capem Padang Luar? Kalau ada, di mana lokasinya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_padang_luar"}
    },
    {
        "text": "Bisa beri informasi tentang posisi ATM yang ada di Kantor Bank Nagari Capem Padang Luar?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_padang_luar"}
    },
    {
        "text": "Kantor Bank Nagari Capem Padang Luar itu ada mesin ATM? Lokasinya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_padang_luar"}
    },
    {
        "text": "Dimana saya bisa menemukan ATM di sekitar Kantor Bank Nagari Capem Padang Luar?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_padang_luar"}
    },

    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Cabang Batusangkar?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_batusangkar"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Cabang Batusangkar?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_batusangkar"}
    },
    {
        "text": "Lokasi ATM di Kantor Bank Nagari Cabang Batusangkar itu di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_batusangkar"}
    },
    {
        "text": "Di sekitar Kantor Bank Nagari Cabang Batusangkar, ada ATM? Kalau ada, di mana letaknya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_batusangkar"}
    },
    {
        "text": "Bisa bantu saya cari tahu lokasi ATM di Kantor Bank Nagari Cabang Batusangkar?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_batusangkar"}
    },
    {
        "text": "Apakah ada mesin ATM yang tersedia di Kantor Bank Nagari Cabang Batusangkar? Di mana posisinya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_batusangkar"}
    },
    {
        "text": "Dimana saya bisa menemukan ATM di area Kantor Bank Nagari Cabang Batusangkar?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_batusangkar"}
    },

    {
        "text": "Di mana lokasi ATM di RSUD Batusangkar?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsud_batusangkar"}
    },
    {
        "text": "Alamat ATM di RSUD Batusangkar?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsud_batusangkar"}
    },
    {
        "text": "Dimana saya bisa menemukan ATM di RSUD Batusangkar?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsud_batusangkar"}
    },
    {
        "text": "Apakah ada mesin ATM yang berada di sekitar RSUD Batusangkar? Di mana tepatnya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsud_batusangkar"}
    },
    {
        "text": "Bisa tolong informasikan lokasi ATM yang ada di RSUD Batusangkar?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsud_batusangkar"}
    },
    {
        "text": "ATM di RSUD Batusangkar itu letaknya di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsud_batusangkar"}
    },
    {
        "text": "Saya sedang mencari ATM di RSUD Batusangkar. Di mana posisinya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsud_batusangkar"}
    },

    {
        "text": "Di mana lokasi ATM di Komplek Kampus STAIN Batusangkar?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "stain_batusangkar"}
    },
{
        "text": "Alamat ATM di Komplek Kampus STAIN Batusangkar?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "stain_batusangkar"}
    },
{
        "text": "Ada ATM di Komplek Kampus STAIN Batusangkar? Kalau ada, lokasinya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "stain_batusangkar"}
    },
{
        "text": "Dimana tempat mesin ATM di sekitar Komplek Kampus STAIN Batusangkar?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "stain_batusangkar"}
    },
{
        "text": "Lokasi ATM yang terdekat dengan Komplek Kampus STAIN Batusangkar itu di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "stain_batusangkar"}
    },
{
        "text": "Bisa kasih tahu saya di mana letak ATM yang ada di Komplek Kampus STAIN Batusangkar?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "stain_batusangkar"}
    },
{
        "text": "Saya sedang mencari mesin ATM di Komplek Kampus STAIN Batusangkar, di mana posisinya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "stain_batusangkar"}
    },

 {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Cabang Painan?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_painan"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Cabang Painan?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_painan"}
    },
    {
        "text": "Ada mesin ATM di sekitar Kantor Bank Nagari Cabang Painan? Lokasinya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_painan"}
    },
    {
        "text": "Kantor Bank Nagari Cabang Painan memiliki ATM, kan? Di mana letaknya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_painan"}
    },
    {
        "text": "Di sekitar Kantor Bank Nagari Cabang Painan, apakah ada mesin ATM? Jika ada, di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_painan"}
    },
    {
        "text": "Mohon informasikan lokasi ATM di Kantor Bank Nagari Cabang Painan?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_painan"}
    },
    {
        "text": "Saya ingin tahu, di mana lokasi ATM yang terletak di Kantor Bank Nagari Cabang Painan?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_painan"}
    },

    {
        "text": "Di mana lokasi ATM di Komplek Kantor Bupati Pesisir Selatan?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_pesisir_selatan"}
    },
    {
        "text": "Alamat ATM di Komplek Kantor Bupati Pesisir Selatan?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_pesisir_selatan"}
    },
    {
        "text": "Ada mesin ATM di sekitar Komplek Kantor Bupati Pesisir Selatan? Lokasinya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_pesisir_selatan"}
    },
    {
        "text": "Kantor Bupati Pesisir Selatan punya ATM? Kalau ada, letaknya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_pesisir_selatan"}
    },
    {
        "text": "Di mana saya bisa menemukan ATM di area Komplek Kantor Bupati Pesisir Selatan?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_pesisir_selatan"}
    },
    {
        "text": "Bisa beri informasi tentang lokasi ATM yang ada di Komplek Kantor Bupati Pesisir Selatan?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_pesisir_selatan"}
    },
    {
        "text": "Saya ingin tahu, dimana tepatnya ATM yang ada di Komplek Kantor Bupati Pesisir Selatan?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_pesisir_selatan"}
    },

    {
        "text": "Di mana lokasi ATM di Pasar Kambang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "pasar_kambang"}
    },
    {
        "text": "Alamat ATM di Pasar Kambang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "pasar_kambang"}
    },
    {
        "text": "Lokasi ATM di Pasar Kambang itu di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "pasar_kambang"}
    },
    {
        "text": "Ada mesin ATM di sekitar Pasar Kambang? Kalau ada, di mana tempatnya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "pasar_kambang"}
    },
    {
        "text": "Dimana saya bisa menemukan ATM di Pasar Kambang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "pasar_kambang"}
    },
    {
        "text": "Bisa kasih tahu di mana lokasi ATM yang ada di Pasar Kambang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "pasar_kambang"}
    },
    {
        "text": "Apakah ada ATM di Pasar Kambang? Kalau ada, di mana tepatnya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "pasar_kambang"}
    },

    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Cabang Pariaman?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_pariaman"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Cabang Pariaman?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_pariaman"}
    },
    {
        "text": "Ada ATM di sekitar Kantor Bank Nagari Cabang Pariaman? Kalau ada, di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_pariaman"}
    },
    {
        "text": "Dimana lokasi ATM yang terdekat dengan Kantor Bank Nagari Cabang Pariaman?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_pariaman"}
    },
    {
        "text": "Bisa bantu saya cari tahu lokasi ATM di Kantor Bank Nagari Cabang Pariaman?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_pariaman"}
    },
    {
        "text": "Di Kantor Bank Nagari Cabang Pariaman ada ATM, kan? Lokasinya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_pariaman"}
    },
    {
        "text": "Saya ingin tahu, di mana tepatnya letak ATM yang ada di Kantor Bank Nagari Cabang Pariaman?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_pariaman"}
    },

    {
        "text": "Di mana lokasi ATM di Komplek Kantor Bupati Padang Pariaman?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_padang_pariaman"}
    },
    {
        "text": "Alamat ATM di Komplek Kantor Bupati Padang Pariaman?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_padang_pariaman"}
    },
    {
        "text": "Ada ATM di sekitar Komplek Kantor Bupati Padang Pariaman? Kalau ada, di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_padang_pariaman"}
    },
    {
        "text": "Bisa tolong informasikan lokasi ATM yang ada di Komplek Kantor Bupati Padang Pariaman?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_padang_pariaman"}
    },
    {
        "text": "Dimana saya bisa menemukan ATM di Komplek Kantor Bupati Padang Pariaman?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_padang_pariaman"}
    },
    {
        "text": "Lokasi ATM yang terletak di Komplek Kantor Bupati Padang Pariaman itu di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_padang_pariaman"}
    },
    {
        "text": "Gimana, di Komplek Kantor Bupati Padang Pariaman ada mesin ATM? Kalau ada, posisinya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_padang_pariaman"}
    },

    {
        "text": "Di mana lokasi ATM di RSUD Pariaman?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsud_pariaman"}
    },
    {
        "text": "Alamat ATM di RSUD Pariaman?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsud_pariaman"}
    },
    {
        "text": "Apakah ada ATM di RSUD Pariaman? Jika ada, di mana lokasinya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsud_pariaman"}
    },
    {
        "text": "Di RSUD Pariaman ada mesin ATM, kan? Lokasinya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsud_pariaman"}
    },
    {
        "text": "Dimana letak ATM yang ada di RSUD Pariaman?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsud_pariaman"}
    },
    {
        "text": "Bisa kasih tahu di mana ATM yang terletak di RSUD Pariaman?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsud_pariaman"}
    },
    {
        "text": "Saya ingin tahu, di mana posisi ATM yang ada di RSUD Pariaman?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsud_pariaman"}
    },

    {
        "text": "Di mana lokasi ATM di Komplek Kantor Balaikota Pariaman?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_balaikota_pariaman"}
    },
    {
        "text": "Alamat ATM di Komplek Kantor Balaikota Pariaman?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_balaikota_pariaman"}
    },
    {
        "text": "Ada mesin ATM di sekitar Komplek Kantor Balaikota Pariaman? Lokasinya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_balaikota_pariaman"}
    },
    {
        "text": "Di Komplek Kantor Balaikota Pariaman, di mana posisi ATM yang terdekat?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_balaikota_pariaman"}
    },
    {
        "text": "Bisa kasih tahu di mana letak ATM yang ada di Komplek Kantor Balaikota Pariaman?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_balaikota_pariaman"}
    },
    {
        "text": "Saya ingin tahu, dimana lokasi ATM di sekitar Komplek Kantor Balaikota Pariaman?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_balaikota_pariaman"}
    },
    {
        "text": "Apakah ada mesin ATM di area Komplek Kantor Balaikota Pariaman? Kalau ada, di mana tempatnya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_balaikota_pariaman"}
    },

    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Cabang Solok?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_solok"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Cabang Solok?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_solok"}
    },
    {
        "text": "Dimana saya bisa menemukan ATM di Kantor Bank Nagari Cabang Solok?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_solok"}
    },
    {
        "text": "Lokasi ATM di Kantor Bank Nagari Cabang Solok itu di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_solok"}
    },
    {
        "text": "Kantor Bank Nagari Cabang Solok ada ATM, kan? Di mana tempatnya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_solok"}
    },
    {
        "text": "Di sekitar Kantor Bank Nagari Cabang Solok, ada mesin ATM? Kalau ada, di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_solok"}
    },
    {
        "text": "Bisa bantu saya cari lokasi ATM di Kantor Bank Nagari Cabang Solok?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_solok"}
    },

    {
        "text": "Di mana lokasi ATM di Komplek Kantor Balaikota Solok?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_balaikota_solok"}
    },
    {
        "text": "Alamat ATM di Komplek Kantor Balaikota Solok?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_balaikota_solok"}
    },
    {
        "text": "Ada ATM di Komplek Kantor Balaikota Solok? Lokasinya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_balaikota_solok"}
    },
    {
        "text": "Di mana letak ATM di sekitar Komplek Kantor Balaikota Solok?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_balaikota_solok"}
    },
    {
        "text": "Di Komplek Kantor Balaikota Solok, ada mesin ATM? Kalau ada, di mana posisi tepatnya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_balaikota_solok"}
    },
    {
        "text": "Dimana saya bisa menemukan ATM yang ada di Komplek Kantor Balaikota Solok?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_balaikota_solok"}
    },
    {
        "text": "Saya sedang mencari ATM di Komplek Kantor Balaikota Solok, di mana letaknya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_balaikota_solok"}
    },

    {
        "text": "Di mana lokasi ATM di Komplek Kantor Bupati Kabupaten Solok?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_kabupaten_solok"}
    },
    {
        "text": "Alamat ATM di Komplek Kantor Bupati Kabupaten Solok?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_kabupaten_solok"}
    },
    {
        "text": "Apakah ada mesin ATM di Komplek Kantor Bupati Kabupaten Solok? Lokasinya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_kabupaten_solok"}
    },
    {
        "text": "Di sekitar Komplek Kantor Bupati Kabupaten Solok, ada ATM? Kalau ada, di mana posisinya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_kabupaten_solok"}
    },
    {
        "text": "Dimana saya bisa menemukan ATM yang berada di Komplek Kantor Bupati Kabupaten Solok?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_kabupaten_solok"}
    },
    {
        "text": "Bisa kasih tahu lokasi ATM di Komplek Kantor Bupati Kabupaten Solok?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_kabupaten_solok"}
    },
    {
        "text": "Lokasi ATM yang terdekat dengan Komplek Kantor Bupati Kabupaten Solok itu di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_kabupaten_solok"}
    },

    {
        "text": "Di mana lokasi ATM di RSUD Solok?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsud_solok"}
    },
    {
        "text": "Alamat ATM di RSUD Solok?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsud_solok"}
    },
    {
        "text": "Dimana letak ATM yang ada di RSUD Solok?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsud_solok"}
    },
    {
        "text": "RSUD Solok ada mesin ATM, kan? Lokasinya di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsud_solok"}
    },
    {
        "text": "Bisa beri informasi mengenai lokasi ATM di RSUD Solok?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsud_solok"}
    },
    {
        "text": "Di mana posisi mesin ATM di RSUD Solok?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsud_solok"}
    },
    {
        "text": "Saya sedang mencari ATM di RSUD Solok, di mana posisinya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsud_solok"}
    },

    {
        "text": "Di mana lokasi ATM di Ruang Taman Hijau Kota Solok?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "ruang_taman_hijau_kota_solok"}
    },
    {
        "text": "Alamat ATM di Ruang Taman Hijau Kota Solok?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "ruang_taman_hijau_kota_solok"}
    },
    {
        "text": "Lokasi ATM yang ada di Ruang Taman Hijau Kota Solok di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "ruang_taman_hijau_kota_solok"}
    },
    {
        "text": "Di sekitar Ruang Taman Hijau Kota Solok, ada ATM? Kalau ada, di mana letaknya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "ruang_taman_hijau_kota_solok"}
    },
    {
        "text": "Dimana posisi ATM yang terletak di Ruang Taman Hijau Kota Solok?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "ruang_taman_hijau_kota_solok"}
    },
    {
        "text": "Ruang Taman Hijau Kota Solok ada mesin ATM, kan? Di mana lokasi tepatnya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "ruang_taman_hijau_kota_solok"}
    },
    {
        "text": "Bisa beri tahu saya di mana ATM yang ada di Ruang Taman Hijau Kota Solok?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "ruang_taman_hijau_kota_solok"}
    },

    {
        "text": "Di mana lokasi ATM di Kantor Bupati Sijunjung?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_sijunjung"}
    },
    {
        "text": "Alamat ATM di Kantor Bupati Sijunjung?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_sijunjung"}
    },
    {
        "text": "Di Kantor Bupati Sijunjung ada ATM? Kalau ada, di mana lokasinya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_sijunjung"}
    },
    {
        "text": "Dimana letak ATM yang berada di sekitar Kantor Bupati Sijunjung?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_sijunjung"}
    },
    {
        "text": "Bisa tolong beri informasi tentang lokasi ATM di Kantor Bupati Sijunjung?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_sijunjung"}
    },
    {
        "text": "Saya ingin tahu, di mana lokasi ATM di Kantor Bupati Sijunjung?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_sijunjung"}
    },
    {
        "text": "Apakah ada mesin ATM di sekitar Kantor Bupati Sijunjung? Lokasinya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_sijunjung"}
    },

    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Cabang Lubuk Sikaping?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_lubuk_sikaping"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Cabang Lubuk Sikaping?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_lubuk_sikaping"}
    },
    {
        "text": "Dimana saya bisa menemukan ATM di Kantor Bank Nagari Cabang Lubuk Sikaping?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_lubuk_sikaping"}
    },
    {
        "text": "Lokasi ATM di Kantor Bank Nagari Cabang Lubuk Sikaping itu di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_lubuk_sikaping"}
    },
    {
        "text": "Ada ATM di Kantor Bank Nagari Cabang Lubuk Sikaping? Di mana letaknya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_lubuk_sikaping"}
    },
    {
        "text": "Bisa tolong informasikan lokasi ATM yang ada di Kantor Bank Nagari Cabang Lubuk Sikaping?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_lubuk_sikaping"}
    },
    {
        "text": "Saya mencari ATM di Kantor Bank Nagari Cabang Lubuk Sikaping. Di mana posisinya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_lubuk_sikaping"}
    },

    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Cabang Padang Panjang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_padang_panjang"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Cabang Padang Panjang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_padang_panjang"}
    },
    {
        "text": "Di mana lokasi ATM yang ada di Kantor Bank Nagari Cabang Padang Panjang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_padang_panjang"}
    },
    {
        "text": "Kantor Bank Nagari Cabang Padang Panjang ada ATM, kan? Lokasinya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_padang_panjang"}
    },
    {
        "text": "Dimana letak ATM yang tersedia di Kantor Bank Nagari Cabang Padang Panjang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_padang_panjang"}
    },
    {
        "text": "Bisa beri informasi lokasi ATM di sekitar Kantor Bank Nagari Cabang Padang Panjang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_padang_panjang"}
    },
    {
        "text": "Di Kantor Bank Nagari Cabang Padang Panjang ada mesin ATM? Kalau ada, di mana letaknya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_padang_panjang"}
    },

    {
        "text": "Di mana lokasi ATM di Komplek Kantor Balaikota Padang Panjang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_balaikota_padang_panjang"}
    },
    {
        "text": "Alamat ATM di Komplek Kantor Balaikota Padang Panjang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_balaikota_padang_panjang"}
    },
    {
        "text": "Ada ATM di Komplek Kantor Balaikota Padang Panjang? Lokasinya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_balaikota_padang_panjang"}
    },
    {
        "text": "Dimana saya bisa menemukan ATM di Komplek Kantor Balaikota Padang Panjang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_balaikota_padang_panjang"}
    },
    {
        "text": "Di Komplek Kantor Balaikota Padang Panjang ada mesin ATM, kan? Letaknya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_balaikota_padang_panjang"}
    },
    {
        "text": "Bisa kasih tahu lokasi ATM di Komplek Kantor Balaikota Padang Panjang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_balaikota_padang_panjang"}
    },
    {
        "text": "Di sekitar Komplek Kantor Balaikota Padang Panjang, ada ATM? Kalau ada, di mana lokasinya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_balaikota_padang_panjang"}
    },

    {
        "text": "Di mana lokasi ATM di Bandar Udara Internasional Minangkabau?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "bandara_internasional_minangkabau"}
    },
    {
        "text": "Alamat ATM di Bandar Udara Internasional Minangkabau?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "bandara_internasional_minangkabau"}
    },
    {
        "text": "Di Bandar Udara Internasional Minangkabau ada mesin ATM? Lokasinya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "bandara_internasional_minangkabau"}
    },
    {
        "text": "Saya ingin tahu, di mana ATM yang ada di Bandar Udara Internasional Minangkabau?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "bandara_internasional_minangkabau"}
    },
    {
        "text": "Dimana posisi ATM di sekitar Bandar Udara Internasional Minangkabau?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "bandara_internasional_minangkabau"}
    },
    {
        "text": "Apakah ada ATM di Bandar Udara Internasional Minangkabau? Kalau ada, di mana letaknya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "bandara_internasional_minangkabau"}
    },
    {
        "text": "Bisa kasih tahu di mana letak ATM yang ada di Bandar Udara Internasional Minangkabau?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "bandara_internasional_minangkabau"}
    },

    {
        "text": "Di mana lokasi ATM di Komplek Kantor Balai Kota Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_balai_kota_padang"}
    },
    {
        "text": "Alamat ATM di Komplek Kantor Balai Kota Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_balai_kota_padang"}
    },
    {
        "text": "Di sekitar Komplek Kantor Balai Kota Padang ada ATM, kan? Lokasinya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_balai_kota_padang"}
    },
    {
        "text": "Lokasi ATM di Komplek Kantor Balai Kota Padang itu di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_balai_kota_padang"}
    },
    {
        "text": "Dimana saya bisa menemukan ATM yang ada di Komplek Kantor Balai Kota Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_balai_kota_padang"}
    },
    {
        "text": "Saya ingin mencari ATM di Komplek Kantor Balai Kota Padang, di mana letaknya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_balai_kota_padang"}
    },
    {
        "text": "Apakah di Komplek Kantor Balai Kota Padang ada ATM? Kalau ada, di mana lokasi pastinya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_balai_kota_padang"}
    },
    {
        "text": "Di mana lokasi ATM di Rumah Sakit Umum Pusat Dr. M. Djamil?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsup_dr_m_djamil"}
    },
    {
        "text": "Alamat ATM di Rumah Sakit Umum Pusat Dr. M. Djamil?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsup_dr_m_djamil"}
    },
    {
        "text": "Di Rumah Sakit Umum Pusat Dr. M. Djamil ada ATM, ya? Lokasinya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsup_dr_m_djamil"}
    },
    {
        "text": "Saya mencari ATM di Rumah Sakit Umum Pusat Dr. M. Djamil. Letaknya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsup_dr_m_djamil"}
    },
    {
        "text": "Dimana posisi ATM yang ada di Rumah Sakit Umum Pusat Dr. M. Djamil?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsup_dr_m_djamil"}
    },
    {
        "text": "Bisa beri tahu di mana ATM yang terletak di Rumah Sakit Umum Pusat Dr. M. Djamil?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsup_dr_m_djamil"}
    },
    {
        "text": "Lokasi ATM di Rumah Sakit Umum Pusat Dr. M. Djamil itu di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "rsup_dr_m_djamil"}
    },
    {
        "text": "Di mana lokasi ATM di Pasar Siteba Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "pasar_siteba_padang"}
    },
    {
        "text": "Alamat ATM di Pasar Siteba Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "pasar_siteba_padang"}
    },
    {
        "text": "Ada mesin ATM di Pasar Siteba Padang? Kalau ada, di mana letaknya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "pasar_siteba_padang"}
    },
    {
        "text": "Di sekitar Pasar Siteba Padang, ada ATM? Lokasinya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "pasar_siteba_padang"}
    },
    {
        "text": "Dimana posisi ATM yang ada di Pasar Siteba Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "pasar_siteba_padang"}
    },
    {
        "text": "Saya mencari ATM di Pasar Siteba Padang. Bisa beri tahu lokasinya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "pasar_siteba_padang"}
    },
    {
        "text": "Pasar Siteba Padang ada mesin ATM, kan? Kalau ada, di mana lokasinya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "pasar_siteba_padang"}
    },
    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Capem Simpang Haru?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_simpang_haru"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Capem Simpang Haru?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_simpang_haru"}
    },
    {
        "text": "Di Kantor Bank Nagari Capem Simpang Haru ada ATM? Lokasinya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_simpang_haru"}
    },
    {
        "text": "Dimana letak ATM yang ada di Kantor Bank Nagari Capem Simpang Haru?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_simpang_haru"}
    },
    {
        "text": "Saya ingin tahu, di mana posisi ATM yang terletak di Kantor Bank Nagari Capem Simpang Haru?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_simpang_haru"}
    },
    {
        "text": "Lokasi ATM di Kantor Bank Nagari Capem Simpang Haru itu di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_simpang_haru"}
    },
    {
        "text": "Ada mesin ATM di sekitar Kantor Bank Nagari Capem Simpang Haru? Kalau ada, di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_simpang_haru"}
    },
    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Kas Tabing?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kas_tabing"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Kas Tabing?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kas_tabing"}
    },
    {
        "text": "Lokasi ATM di Kantor Bank Nagari Kas Tabing itu di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kas_tabing"}
    },
    {
        "text": "Ada mesin ATM di Kantor Bank Nagari Kas Tabing? Di mana posisinya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kas_tabing"}
    },
    {
        "text": "Dimana saya bisa menemukan ATM di Kantor Bank Nagari Kas Tabing?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kas_tabing"}
    },
    {
        "text": "Di Kantor Bank Nagari Kas Tabing, ada ATM? Lokasinya di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kas_tabing"}
    },
    {
        "text": "Bisa beri tahu di mana letak ATM di Kantor Bank Nagari Kas Tabing?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kas_tabing"}
    },
    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Capem Ulak Karang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_ulak_karang"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Capem Ulak Karang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_ulak_karang"}
    },
    {
        "text": "Di Kantor Bank Nagari Capem Ulak Karang ada ATM, ya? Di mana lokasi pastinya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_ulak_karang"}
    },
    {
        "text": "Dimana letak ATM yang ada di Kantor Bank Nagari Capem Ulak Karang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_ulak_karang"}
    },
    {
        "text": "Bisa kasih tahu di mana ATM di Kantor Bank Nagari Capem Ulak Karang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_ulak_karang"}
    },
    {
        "text": "Saya mencari ATM di Kantor Bank Nagari Capem Ulak Karang, di mana lokasinya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_ulak_karang"}
    },
    {
        "text": "Lokasi ATM di Kantor Bank Nagari Capem Ulak Karang itu di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_ulak_karang"}
    },
    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Capem Bandar Buat?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_bandar_buat"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Capem Bandar Buat?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_bandar_buat"}
    },
    {
        "text": "Ada ATM di sekitar Kantor Bank Nagari Capem Bandar Buat? Di mana letaknya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_bandar_buat"}
    },
    {
        "text": "Di Kantor Bank Nagari Capem Bandar Buat ada mesin ATM, kan? Lokasinya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_bandar_buat"}
    },
    {
        "text": "Dimana posisi ATM di Kantor Bank Nagari Capem Bandar Buat?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_bandar_buat"}
    },
    {
        "text": "Bisa kasih informasi lokasi ATM yang ada di Kantor Bank Nagari Capem Bandar Buat?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_bandar_buat"}
    },
    {
        "text": "Saya ingin tahu, di mana letak ATM yang terletak di Kantor Bank Nagari Capem Bandar Buat?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_bandar_buat"}
    },
    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Kas Belimbing?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kas_belimbing"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Kas Belimbing?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kas_belimbing"}
    },
    {
        "text": "Di Kantor Bank Nagari Kas Belimbing ada ATM? Kalau ada, di mana letaknya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kas_belimbing"}
    },
    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Kas Belimbing?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kas_belimbing"}
    },
    {
        "text": "Saya ingin tahu, ada mesin ATM di Kantor Bank Nagari Kas Belimbing? Lokasinya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kas_belimbing"}
    },
    {
        "text": "Dimana letak ATM yang ada di Kantor Bank Nagari Kas Belimbing?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kas_belimbing"}
    },
    {
        "text": "Bisa beri tahu saya di mana letak ATM di Kantor Bank Nagari Kas Belimbing?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kas_belimbing"}
    },
    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Capem Lubuk Buaya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_lubuk_buaya"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Capem Lubuk Buaya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_lubuk_buaya"}
    },
    {
        "text": "Dimana saya bisa menemukan ATM yang ada di Kantor Bank Nagari Capem Lubuk Buaya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_lubuk_buaya"}
    },
    {
        "text": "Lokasi ATM di Kantor Bank Nagari Capem Lubuk Buaya itu di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_lubuk_buaya"}
    },
    {
        "text": "Ada ATM di sekitar Kantor Bank Nagari Capem Lubuk Buaya? Lokasinya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_lubuk_buaya"}
    },
    {
        "text": "Bisa kasih tahu di mana lokasi ATM yang terletak di Kantor Bank Nagari Capem Lubuk Buaya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_lubuk_buaya"}
    },
    {
        "text": "Di Kantor Bank Nagari Capem Lubuk Buaya, ada mesin ATM? Lokasinya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_lubuk_buaya"}
    },
    {
        "text": "Di mana lokasi ATM di SPBU Coco Mata Air?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "spbu_coco_mata_air"}
    },
    {
        "text": "Alamat ATM di SPBU Coco Mata Air?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "spbu_coco_mata_air"}
    },
    {
        "text": "Di SPBU Coco Mata Air, ada ATM? Lokasinya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "spbu_coco_mata_air"}
    },
    {
        "text": "Dimana saya bisa menemukan ATM di sekitar SPBU Coco Mata Air?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "spbu_coco_mata_air"}
    },
    {
        "text": "Lokasi ATM yang ada di SPBU Coco Mata Air itu di mana, ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "spbu_coco_mata_air"}
    },
    {
        "text": "Apakah ada ATM di SPBU Coco Mata Air? Kalau ada, di mana tepatnya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "spbu_coco_mata_air"}
    },
    {
        "text": "Bisa beri tahu di mana ATM yang terletak di SPBU Coco Mata Air?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "spbu_coco_mata_air"}
    },

    {
        "text": "Di mana lokasi ATM di Komplek Pertokoan Pasar Remaja?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "komplek_pertokoan_pasar_remaja"}
    },
    {
        "text": "Alamat ATM di Komplek Pertokoan Pasar Remaja?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "komplek_pertokoan_pasar_remaja"}
    },
    {
        "text": "Ada ATM di Komplek Pertokoan Pasar Remaja? Di mana lokasinya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "komplek_pertokoan_pasar_remaja"}
    },
    {
        "text": "Di sekitar Komplek Pertokoan Pasar Remaja, ada ATM? Kalau ada, di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "komplek_pertokoan_pasar_remaja"}
    },
    {
        "text": "Dimana lokasi ATM yang terletak di Komplek Pertokoan Pasar Remaja?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "komplek_pertokoan_pasar_remaja"}
    },
    {
        "text": "Lokasi ATM di Komplek Pertokoan Pasar Remaja itu di mana, ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "komplek_pertokoan_pasar_remaja"}
    },
    {
        "text": "Saya cari ATM di Komplek Pertokoan Pasar Remaja, bisa kasih tahu di mana letaknya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "komplek_pertokoan_pasar_remaja"}
    },
    {
        "text": "Lokasi ATM-1 di Kantor Bank Nagari Cabang Simpang Empat di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "atm_1_cabang_simpang_empat"}
    },
    {
        "text": "Tolong beri tahu lokasi ATM-1 di Kantor Bank Nagari Cabang Simpang Empat?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "atm_1_cabang_simpang_empat"}
    },
    {
        "text": "Apa alamat ATM-1 di Bank Nagari Cabang Simpang Empat?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "atm_1_cabang_simpang_empat"}
    },
    {
        "text": "Dimana letak ATM 1 di Kantor Bank Nagari Cabang Simpang Empat?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "atm_1_cabang_simpang_empat"}
    },
    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Capem Kinali?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_kinali"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Capem Kinali?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_kinali"}
    },
    {
        "text": "Di sekitar Kantor Bank Nagari Capem Kinali, ada ATM? Lokasinya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_kinali"}
    },
    {
        "text": "Dimana posisi ATM di Kantor Bank Nagari Capem Kinali?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_kinali"}
    },
    {
        "text": "Apakah ada mesin ATM di Kantor Bank Nagari Capem Kinali? Di mana letaknya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_kinali"}
    },
    {
        "text": "Lokasi ATM yang ada di Kantor Bank Nagari Capem Kinali itu di mana, ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_kinali"}
    },
    {
        "text": "Bisa beri tahu saya di mana ATM yang terletak di Kantor Bank Nagari Capem Kinali?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_kinali"}
    },
    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Kas Simpang Tiga?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kas_simpang_tiga"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Kas Simpang Tiga?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kas_simpang_tiga"}
    },
    {
        "text": "Ada ATM di Kantor Bank Nagari Kas Simpang Tiga? Di mana tepatnya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kas_simpang_tiga"}
    },
    {
        "text": "Dimana lokasi ATM yang berada di Kantor Bank Nagari Kas Simpang Tiga?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kas_simpang_tiga"}
    },
    {
        "text": "Lokasi ATM di Kantor Bank Nagari Kas Simpang Tiga itu di mana, ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kas_simpang_tiga"}
    },
    {
        "text": "Saya ingin tahu, di mana ATM yang ada di Kantor Bank Nagari Kas Simpang Tiga?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kas_simpang_tiga"}
    },
    {
        "text": "Dimana saya bisa menemukan ATM di sekitar Kantor Bank Nagari Kas Simpang Tiga?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kas_simpang_tiga"}
    },
    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Cabang Muara Labuh?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_muara_labuh"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Cabang Muara Labuh?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_muara_labuh"}
    },
    {
        "text": "Apakah di Kantor Bank Nagari Cabang Muara Labuh ada ATM? Jika ada, di mana letaknya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_muara_labuh"}
    },
    {
        "text": "Saya cari ATM di Kantor Bank Nagari Cabang Muara Labuh. Lokasinya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_muara_labuh"}
    },
    {
        "text": "Dimana letak ATM yang ada di Kantor Bank Nagari Cabang Muara Labuh?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_muara_labuh"}
    },
    {
        "text": "Lokasi ATM di Kantor Bank Nagari Cabang Muara Labuh itu di mana, ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_muara_labuh"}
    },
    {
        "text": "Bisa beri tahu saya di mana posisi ATM di Kantor Bank Nagari Cabang Muara Labuh?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_muara_labuh"}
    },

    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Capem Lubuk Gadang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_lubuk_gadang"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Capem Lubuk Gadang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_lubuk_gadang"}
    },
    {
        "text": "Di Kantor Bank Nagari Capem Lubuk Gadang, ada ATM? Di mana letaknya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_lubuk_gadang"}
    },
    {
        "text": "Lokasi ATM yang terletak di Kantor Bank Nagari Capem Lubuk Gadang itu di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_lubuk_gadang"}
    },
    {
        "text": "Saya ingin tahu, di mana ATM di Kantor Bank Nagari Capem Lubuk Gadang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_lubuk_gadang"}
    },
    {
        "text": "Dimana posisi ATM di Kantor Bank Nagari Capem Lubuk Gadang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_lubuk_gadang"}
    },
    {
        "text": "Bisa beri tahu saya lokasi ATM yang ada di Kantor Bank Nagari Capem Lubuk Gadang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_lubuk_gadang"}
    },
    {
        "text": "Di mana lokasi ATM di Komplek Kantor Bupati Solok Selatan?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_solok_selatan"}
    },
    {
        "text": "Alamat ATM di Komplek Kantor Bupati Solok Selatan?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_solok_selatan"}
    },
    {
        "text": "Di sekitar Komplek Kantor Bupati Solok Selatan, ada ATM? Lokasinya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_solok_selatan"}
    },
    {
        "text": "Dimana letak ATM di Komplek Kantor Bupati Solok Selatan?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_solok_selatan"}
    },
    {
        "text": "Lokasi ATM di Komplek Kantor Bupati Solok Selatan itu di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_solok_selatan"}
    },
    {
        "text": "Apakah di Komplek Kantor Bupati Solok Selatan ada mesin ATM? Di mana posisinya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_solok_selatan"}
    },
    {
        "text": "Bisa kasih tahu di mana ATM yang ada di Komplek Kantor Bupati Solok Selatan?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_solok_selatan"}
    },
    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Cabang Pulau Punjung?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_pulau_punjung"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Cabang Pulau Punjung?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_pulau_punjung"}
    },
    {
        "text": "Dimana saya bisa menemukan ATM di Kantor Bank Nagari Cabang Pulau Punjung?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_pulau_punjung"}
    },
    {
        "text": "Lokasi ATM di Kantor Bank Nagari Cabang Pulau Punjung itu di mana, ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_pulau_punjung"}
    },
    {
        "text": "Apakah ada mesin ATM di Kantor Bank Nagari Cabang Pulau Punjung? Di mana tepatnya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_pulau_punjung"}
    },
    {
        "text": "Bisa beri tahu di mana letak ATM di Kantor Bank Nagari Cabang Pulau Punjung?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_pulau_punjung"}
    },
    {
        "text": "Di sekitar Kantor Bank Nagari Cabang Pulau Punjung, ada ATM? Lokasinya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_pulau_punjung"}
    },
    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Cabang Koto Baru?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_koto_baru"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Cabang Koto Baru?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_koto_baru"}
    },
    {
        "text": "Di mana letak ATM yang ada di Kantor Bank Nagari Cabang Koto Baru?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_koto_baru"}
    },
    {
        "text": "Saya ingin tahu lokasi ATM di Kantor Bank Nagari Cabang Koto Baru. Bisa beri tahu?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_koto_baru"}
    },
    {
        "text": "Lokasi ATM di Kantor Bank Nagari Cabang Koto Baru itu di mana, ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_koto_baru"}
    },
    {
        "text": "Ada ATM di Kantor Bank Nagari Cabang Koto Baru? Jika ada, di mana letaknya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_koto_baru"}
    },
    {
        "text": "Di sekitar Kantor Bank Nagari Cabang Koto Baru, ada mesin ATM? Di mana posisinya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_koto_baru"}
    },
    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Capem Sungai Rumbai?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_sungai_rumbai"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Capem Sungai Rumbai?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_sungai_rumbai"}
    },
    {
        "text": "Di Kantor Bank Nagari Capem Sungai Rumbai, ada ATM? Lokasinya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_sungai_rumbai"}
    },
    {
        "text": "Saya cari ATM di Kantor Bank Nagari Capem Sungai Rumbai. Bisa kasih tahu di mana letaknya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_sungai_rumbai"}
    },
    {
        "text": "Dimana saya bisa menemukan ATM di Kantor Bank Nagari Capem Sungai Rumbai?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_sungai_rumbai"}
    },
    {
        "text": "Bisa beri tahu saya lokasi ATM yang ada di Kantor Bank Nagari Capem Sungai Rumbai?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_sungai_rumbai"}
    },
    {
        "text": "Lokasi ATM di Kantor Bank Nagari Capem Sungai Rumbai itu di mana, ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_sungai_rumbai"}
    },

    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Capem Sungai Tambang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_sungai_tambang"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Capem Sungai Tambang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_sungai_tambang"}
    },
    {
        "text": "Di Kantor Bank Nagari Capem Sungai Tambang ada ATM? Dimana letaknya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_sungai_tambang"}
    },
    {
        "text": "Lokasi ATM di Kantor Bank Nagari Capem Sungai Tambang itu di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_sungai_tambang"}
    },
    {
        "text": "Saya sedang mencari ATM di Kantor Bank Nagari Capem Sungai Tambang. Bisa bantu cari?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_sungai_tambang"}
    },
    {
        "text": "Di mana posisi ATM yang ada di Kantor Bank Nagari Capem Sungai Tambang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_sungai_tambang"}
    },
    {
        "text": "Bisa kasih tahu saya di mana letak ATM di Kantor Bank Nagari Capem Sungai Tambang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_sungai_tambang"}
    },
    {
        "text": "Di mana lokasi ATM di Komplek Kantor Bupati Dharmasraya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_dharmasraya"}
    },
    {
        "text": "Alamat ATM di Komplek Kantor Bupati Dharmasraya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_dharmasraya"}
    },
    {
        "text": "Di sekitar Komplek Kantor Bupati Dharmasraya, ada ATM? Di mana letaknya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_dharmasraya"}
    },
    {
        "text": "Dimana posisi ATM yang terletak di Komplek Kantor Bupati Dharmasraya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_dharmasraya"}
    },
    {
        "text": "Lokasi ATM di Komplek Kantor Bupati Dharmasraya itu di mana, ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_dharmasraya"}
    },
    {
        "text": "Apakah ada mesin ATM di Komplek Kantor Bupati Dharmasraya? Di mana letaknya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_dharmasraya"}
    },
    {
        "text": "Bisa kasih tahu di mana ATM yang ada di Komplek Kantor Bupati Dharmasraya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kantor_bupati_dharmasraya"}
    },
    {
        "text": "Di mana lokasi ATM di Kampus STIKES Dharmasraya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kampus_stikes_dharmasraya"}
    },
    {
        "text": "Alamat ATM di Kampus STIKES Dharmasraya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kampus_stikes_dharmasraya"}
    },
    {
        "text": "Lokasi ATM di Kampus STIKES Dharmasraya itu di mana, ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kampus_stikes_dharmasraya"}
    },
    {
        "text": "Di Kampus STIKES Dharmasraya ada ATM? Bisa beri tahu di mana letaknya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kampus_stikes_dharmasraya"}
    },
    {
        "text": "Dimana posisi ATM yang ada di Kampus STIKES Dharmasraya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kampus_stikes_dharmasraya"}
    },
    {
        "text": "Saya ingin tahu di mana lokasi ATM di Kampus STIKES Dharmasraya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kampus_stikes_dharmasraya"}
    },
    {
        "text": "Bisa beri tahu saya di mana letak ATM yang ada di Kampus STIKES Dharmasraya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "kampus_stikes_dharmasraya"}
    },
    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Cabang Ujung Gading?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_ujung_gading"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Cabang Ujung Gading?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_ujung_gading"}
    },
    {
        "text": "Dimana letak ATM di Kantor Bank Nagari Cabang Ujung Gading?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_ujung_gading"}
    },
    {
        "text": "Lokasi ATM yang ada di Kantor Bank Nagari Cabang Ujung Gading itu di mana, ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_ujung_gading"}
    },
    {
        "text": "Bisa beri tahu saya lokasi ATM di Kantor Bank Nagari Cabang Ujung Gading?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_ujung_gading"}
    },
    {
        "text": "Di Kantor Bank Nagari Cabang Ujung Gading, ada mesin ATM? Di mana posisinya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_ujung_gading"}
    },
    {
        "text": "Di sekitar Kantor Bank Nagari Cabang Ujung Gading, ada ATM? Lokasinya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_ujung_gading"}
    },
    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Capem Ranah Batahan?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_ranah_batahan"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Capem Ranah Batahan?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_ranah_batahan"}
    },
    {
        "text": "Apakah ada ATM di Kantor Bank Nagari Capem Ranah Batahan? Di mana letaknya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_ranah_batahan"}
    },
    {
        "text": "Dimana lokasi ATM di Kantor Bank Nagari Capem Ranah Batahan?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_ranah_batahan"}
    },
    {
        "text": "Saya cari ATM di Kantor Bank Nagari Capem Ranah Batahan. Bisa kasih tahu di mana posisinya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_ranah_batahan"}
    },
    {
        "text": "Lokasi ATM di Kantor Bank Nagari Capem Ranah Batahan itu di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_ranah_batahan"}
    },
    {
        "text": "Bisa beri tahu saya di mana posisi ATM yang ada di Kantor Bank Nagari Capem Ranah Batahan?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_ranah_batahan"}
    },
    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Cabang Lubuk Basung?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_lubuk_basung"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Cabang Lubuk Basung?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_lubuk_basung"}
    },
    {
        "text": "Di Kantor Bank Nagari Cabang Lubuk Basung, ada ATM? Dimana letaknya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_lubuk_basung"}
    },
    {
        "text": "Saya ingin tahu lokasi ATM di Kantor Bank Nagari Cabang Lubuk Basung, di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_lubuk_basung"}
    },
    {
        "text": "Di mana posisi ATM yang ada di Kantor Bank Nagari Cabang Lubuk Basung?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_lubuk_basung"}
    },
    {
        "text": "Lokasi ATM di Kantor Bank Nagari Cabang Lubuk Basung itu di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_lubuk_basung"}
    },
    {
        "text": "Di sekitar Kantor Bank Nagari Cabang Lubuk Basung, ada mesin ATM? Di mana letaknya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_lubuk_basung"}
    },
    {
        "text": "Di mana lokasi ATM di Komplek Pasar Lama Lubuk Basung?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "komplek_pasar_lama_lubuk_basung"}
    },
    {
        "text": "Alamat ATM di Komplek Pasar Lama Lubuk Basung?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "komplek_pasar_lama_lubuk_basung"}
    },
    {
        "text": "Dimana posisi ATM di Komplek Pasar Lama Lubuk Basung?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "komplek_pasar_lama_lubuk_basung"}
    },
    {
        "text": "Ada ATM di Komplek Pasar Lama Lubuk Basung? Lokasinya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "komplek_pasar_lama_lubuk_basung"}
    },
    {
        "text": "Saya sedang mencari ATM di Komplek Pasar Lama Lubuk Basung, bisa kasih tahu dimana letaknya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "komplek_pasar_lama_lubuk_basung"}
    },
    {
        "text": "Lokasi ATM yang ada di Komplek Pasar Lama Lubuk Basung itu di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "komplek_pasar_lama_lubuk_basung"}
    },
    {
        "text": "Bisa beri tahu saya dimana ATM di Komplek Pasar Lama Lubuk Basung?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "komplek_pasar_lama_lubuk_basung"}
    },
    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Cabang Lubuk Alung?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_lubuk_alung"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Cabang Lubuk Alung?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_lubuk_alung"}
    },
    {
        "text": "Dimana saya bisa menemukan ATM di Kantor Bank Nagari Cabang Lubuk Alung?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_lubuk_alung"}
    },
    {
        "text": "Lokasi ATM di Kantor Bank Nagari Cabang Lubuk Alung itu di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_lubuk_alung"}
    },
    {
        "text": "Apakah ada ATM di Kantor Bank Nagari Cabang Lubuk Alung? Bisa beri tahu lokasinya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_lubuk_alung"}
    },
    {
        "text": "Saya cari ATM di Kantor Bank Nagari Cabang Lubuk Alung, bisa bantu beri tahu di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_lubuk_alung"}
    },
    {
        "text": "Dimana tepatnya letak ATM di Kantor Bank Nagari Cabang Lubuk Alung?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_lubuk_alung"}
    },
    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Capem Sicincin?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_sicincin"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Capem Sicincin?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_sicincin"}
    },
    {
        "text": "Di mana letak ATM di Kantor Bank Nagari Capem Sicincin?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_sicincin"}
    },
    {
        "text": "Bisa beri tahu saya lokasi ATM di Kantor Bank Nagari Capem Sicincin?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_sicincin"}
    },
    {
        "text": "Lokasi mesin ATM yang ada di Kantor Bank Nagari Capem Sicincin itu di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_sicincin"}
    },
    {
        "text": "Ada ATM di Kantor Bank Nagari Capem Sicincin? Kalau ada, di mana letaknya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_sicincin"}
    },
    {
        "text": "Dimana saya bisa menemukan ATM di Kantor Bank Nagari Capem Sicincin?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_sicincin"}
    },
    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Cabang Pangkalan?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_pangkalan"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Cabang Pangkalan?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_pangkalan"}
    },
    {
        "text": "Saya ingin tahu lokasi ATM di Kantor Bank Nagari Cabang Pangkalan. Di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_pangkalan"}
    },
    {
        "text": "Di sekitar Kantor Bank Nagari Cabang Pangkalan, ada ATM? Di mana posisinya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_pangkalan"}
    },
    {
        "text": "Bisa beri tahu saya di mana letak ATM di Kantor Bank Nagari Cabang Pangkalan?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_pangkalan"}
    },
    {
        "text": "Lokasi ATM di Kantor Bank Nagari Cabang Pangkalan itu ada di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_pangkalan"}
    },
    {
        "text": "Ada ATM di Kantor Bank Nagari Cabang Pangkalan? Dimana letaknya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_pangkalan"}
    },

    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Cabang Tapan?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_tapan"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Cabang Tapan?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_tapan"}
    },
    {
        "text": "Dimana lokasi ATM di Kantor Bank Nagari Cabang Tapan?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_tapan"}
    },
    {
        "text": "Apakah ada ATM di Kantor Bank Nagari Cabang Tapan? Kalau ada, di mana letaknya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_tapan"}
    },
    {
        "text": "Di Kantor Bank Nagari Cabang Tapan ada ATM? Lokasinya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_tapan"}
    },
    {
        "text": "Bisa kasih tahu saya lokasi ATM yang ada di Kantor Bank Nagari Cabang Tapan?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_tapan"}
    },
    {
        "text": "Lokasi ATM di Kantor Bank Nagari Cabang Tapan itu di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_tapan"}
    },
    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Capem Silaut?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_silaut"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Capem Silaut?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_silaut"}
    },
    {
        "text": "Dimana letak ATM di Kantor Bank Nagari Capem Silaut?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_silaut"}
    },
    {
        "text": "Saya cari ATM di Kantor Bank Nagari Capem Silaut, bisa bantu beri tahu di mana lokasinya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_silaut"}
    },
    {
        "text": "Di Kantor Bank Nagari Capem Silaut, apakah ada mesin ATM? Lokasinya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_silaut"}
    },
    {
        "text": "Apakah ATM di Kantor Bank Nagari Capem Silaut tersedia? Dimana saya bisa menemukannya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_silaut"}
    },
    {
        "text": "Lokasi ATM yang ada di Kantor Bank Nagari Capem Silaut itu di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_silaut"}
    },
    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Capem Air Haji?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_air_haji"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Capem Air Haji?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_air_haji"}
    },
    {
        "text": "Di mana saya bisa menemukan ATM di Kantor Bank Nagari Capem Air Haji?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_air_haji"}
    },
    {
        "text": "Lokasi ATM di Kantor Bank Nagari Capem Air Haji itu di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_air_haji"}
    },
    {
        "text": "Bisa kasih tahu di mana letak ATM di Kantor Bank Nagari Capem Air Haji?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_air_haji"}
    },
    {
        "text": "Di sekitar Kantor Bank Nagari Capem Air Haji, ada ATM? Dimana posisi tepatnya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_air_haji"}
    },
    {
        "text": "Apakah di Kantor Bank Nagari Capem Air Haji ada mesin ATM? Di mana letaknya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "capem_air_haji"}
    },
    {
        "text": "Di mana lokasi ATM di Kantor Bank Nagari Cabang Lintau?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_lintau"}
    },
    {
        "text": "Alamat ATM di Kantor Bank Nagari Cabang Lintau?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_lintau"}
    },
    {
        "text": "Di Kantor Bank Nagari Cabang Lintau ada ATM? Lokasinya di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_lintau"}
    },
    {
        "text": "Lokasi ATM yang ada di Kantor Bank Nagari Cabang Lintau itu di mana?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_lintau"}
    },
    {
        "text": "Bisa beri tahu di mana letak ATM di Kantor Bank Nagari Cabang Lintau?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_lintau"}
    },
    {
        "text": "Dimana saya bisa menemukan ATM di Kantor Bank Nagari Cabang Lintau?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_lintau"}
    },
    {
        "text": "Apakah ada ATM di Kantor Bank Nagari Cabang Lintau? Kalau ada, di mana posisinya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "cabang_lintau"}
    },
    {
        "text": "Dimana saya bisa menemukan ATM 1 di Kantor Bank Nagari Cabang Utama Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "atm_1_cabang_utama_padang"}
    },
    {
        "text": "Diman ssya bisz meemukan ATJ 1 di antor Bak Nagari Caang Urama Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "atm_1_cabang_utama_padang"}
    },
    {
        "text": "Dimana aya bia menrmukan AT 1 di Kntor ank Nxgari Cahang Uama Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "atm_1_cabang_utama_padang"}
    },
    {
        "text": "Di Kantor Bank Nagari Cabang Utama Padang, ada ATM 1? Dimana saya bisa menemukannya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "atm_1_cabang_utama_padang"}
    },
    {
        "text": "Bisa beri tahu saya lokasi ATM 1 di Kantor Bank Nagari Cabang Utama Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "atm_1_cabang_utama_padang"}
    },
    {
        "text": "Lokasi ATM 1 di Kantor Bank Nagari Cabang Utama Padang itu di mana ya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "atm_1_cabang_utama_padang"}
    },
    {
        "text": "Dimana tepatnya posisi ATM 1 yang ada di Kantor Bank Nagari Cabang Utama Padang?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "atm_1_cabang_utama_padang"}
    },
    {
        "text": "Saya sedang mencari ATM 1 di Kantor Bank Nagari Cabang Utama Padang, di mana letaknya?",
        "intent": "atm_inquiry",
        "entities": {"atm_name": "atm_1_cabang_utama_padang"}
    },
]
# Label intent untuk klasifikasi
intent_labels = [
    'greeting',
    'thanks',
    'product_inquiry',
    'promo_inquiry',
    'branch_inquiry',
    "capem_inquiry",
    "branch_kas_inquiry",
    "atm_inquiry",
]
