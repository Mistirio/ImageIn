from PIL import Image
from io import BytesIO
from discord.ext import commands
import discord


class Images(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def gun(self, ctx):
        author_pfp = ctx.author.avatar_url_as(size=128)
        author_pfp = BytesIO(await author_pfp.read())
        author_pfp = Image.open(author_pfp)
        author_pfp = author_pfp.resize((500, 500))
        gun = Image.open("assets/images/gun.jpg")
        gun = gun.resize((142, 266))
        author_pfp.paste(gun, (100, 269))
        author_pfp.save("temp/profile_gun.jpg")
        await ctx.send(file=discord.File("temp/prof_gun.jpg"))

    @commands.command()
    async def slap(self, ctx, user: discord.User = None):
        if user is None :
            await ctx.send("Please Mention a user to slap")
            return
        base = Image.open("assets/images/slap.jpg")
        author_pfp = ctx.author.avatar_url_as(size=128)
        author_pfp = BytesIO(await author_pfp.read())
        author_pfp = Image.open(author_pfp)
        author_pfp = author_pfp.resize((94, 78))
        base.pase(author_pfp, (288, 82))
        target_pfp = user.avatar_url_as(size=128)
        target_pfp = BytesIO(await target_pfp.read())
        target_pfp = Image.open(target_pfp)
        target_pfp = target_pfp.resize((115, 84))
        base.paste(target_pfp, (55, 109))
        base.save("temp/prof_slap.jpg")
        await ctx.send(file=discord.File("temp/prof_slap.jpg"))

    @commands.command()
    async def really(self , ctx , user:discord.Member=None):
        if user is None:
            user = ctx.author
        base = Image.open("assets/images/really.jpg")
        user_pfp = user.avatar_url_as(size=128)
        user_pfp = BytesIO(await user_pfp.read())
        user_pfp = Image.open(user_pfp)
        user_pfp = user_pfp.resize((100,80))
        base.paste(user_pfp , (70,37))
        base.save("temp/prof_really.jpg")
        await ctx.send(file=discord.file("temp/prof_really.jpg"))

    @commands.command()
    async def wanted(self , ctx , user: discord.Member):
        if user is None:
            user = ctx.author
        base = Image.open("assets/images/wanted.jpg")
        user_pfp = user.avatar_url_as(size=128)
        user_pfp = BytesIO(await user_pfp.read())
        user_pfp = Image.open(user_pfp)
        user_pfp = user_pfp.resize((177,177))
        base.paste(user_pfp , (120,212))
        base.save("temp/prof_wanted.jpg")
        await ctx.send(file=discord.File("temp/prof_wanted.jpg"))
    @commands.command()
    async def rip(self , ctx , user: discord.Member=None):
        if user is None:
            user = ctx.author
        base=Image.open("assets/images/rip.png")
        user_pfp = user.avatar_url_as(size=128)
        user_pfp = BytesIO(await user_pfp.read())
        user_pfp = Image.open(user_pfp)
        user_pfp = user_pfp.resize((300,300))
        base.paste(user_pfp , (124,339))
        base.save("temp/prof_rip.png")
        await ctx.send(file=discord.File("temp/prof_rip.png"))

    @commands.command()
    async def eat(self , ctx , user: discord.Member):
        if user is None:
            await ctx.send("Please tag a user to use this command")
            return
        base = Image.open("assets/images/eat.jpg")
        author_pfp = ctx.author.avatar_url_as(size=128)
        author_pfp = BytesIO(await author_pfp.read())
        author_pfp = Image.open(author_pfp)
        author_pfp = author_pfp.resize((63,50))
        base.paste(author_pfp , (144,37))
        user_pfp=user.avatar_url_as(size=128)
        user_pfp = BytesIO(await user_pfp.read())
        user_pfp = Image.open(user_pfp)
        user_pfp = user_pfp.resize((39,39))
        base.paste(user_pfp , (56,75))
        base.save("temp/prof_eat.jpg")

    @commands.command()
    async def trash(self , ctx , user:discord.Member):
        if user is None:
            user = ctx.author
        user_pfp=user.avatar_url_as(size=128)
        base = Image.open("assets/images/trash.jpg")
        user_pfp = BytesIO(await user_pfp.read())
        user_pfp = Image.open(user_pfp)
        user_pfp = user_pfp.resize((94,78))
        base.paste(user_pfp , (85,216))
        base.paste(user_pfp, (1080, 612))
        base.paste(user_pfp, (288, 82))
        base.paste(user_pfp, (55, 109))
        base.save("temp/prof_trash.jpg")
        await ctx.send(file=discord.File("temp/prof_trash.jpg"))

    #TODO: Add `i!burn` command



def setup(client):
    client.add_cog(Images(client))


