# repo_bleed/rules.py

SIGNATURES = {
    "AWS Access Key": r"(A3T[A-Z0-9]|AKIA|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{16}",
    "Stripe Standard API Key": r"sk_live_[0-9a-zA-Z]{24}",
    "Stripe Restricted API Key": r"rk_live_[0-9a-zA-Z]{24}",
    "Google Cloud API Key": r"AIza[0-9A-Za-z\\-_]{35}",
    "Slack Token": r"(xox[pboa]-[0-9]{12}-[0-9]{12}-[0-9]{12}-[a-z0-9]{32})",
    "RSA Private Key": r"-----BEGIN RSA PRIVATE KEY-----",
    "Generic Password/Secret in Code": r"(?i)(password|secret|api_key|token)[\s\=\:\"]+([a-zA-Z0-9\-\_\.]{16,})"
}