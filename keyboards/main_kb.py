from aiogram.types import InlineKeyboardButton as ikb, InlineKeyboardMarkup as ikm

def refresh_kb():

	kb= ikm(inline_keyboard=[
		[ikb('🔄', callback_data='refreshInfo')]
		])
	return kb