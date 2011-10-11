[System.Reflection.Assembly]::LoadWithPartialName("System.windows.forms") | Out-Null

$ColorDialog = New-Object System.Windows.Forms.ColorDialog

$ColorDialog.FullOpen = 1;
$ret = $ColorDialog.ShowDialog()

if ($ret -eq "OK")
{
	$hex = [Convert]::ToString($ColorDialog.Color.R, 16) + [Convert]::ToString($ColorDialog.Color.G, 16) + [Convert]::ToString($ColorDialog.Color.B, 16)
	Write-Host `#$hex
}