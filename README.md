<h1 align="center">
  <b>Save restricted Content Bot | Enterprise Release June 2024. </b>
</h1>

    
Contact: [Telegram](https://t.me/hakutakaid)

---

## ENTERPRISE RELEASE INFO

**Pembaruan**: Bot ini diperbarui dengan fungsi login, penambahan tag ganti nama khusus, grup log, perubahan teks, dan banyak lagi gulir ke bawah hingga terakhir untuk melihat pembaruan terkini yaitu pada 28 Juni 2024.

## Features:

- Mampu mengekstrak konten dari entitas/saluran/grup swasta atau publik
- langsung ganti nama dan teruskan ke saluran/grup/pengguna
- Judul/thumbnail khusus
- penghapusan thumbnail default otomatis dari video
- Menghapus/Mengganti kata-kata dari nama file dan caption
- Mudah digunakan dan diterapkan
- pesan pin otomatis (jika disematkan)
- login melalui nomor telepon
- Mampu mendownload video Youtube + 30 situs lainnya didukung melalui perintah `/dl`

### Try Live Bot
Bot link - [CLICK HERE](https://t.me/skmfilestoresbot)
---
Bot telegram yang stabil untuk menerima pesan terbatas dari grup/saluran/bot dengan dukungan thumbnail khusus, dibuat oleh [TEAM SPY](https://t.me/hakutakaid) Bot ini dapat berjalan di saluran secara langsung.


## How to get vars - [TEAM SPY](https://t.me/hakutakaid)

- `BOT TOKEN`: @Botfather di telegram

- `OWNER_ID`: Buka @missrose_bot, mulai dan kirim /info untuk mendapatkan id Anda

- `FORCESUB`: Sebelum mulai membuat bot, buat saluran publik dan dapatkan nama pengguna tanpa '@'Jadikan bot sebagai admin di saluran itu.

- `LOG_GROUP`: Dapatkan dengan menyalin tautan posting apa pun dan mengekstrak nilainya tepat setelah `https:t.me/c/` dan berikutnya `/` lalu setelah meletakkan `-100` sebelumnya. Jadikan bot ADMIN di channel atau grup tersebut.
 
- `API_ID` dan `API_HASH`: [Telegram.org](https://my.telegram.org/auth)

- `MONGO_DB`: Buat mongo db baru tidak disarankan menggunakan yang default jika Anda tidak tahu cara membuatnya, Anda dapat menggunakan jika tidak, jangan gunakan karena dapat menyebabkan peretasan/penghapusan akun melalui sesi.
## Deploying Guide - [TEAM SPY](https://t.me/hakutakaid)

### Deploy on `VPS`

Metode Mudah:
- Garpu dan bintangi repo
- Masuk ke main lalu edit ```config.py``` seperti di bawah ini
- Masukkan nilai masing-masing di `""` dan simpan.

```
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", ""))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", ")
LOG_GROUP = int(getenv("LOG_GROUP", ""))
FORCESUB = getenv("FORCESUB", "")
```

- Now run following commands one by one...

```
sudo apt update
sudo apt install ffmpeg git python3-pip
git clone your_repo_link
cd you_repo_name
pip3 install -r requirements.txt
python3 -m curkontent
```

- jika Anda ingin bot berjalan di latar belakang, masukkan `screen -S gagan` sebelum `python3 -m curkontent` 
- setelah `python3 -m curkontent`, klik `ctrl+A`, `ctrl+D`
- jika Anda ingin menghentikan bot, masukkan `screen -r gagan` dan untuk mematikan layar masukkan `screen -S gagan -X quit`.


## Deploy your bot on `heroku`

» Method - 1:
- Bintangi repo, dan fork dalam mode desktop
- Click on  [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?template=https://github.com/hakutakaid/CuriKontentBot)
- Fill your values and done ✅
 
» Method - 2:
- Bintangi repo, beri peringkat, dan fork dalam mode desktop
- buat aplikasi di heroku
- masuk ke pengaturan ```aplikasi›› tampilkan config vars››``` tambahkan semua variabel seperti yang ditunjukkan di atas dengan mengetikkan nama dan nilainya yang benar.
- tambahkan buildpack yaitu `python` dan `https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git`
- sambungkan ke github dan terapkan
- nyalakan dino
- Catatan: Anda harus menambahkan buildpack di heroku untuk mendapatkan thumbnail video asli dan menghapus thumbnail yang sudah disetel jika tidak, Anda akan mendapatkan video hitam
<b> Bagaimana cara menambahkannya? </b>
- Buka pengaturan heroku
- gulir ke bawah dan klik tambahkan buildpack
- sekarang tempel tautan berikut yaitu `https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git` di bilah input dan klik tambahkan buildpack
- Sekarang kembali dan pindahkan

## Deploy on Render
- Garpu dan bintangi repo
- edit `config.py` sama seperti yang dipandu untuk penerapan VPS (Anda juga dapat mengedit saat render dengan mengisi variabel lingkungan)
- Buka render.com dan singup/signin
- buat layanan web baru dan pilih paket gratis
- sambungkan github dan repositori Anda
- Klik Terapkan
- Selesai ✅
- Lihat tutorialnya
https://t.me/save_restricted_content_bots/759

## Koyeb Deployment

- Garpu dan bintangi repo
- edit `config.py` sama seperti yang dipandu untuk penerapan VPS (Anda juga dapat mengedit di koyeb dengan mengisi variabel lingkungan)
- Buka koyeb.com dan singup/signin
- buat layanan web baru pastikan Anda harus memilih tipe build `Dokerfile` karena di Koyeb sebagai default dicentang ke `buildpacks` jadi Anda harus mengubahnya.
- sambungkan github dan repositori Anda
- Klik Terapkan
- Selesai ✅

## Terms of USE / Modification 
Visit [Terms](https://github.com/devgaganin/Save-Restricted-Content-Bot-Repo/blob/main/TERMS_OF_USE.md) and accept the guidelines.

# Updates

Last update 8 JULY 2024

### Available Commands

You can copy and paste the following commands into @BotFather:

```plaintext
start - ✅ Check if I am alive!
batch - 😎 batch method
dl - 🎞 Download videos from YouTube, Xsite, Instagram, Amazon Mini TV, Pinterest, LinkedIn, Internet Archive, etc. /dl <link>
login - login via phone number
auth - authorize users
unauth - revoke access
settings - Get all settings in a single command for rename, replace delete, setchat everything
broadcast - send message to bot users
session - generate Pyrogram V2 session
plan - 💰 Learn about premium plan details
terms - 📋 View the bot's terms and conditions
stats - 📊 Check the statistics
speedtest - 🔴 Check speed (Only for sudo users)
get - 🙃 Get a list of current users
list - 🍏 List authorized users
lock - ⚡ Add channels to the protected list to prevent extraction
pro - 💎 Add session to save restricted files from private chats/bots
noob - 😭 Delete the Pro activation
host - ☁️ Host your own SRC Bot
unhost - 🌨️ Unhost the SRC and FWD Bot
help - 😧 Get command help
cancel - ❌ Cancel ongoing process
```

---

## Important Note

**Catatan**: Mengubah syarat dan perintah tidak secara ajaib menjadikan Anda seorang pengembang. Pengembangan nyata melibatkan pemahaman kode, penulisan fungsi baru, dan debugging masalah, bukan hanya mengganti nama sesuatu. Andai saja semudah itu!