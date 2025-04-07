import discord
from discord.ext import commands
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
TARGET_USER_ID = 1051413283145535498

@bot.event
async def on_ready():
    print(f'Bot đã sẵn sàng! Đăng nhập với tên: {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if str(TARGET_USER_ID) in [str(m.id) for m in message.mentions]:
        response = (f"<@!{message.author.id}> Bro bạn có biết là vịt đang thử thách "
                   "360 ngày sục liên tục ko lên là stop ping đi nhé đợi lâu lắm ảnh mới rep đó !!!")
        await message.channel.send(response)
    await bot.process_commands(message)

async def main():
    try:
        await bot.start(TOKEN)
    except discord.LoginFailure:
        print("Token không hợp lệ. Vui lòng kiểm tra lại.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

if __name__ == "__main__":
    asyncio.run(main())
