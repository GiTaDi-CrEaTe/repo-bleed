# repo_bleed/scanner.py
import subprocess
import re
from colorama import Fore, Style
from .rules import SIGNATURES

class GitScanner:
    def __init__(self):
        self.findings = []

    def run_history_scan(self):
        print(f"{Fore.CYAN}[*] Initializing REPO-BLEED Deep History Scan...{Style.RESET_ALL}")
        
        try:
            # Extract the entire git patch history
            result = subprocess.run(
                ["git", "log", "-p", "--all"], 
                capture_output=True, text=True, check=True
            )
            history = result.stdout
        except subprocess.CalledProcessError:
            print(f"{Fore.RED}[!] FATAL: Not a git repository.{Style.RESET_ALL}")
            return

        lines = history.split('\n')
        current_commit = "UNKNOWN"

        for i, line in enumerate(lines):
            if line.startswith("commit "):
                current_commit = line.split(" ")[1][:8]
            
            # Only scan added or modified lines
            if line.startswith("+") and not line.startswith("+++"):
                for name, pattern in SIGNATURES.items():
                    matches = re.finditer(pattern, line)
                    for match in matches:
                        self.findings.append({
                            "type": name,
                            "commit": current_commit,
                            "leak": match.group(0)
                        })

    def report(self):
        if not self.findings:
            print(f"{Fore.GREEN}[+] SECURE: No exposed secrets detected in Git history.{Style.RESET_ALL}")
            return

        print(f"\n{Fore.RED}[!] CRITICAL VULNERABILITIES DETECTED: {len(self.findings)} Leaks Found{Style.RESET_ALL}")
        print("-" * 60)
        for idx, finding in enumerate(self.findings):
            print(f"{Fore.YELLOW}[Leak {idx+1}]{Style.RESET_ALL} Type: {finding['type']}")
            print(f"         Commit: {finding['commit']}")
            # Mask the secret so we don't accidentally display the whole thing on screen
            masked_leak = finding['leak'][:4] + "*" * (len(finding['leak'])-8) + finding['leak'][-4:]
            print(f"         Payload: {Fore.RED}{masked_leak}{Style.RESET_ALL}\n")
        
        print(f"{Fore.CYAN}[?] Run 'repo-bleed nuke <commit_hash>' to rewrite history and destroy the payload.{Style.RESET_ALL}")