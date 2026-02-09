from django.core.management.base import BaseCommand
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


class Command(BaseCommand):
    help = 'Run the chatbot in the terminal'

    def handle(self, *args, **kwargs):
        chatbot = ChatBot(
            'TerminalBot',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            logic_adapters=[
                'chatterbot.logic.BestMatch'
            ],
            database_uri='sqlite:///db.sqlite3'
        )

        trainer = ChatterBotCorpusTrainer(chatbot)
        trainer.train('chatterbot.corpus.english')

        self.stdout.write(
            self.style.SUCCESS("Chatbot is ready! Type 'exit' to quit.\n")
        )

        while True:
            user_input = input("user: ")

            if user_input.lower() == 'exit':
                print("bot: Goodbye!")
                break

            response = chatbot.get_response(user_input)
            print(f"bot: {response}")