from PyQt6.QtWidgets import (
    QApplication, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QWidget, QMessageBox
)
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 輸入與互動")
        self.resize(400, 300)

        # 元件：標籤、輸入框、按鈕
        self.label = QLabel("請輸入文字並點擊按鈕：", self)
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("在這裡輸入...")
        self.display_button = QPushButton("顯示文字", self)
        self.reverse_button = QPushButton("反轉文字", self)
        self.clear_button = QPushButton("清除文字", self)

        # 設定佈局
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.display_button)
        layout.addWidget(self.reverse_button)
        layout.addWidget(self.clear_button)
        self.setLayout(layout)

        # 事件連接
        self.display_button.clicked.connect(self.display_text)
        self.reverse_button.clicked.connect(self.reverse_text)
        self.clear_button.clicked.connect(self.clear_text)

    def display_text(self):
        text = self.input_field.text()
        if len(text) >= 10:
            QMessageBox.warning(self, "警告", "輸入文字太長！")
        elif text.strip():
            self.label.setText(f"您輸入了：{text}")
        else:
            QMessageBox.warning(self, "警告", "輸入欄位為空！")

    def clear_text(self):
        self.input_field.clear()
        self.label.setText("請輸入文字並點擊按鈕：")

    def reverse_text(self):
        text = self.input_field.text()
        if len(text) >= 10:
            QMessageBox.warning(self, "警告", "輸入文字太長！")
        elif text.strip():
            reversed_text = text[::-1]
            self.label.setText(f"反轉結果：{reversed_text}")
        else:
            QMessageBox.warning(self, "警告", "輸入欄位為空！")

# 主程式入口
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())