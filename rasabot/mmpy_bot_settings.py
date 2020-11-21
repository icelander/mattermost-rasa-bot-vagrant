SSL_VERIFY = False  # Whether to perform SSL cert verification
BOT_URL = 'http://mattermost.planex.com/api/v4'  # with 'http://' and with '/api/v4' path. without trailing slash.
BOT_LOGIN = 'rasabot'
BOT_PASSWORD = 'n4e131zef38h7f9kkfixmi6sua'
BOT_TOKEN = 'n4e131zef38h7f9kkfixmi6sua' # or '<bot-personal-access-token>' if you have set bot personal access token.
BOT_TEAM = 'planet-express'  # possible in lowercase

RASA_URL = 'http://mattermost.planex.com:5005/'

PLUGINS = [
	'rasa',
]