import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True  # 启用成员意图


client = commands.Bot(command_prefix='/',intents=intents)

# 检查管理员权限
def is_admin(ctx):
    return ctx.author.guild_permissions.administrator

# 状态命令
@commands.check(is_admin)
@client.command()
async def status(ctx, status_type, *, status_message):
    if status_type == "玩":
        await client.change_presence(activity=discord.Game(name=status_message))
    elif status_type == "听":
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=status_message))
    elif status_type == "自定义":
        activity = {
            "type": discord.ActivityType.playing,
            "name": status_message
        }
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.custom, name=activity))
    elif status_type == "直播":
        await client.change_presence(activity=discord.Streaming(name=status_message, url="https://www.twitch.tv/"))
    elif status_type == "看":
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status_message))
    else:
        await ctx.send("无效的状态类型")

# 公告命令
@commands.check(is_admin)
@client.command()
async def announce(ctx, channel: discord.TextChannel, *, message):
    await channel.send(message)

# 机器人启动事件
@client.event
async def on_ready():
    print('Bot is ready!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.custom, name="艹死某骚0"))


@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

# 启动机器人
client.run('MTA4MTEyMjE5NTczNDAwMzcxMg.Ge4hD1.y5JT3mCS2XDocHUTwNu7Xh0jnQ7vGVTVrB9AlI')