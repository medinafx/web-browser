import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget

class Browser(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.load_turing()
    
    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Cargando TURING...")
        
        self.view = QWebEngineView(self)        
        layout = QVBoxLayout(self)
        layout.addWidget(self.view)
        
        self.showMaximized()

    def on_load_finished(self):
        self.setWindowTitle("INSS - TURING")

    def load_turing(self):
        self.setWindowTitle("Cargando TURING...")
        self.view.setUrl(QUrl('https://turing-portal.inss.gob.ni/auth-service/login'))
        self.view.loadFinished.connect(self.on_load_finished)

app = QApplication(sys.argv)
browser = Browser()
sys.exit(app.exec_())