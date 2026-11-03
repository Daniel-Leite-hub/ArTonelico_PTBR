param([switch]$Apply)
$ErrorActionPreference = 'Stop'
$root = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
$prefix = $root.TrimEnd('\') + '\'
function SafePath([string]$relative) {
    $full = [IO.Path]::GetFullPath((Join-Path $root $relative))
    if (-not $full.StartsWith($prefix, [StringComparison]::OrdinalIgnoreCase)) { throw "Fora do projeto: $full" }
    return $full
}
$actions = [Collections.Generic.List[object]]::new()
function AddAction($kind, $relative, $destination, $reason) {
    $path = SafePath $relative
    if (-not (Test-Path -LiteralPath $path)) { return }
    $item = Get-Item -LiteralPath $path -Force
    $children = if ($item.PSIsContainer) { @(Get-ChildItem -LiteralPath $path -Recurse -Force) } else { @() }
    if (($item.Attributes -band [IO.FileAttributes]::ReparsePoint) -or @($children | Where-Object { $_.Attributes -band [IO.FileAttributes]::ReparsePoint }).Count) { throw "Link recusado: $path" }
    if ($destination -and (Test-Path -LiteralPath (SafePath $destination))) { throw "Destino existente: $destination" }
    $files = if ($item.PSIsContainer) { @($children | Where-Object { -not $_.PSIsContainer }) } else { @($item) }
    $actions.Add([pscustomobject]@{action=$kind;source=$relative;destination=$destination;reason=$reason;bytes=[long](($files | Measure-Object Length -Sum).Sum);sha256=if (-not $item.PSIsContainer) { (Get-FileHash -LiteralPath $path).Hash } else { $null }})
}
foreach ($file in Get-ChildItem -LiteralPath (SafePath 'isos_teste') -File -Filter 'ArTonelico_PTBR_EVD_corrigido_20261008.*') {
    AddAction 'move' ('isos_teste\'+$file.Name) ('release\iso\'+$file.Name) 'ISO aprovada e seus relatórios agrupados na entrega atual'
}
AddAction 'move' 'testes pt br' 'relatorios\testes\historico_20260926' 'Relatórios e captura de testes anteriores'
# Moves remaining reports after the current image has left this folder.
AddAction 'move' 'isos_teste' 'relatorios\testes\historico_20261006_08' 'Relatórios de ISOs substituídas; pasta sem imagens após movimentos anteriores'
foreach ($file in Get-ChildItem -LiteralPath (SafePath 'release\historico\executaveis') -File -Filter '*.exe') {
    if ($file.Name -ne 'ArTonelico_PTBR_Studio_antes_paddingEVD_20261008.exe') {
        AddAction 'delete' ('release\historico\executaveis\'+$file.Name) '' 'Versão antiga substituída; código-fonte e backup mais recente preservados'
    }
}
foreach ($relative in @('__pycache__','artonelico_tool\__pycache__','tools\__pycache__','tests\__pycache__','build','work\test_output')) {
    AddAction 'delete' $relative '' 'Cache ou resultado regenerável de compilação/testes'
}
$dist = SafePath 'dist\ArTonelico_PTBR_Studio.exe'
if ((Test-Path -LiteralPath $dist) -and ((Get-FileHash -LiteralPath $dist).Hash -eq (Get-FileHash -LiteralPath (SafePath 'release\ArTonelico_PTBR_Studio.exe')).Hash)) {
    AddAction 'delete' 'dist' '' 'Saída de compilação; EXE idêntico SHA256 ao entregue'
}
$summary = [pscustomobject]@{delete_targets=@($actions | Where-Object action -eq 'delete').Count;move_targets=@($actions | Where-Object action -eq 'move').Count;bytes_freed=[long](($actions | Where-Object action -eq 'delete' | Measure-Object bytes -Sum).Sum);applied=[bool]$Apply}
if (-not $Apply) { $summary | ConvertTo-Json; $actions | ConvertTo-Json -Depth 5; exit }
$log = SafePath 'relatorios\organizacao_20261008'
if (Test-Path -LiteralPath $log) { throw 'Trilha já existe; não sobrescrever.' }
New-Item -ItemType Directory -Path $log | Out-Null
$actions | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath (Join-Path $log 'plano.json') -Encoding utf8
$protect = @('Ar tonelico - Melody of Elemia (Undub).iso','release\ArTonelico_PTBR_Studio.exe','release\ArTonelico_PTBR_adaptado_108_20260926.atproj','release\videos_ptbr\manifest.json')
$protect += @(Get-ChildItem -LiteralPath (SafePath 'release\videos_ptbr') -File -Filter '*.SFD' | ForEach-Object { 'release\videos_ptbr\'+$_.Name })
$hashes = @($protect | ForEach-Object { [pscustomobject]@{path=$_;sha256=(Get-FileHash -LiteralPath (SafePath $_)).Hash} })
$hashes | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $log 'preservados.json') -Encoding utf8
$completed = [Collections.Generic.List[object]]::new()
foreach ($action in $actions) {
    $path = SafePath $action.source
    if ($action.sha256 -and (Get-FileHash -LiteralPath $path).Hash -ne $action.sha256) { throw "Arquivo mudou: $path" }
    if ($action.action -eq 'move') {
        $destination = SafePath $action.destination
        New-Item -ItemType Directory -Force -Path (Split-Path -Parent $destination) | Out-Null
        Move-Item -LiteralPath $path -Destination $destination
        if ($action.sha256 -and (Get-FileHash -LiteralPath $destination).Hash -ne $action.sha256) { throw "Hash mudou: $destination" }
    } else {
        Remove-Item -LiteralPath $path -Recurse -Force
    }
    $completed.Add($action)
    $completed | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath (Join-Path $log 'concluidos.json') -Encoding utf8
}
foreach ($item in $hashes) {
    if ((Get-FileHash -LiteralPath (SafePath $item.path)).Hash -ne $item.sha256) { throw "Arquivo protegido mudou: $($item.path)" }
}
$summary | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $log 'resumo.json') -Encoding utf8
$summary | ConvertTo-Json -Compress
