from models.software import Software
from utils.registry_query import get_installed_software
import subprocess

class SoftwareService:
    @staticmethod
    def get_all_software():
        raw_data = get_installed_software()
        software_objects = []
        for item in raw_data:
            software = Software(
                name=item.get("DisplayName"),
                version=item.get("DisplayVersion"),
                install_date=item.get("InstallDate"),
                uninstall_string=item.get("UninstallString"),
                publisher=item.get("Publisher")
            )
            software_objects.append(software)
        return software_objects

    @staticmethod
    def uninstall(software):
        """执行卸载命令"""
        try:
            if not hasattr(software, 'uninstall_string'):
                raise ArithmeticError("无效的软件对象")

            cmd = software.uninstall_string
            if "MsiExec.exe" in cmd:
                cmd = f'msiexec /x {{{software.uninstall_string.split("{{")[1].split("}}")[0]}}} /quiet'
            
            subprocess.run(
                cmd, 
                shell=True,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            return True
        except subprocess.CalledProcessError as e:
            print(f"卸载失败: {e.stderr.decode()}")
            return False
        except AttributeError as e:
            print(f"无效软件对象: {str(e)}")
            return False