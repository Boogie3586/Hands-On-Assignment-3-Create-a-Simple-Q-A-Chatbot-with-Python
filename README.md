# Terminal Chatbot using Django and ChatterBot

This project demonstrates a terminal-based chatbot implemented in Python using Django and ChatterBot. The chatbot responds to user input using a pre-trained English corpus and can learn from new interactions stored in a SQLite database.

## Features

- Chat with the bot directly in the terminal.
- Uses ChatterBot's machine learning-based conversational engine.
- Stores responses in a SQLite database for continuous learning.
- Trained using the ChatterBot English corpus.

## Installation

1. Clone this repository:

```bash
git clone <your-repo-url>
cd chatbot_project
Create and activate a virtual environment:
```
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# or source venv/bin/activate  # Linux/macOS
Install the required packages:
```
```bash
pip install -r requirements.txt
Download the spaCy English model:
```
```bash
python -m spacy download en_core_web_sm
Usage
Apply migrations:
```
```bash
python manage.py migrate
Run the chatbot:
```
```bash
python manage.py chat_bot
Chat with the bot in the terminal. Type exit to quit.
```
```Example Conversation
user: Good morning!
bot: I am doing very well, thank you for asking.
user: What's your name?
bot: My name is TerminalBot.
user: exit
bot: Goodbye!
```
```Project Structure
chatbot_project/
├── chatbot/                    # Django app
│   ├── management/
│   │   └── commands/
│   │       └── chat_bot.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── chatbot_project/            # Django project
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```
