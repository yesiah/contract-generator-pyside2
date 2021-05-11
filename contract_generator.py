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
        # ---- works for onedir mode ----
        # path = os.path.join(pathlib.Path(sys.executable).parent, "templates/contract_templates/cht/中文契約範本.template")
        # with open(path, 'rb') as f:
        #     txt = f.read().decode('UTF-8')
        #     QMessageBox.information(self, "Info", txt)
        # ---- works for onedir mode ----

        # run-time root: os.path.dirname(__file__)
        run_time_root = os.path.dirname(__file__)
        tmp_path = os.path.join(run_time_root, "templates/contract_templates/cht/中文契約範本.template")
        QMessageBox.information(self, "Info", tmp_path)
        with open(tmp_path, 'rb') as f:
            txt = f.read().decode('UTF-8')
            QMessageBox.information(self, "Info", txt)

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
