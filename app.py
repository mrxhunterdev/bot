from pyrogram import Client

api_id = 2427314;
api_hash = "db7262e94f4881d8f813de0ae719f8c0";
bot_token = "6489315176:AAHoqhkIHCbZkY2oFRDggeB1h-98INQ2Xrg";

app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

@app.on_message(filters.private)
async def hello(client, message):
    await message.reply("Hello from Pyrogram!")


app.run()