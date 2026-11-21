from highrise import BaseBot, Bot

TOKEN = "467f1ef4bb363f6467c7904bb758260119744f4afa0792a69cec72e620f9ff27"
ROOM = "6afa388fe55b07081c029569"

class MiBot(BaseBot):
    async def on_start(self, session_metadata):
        print("¡Bot conectado!")

    async def on_chat(self, user, message):
        if message == "1":
            await self.highrise.send_emote("emote-wave", user.id)
        elif message == "2":
            await self.highrise.send_emote("emote-hello", user.id)
        elif message == "3":
            await self.highrise.send_emote("emote-bow", user.id)
        elif message == "4":
            await self.highrise.send_emote("emote-laugh", user.id)
        elif message.lower() == "hola":
            await self.highrise.chat(f"Hola {user.username}!")

MiBot().run(ROOM, TOKEN)
