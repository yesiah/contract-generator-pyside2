import os
import sys
import pathlib
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtWidgets import QMessageBox

import markdown
from weasyprint import HTML

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
    
    def on_language_selector_changed(self):
        return
    
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
    
    html = markdown.markdown(md)
    html_path = pathlib.Path(sys.executable).parent / "sandbox2.html"
    print(html_path)
    with open(html_path, "w", encoding="utf-8", errors="xmlcharrefreplace") as f:
        f.write(html)
    
    pdf_path = html_path.with_suffix(".pdf")
    print(pdf_path)
    HTML(string=html).write_pdf(pdf_path)

# ----------------------------------------------------------------------------

    sys.exit(app.exec_())
