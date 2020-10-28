import discord

from discord.ext import commands

import PIL

from PIL import Image,ImageDraw,ImageFont

from io import BytesIO

bot=commands.Bot(command_prefix=["img!"])
bot.remove_command("help")
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=f"Manipulating images in {str(len(bot.guilds))} servers|img!help "))
    return
@bot.command()
@commands.has_role("Owner")
async def anounce(ctx,*,arg):
    if ctx.guild.id==#your servers id:
        a=bot.get_channel(#announcement channel id)
        await a.send(arg)
        return
    else:
         #code what you want your bot to do if the guild in which it was used is not your guild
        
    

@bot.command()
async def help(ctx):
    a=discord.Embed(title="help",description="  youtried,eat,gun,really,rip,slap,wanted ",color=discord.Color.from_rgb(24,244,207))
    await ctx.send(embed=a)
@bot.command()
async def youtried(ctx):
    await ctx.send(file=discord.File("tenor.gif"))

       

@bot.command()

async def gun(ctx):

    asp=ctx.author.avatar_url_as(size=128)

    data=BytesIO(await asp.read())

    pfp=Image.open(data)

    pf=pfp.resize((500,500))

    b=Image.open("Gun.jpg")

    gu=b.resize((142,266))

    pf.paste(gu,(100,269))

    pf.save("prof2*.jpg")

    await ctx.send(file=discord.File("prof2*.jpg"))

                                      

@bot.command()

async def eat (ctx,*,user:discord.Member=None):

      real=Image.open("pp.jpg")

      asp=ctx.author.avatar_url_as(size=128)

      data=BytesIO(await asp.read())

      pfp=Image.open(data)

      pf=pfp.resize((63,50))

      real.paste(pf,(144,37))

      asp=user.avatar_url_as(size=128)

      data=BytesIO(await asp.read())

      pfp=Image.open(data)

      pf=pfp.resize((38,39))

      real.paste(pf,(56,75))

      real.save("prof3.png")

      await ctx.send(file=discord.File("prof3.png"))

@bot.command()

async def slap (ctx,*,user:discord.Member=None):

      real=Image.open("pope.jpg")

      asp=ctx.author.avatar_url_as(size=128)

      data=BytesIO(await asp.read())

      pfp=Image.open(data)

      pf=pfp.resize((94,78))

      real.paste(pf,(288,82))

      asp=user.avatar_url_as(size=128)

      data=BytesIO(await asp.read())

      pfp=Image.open(data)

      pf=pfp.resize((115,84))

      real.paste(pf,(55,109))

      real.save("prof3.png")

      await ctx.send(file=discord.File("prof3.png"))

      

      

        

           

    

     

     

    

   

    

        

      

        

        

    

@bot.command()

async def really (ctx,*,user:discord.Member=None):

    if user==None:

        

      real=Image.open("Real.jpg")

      asp=ctx.author.avatar_url_as(size=128)

      data=BytesIO(await asp.read())

      pfp=Image.open(data)

      pf=pfp.resize((100,80))

      real.paste(pf,(70,37))

      real.save("prof.jpg")

      await ctx.send(file=discord.File("prof.jpg"))

        

        

    real=Image.open("Real.jpg")

    asp=user.avatar_url_as(size=128)

    data=BytesIO(await asp.read())

    pfp=Image.open(data)

    pf=pfp.resize((100,80))

    real.paste(pf,(70,37))

    real.save("prof.jpg")

    await ctx.send(file=discord.File("prof.jpg"))

@bot.command()

async def rip(ctx,*,user:discord.Member=None):

    if user==None:

        real=Image.open("Rip.png")

        asp=ctx.author.avatar_url_as(size=128)

        data=BytesIO(await asp.read())

        pfp=Image.open(data)

        pf=pfp.resize((300,300))

        real.paste(pf,(124,339))

        real.save("prof1.png")

        await ctx.send(file=discord.File("prof1.png"))

    

      

        

    real=Image.open("Rip.png")

    asp=user.avatar_url_as(size=128)

    data=BytesIO(await asp.read())

    pfp=Image.open(data)

    pf=pfp.resize((300,300))

    real.paste(pf,(124,339))

    real.save("prof1.png")

    await ctx.send(file=discord.File("prof1.png"))

    return

@bot.command()

async def wanted (ctx,*,user:discord.Member=None):

    if user==None:

        real=Image.open("wanted.jpg")

        asp=ctx.author.avatar_url_as(size=128)

        data=BytesIO(await asp.read())

        pfp=Image.open(data)

        pf=pfp.resize((177,177))

        real.paste(pf,(120,212))

 

        real.save("prof.jpg")

        await ctx.send(file=discord.File("prof.jpg"))

       

        

    real=Image.open("wanted.jpg")

    asp=user.avatar_url_as(size=128)

    data=BytesIO(await asp.read())

    pfp=Image.open(data)

    pf=pfp.resize((177,177))

    real.paste(pf,(120,212))

    real.save("prof.jpg")

    await ctx.send(file=discord.File("prof.jpg"))

    

    

    return

bot.run("NzY5MjAyMzc4OTU1ODE2OTYx.X5Llig.GjK2UQc7Dk-mJ3c3Yp_MxzP7ac8")
