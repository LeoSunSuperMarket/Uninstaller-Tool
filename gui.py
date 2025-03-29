import tkinter as tk
from tkinter import ttk, messagebox
from models.software import Software
from services.software_service import SoftwareService

class UninstallerGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python Software Uninstaller")
        self.geometry("1000x600")
        self._create_widgets()
        self._load_software_list()
        
    def _create_widgets(self):
        # 创建表格
        self.tree = ttk.Treeview(self, columns=("Name", "Version", "Publisher", "InstallDate"), show="headings")
        self.tree.heading("Name", text="软件名称")
        self.tree.heading("Version", text="版本")
        self.tree.heading("Publisher", text="发布者")
        self.tree.heading("InstallDate", text="安装日期")
        
        # 创建滚动条
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # 卸载按钮
        self.uninstall_btn = ttk.Button(
            self, 
            text="卸载选中软件", 
            command=self._perform_uninstall
        )
        
        # 布局
        self.tree.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.uninstall_btn.grid(row=1, column=0, pady=10)
        
        # 配置网格布局
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
    def _load_software_list(self):
        self.software_objects = SoftwareService.get_all_software()  # 新增成员变量存储对象
        for software in self.software_objects:
            self.tree.insert("", "end", values=(
                software.name,
                software.version,
                software.publisher,
                software.install_date
            ), tag=id(software))  # 添加tag存储对象标识

    
    def _perform_uninstall(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("警告", "请先选择要卸载的软件！")
            return
    
        # 通过tag获取对应的Software对象
        software_id = int(self.tree.item(selected_item[0], "tag")[0])
        selected_software = next(
            (s for s in self.software_objects if id(s) == software_id),
            None
        )

        if selected_software:
            success = SoftwareService.uninstall(selected_software)