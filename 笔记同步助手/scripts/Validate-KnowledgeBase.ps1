[CmdletBinding()]
param(
    [string]$ProjectRoot = (Split-Path -Parent $PSScriptRoot)
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$project = (Resolve-Path -LiteralPath $ProjectRoot).Path
$vaultRoot = Split-Path -Parent $project
$errors = New-Object 'System.Collections.Generic.List[string]'

$requiredDirectories = @(
    'raw/articles',
    'raw/papers',
    'raw/books',
    'raw/chats',
    'raw/notes',
    'raw/meetings',
    'wiki/sources',
    'wiki/concepts',
    'wiki/entities',
    'wiki/topics',
    'workflows',
    'scripts'
)

$requiredFiles = @(
    'AGENTS.md',
    'index.md',
    'log.md',
    'wiki/sources/_template.md',
    'wiki/concepts/_template.md',
    'wiki/entities/_template.md',
    'wiki/topics/_template.md'
)

foreach ($relativePath in $requiredDirectories) {
    $path = Join-Path $project ($relativePath -replace '/', '\')
    if (-not (Test-Path -LiteralPath $path -PathType Container)) {
        [void]$errors.Add("Missing directory: $relativePath")
    }
}

foreach ($relativePath in $requiredFiles) {
    $path = Join-Path $project ($relativePath -replace '/', '\')
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
        [void]$errors.Add("Missing file: $relativePath")
    }
}

$requiredYamlFields = @('title', 'type', 'aliases', 'tags', 'sources', 'created', 'updated', 'status')
$wikiFiles = Get-ChildItem -LiteralPath (Join-Path $project 'wiki') -Recurse -File -Filter '*.md'

foreach ($file in $wikiFiles) {
    $content = Get-Content -Raw -Encoding UTF8 -LiteralPath $file.FullName
    $frontMatter = [regex]::Match(
        $content,
        '\A---\r?\n(?<yaml>.*?)\r?\n---',
        [System.Text.RegularExpressions.RegexOptions]::Singleline
    )

    if (-not $frontMatter.Success) {
        [void]$errors.Add("Missing YAML front matter: $($file.FullName)")
        continue
    }

    $yaml = $frontMatter.Groups['yaml'].Value
    foreach ($field in $requiredYamlFields) {
        if ($yaml -notmatch "(?m)^$([regex]::Escape($field))\s*:") {
            [void]$errors.Add("Missing YAML field '$field': $($file.FullName)")
        }
    }
}

$linkFiles = @()
$linkFiles += Get-ChildItem -LiteralPath $project -File -Filter '*.md'
$linkFiles += Get-ChildItem -LiteralPath (Join-Path $project 'wiki') -Recurse -File -Filter '*.md'
$linkFiles += Get-ChildItem -LiteralPath (Join-Path $project 'workflows') -Recurse -File -Filter '*.md'

foreach ($file in ($linkFiles | Sort-Object FullName -Unique)) {
    $content = Get-Content -Raw -Encoding UTF8 -LiteralPath $file.FullName
    foreach ($match in [regex]::Matches($content, '\[\[([^\]]+)\]\]')) {
        $target = $match.Groups[1].Value
        $target = ($target -split '\|', 2)[0]
        $target = ($target -split '#', 2)[0]
        $target = $target.Trim()

        if ($target -notmatch '^笔记同步助手/') {
            continue
        }

        $relativeTarget = $target -replace '/', '\'
        if ([string]::IsNullOrWhiteSpace([System.IO.Path]::GetExtension($relativeTarget))) {
            $relativeTarget += '.md'
        }

        $resolvedTarget = Join-Path $vaultRoot $relativeTarget
        if (-not (Test-Path -LiteralPath $resolvedTarget -PathType Leaf)) {
            [void]$errors.Add("Broken link '$target' in $($file.FullName)")
        }
    }
}

if ($errors.Count -gt 0) {
    Write-Host "Knowledge base validation failed with $($errors.Count) error(s):" -ForegroundColor Red
    foreach ($validationError in $errors) {
        Write-Host "- $validationError" -ForegroundColor Red
    }
    exit 1
}

Write-Host 'Knowledge base validation passed.' -ForegroundColor Green
Write-Host "Wiki files checked: $($wikiFiles.Count)"
Write-Host "Markdown files checked for full-path links: $($linkFiles.Count)"

