from aiogram import executor

from engine import dp

import user

from serv import keep_alive


async def on_startup(_):
	user.setup()
	


if __name__ == '__main__':
	keep_alive()
	executor.start_polling(dp, skip_updates=True, on_startup=on_startup)