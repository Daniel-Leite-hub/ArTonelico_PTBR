param([switch]$Apply)
$ErrorActionPreference = 'Stop'
$root = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
$prefix = $root.TrimEnd('\') + '\'
function SafePath($relative) {
    $path = [IO.Path]::GetFullPath((Join-Path $root $relative))
    if (-not $path.StartsWith($prefix,[StringComparison]::OrdinalIgnoreCase)) { throw "Outside workspace: $path" }
    return $path
}
$actions = [Collections.Generic.List[object]]::new()
function Plan($kind,$relative,$destination,$reason) {
    $path = SafePath $relative
    if (-not (Test-Path -LiteralPath $path)) { return }
    $item = Get-Item -LiteralPath $path -Force
    $children = if ($item.PSIsContainer) { @(Get-ChildItem -LiteralPath $path -Recurse -Force) } else { @() }
    if (($item.Attributes -band [IO.FileAttributes]::ReparsePoint) -or @($children | Where-Object { $_.Attributes -band [IO.FileAttributes]::ReparsePoint }).Count) { throw "Link refused: $path" }
    $files = if ($item.PSIsContainer) { @($children | Where-Object { -not $_.PSIsContainer }) } else { @($item) }
    # No permanent deletion: automatic review requested explicit confirmation.
    if ($kind -eq 'delete') { $kind = 'segregate'; $destination = 'Obsoletos_pendentes_exclusao\'+$relative }
    $actions.Add([pscustomobject]@{action=$kind;source=$relative;destination=$destination;reason=$reason;bytes=[long](($files|Measure-Object Length -Sum).Sum)})
}
foreach ($relative in @('backups','release\backups','release\historico\executaveis','build','dist','work\test_output','artonelico_tool\__pycache__','tests\__pycache__','tools\__pycache__')) {
    Plan 'delete' $relative '' 'Obsolete backup, executable or regenerable build/cache'
}
foreach ($dir in Get-ChildItem -LiteralPath (SafePath 'work') -Directory -Filter 'tmp*') {
    # Only temporary test directories; reject any content outside the known
    # synthetic video-pack test fixtures instead of deleting unknown data.
    $files = @(Get-ChildItem -LiteralPath $dir.FullName -Recurse -File -Force)
    if (@($files | Where-Object { $_.Name -notin @('base.iso','test.SFD','manifest.json') -or $_.Length -gt 65536 }).Count) { continue }
    Plan 'delete' ('work\'+$dir.Name) '' 'Empty or synthetic temporary video-pack test directory'
}
foreach ($file in Get-ChildItem -LiteralPath (SafePath 'release\iso') -File -Filter '*.iso') {
    Plan 'delete' ('release\iso\'+$file.Name) '' 'Previous generated ISO superseded by complete 20261014 image'
}
foreach ($item in Get-ChildItem -LiteralPath $root -Force) {
    if ($item.Name -in @('ISOs','Ferramentas_Traducao','Obsoletos_pendentes_exclusao','Ar tonelico - Melody of Elemia (Undub).iso','backups','build','dist')) { continue }
    Plan 'move' $item.Name ('Ferramentas_Traducao\'+$item.Name) 'Translation package preserving relative source/tool paths'
}
$summary = [pscustomobject]@{delete_targets=0;segregated_targets=@($actions|Where-Object action -eq 'segregate').Count;move_targets=@($actions|Where-Object action -eq 'move').Count;bytes_pending_deletion=[long](($actions|Where-Object action -eq 'segregate'|Measure-Object bytes -Sum).Sum);applied=[bool]$Apply}
if (-not $Apply) { $summary|ConvertTo-Json; $actions|ConvertTo-Json -Depth 5; exit }
$image = SafePath 'ISOs\ArTonelico_PTBR_completo_20261014.iso'
$report = Get-Content -LiteralPath (SafePath 'ISOs\ArTonelico_PTBR_completo_20261014.build.json') -Raw | ConvertFrom-Json
if ($report.verified_lines -ne 32641 -or $report.capacity_fallback_count -ne 0 -or (Get-FileHash -LiteralPath $image).Hash.ToLower() -ne $report.output_sha256) { throw 'New ISO validation failed' }
if (Test-Path -LiteralPath (SafePath 'Ferramentas_Traducao')) { throw 'Destination already exists' }
$log = SafePath 'relatorios\organizacao_drive_20261014'
if (Test-Path -LiteralPath $log) { throw 'Existing log refused' }
New-Item -ItemType Directory -Path $log | Out-Null
$actions|ConvertTo-Json -Depth 5|Set-Content -LiteralPath (Join-Path $log 'plano.json') -Encoding utf8
$protected = @('Ar tonelico - Melody of Elemia (Undub).iso','release\ArTonelico_PTBR_Studio.exe','release\ArTonelico_PTBR_adaptado_108_20260926.atproj','release\videos_ptbr\manifest.json')
$protected += @(Get-ChildItem -LiteralPath (SafePath 'release\videos_ptbr') -File -Filter '*.SFD'|ForEach-Object {'release\videos_ptbr\'+$_.Name})
$hashes = @($protected|ForEach-Object {[pscustomobject]@{path=$_;sha256=(Get-FileHash -LiteralPath (SafePath $_)).Hash}})
$hashes|ConvertTo-Json|Set-Content -LiteralPath (Join-Path $log 'preservados.json') -Encoding utf8
New-Item -ItemType Directory -Path (SafePath 'Ferramentas_Traducao') | Out-Null
$completed = [Collections.Generic.List[object]]::new()
foreach ($action in $actions) {
    $source = SafePath $action.source
    $destination = SafePath $action.destination
    if (Test-Path -LiteralPath $destination) { throw "Destination exists: $destination" }
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $destination) | Out-Null
    Move-Item -LiteralPath $source -Destination $destination
    $completed.Add($action)
    $currentLog = if (Test-Path -LiteralPath $log) { $log } else { SafePath 'Ferramentas_Traducao\relatorios\organizacao_drive_20261014' }
    $completed|ConvertTo-Json -Depth 5|Set-Content -LiteralPath (Join-Path $currentLog 'concluidos.json') -Encoding utf8
}
$log = SafePath 'Ferramentas_Traducao\relatorios\organizacao_drive_20261014'
foreach ($record in $hashes) {
    $relative = if ($record.path.EndsWith('.iso')) { $record.path } else { 'Ferramentas_Traducao\'+$record.path }
    if ((Get-FileHash -LiteralPath (SafePath $relative)).Hash -ne $record.sha256) { throw "Protected content changed: $relative" }
}
$summary|ConvertTo-Json|Set-Content -LiteralPath (Join-Path $log 'resumo.json') -Encoding utf8
$summary|ConvertTo-Json -Compress
