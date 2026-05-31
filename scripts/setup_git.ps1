# Run from PowerShell at the repo root.
# Resets a partially-initialized .git (mount artifact) and starts fresh.
# Usage: powershell -ExecutionPolicy Bypass -File scripts\setup_git.ps1

$ErrorActionPreference = "Stop"
$repo = (Get-Item -Path ".").FullName
Write-Host "Resetting git at $repo"

if (Test-Path ".git") {
    Remove-Item -Recurse -Force ".git"
}

git init -b main
git config user.email "silentyouval@gmail.com"
git config user.name "Youval"
git add -A
git commit -m "Phase 0: scaffold AI Venture Factory MVP"

Write-Host "Git initialized and Phase 0 committed."
git log --oneline | Select-Object -First 3
