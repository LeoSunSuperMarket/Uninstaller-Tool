# utils/sys_utils.py
import ctypes
import sys

def require_admin():
    """请求管理员权限，自动重启程序"""
    try:
        if ctypes.windll.shell32.IsUserAnAdmin() == 0:
            ctypes.windll.shell32.ShellExecuteW(
                None, 
                "runas", 
                sys.executable, 
                " ".join([sys.argv[0]] + sys.argv[1:]), 
                None, 
                1
            )
            sys.exit()
    except Exception as e:
        print(f"权限请求失败: {str(e)}")
        sys.exit(1)