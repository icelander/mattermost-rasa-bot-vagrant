from mmpy_bot.bot import respond_to

import mmpy_bot_settings

import json
import requests

@respond_to('')
def send_to_rasa(message):
	post_data = message.body['data']['post']
	print(post_data)
	# Skip all but regular posts
	# TODO, skip @all, @channel, @here
	if post_data['type'] != '':
		return

	outgoing_data = {
		'channel_id': post_data['channel_id'],
		'channel_name': message.get_channel_name(),
		'team_domain': 'planet-express', # Need to improve mmpy_bot to get team name
		'team_id': message.get_team_id(),
		'post_id': post_data['id'],
		'text': message.get_message(),
		'timestamp': int(post_data['update_at']/1000),
		'token': mmpy_bot_settings.BOT_TOKEN,
		'trigger_word': '@'+mmpy_bot_settings.BOT_LOGIN,
		'user_id': message.get_user_id(),
		'user_name': message.get_username()
	}

	print(json.dumps(outgoing_data, indent=2))

	if 'file_ids' in post_data:
		outgoing_data['file_ids'] = post_data['file_ids']

	rasa_url = mmpy_bot_settings.RASA_URL

	if rasa_url[-1] != '/':
		rasa_url += '/'

	rasa_url += 'webhooks/mattermost/webhook'

	try:
		resp = requests.post(rasa_url, json=outgoing_data)

		if resp.status_code != 200:
			print(json.dumps(resp.json(), indent=2))
			message.send("Rasabot is having technical difficulties. Please try again.")
			pass
	except Exception as e:
		message.send("Rasabot is having technical difficulties. Please try again.")
		

	
	

	