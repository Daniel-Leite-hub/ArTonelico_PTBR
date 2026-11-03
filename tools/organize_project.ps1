param([switch]$Apply)
$ErrorActionPreference = 'Stop'
$root = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
$prefix = $root.TrimEnd('\') + '\'
$actions = [Collections.Generic.List[object]]::new()
function SafePath([string]$relative) {
    $full = [IO.Path]::GetFullPath((Join-Path $root $relative))
    if (-not $full.StartsWith($prefix, [StringComparison]::OrdinalIgnoreCase)) { throw "Fora do projeto: $full" }
    return $full
}
function AddAction([string]$kind, [string]$source, [string]$destination, [string]$reason) {
    $path = SafePath $source
    if (-not (Test-Path -LiteralPath $path)) { return }
    $item = Get-Item -LiteralPath $path -Force
    if ($item.Attributes -band [IO.FileAttributes]::ReparsePoint) { throw "Link recusado: $path" }
    $files = if ($item.PSIsContainer) { @(Get-ChildItem -LiteralPath $path -Recurse -Force -File) } else { @($item) }
    if ($item.PSIsContainer) {
        $links = @(Get-ChildItem -LiteralPath $path -Recurse -Force | Where-Object { $_.Attributes -band [IO.FileAttributes]::ReparsePoint })
        if ($links.Count) { throw "Pasta com links recusada: $path" }
    }
    $bytes = ($files | Measure-Object Length -Sum).Sum
    $hash = if (-not $item.PSIsContainer) { (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash } else { $null }
    if ($destination -and (Test-Path -LiteralPath (SafePath $destination))) { throw "Destino existente: $destination" }
    $actions.Add([pscustomobject]@{action=$kind;source=$source;destination=$destination;reason=$reason;bytes=[long]$bytes;sha256=$hash})
}

# Preserve application, curated project, movie pack and all project backups in place.
Get-ChildItem -LiteralPath (SafePath 'release') -File -Filter '*_antes_*.exe' | ForEach-Object {
    AddAction 'move' ('release\'+$_.Name) ('release\historico\executaveis\'+$_.Name) 'EXE anterior preservado para rollback'
}
foreach ($name in @('BANCO_ADICIONAL_EXPERIMENTAL.md','COBERTURA.md','DIAGNOSTICO_ACENTOS_MENU.md','REALOCACAO_STRINGS.md')) {
    AddAction 'move' $name ('docs\tecnica\'+$name) 'Documentacao tecnica agrupada'
}
foreach ($name in @('BANCO_ADICIONAL_EXPERIMENTAL.md','COBERTURA.md','CONTINUIDADE.md','REALOCACAO_STRINGS.md')) {
    AddAction 'move' ('release\'+$name) ('release\historico\documentacao\'+$name) 'Documentacao antiga de entrega preservada'
}
AddAction 'move' 'teste.capacity_fallbacks.json' 'relatorios\testes\teste.capacity_fallbacks.json' 'Relatorio antigo de montagem'
Get-ChildItem -LiteralPath (SafePath 'Videos_editados_PTBR') -File -Filter '*.png' | ForEach-Object {
    AddAction 'move' ('Videos_editados_PTBR\'+$_.Name) ('Videos_editados_PTBR\historico\capturas\'+$_.Name) 'Capturas historicas agrupadas'
}
foreach ($relative in @('__pycache__','artonelico_tool\__pycache__','tools\__pycache__','tests\__pycache__','build','work\test_output','tools\SFD_Muxer.obj')) {
    AddAction 'delete' $relative '' 'Cache ou artefato regeneravel de compilacao/testes'
}
$releaseExe = SafePath 'release\ArTonelico_PTBR_Studio.exe'
$distExe = SafePath 'dist\ArTonelico_PTBR_Studio.exe'
if ((Test-Path -LiteralPath $distExe) -and ((Get-FileHash -LiteralPath $distExe).Hash -eq (Get-FileHash -LiteralPath $releaseExe).Hash)) {
    AddAction 'delete' 'dist\ArTonelico_PTBR_Studio.exe' '' 'Duplicata SHA256 do EXE mantido em release'
}
$obsolete = @(
 'AVAN_AT_PTBR_65_30fps.m1v','AVAN_AT_PTBR_65_30fps.SFD','AVAN_AT_PTBR_fundo_65.SFD',
 'AVAN_AT_PTBR_mascaras_reduzidas_v2.m1v','AVAN_AT_PTBR_mascaras_reduzidas.m1v',
 'AVAN_AT_PTBR_portugues_destacado.m1v','AVAN_AT_PTBR_previa_mascaras_reduzidas_v2.mp4',
 'AVAN_AT_PTBR_previa_mascaras_reduzidas.mp4','AVAN_AT_PTBR_previa_portugues_destacado.mp4',
 'AVAN_AT_PTBR_previa_Trebuchet_fundo_suave.mp4','AVAN_AT_PTBR_previa_Trebuchet_sem_fundo.mp4',
 'AVAN_AT_PTBR_previa.mp4','AVAN_AT_PTBR_Trebuchet_fundo_suave.m1v',
 'AVAN_AT_PTBR_Trebuchet_sem_fundo.m1v','AVAN_AT_PTBR.m1v'
)
foreach ($name in $obsolete) { AddAction 'delete' ('Videos_editados_PTBR\'+$name) '' 'Previa intermediaria substituida pela abertura aprovada 65% 30fps v2' }
$audioOriginal = SafePath 'Videos_editados_PTBR\AVAN_AT_audio_original.adx'
foreach ($name in @('AVAN_AT_audio_30fps_reaberto.adx','AVAN_AT_audio_30fps_v2_reaberto.adx','AVAN_AT_audio_reaberto.adx')) {
    $path = SafePath ('Videos_editados_PTBR\'+$name)
    if ((Test-Path -LiteralPath $path) -and ((Get-FileHash -LiteralPath $path).Hash -eq (Get-FileHash -LiteralPath $audioOriginal).Hash)) {
        AddAction 'delete' ('Videos_editados_PTBR\'+$name) '' 'Audio de verificacao identico SHA256 ao original preservado'
    }
}
$deleted = @($actions | Where-Object action -eq 'delete')
$moved = @($actions | Where-Object action -eq 'move')
$summary = [pscustomobject]@{delete_targets=$deleted.Count;move_targets=$moved.Count;bytes_to_free=[long](($deleted | Measure-Object bytes -Sum).Sum);applied=[bool]$Apply}
$summary | ConvertTo-Json -Compress
if (-not $Apply) { $actions | ConvertTo-Json -Depth 5; exit }
$logdir = SafePath 'relatorios\organizacao_20261003'
if (Test-Path -LiteralPath $logdir) { throw 'Organizacao ja registrada; nao sobrescrever a trilha.' }
New-Item -ItemType Directory -Path $logdir | Out-Null
$actions | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath (Join-Path $logdir 'plano.json') -Encoding utf8
$protectedPaths = @('Ar tonelico - Melody of Elemia (Undub).iso','release\ArTonelico_PTBR_adaptado_108_20260926.atproj','release\ArTonelico_PTBR_Studio.exe','release\videos_ptbr\manifest.json')
$protectedPaths += @(Get-ChildItem -LiteralPath (SafePath 'release\videos_ptbr') -File -Filter '*.SFD' | ForEach-Object { 'release\videos_ptbr\'+$_.Name })
$protected = @($protectedPaths | ForEach-Object { [pscustomobject]@{path=$_;sha256=(Get-FileHash -LiteralPath (SafePath $_) -Algorithm SHA256).Hash} })
$protected | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $logdir 'preservados.json') -Encoding utf8
$results = [Collections.Generic.List[object]]::new()
foreach ($action in $actions) {
    $source = SafePath $action.source
    if ($action.sha256 -and (Get-FileHash -LiteralPath $source -Algorithm SHA256).Hash -ne $action.sha256) { throw "Arquivo mudou: $source" }
    if ($action.action -eq 'move') {
        $destination = SafePath $action.destination
        New-Item -ItemType Directory -Force -Path (Split-Path -Parent $destination) | Out-Null
        Move-Item -LiteralPath $source -Destination $destination
        if ($action.sha256 -and (Get-FileHash -LiteralPath $destination -Algorithm SHA256).Hash -ne $action.sha256) { throw "Hash alterado: $destination" }
    } else {
        # Exact resolved targets only, verified as inside this workspace above.
        Remove-Item -LiteralPath $source -Recurse -Force
    }
    $results.Add($action)
    $results | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath (Join-Path $logdir 'concluidos.json') -Encoding utf8
}
foreach ($item in $protected) {
    if ((Get-FileHash -LiteralPath (SafePath $item.path) -Algorithm SHA256).Hash -ne $item.sha256) { throw "Arquivo protegido mudou: $($item.path)" }
}
$summary | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $logdir 'resumo.json') -Encoding utf8
$summary | ConvertTo-Json -Compress
