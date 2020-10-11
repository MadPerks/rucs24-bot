from discord.ext import commands
import requests
from .utils import get_config

class WeatherCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot # This line in the constructor is required
    
    @commands.command()
    async def test(self, ctx): # the ctx parameter is short for 'context'
        """Sends a message that indicates that the command has worked"""
        await ctx.send("Test succeeded. Command is operational")


    @commands.command()
    async def weather(self, ctx):
        config = get_config()    
        payload = {
            "q" : "New Brunswick,US-NJ,US",
            "appid" : config["WeatherAPIKey"],
         "units" : "imperial"
        }
        response = requests.get("http://api.openweathermap.org/data/2.5/weather", params=payload)       
        response_content = response.json()
        temp = response_content["main"]["temp"]
        await ctx.send(f"The weather in New Brunswick is {temp}")



def setup(bot):
    bot.add_cog(WeatherCog(bot))