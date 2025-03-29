class Software:
    def __repr__(self):
        return f"<Software {self.name} v{self.version}>"

    def __init__(self, name, version, install_date, uninstall_string, publisher):
        self.name = name
        self.version = version
        self.install_date = install_date
        self.uninstall_string = uninstall_string
        self.publisher = publisher

    def to_dict(self):
        return {
            "name": self.name,
            "version": self.version,
            "install_date": self.install_date,
            "publisher": self.publisher
        }