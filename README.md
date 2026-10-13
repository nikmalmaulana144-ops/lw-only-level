# 🎮 MALZ Level Up System

> Automated Free Fire Lone Wolf leveling bot with a real-time web dashboard.
> Persistent device identity • Smart DNS resolver • Parallel account workers • Live EXP tracker

![Version](https://img.shields.io/badge/version-0.2-blueviolet?style=flat-square)
![Python](https://img.shields.io/badge/python-3.11+-blue?style=flat-square)
![License](https://img.shields.io/badge/license-Private-red?style=flat-square)
![Platform](https://img.shields.io/badge/platform-Railway-black?style=flat-square)

---

## 📖 Table of Contents

- [Features](#-features)
- [Architecture](#-architecture)
- [Project Structure](#-project-structure)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Running Locally](#-running-locally)
- [Deploying to Railway](#-deploying-to-railway)
- [Dashboard Guide](#-dashboard-guide)
- [API Reference](#-api-reference)
- [Accounts Format](#-accounts-format)
- [Logs & Diagnostics](#-logs--diagnostics)
- [Troubleshooting](#-troubleshooting)
- [FAQ](#-faq)
- [Disclaimer](#-disclaimer)

---

## ✨ Features

### Core Engine
- 🔐 **Guest (UID + Password) or Access Token login** with automatic cache and refresh
- 🧠 **Persistent Device Identity** — 1 account = 1 stable fingerprint (`devices.json`)
- ⚡ **Parallel account workers** — every account runs independently with its own TCP gateway
- 🎯 **Automatic mode switching**
  - Level 1–2 → **Battle Royale (BR)** search
  - Level 3+ → **Lone Wolf** auto-switch (higher EXP/hour)
- 🛰️ **Cloudflare DNS Resolver** (1.1.1.1 / 1.0.0.1) with fallback to system DNS
- 🔁 **Auto-heal reconnection** with exponential backoff and cache invalidation
- 🧩 **Hand-rolled protobuf + AES-CBC + TEA-CBC** codec (no external schema)
- 💾 **Token cache** (`token_cache.json`) with TTL to prevent redundant logins
- 🕐 **Version config cache** to reduce version server load

### Web Dashboard
- 🌐 **Real-time** stats refreshed every 5 seconds
- 🎨 **5 color themes** (Violet, Cyan, Emerald, Gold, Rose) + Dark/Light mode
- 📊 **Live EXP tracker** with animated counters and confetti on level-up
- 🏆 **Top Harvester podium** (Silver / Gold / Bronze)
- 👥 **Account cards** with 3 density modes (Comfortable / Compact / Dense)
- 🔍 **Search, filter, sort, bulk-select, bulk-pause, bulk-delete**
- 📟 **Terminal-style live log viewer** with category filters and search
- 📦 **Batch JSON import** (single + bulk with preview)
- 🎵 **Background music** with toggle button

---

## 🏗 Architecture
