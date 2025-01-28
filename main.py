from telethon import TelegramClient, events

import config as cfg
from utils import chat_request

app = TelegramClient('UserBot_Session', cfg.API_ID, cfg.API_HASH)


@app.on(events.NewMessage(incoming=True))
async def on_incoming_message(event: events.NewMessage.Event):
    prompt = event.message.message
    answer = chat_request(prompt)

    if answer:
        await event.message.reply(answer)
    else:
        await event.message.reply("Error. Try again.")


if __name__ == "__main__":
    try:
        print("Program Started")
        app.start(phone=cfg.PHONE, password=cfg.TWO_STEP_PASS)
        app.run_until_disconnected()
    except KeyboardInterrupt:
        print("Program Finished")
