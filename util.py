
import os
from string import Formatter

from PySide2.QtCore import QLocale

run_time_root = os.path.dirname(__file__)
# contract_template_path = os.path.join(run_time_root, "templates/contract_templates/cht/中文契約範本.template")
# QMessageBox.information(self, "Info", contract_template_path)
# with open(contract_template_path, 'rb') as f:
#     txt = f.read().decode('UTF-8')
#     QMessageBox.information(self, "Info", txt)

# party_a_template_path = os.path.join(run_time_root, "templates/party_a_template/cht/cht-甲方.template")
# QMessageBox.information(self, "Info", party_a_template_path)
# with open(party_a_template_path, 'rb') as f:
#     txt = f.read().decode('UTF-8')
#     QMessageBox.information(self, "Info", txt)

"""
IBM 3 character code
"""
def lang2code(name):
    return {
        u"\u7e41\u9ad4\u4e2d\u6587": "cht",
        u"English": "enu",
        u"\u65e5\u672c\u8a9e": "jpn",
        u"\ud55c\uad6d\uc5b4": "kor"
    }.get(name, "cht")

# path utils
def get_contract_template_dir(lang):
    return os.path.join(run_time_root, "templates/contract_templates/", lang2code(lang))

def get_party_a_template_dir(lang):
    return os.path.join(run_time_root,"templates/party_a_template/", lang2code(lang))

def get_payment_method_template_dir(lang):
    return os.path.join(run_time_root, "templates/payment_method_templates/", lang2code(lang))

# control utils
def enable_controls(control_list, enable):
    for control in control_list:
        control.setEnabled(enable)

# text file utils
def read_utf8(path):
    if os.path.exists(path):
        with open(path, 'rb') as f:
            return f.read().decode('UTF-8')

def parse_fields(txt):
    if txt:
        return [fname for _, fname, _, _ in Formatter().parse(txt) if fname]

def read_fields(path):
    txt = read_utf8(path)
    return parse_fields(txt)

# date
def zh_tw_date_format():
    return "yyyy 年 MM 月 dd 日"

def en_us_date_format():
    return "MMMM dd, yyyy"

def ja_jp_date_format():
    return "yyyy 年 MM 月 dd 日"

def ko_kr_date_format():
    return "yyyy 년 MM 월 dd 일"

def select_date_format(x):
    return {
        "繁體中文": zh_tw_date_format(),
        "English": en_us_date_format(),
        "日本語": ja_jp_date_format(),
        "한국어": ko_kr_date_format()
    }.get(x, en_us_date_format())

# locale
def zh_tw_locale():
    return QLocale(QLocale.Chinese, QLocale.TraditionalChineseScript, QLocale.Taiwan)

def en_us_locale():
    return QLocale(QLocale.English, QLocale.UnitedStates)

def ja_jp_locale():
    return QLocale(QLocale.Japanese, QLocale.Japan)

def ko_kr_locale():
    return QLocale(QLocale.Korean, QLocale.SouthKorea)

def select_locale(x):
    return {
        "繁體中文": zh_tw_locale(),
        "English": en_us_locale(),
        "日本語": ja_jp_locale(),
        "한국어": ko_kr_locale()
    }.get(x, en_us_locale())

# locale and date util
def select_locale_and_date_format(x):
    return (select_locale(x), select_date_format(x))

def to_date_str(lang, qdate):
    curr_locale, date_fmt = select_locale_and_date_format(lang)
    return curr_locale.toString(qdate, date_fmt)
