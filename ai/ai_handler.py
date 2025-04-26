from config.config import ai_config


class AIHandler:
    def __init__(self):
        self.config = ai_config

    @staticmethod
    async def generate_response(message: str) -> str:
        # Здесь реализация вызова AI API
        # response = await ollama.chat(model=self.config.model, messages=[...])
        return f"AI: {message}"  # Заглушка
