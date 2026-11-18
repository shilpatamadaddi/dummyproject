import configparser


cofig = configparser.RawConfigParser()
cofig.read(".\\configs\\cofig.ini")

class  Read_Configs:
    @staticmethod
    def get_admin_page_url():
        url = config.get('admin login info','admin+page_url')
        return url

    @staticmethod
    def get_username():
        username = config.get('admin login info','username')