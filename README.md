# Mattermost Recipe - Making a chat bot with Rasa

## Problem

You want to use Rasa to add some intelligence to your chat bot, but need it to work in private channels

## Solution

Because Outgoing Webhooks don't work in private channels, we'll have to use `mmpy_bot` to write some middleware to forward posts from private channels to 

### Quick Start

If you already have Vagrant installed follow these instructions:

1. Edit your hosts file to point `mattermost.planex.com` to the IP address on line 19 of the Vagrant file
1. Run `vagrant up`
2. Create a bot user, add them to the team, and set the token value in:
	- `rasa/credentials.yml`
	- `rasabot/mmpy_bot_settings.py`
2. Run `vagrant ssh` and then
	1. `cd /vagrant/rasa`
	2. `rasa run`
3. Open a new terminal window, run `vagrant ssh` again and then
	1. `cd /vagrant/rasabot`
	2. `MATTERMOST_BOT_SETTINGS_MODULE=mmpy_bot_settings mmpy_bot`
4. Invite the bot user to any channels you like, or DM them

### 1. Create a Mattermost Bot

Follow our instructions to create a Mattermost Bot account, then add that user to any channel you want to monitor. Be sure to give it permission to post to any channel.

### 2. Install & Configure `mmpy_bot`

Because Rasa uses outgoing webhooks you're going to need to forward requests from private channels - or a DM with the bot user - to Rasa.

Use this command to install the `mmpy_bot` Python package:

```bash
pip3 install mmpy_bot
```

Then edit the `mmpy_bot_settings.py` to set the `BOT_LOGIN` and `BOT_TOKEN` to the values from the first step.

Also, you have to set `RASA_URL` to the correct value. (Default port is `5005`)

### 3. Install & Configure Rasa

While you can do a lot of very useful things with `mmpy_bot`, the open source machine-learning tool Rasa can make interactions much more fluid. To install it, run this command:

```bash
pip3 install rasa
```

Then edit `credentials.yml` to set the bot name, token, and the Rasa webhook URL.

```yaml
mattermost:
  url: "https://chat.example.com/api/v4" # Your Mattermost URL *with* `api/v4`
  token: "xxxxx" #  the token for the bot account
  webhook_url: "https://server.example.com/webhooks/mattermost/webhook"  # The Rasa webhook URL
```

### 4. Start `mmpy_bot` and Rasa

In one terminal window, start up `mmpy_bot` with this command from inside the `rasabot` directory in this directory:

```bash
MATTERMOST_BOT_SETTINGS_MODULE=mmpy_bot_settings mmpy_bot
```

Then, in another window, start the Rasa server from inside the `rasa` in this directory:

```bash
cd /vagrant/rasa # If you're using
rasa run
```

Finally, send a message to your bot in Mattermost and watch it respond!

## Discussion

Integrating Natural Language Processing into Mattermost is surprisingly easy and requires very little real code. Other than the settings file, this is all `mmpy_bot` needs to send information to the Rasa server. It responds to everything - meaning an @ reply or direct message - by sending a properly formatted outgoing webhook to the Rasa server.

The Rasa server then sends an API request to Mattermost to post its reply to the channel. Since the `mmpy_bot` setup is small, you can easily run it on the same machine as your Mattermost server, so Rasa won't know that it's not Mattermost sending the webhooks.

Because these bots can talk to other systems via APIs or RPCs, they can do things like get the weather, search google, or even manage IoT devices.

### Resources

- [GitHub - attzonko/mmpy_bot: A python based chat bot for MatterMost (http://www.mattermost.org).](https://github.com/attzonko/mmpy_bot)
- [Rasa: Open source conversational AI - Rasa](https://rasa.com/)
- [Vagrant by HashiCorp](https://www.vagrantup.com/)