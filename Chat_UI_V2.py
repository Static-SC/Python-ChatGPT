import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
import openai
from dotenv import load_dotenv

load_dotenv()

# Load the Chat.ui file
form_class = uic.loadUiType("ChatV2.ui")[0]

# Set up OpenAI API credentials
openai.api_key = os.getenv("OPENAI_API_KEY")

# GPT-3.5-turbo parameters
model = "gpt-3.5-turbo"
temperature = 0.0
max_tokens = 100

class ChatWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.question_box.setText("What are you?")
        self.ask_button.clicked.connect(self.send_question)

    def send_question(self):
        question = self.question_box.text()
        answer = self.get_gpt3_response(question)
        self.reply_box.append(f"Question: {question}\nAnswer: {answer}")
        self.question_box.clear()

    def get_gpt3_response(self, question):
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": question}],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content.strip()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    sys.exit(app.exec())
