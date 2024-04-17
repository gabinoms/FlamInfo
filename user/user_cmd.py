import uuid
from datetime import datetime

from aiogram.types import InlineQueryResultArticle, InputTextMessageContent

from aiogram.utils.exceptions import MessageNotModified
from contextlib import suppress

from decouple import config

from core.core_methods import info_msg

from keyboards.main_kb import refresh_kb

async def genid():
	tmp = uuid.uuid4()
	pid = str(str(tmp).split('-')[0])
	return pid

async def init_one(message):
	await message.delete()

	root_id = config('ADMIN')
	
	
	if message.from_user.id == int(root_id):
		text = await info_msg()
		time = message.date.time()
		await message.answer(str(time)+text, reply_markup=refresh_kb())



async def show_rates(call):

	with suppress(MessageNotModified):
		text = await info_msg()
		time = datetime.now().strftime('%H:%M:%S')

		await call.message.edit_text(str(time)+text, reply_markup=refresh_kb())


async def someinline(query):

	text = query.query or 'echo'
	input_content = InputTextMessageContent(await info_msg())
	result_id = await genid()
	item = InlineQueryResultArticle(
		input_message_content=input_content,
		id=result_id,
		title='🦩 click me'
		)

	await query.answer(results=[item], cache_time=1)