# main.py
import sys
import os
from utils.sys_utils import require_admin
from gui import UninstallerGUI

def main():
    # 在main.py开头添加路径修正代码（应对不同执行方式）
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    
    # 检查并获取管理员权限
    require_admin()
    
    # 启动主程序
    app = UninstallerGUI()
    app.mainloop()

if __name__ == "__main__":
    # 添加项目根目录到Python路径（确保导入正常）
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    main()