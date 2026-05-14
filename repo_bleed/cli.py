# repo_bleed/cli.py
import argparse
import sys
from colorama import init
from .scanner import GitScanner

def main():
    init() # Initialize colors for Windows/Linux
    parser = argparse.ArgumentParser(description="REPO-BLEED: Git History Secret Scanner")
    subparsers = parser.add_subparsers(dest="command")

    # Command: scan
    scan_parser = subparsers.add_parser("scan", help="Scan entire git history for leaked API keys")

    # Command: nuke (Placeholder for the history rewriting logic)
    nuke_parser = subparsers.add_parser("nuke", help="Rewrite git history to remove a target")
    nuke_parser.add_argument("target", help="The commit hash or file to scrub")

    args = parser.parse_args()

    if args.command == "scan":
        scanner = GitScanner()
        scanner.run_history_scan()
        scanner.report()
    elif args.command == "nuke":
        print(f"[*] Commencing BFG Repo-Cleaner protocol on {args.target}...")
        print("[!] WARN: Feature pending v1.1 update. For now, use 'git filter-branch'.")
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()