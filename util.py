
import os

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

def get_contract_template_dir(lang):
    return os.path.join(run_time_root, "templates/contract_templates/", lang2code(lang))

def enable_controls(control_list, enable):
    for control in control_list:
        control.setEnabled(enable)