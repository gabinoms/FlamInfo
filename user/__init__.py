from aiogram.dispatcher.filters import Text, Command

from engine import dp

from .user_cmd import init_one, show_rates
from .user_cmd import someinline

def setup():
	dp.register_message_handler(init_one, Command('givemeprice', prefixes='!', ignore_case=True))
	dp.register_callback_query_handler(show_rates, Text('refreshInfo'))

	dp.register_inline_handler(someinline)
