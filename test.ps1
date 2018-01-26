Get-WMIObject win32_group -filter "LocalAccount='True'" -computername $Server | Select Name

Get-WMIObject