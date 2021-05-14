import ast
import os
import pathlib
import sys

from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtWidgets import QMessageBox
from markdown import markdown as md2html
from weasyprint import HTML as make_html

import util
from contract_generator_ui_model import Ui_MainWindow

# TODO add swift code on changed slot

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

    # getter ------------------------------------------------------------------
    def get_contract_template_path(self):
        return os.path.join(util.get_contract_template_dir(self.ui.lang_selector.currentText()), self.ui.contract_template_selector.currentText() + ".template")
    
    def get_payment_method_template_path(self):
        return os.path.join(util.get_payment_method_template_dir(self.ui.lang_selector.currentText()), self.ui.payment_method_selector.currentText() + ".template")
    
    def get_cross_border_payment(self):
        if self.ui.cross_border_payment_group.isEnabled():
            return self.ui.cross_border_payment_button_group.checkedButton().text()
    
    def is_cross_border_payment(self):
        return self.ui.cross_border_payment_group.isEnabled() and self.get_cross_border_payment() == "Yes"
    
    def read_contract_template(self):
        template_path = self.get_contract_template_path()
        return util.read_utf8(template_path)

    def read_payment_method_template(self):
        template_path = self.get_payment_method_template_path()
        return util.read_utf8(template_path)
    
    def get_start_date_str(self):
        return util.to_date_str(self.ui.lang_selector.currentText(), self.ui.start_date_selector.date())

    def get_end_date_str(self):
        return util.to_date_str(self.ui.lang_selector.currentText(), self.ui.end_date_selector.date())

    def get_party_a_name(self):
        return self.ui.party_a_name_selector.currentText()

    def get_party_a_representative(self):
        return self.ui.party_a_representative_selector.currentText()

    def get_party_a_registered_address(self):
        return self.ui.party_a_registered_address_edit.text()

    def get_party_a_contact_address(self):
        return self.ui.party_a_contact_address_edit.text()

    def get_party_b_name(self):
        return self.ui.party_b_name_edit.text()

    def get_party_b_representative(self):
        return self.ui.party_b_representative_edit.text()

    def get_party_b_registered_address(self):
        return self.ui.party_b_registered_address_edit.text()

    def get_party_b_contact_address(self):
        return self.ui.party_b_contact_address_edit.text()

    def get_signature_date(self):
        return util.to_date_str(self.ui.lang_selector.currentText(), self.ui.signature_date_selector.date())

    def get_payment_method(self):
        return self.get_payment_method_markdown()

    def get_currency(self):
        return self.ui.currency_selector.currentText()

    def get_cross_border_payment(self):
        if self.ui.cross_border_payment_group.isEnabled():
            return self.ui.cross_border_payment_button_group.checkedButton().text()

    def get_bank_account(self):
        return self.ui.bank_account_edit.text()

    def get_account_name(self):
        return self.ui.account_name_edit.text()

    def get_name_of_the_bank(self):
        return self.ui.name_of_the_bank_edit.text()

    def get_bank_code(self):
        return self.ui.bank_code_edit.text()

    def get_name_of_the_branch(self):
        return self.ui.name_of_the_branch_edit.text()

    def get_branch_code(self):
        return self.ui.branch_code_edit.text()

    def get_country_of_the_bank_receiving_the_payment(self):
        return self.ui.country_of_the_bank_receiving_the_payment_edit.text()

    def get_swift_code(self):
        return self.ui.swift_code_edit.text()

    def get_other_code(self):
        if self.ui.other_code_group.isEnabled():
            return self.ui.other_code_button_group.checkedButton().text()

    def get_other_code_edit(self):
        if self.ui.other_code_edit.isEnabled():
            return self.ui.other_code_edit.text()
    
    def get_field_value(self, field):
        return {
            "start_date": self.get_start_date_str(),
            "end_date": self.get_end_date_str(),
            "party_a_name": self.get_party_a_name(),
            "party_a_representative": self.get_party_a_representative(),
            "party_a_registered_address": self.get_party_a_registered_address(),
            "party_a_contact_address": self.get_party_a_contact_address(),
            "party_b_name": self.get_party_b_name(),
            "party_b_representative": self.get_party_b_representative(),
            "party_b_registered_address": self.get_party_b_registered_address(),
            "party_b_contact_address": self.get_party_b_contact_address(),
            "signature_date": self.get_signature_date(),
            "payment_method": self.get_payment_method()
        }.get(field, None)
    
    def get_field_values(self, fields):
        return list(map(self.get_field_value, fields))

    def get_payment_method_field_value(self, field):
        return {
            "currency": self.get_currency(),
            "cross_border_payment": self.get_cross_border_payment(),
            "bank_account": self.get_bank_account(),
            "account_name": self.get_account_name(),
            "name_of_the_bank": self.get_name_of_the_bank(),
            "bank_code": self.get_bank_code(),
            "name_of_the_branch": self.get_name_of_the_branch(),
            "branch_code": self.get_branch_code(),
            "country_of_the_bank_receiving_the_payment": self.get_country_of_the_bank_receiving_the_payment(),
            "swift_code": self.get_swift_code(),
            "other_code": self.get_other_code(),
            "other_code_text": self.get_other_code_edit()
        }.get(field, None)

    def get_payment_method_field_values(self, fields):
        return list(map(self.get_payment_method_field_value, fields))

    def get_payment_method_markdown(self):
        if self.ui.payment_method_selector.isEnabled():
            template_txt = self.read_payment_method_template()
            fields = util.parse_fields(template_txt)
            values = self.get_payment_method_field_values(fields)
            d = dict(zip(fields, values))
            return template_txt.format(**d)
    
    def get_markdown(self):
        template = self.read_contract_template()
        field_names = util.parse_fields(template)
        field_values = self.get_field_values(field_names)
        d = dict(zip(field_names, field_values))
        return template.format(**d)

        md = """# title

            ## subtitle

            text
            - item1
            - item2"""
        return md

    """
    Json format, eval as dict

    Party A template stores all possible Party A names
    """
    def load_party_a_template(self):
        template_dir = util.get_party_a_template_dir(self.ui.lang_selector.currentText())
        for _, _, files in os.walk(template_dir):
            for f in files:
                if f.endswith(".template"):
                    with open(os.path.join(template_dir, f), 'rb') as utf8_file:
                        txt = utf8_file.read().decode('UTF-8')
                        return ast.literal_eval(txt)

    # internal utils ----------------------------------------------------------
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

    """
    Enable/Disable all controls related to field names
    """

    def enable_field_controls(self, fields, enable):
        util.enable_controls(self.fields2controls(fields), enable)

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
        self.enable_field_controls(fields, enable)
    
    def enable_controls_below_payment_method_selector(self, enable):
        fields = ["currency",
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
        self.enable_field_controls(fields, enable)

    def refresh_contract_template_selector(self):
        if self.ui.contract_template_selector.isEnabled():
            self.ui.contract_template_selector.clear()
            template_dir = util.get_contract_template_dir(self.ui.lang_selector.currentText())
            templates = [pathlib.Path(f).stem for f in os.listdir(template_dir) if f.endswith(".template")]
            self.ui.contract_template_selector.addItems(templates)

    def refresh_party_a_name_selector(self):
        if self.ui.party_a_name_selector.isEnabled():
            self.party_a_template = self.load_party_a_template()
            if self.party_a_template:
                self.ui.party_a_name_selector.clear()
                self.ui.party_a_representative_selector.clear()
                self.ui.party_a_name_selector.addItems(self.party_a_template.keys())

    def refresh_payment_method_selector(self):
        if self.ui.payment_method_selector.isEnabled():
            self.ui.payment_method_selector.clear()
            template_dir = util.get_payment_method_template_dir(self.ui.lang_selector.currentText())
            templates = [pathlib.Path(f).stem for f in os.listdir(template_dir) if f.endswith(".template")]
            self.ui.payment_method_selector.addItems(templates)

    # signal slots ------------------------------------------------------------
    def on_language_selector_changed(self):
        self.enable_controls_below_contract_template_selector(False)

        # Enable template selector
        fields = ["contract_template"]
        enable = self.ui.lang_selector.currentIndex() != -1
        self.enable_field_controls(fields, enable)
        self.refresh_contract_template_selector()

    def on_contract_template_selector_changed(self):
        self.enable_controls_below_contract_template_selector(False)
        template_path = self.get_contract_template_path()
        fields = util.read_fields(template_path)
        if fields:
            self.enable_field_controls(fields, True)

        self.refresh_party_a_name_selector()
        self.refresh_payment_method_selector()

    def on_party_a_name_selector_changed(self):
        if self.party_a_template:
            self.enable_field_controls(["party_a_representative"], True)
            self.ui.party_a_representative_selector.clear()
            party_a_representatives = self.party_a_template[self.ui.party_a_name_selector.currentText()]
            self.ui.party_a_representative_selector.addItems(party_a_representatives)

    def on_payment_method_selector_changed(self):
        self.enable_controls_below_payment_method_selector(False)
        template_path = self.get_payment_method_template_path()
        fields = util.read_fields(template_path)
        self.enable_field_controls(fields, True)

    def on_cross_border_payment_button_group_toggled(self, button, checked):
        # TODO enable/disable swift code and other code (text)
        self.check_mandatory_fields()

    def on_other_code_button_group_toggled(self, button, checked):
        # TODO enable/disable swift code and other code text
        self.check_mandatory_fields()

    def check_mandatory_fields(self):
        print("check")
        self.ui.execute_button.setEnabled(False)
        if self.ui.lang_selector.currentIndex() == -1 or self.ui.contract_template_selector.currentIndex() == -1:
            print("lang wrong")
            return

        if self.ui.start_date_selector.isEnabled() and self.ui.end_date_selector.isEnabled() and (self.ui.end_date_selector.date() < self.ui.start_date_selector.data()):
            print("start date wrong")
            return

        if self.ui.party_a_name_selector.isEnabled() and self.ui.party_a_name_selector.currentIndex() == -1:
            print("party a name wrong")
            return

        if self.ui.party_a_representative_selector.isEnabled() and self.ui.party_a_representative_selector.currentIndex() == -1:
            print("party a repre wrong")
            return

        if self.ui.party_a_registered_address_edit.isEnabled() and self.ui.party_a_registered_address_edit.text() == "":
            print("party a address wrong")
            return

        if self.ui.party_b_name_edit.isEnabled() and self.ui.party_b_name_edit.text() == "":
            print("party b name wrong")
            return

        if self.ui.party_b_representative_edit.isEnabled() and self.ui.party_b_representative_edit.text() == "":
            print("party b repre wrong")
            return

        if self.ui.party_b_registered_address_edit.isEnabled() and self.ui.party_b_registered_address_edit.text() == "":
            print("party b addres wrong")
            return

        if self.ui.payment_method_selector.isEnabled() and self.ui.payment_method_selector.currentIndex() == -1:
            print("payment wrong")
            return

        if self.ui.currency_selector.isEnabled() and self.ui.currency_selector.currentIndex() == -1:
            print("currency wrong")
            return

        if self.ui.cross_border_payment_group.isEnabled():
            if self.ui.cross_border_payment_button_group.checkedId() == -1:
                print("cross boader wrong")
                return

        if self.ui.bank_account_edit.isEnabled() and self.ui.bank_account_edit.text() == "":
            print("bank account wrong")
            return

        if self.ui.account_name_edit.isEnabled() and self.ui.account_name_edit.text() == "":
            print("account name wrong")
            return

        if self.ui.name_of_the_bank_edit.isEnabled() and self.ui.name_of_the_bank_edit.text() == "":
            print("bank name wrong")
            return

        if self.ui.bank_code_edit.isEnabled() and self.ui.bank_code_edit.text() == "":
            print("bank code wrong")
            return

        if self.ui.name_of_the_branch_edit.isEnabled() and self.ui.name_of_the_branch_edit.text() == "":
            print("branch name wrong")
            return

        if self.ui.branch_code_edit.isEnabled() and self.ui.branch_code_edit.text() == "":
            print("branch code wrong")
            return

        if self.ui.country_of_the_bank_receiving_the_payment_edit.isEnabled() and self.ui.country_of_the_bank_receiving_the_payment_edit.text() == "":
            print("country")
            return

        if self.is_cross_border_payment():
            if self.ui.swift_code_edit.text() == "":
                print("swift code empty")
                return

            if self.ui.other_code_button_group.checkedId() != -1 and self.ui.other_code_edit.text() == "":
                print("other code empty")
                return

        self.ui.execute_button.setEnabled(True)

    def on_execute(self):
        md = self.get_markdown()
        html = md2html(md)
        # TODO decide where to store files
        html_path = pathlib.Path(sys.executable).parent / "contract.html"
        with open(html_path, "w", encoding="utf-8", errors="xmlcharrefreplace") as f:
            f.write(html)
            msg = "Saved html to " + str(html_path)
            QMessageBox.information(self, "Info", msg)

        pdf_path = html_path.with_suffix(".pdf")
        make_html(string=html).write_pdf(pdf_path)
        msg = "Saved pdf to " + str(pdf_path)
        QMessageBox.information(self, "Info", msg)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

# ----------------------------------------------------------------------------

    # md = """# title

    #      ## subtitle

    #      text
    #      - item1
    #      - item2"""

    # html = md2html(md)
    # html_path = pathlib.Path(sys.executable).parent / "sandbox2.html"
    # print(html_path)
    # with open(html_path, "w", encoding="utf-8", errors="xmlcharrefreplace") as f:
    #     f.write(html)

    # pdf_path = html_path.with_suffix(".pdf")
    # print(pdf_path)
    # make_html(string=html).write_pdf(pdf_path)

# ----------------------------------------------------------------------------

    sys.exit(app.exec_())
