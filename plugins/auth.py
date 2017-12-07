from lib import db


async def run(client, logger, message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    authstring = message.content.split()[1]
    reply = db.select_pending(authstring)
    await client.send_message(message.channel, reply)
