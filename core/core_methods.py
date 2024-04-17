import aiohttp


async def price_parser():

	headers = {
		'accept': 'application/json',
	}

	url = 'https://api.geckoterminal.com/api/v2/networks/ton/pools/EQCJswqn8kKJ_u9r9SlWZqZ3Wb0ulCr3uX6DgHcBLkgVyC-J'
	# url = 'https://api.geckoterminal.com/api/v2/networks/ton/pools/EQCigkE-TgQ2aa5pM_VOzlSKQMwmUPC6T2B6LUO7wpMNwVoF'
	

	try:
		async with aiohttp.ClientSession() as session:
			async with session.get(url, headers=headers) as response:
				res = await response.json()
				main = res['data']['attributes']
				price_usd = format(float(main['base_token_price_usd']), '.5f')
				price_ton = format(float(main['base_token_price_native_currency']), '.6f')
				volumes = main['price_change_percentage']

				return price_usd, price_ton, volumes
		

	except Exception as e:
		print('someErr:\n', e)




async def info_msg():

	data = await price_parser()

	res = f"""
	📊 <a href='https://www.geckoterminal.com/ru/ton/pools/EQCJswqn8kKJ_u9r9SlWZqZ3Wb0ulCr3uX6DgHcBLkgVyC-J'>$FLAM</a> price:
	💵 <code>{data[0]}</code>
	💎 <code>{data[1]}</code>

	<i>Volumes</i>:
	5m: {data[2]['m5']}%  6h: {data[2]['h6']}%
	1h: {data[2]['h1']}%  24h: {data[2]['h24']}%
	"""
	return res