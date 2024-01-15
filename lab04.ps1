# CIS 1.1.5
# create var for registry path
$regPath = "HKLM:\SYSTEM\CurrentControlSet\Control\Lsa"

# create var for registry property
$regProp = "LimitBlankPasswordUse"

# create var for registry value (1 enables, 0 disables)
$regValue = 1

# Set registry value
Set-ItemProperty -Path $regPath -Name $regProp -Value $regValue



# CIS 18.4.3
# disable SMB v1
Disable-WindowsOptionalFeature -Online -FeatureName "SMB1Protocol-Client"