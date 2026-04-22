class ConversationMemory:
    def __init__(self):
        self.history = []

    def add_user_message(self, message):
        self.history.append(f"User: {message}")

    def add_ai_message(self, message):
        self.history.append(f"AI: {message}")

    def get_history(self):
        return "\n".join(self.history)