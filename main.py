# -*- coding: utf-8 -*-
import ctypes
import re
import socket
import uuid
from prettytable import PrettyTable
import cowsay
import random
import getpass

class Monitor:
    def __init__(self):
        self._nameMashin = socket.gethostname()
        table = self._createTableReport()
        table.add_row(self.getNameMashin())
        table.add_row(self.getDomainName())
        table.add_row(self.getMacAddress())
        table.add_row(self.get_display_name(), divider=True)
        table.add_row(self.getIPAddress(), divider=True)
        table.add_row(self.getAccountName())
        print(table)
        if self.getChans():
            cowsay.cow(self.__randomInscription())

    def getNameMashin(self):
        return ["Имя компьютера",  self._nameMashin]

    def getDomainName(self):
        fqdn = socket.getfqdn()
        if "." in fqdn:
            domain = fqdn[fqdn.find(".") + 1:]
            return ["Domain", domain]
        else:
            return ["Domain", "не в домене"]

    def getMacAddress(self):
        return ["MAC", ':'.join(re.findall('..', '%012x' % uuid.getnode()))]

    def get_display_name(self):
        GetUserNameEx = ctypes.windll.secur32.GetUserNameExW
        NameDisplay = 3

        size = ctypes.pointer(ctypes.c_ulong(0))
        GetUserNameEx(NameDisplay, None, size)

        nameBuffer = ctypes.create_unicode_buffer(size.contents.value)
        GetUserNameEx(NameDisplay, nameBuffer, size)
        return ["Пользователь", nameBuffer.value]

    def getIPAddress(self):
        return ["IP address", "\n".join(socket.gethostbyname_ex(socket.gethostname())[2])]

    def getAccountName(self):
        return ["Учетная запись",getpass.getuser()]

    def _createTableReport(self):
        table = PrettyTable()
        table.field_names = ["Параметр", "Значение"]
        return table

    def __randomInscription(self):
        listPhrases = ["Не пялься на меня так", "ПОРНО detected ;-)", "Бросай все, пошли есть", "Мне больше не наливай",
                       "Выключай все, пошли домой", "Я что-то удалила...", "Нажми, нажми еще раз...", "Я настоящая тЁлка",
                       "Муу..", "Давай по новой, все )№!:%", "А ты заплатил за это ПО ?!",
                       "Судно — транспортное средство, которое пристаёт к причалу, а причаливает к пристани",
                       "Работай-работай не отвлекайся..", "Сейчас бы картошечки с котлеткой, а не вот это вот все...",
                       "Ну что опять?",
                       "ты знал, что минимальная температура во Вселенной –273,15 °С, а максимальная больше 10 "
                       "триллионов градусов Цельсия. Получается мы любим холод))"]
        return random.choice(listPhrases)

    def getChans(self):
        return True if random.randint(1, 100) < 50 else False


if __name__ == "__main__":


    monitor = Monitor()
    input()


