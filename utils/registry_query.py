import subprocess
import json

def get_installed_software():
    """通过PowerShell查询已安装软件列表"""
    try:
        cmd = [
            "powershell",
            "-Command",
            "Get-ItemProperty HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\*, "
            "HKLM:\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* "
            "| Where-Object { $_.DisplayName -ne $null } "
            "| Select-Object DisplayName, DisplayVersion, InstallDate, UninstallString, Publisher "
            "| ConvertTo-Json"
        ]
        
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
        software_list = json.loads(result.decode('utf-8', errors='ignore'))
        return software_list
    except Exception as e:
        print(f"Error querying registry: {str(e)}")
        return []