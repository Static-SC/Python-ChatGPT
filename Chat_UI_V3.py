import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
import openai
from dotenv import load_dotenv

load_dotenv()

# Load the Chat.ui file
form_class = uic.loadUiType("ChatV3.ui")[0]

# Set up OpenAI API credentials
openai.api_key = os.getenv("OPENAI_API_KEY")

# GPT-3.5-turbo parameters
Models = "gpt-3.5-turbo"
temperature = 0.2
max_tokens = 100

class ChatWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Set initial values
        self.models_combobox.setCurrentText(Models)
        self.temp_combobox.setCurrentText(str(temperature))
        self.tokens_combobox.setCurrentText(str(max_tokens))
        
        # Populate dropdown lists
        self.models_combobox.addItems(["gpt-3.5-turbo", "gpt-3.5-turbo-0301", "gpt-4"])
        self.temp_combobox.addItems([str(i/10) for i in range(11)])
        self.tokens_combobox.addItems([str(i) for i in range(100, 2100, 100)])

        # Connect button click event
        self.ask_button.clicked.connect(self.send_question)

    def send_question(self):
        question = self.question_box.text()
        answer = self.get_gpt3_response(question)
        self.reply_box.append(f"Question: {question}\nAnswer: {answer}")
        self.question_box.clear()

    def get_gpt3_response(self, question):
        response = openai.ChatCompletion.create(
            model=self.models_combobox.currentText(),
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ],
            temperature=float(self.temp_combobox.currentText()),
            max_tokens=int(self.tokens_combobox.currentText())
        )
        return response.choices[0].message.content.strip()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    sys.exit(app.exec())
