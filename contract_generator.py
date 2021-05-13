import os
import sys
import pathlib

from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtWidgets import QMessageBox
from markdown import markdown as md2html
from weasyprint import HTML as make_html

import util
from contract_generator_ui_model import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # run_time_root = os.path.dirname(__file__)
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
    
    def field2control(self, field):
        return {
            "contract_template": [self.ui.contract_template_label, self.ui.contract_template_selector],
            "start_date": [self.ui.start_date_label, self.ui.start_date_selector],
            "end_date": [self.ui.end_date_label, self.ui.end_date_selector],
            "party_a_name": [self.ui.party_a_name_label, self.ui.party_a_name_selector],
            "party_a_representative": [self.ui.party_a_representative_label, self.ui.party_a_representative_selector],
            "party_a_registered_address": [self.ui.party_a_registered_address_label, self.ui.party_a_registered_address_edit,
                                           self.ui.party_a_contact_address_label, self.ui.party_a_contact_address_edit],
            "party_b_name": [self.ui.party_b_name_label, self.ui.party_b_name_edit],
            "party_b_representative": [self.ui.party_b_representative_label, self.ui.party_b_representative_edit],
            "party_b_registered_address": [self.ui.party_b_registered_address_label, self.ui.party_b_registered_address_edit,
                                           self.ui.party_b_contact_address_label, self.ui.party_b_contact_address_edit],
            "signature_date": [self.ui.signature_date_label, self.ui.signature_date_selector],
            "payment_method": [self.ui.payment_method_label, self.ui.payment_method_selector],
            "currency": [self.ui.currency_label, self.ui.currency_selector],
            "cross_border_payment": [self.ui.cross_border_payment_group, self.ui.cross_border_payment_yes, self.ui.cross_border_payment_no],
            "bank_account": [self.ui.bank_account_label, self.ui.bank_account_edit],
            "account_name": [self.ui.account_name_label, self.ui.account_name_edit],
            "name_of_the_bank": [self.ui.name_of_the_bank_label, self.ui.name_of_the_bank_edit],
            "bank_code": [self.ui.bank_code_label, self.ui.bank_code_edit],
            "name_of_the_branch": [self.ui.name_of_the_branch_label, self.ui.name_of_the_branch_edit],
            "branch_code": [self.ui.branch_code_label, self.ui.branch_code_edit],
            "country_of_the_bank_receiving_the_payment": [self.ui.country_of_the_bank_receiving_the_payment_label, self.ui.country_of_the_bank_receiving_the_payment_edit],
            "swift_code": [self.ui.swift_code_label, self.ui.swift_code_edit],
            "other_code": [self.ui.other_code_group,
                           self.ui.other_code_cnaps,
                           self.ui.other_code_skn_code,
                           self.ui.other_code_bsb_number,
                           self.ui.other_code_iban_code],
            "other_code_text": [self.ui.other_code_edit]
        }.get(field)
    
    def fields2controls(self, fields):
        controls = []
        for field in fields:
            controls.extend(self.field2control(field))

        return controls
    
    # internal functions ------------------------------------------------------
    def enable_controls_below_contract_template_selector(self, enable):
        fields = ["start_date",
                  "end_date",
                  "party_a_name",
                  "party_a_representative",
                  "party_a_registered_address",
                  "party_b_name",
                  "party_b_representative",
                  "party_b_registered_address",
                  "signature_date",
                  "payment_method",
                  "currency",
                  "cross_border_payment",
                  "bank_account",
                  "account_name",
                  "name_of_the_bank",
                  "bank_code",
                  "name_of_the_branch",
                  "branch_code",
                  "country_of_the_bank_receiving_the_payment",
                  "swift_code",
                  "other_code",
                  "other_code_text"]
        util.enable_controls(self.fields2controls(fields), enable)
    
    def refresh_contract_template_selector(self):
        if self.ui.contract_template_selector.isEnabled():
            self.ui.contract_template_selector.clear()
            template_dir = util.get_contract_template_dir(self.ui.lang_selector.currentText())
            templates = [pathlib.Path(f).stem for f in os.listdir(template_dir) if f.endswith(".template")]
            self.ui.contract_template_selector.addItems(templates)

    
    # signal slots ------------------------------------------------------------
    def on_language_selector_changed(self):
        # Disable all other controls
        self.enable_controls_below_contract_template_selector(False)
        # Enable template selector
        enable = self.ui.lang_selector.currentIndex() != -1
        contract_template_controls = self.field2control("contract_template")
        util.enable_controls(contract_template_controls, enable)
        self.refresh_contract_template_selector()
    
    def on_contract_template_selector_changed(self):
        return
    
    def on_party_a_name_selector_changed(self):
        return
    
    def on_payment_method_selector_changed(self):
        return
    
    def on_cross_border_payment_button_group_toggled(self, button, checked):
        return
    
    def on_other_code_button_group_toggled(self, button, checked):
        return
    
    def check_mandatory_fields(self):
        return
    
    def on_execute(self):
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

# ----------------------------------------------------------------------------

    md = """# title

         ## subtitle

         text
         - item1
         - item2"""
    
    html = md2html(md)
    html_path = pathlib.Path(sys.executable).parent / "sandbox2.html"
    print(html_path)
    with open(html_path, "w", encoding="utf-8", errors="xmlcharrefreplace") as f:
        f.write(html)
    
    pdf_path = html_path.with_suffix(".pdf")
    print(pdf_path)
    make_html(string=html).write_pdf(pdf_path)

# ----------------------------------------------------------------------------

    sys.exit(app.exec_())
