from pyrogram import Client

api_id = 2427314;
api_hash = "db7262e94f4881d8f813de0ae719f8c0";
bot_token = "6489315176:AAHoqhkIHCbZkY2oFRDggeB1h-98INQ2Xrg";

def main():
    with Client("my_account", api_id, api_hash, bot_token) as app:
     app.send_message("me", "Greetings from **Pyrogram**!")

main()