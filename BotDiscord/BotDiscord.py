import discord
from discord.ext import commands 
import requests
import secrets  
import secretos #el archivo en donde está el token

intents = discord.Intents.default()  #acceder a los distintos eventos de la api de discord
intents.message_content = True  # acceder a los mensajes enviados en el servidor

bot= commands.Bot(command_prefix='$', intents=intents) #configuracion inicial de los comandos


#funcion de prueba (el bot repite lo que el usuario escribe en el chatr)
@bot.command()
async def test(ctx, *args):
    respuesta= ' '.join(args)
    await ctx.send(respuesta)

#funcion que muestra en el chat general una breve introducción a Kodland
@bot.command()
async def kodland(ctx, *args):
    k= "Con Kodland, los niños aprenden habilidades digitales y practican la creación de proyectos reales en cursos. Nuestro programa de programación para niños está diseñado para liberar su talento artístico y sus habilidades emprendedoras."
    await ctx.send(k)

#funcion que muestra en el chat general los cursos disponibles en Kodland
@bot.command()
async def cursos(ctx, *args):
    c= """En Kodland podrás aprender lo siguiente:
* Python básico y avanzado
* Diseño gráfico
* Roblox Studio
* Matemáticas
* Unity
* Diseño Web
* Diseño gráfico
y mucho más...."""
    await ctx.send(c)

#funcion que muestra en el chat general información acerca del curso Python Pro
@bot.command()
async def PythonPro(ctx, *args):
    p= """ En este curso orientado a adolescentes, ¡darán rienda suelta a su creatividad y explorarán las capacidades avanzadas del lenguaje Python!

Crearás aplicaciones avanzadas como chatbots, sitios web y programas que giran en torno a la inteligencia artificial.

No sólo obtendrá experiencia práctica con herramientas y técnicas estándar, sino que también aprenderá a desarrollar y publicar sus propios proyectos de código abierto.

Los conocimientos adquiridos a lo largo de este curso te permitirán impresionar a tus amigos y dar un paso importante en el mundo de la tecnología. """
    await ctx.send(p)

#funcion principal: el bot devuelve la imagen del pokemon que el usuario escriba en el chat
@bot.command()
async def poke(ctx, arg):
    try:
        pokemon= arg.split(" ", 1)[0].lower()
        result = requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon) #enlazamos la API de pokemón a la búsqueda
        if result.text == "Not Found":  #si se ingresó un nombre equivocado
            await ctx.send("Pokemon no encontrado, reescribe su nombre correctamente!!!!!!!!")
        else:
           image_url= result.json()['sprites']['front_default'] #imagen del pokemon
           print(image_url)
           await ctx.send(image_url)


    except Exception as e:  #si el usuario hace cualquier otra cosa no especificada
        print("ERROR 777: ", e)
@poke.error
async def error_type(ctx, error): #esta funcion contempla el caso en q el usuario ponga el comando pero no escriba nada
    if isinstance(error, commands.errors.MissingRequiredArgument): 
        await ctx.send("Escribe el nombre de algún pokemón!!")
    
    

@bot.event
async def on_ready():
    print(f"En marcha!! {bot.user}") #avisa cuando se haya iniciado el bot

#comando para vaciar el chat de discord automaticamente con el bot
@bot.command()
async def limpiar(ctx): 
    await ctx.channel.purge()
    await ctx.send("Mensajes Eliminados", delete_after=2)

bot.run(secretos.TOKEN) #para correr el bot  


