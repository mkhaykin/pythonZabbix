# Zabbix login info and environment settings.
$zabbixUser = "delme"
$zabbixPass = "Q1q123456"
$zabbixUri = "http://10.207.1.39:8080"
$graphSavePath = "C:\Users\kmi\Desktop\test.png"

# The body of login form.
$loginBody = @{
   name=$zabbixUser;
   password=$zabbixPass;
   enter="Sign in"
}

# Login to Zabbix console to get Cookie.
# Zabbix 6.0 can't reuse zbx_session of API.
# Because the session of Zabbix 6.0 expires when the browsing session ends.
# @see https://www.zabbix.com/documentation/6.0/en/manual/web_interface/cookies
$loginResult = Invoke-WebRequest -Method Post -Uri $zabbixUri -SessionVariable zbx_session -Body $loginBody
Write-Host "Login http request:" $loginResult.StatusDescription
write-host $zbx_session.Cookies.GetAllCookies()

# Save Zabbix graph to local.
# Use "-WebSession" option to keep Zabbix console session.
# You can change graph's id, size, period and so on freely.
Invoke-WebRequest -Method Get -Uri ($zabbixUri + "/chart2.php?graphid=469&from=now-3h&to=now&height=150&width=660&profileIdx=web.charts.filter") -WebSession $zbx_session -OutFile $graphSavePath

# Logout from Zabbix console.
$logoutResult = Invoke-WebRequest -Method Get -Uri ($zabbixUri + "/index.php?reconnect=1") -WebSession $zbx_session
Write-Host "Logout http requesr:" $logoutResult.StatusDescription
