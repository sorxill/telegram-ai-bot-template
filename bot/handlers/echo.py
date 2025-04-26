from aiogram import Router, F
from aiogram.types import Message
from ai.ai_handler import AIHandler

router = Router()
ai_handler = AIHandler()

@router.message(F.text)
async def echo_handler(message: Message):
    response = await ai_handler.generate_response(message.text)
    await message.answer(response)