import pymongo
from .. import bot as gagan
from telethon import events, Button
from pyrogram import Client, filters
from telethon.tl.types import DocumentAttributeVideo
from multiprocessing import Process, Manager
import re
import logging
import pymongo
import sys
from pyrogram.types import Message
from mutagen.easyid3 import EasyID3
import math
import os
import yt_dlp
import time
from datetime import datetime as dt, timedelta
import json
import asyncio
import cv2
from yt_dlp import YoutubeDL
from telethon.sync import TelegramClient
from .. import sigma as app
from curkontent.assets.functions import screenshot
import subprocess
from config import MONGODB_CONNECTION_STRING, OWNER_ID, LOG_GROUP

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DB_NAME = "start_users"
COLLECTION_NAME = "registered_users_collection"

mongo_client = pymongo.MongoClient(MONGODB_CONNECTION_STRING)
db = mongo_client[DB_NAME]
collection = db[COLLECTION_NAME]

def load_registered_users():
    registered_users = set()
    for user_doc in collection.find():
        registered_users.add(user_doc["user_id"])
    return registered_users

def save_registered_users(registered_users):
    for user_id in registered_users:
        collection.update_one({"user_id": user_id}, {"$set": {"user_id": user_id}}, upsert=True)

REGISTERED_USERS = load_registered_users()

@gagan.on(events.NewMessage(pattern=f"^/start"))
async def start(event):
    """
    Command to start the bot
    """
    user_id = event.sender_id
    collection.update_one({"user_id": user_id}, {"$set": {"user_id": user_id}}, upsert=True)
    buttons = [
        [Button.url("Join Channel", url="https://t.me/AnonymousX888")],
        [Button.url("Contact Me", url="https://t.me/HakutakaID")],
    ]
    await gagan.send_message(
        event.chat_id,
#        file=START_PIC,
        message=TEXT,
        buttons=buttons,
        link_preview=False,        
    )

@gagan.on(events.NewMessage(pattern=f"^/gcast"))
async def broadcast(event):
    if event.sender_id != OWNER_ID:
        return await event.respond("You are not authorized to use this command.")

    message = event.message.text.split(' ', 1)[1]
    for user_doc in collection.find():
        try:
            user_id = user_doc["user_id"]
            await gagan.send_message(user_id, message)
        except Exception as e:
            logger.error(f"Error sending message to user {user_id}: {str(e)}")

def get_registered_users():
    registered_users = []
    for user_doc in collection.find():
        registered_users.append((str(user_doc["user_id"]), user_doc.get("first_name", "")))
    return registered_users

# Function to save user IDs and first names to a text file
def save_user_ids_to_txt(users_info, filename):
    with open(filename, "w") as file:
        for user_id, first_name in users_info:
            file.write(f"{user_id}: {first_name}\n")

@gagan.on(events.NewMessage(incoming=True, pattern='/get'))
async def get_registered_users_command(event):
    # Check if the command is initiated by the owner
    if event.sender_id != OWNER_ID:
        return await event.respond("You are not authorized to use this command.")
    
    # Get all registered user IDs and first names
    registered_users = get_registered_users()

    # Save user IDs and first names to a text file
    filename = "registered_users.txt"
    save_user_ids_to_txt(registered_users, filename)

    # Send the text file
    await event.respond(file=filename, force_document=True)
    os.remove(filename)  # Remove the temporary file after sending

S = "/start"
START_PIC = "https://graph.org/file/1dfb96bd8f00a7c05f164.gif"
TEXT = "Hai! Saya adalah Bot Penghemat Konten Tingkat Lanjut, lakukan login di bot dengan /login dan mulai menyimpan dari saluran/grup publik/pribadi melalui pengiriman tautan pos.\n\n👉🏻 Jalankan /batch untuk proses massal hingga rentang 1.000 file."


M = "/plan"
PRE_TEXT = """💰 **Harga Premium**: Mulai dari $2 atau 200 INR yang diterima melalui **__Amazon Gift Card__** (syarat dan ketentuan berlaku).
📥 **Batas Unduhan**: Pengguna dapat mengunduh hingga 100 file dalam satu perintah batch.
🛑 **Batch**: Anda akan mendapatkan dua mode /bulk dan /batch.
   - Pengguna disarankan untuk menunggu proses pembatalan otomatis sebelum melanjutkan pengunduhan atau pengunggahan apa pun.\n
📜 **Syarat dan Ketentuan** : Untuk keterangan lebih lanjut dan syarat dan ketentuan selengkapnya, silakan kirim /terms.
"""

@gagan.on(events.NewMessage(pattern=f"^{M}"))
async def plan_command(event):
    # Creating inline keyboard with buttons
    buttons = [
        [Button.url("Kirim Kode Kartu Hadiah", url="https://t.me/skmfilestoresbot")]
    ]
    # Sending photo with caption and buttons
    await gagan.send_message(
        event.chat_id,
        message=PRE_TEXT,
        buttons=buttons,
        link_preview=False,
    )

T = "/terms"
TERM_TEXT = """📜 **Syarat dan Ketentuan** 📜\n
✨ Kami tidak bertanggung jawab atas perbuatan pengguna, dan kami tidak mempromosikan konten berhak cipta. Jika ada pengguna yang terlibat dalam aktivitas tersebut, itu sepenuhnya merupakan tanggung jawab mereka.
✨ Saat pembelian, kami tidak menjamin uptime, downtime, atau validitas paket. __Otorisasi dan pelarangan pengguna merupakan kebijaksanaan kami; kami berhak melarang atau mengizinkan pengguna kapan saja.__
✨ Pembayaran kepada kami **__tidak menjamin__** otorisasi untuk perintah /batch. Semua keputusan mengenai otorisasi dibuat berdasarkan kebijaksanaan dan suasana hati kami.
"""

@gagan.on(events.NewMessage(pattern=f"^{T}"))
async def term_command(event):
    # Creating inline keyboard with buttons
    buttons = [
        [Button.url("Query?", url="https://t.me/skmfilestoresbot"),
         Button.url("Channel", url="https://telegram.dog/AnonymousX888")]
    ]

    # Sending photo with caption and buttons
    await gagan.send_message(
        event.chat_id,
        message=TERM_TEXT,
        buttons=buttons,
        link_preview=False,
    )

REPO_URL = "https://github.com/hakutakaid/CuriKontentBot"

HELP_TEXT = """Berikut adalah perintah yang tersedia:

➡️ /batch - untuk memproses tautan satu per satu secara berulang melalui satu id pesan.

➡️ /dl - untuk mendownload video youtube.

➡️ /host - untuk mengunduh video youtube.

➡️ /cancel - untuk membatalkan batch

➡️ /settings - untuk mengedit pengaturan.

[Repositori GitHub](%s)
""" % REPO_URL

# Purchase premium for more website supported repo and /adl repo.

@gagan.on(events.NewMessage(pattern='/help'))
async def help_command(event):
    buttons = [[Button.url("REPO", url=REPO_URL)]]
    await event.respond(HELP_TEXT, buttons=buttons, link_preview=False)


def thumbnail(chat_id):
    return f'{chat_id}.jpg' if os.path.exists(f'{chat_id}.jpg') else f'thumb.jpg'

# Function to get video info including duration
def get_youtube_video_info(url):
    ydl_opts = {'quiet': True, 'skip_download': True}
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        if not info_dict:
            return None
        return {
            'title': info_dict.get('title', 'Unknown Title'),
            'duration': info_dict.get('duration', 0),  # Duration in seconds
        }

@app.on_message(filters.command("dl", prefixes="/"))
async def youtube_dl_command(_, message):
    # Check if the command has an argument (YouTube URL)
    if len(message.command) > 1:
        youtube_url = message.command[1]
        
        # Send initial message indicating downloading
        progress_message = await message.reply("Fetching video info...")

        try:
            # Fetch video info using yt-dlp
            video_info = get_youtube_video_info(youtube_url)
            if not video_info:
                await progress_message.edit_text("Failed to fetch video info.")
                return

            # Check if video duration is greater than 3 hours (10800 seconds)
            if video_info['duration'] > 10800:
                await progress_message.edit_text("Video duration exceeds 3 hours. Not allowed.")
                return
            
            await progress_message.edit_text("Downloading video...")

            # Safe file naming
            original_file = f"{video_info['title'].replace('/', '_').replace(':', '_')}.mp4"
            thumbnail_path = f"{video_info['title'].replace('/', '_').replace(':', '_')}.jpg"

            # Download video
            ydl_opts = {
                'format': 'best',
                'outtmpl': original_file,  # Output file template
                'noplaylist': True,  # Disable downloading playlists
            }

            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([youtube_url])  # Start downloading the video

            # Check if the original file exists before renaming
            if not os.path.exists(original_file):
                await progress_message.edit_text("Failed to download video.")
                return

            # Edit the progress message to indicate uploading
            await progress_message.edit_text("Uploading video...")

            # Get video metadata
            metadata = video_metadata(original_file)
            caption = f"{video_info['title']}\n\n__**Powered by [Advance Content Saver Bot](https://t.me/skmfilestoresbot)**__"  # Set caption to the title of the video
            
            # Send the video file and thumbnail
            curkontent = message.chat.id
            k = thumbnail(curkontent)
            result = await app.send_video(
                chat_id=message.chat.id,
                video=original_file,
                caption=caption,
                thumb=k,
                width=metadata['width'],
                height=metadata['height'],
                duration=metadata['duration'],
            )
            await result.copy(LOG_GROUP)

            os.remove(original_file)

            # Delete the progress message after sending video
            await progress_message.delete()

        except Exception as e:
            await progress_message.edit_text(f"An error occurred: {str(e)}")

    else:
        await message.reply("Please provide a YouTube URL after /dl.")

def video_metadata(file):
    vcap = cv2.VideoCapture(f'{file}')
    width = round(vcap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = round(vcap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = vcap.get(cv2.CAP_PROP_FPS)
    frame_count = vcap.get(cv2.CAP_PROP_FRAME_COUNT)
    duration = round(frame_count / fps)
    return {'width': width, 'height': height, 'duration': duration}
