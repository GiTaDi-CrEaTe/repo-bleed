#  REPO-BLEED // Git History Secret Scanner

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python 3.7+](https://img.shields.io/badge/Python-3.7%2B-3776AB?logo=python)
![Release](https://img.shields.io/github/v/release/GiTaDi-CrEaTe/repo-bleed)

**REPO-BLEED** is a high-speed command-line interface (CLI) tool designed for DevSecOps and threat intelligence. It bypasses the current working directory and directly interrogates the `.git` database, reconstructing historical patches to hunt down leaked API keys, tokens, and passwords that developers mistakenly committed and "deleted."

If it was ever in your repo, **REPO-BLEED** will find it.

---

## ⚡ The Problem
Deleting a file containing an AWS key and making a new commit does **not** secure your repository. The key permanently exists in the Git history, waiting to be scraped by automated bots. REPO-BLEED identifies these buried threats before bad actors do.

## 🛠️ Features
* **Deep Patch Inspection:** Scans raw Git diffs across the entire commit tree.
* **High-Fidelity Heuristics:** Uses targeted Regex signatures to identify:
  * AWS Access Keys (AKIA, ASIA, etc.)
  * Stripe API Keys (Live & Restricted)
  * Google Cloud / GCP Tokens
  * Slack Webhook Tokens
  * RSA Private Keys
* **Color-Coded Terminal UI:** Clear, readable output masking the full payload to prevent shoulder-surfing.

---

## 🚀 Installation

Since this tool directly analyzes system files, it is packaged as a standalone Python Wheel (`.whl`). 

1. **Download the binary:** Go to the [Releases](https://github.com/GiTaDi-CrEaTe/repo-bleed/releases) tab and download the latest `repo_bleed-X.X.X-py3-none-any.whl` file.
2. **Install via pip:**
```bash
pip install repo_bleed-1.0.0-py3-none-any.whl

(Note: If you are on a strict OS like Kali Linux, install this inside a Python Virtual Environment).
🎯 Usage

Navigate to any local Git repository in your terminal and run:
Bash

# Run a deep history scan for exposed secrets
repo-bleed scan

Example Output
Plaintext

[*] Initializing REPO-BLEED Deep History Scan...

[!] CRITICAL VULNERABILITIES DETECTED: 1 Leaks Found
------------------------------------------------------------
[Leak 1] Type: AWS Access Key
         Commit: 5c617b8a
         Payload: AKIA************MPLE

[?] Run 'repo-bleed nuke <commit_hash>' to rewrite history and destroy the payload.

(Note: The nuke command utilizing BFG Repo-Cleaner logic is slated for the v1.1 update. For now, use git filter-branch to destroy identified targets).

Developed by Adi as part of a high-end cybersecurity research initiative.
