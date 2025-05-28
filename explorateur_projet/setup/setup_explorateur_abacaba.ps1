
# ===============================
# Script PowerShell de configuration AIAF GitHub
# ===============================

$repoName = "explorateur_abacaba_github_repo"
$targetPath = "E:\$repoName"
$gitUrl = "https://github.com/explorateuraiaf/GPT-Explorateur-ABACABA.git"

# ===> 1. Fermer VS Code dans ce dossier (si ouvert)
Write-Host "🔒 Fermeture de VS Code..." -ForegroundColor Yellow
taskkill /F /IM Code.exe > $null 2>&1
Start-Sleep -Seconds 2

# ===> 2. Supprimer l'ancien dossier
if (Test-Path $targetPath) {
    Write-Host "📦 Suppression de l'ancien dossier $repoName..." -ForegroundColor DarkYellow
    try {
        Remove-Item -Recurse -Force $targetPath
        Write-Host "✅ Dossier supprimé avec succès."
    } catch {
        Write-Host "⛔ Impossible de supprimer le dossier. Vérifiez qu’il n’est pas utilisé." -ForegroundColor Red
        exit
    }
}

# ===> 3. Créer un nouveau dossier vide
New-Item -ItemType Directory -Path $targetPath | Out-Null
Set-Location -Path $targetPath

# ===> 4. Clonage du dépôt GitHub
Write-Host "🔁 Clonage depuis GitHub..." -ForegroundColor Cyan
git clone $gitUrl .

# ===> 5. Ajouter comme safe.directory
Write-Host "🛡️  Ajout à Git safe.directory..." -ForegroundColor Green
git config --global --add safe.directory $targetPath

# ===> 6. Statut du dépôt
git status

# ===> 7. Réouverture dans VS Code
Write-Host "🚀 Réouverture dans VS Code..." -ForegroundColor Magenta
code .
