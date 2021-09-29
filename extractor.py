import requests
from bs4 import BeautifulSoup
import os
import discord

discord_key = 'ODI3MTEzMTMzMTEzNzM3MjE3.YGWTIQ.iEl_LgfsynN4zpxgIXkabiDBbTU'


#URL for all products
input_URL = "https://www.newegg.com/global/ae-en/p/pl?N=101688105%208000%20601357282%20601359511&PageSize=96" 

'''
List of all URLs for the given products that 
are not Out of stock
'''
target_URL = [] 

def phase1():
    """
    1. find {div: class="item-cell"}
    if "Out of Stock" not in item-cell  
        go the href="URL"
    """
    html = requests.get(input_URL).content
    unicode_str = html.decode("utf8")
    encoded_str = unicode_str.encode("ascii", 'ignore')
    soup = BeautifulSoup(encoded_str, "html.parser")

    raw_list = []

    raw_content = soup.find_all("div",{"class":"item-cell"})
    

    for item in raw_content:
        raw_list.append(str(item))

    final_list = []

    for element in raw_list:
        if "OUT OF STOCK" not in element:
            final_list.append(element)

    if len(final_list ) == 1:
        reply=("There is only 1 item in stock.")
    elif len(final_list ) == 0:
        reply=("There are no items in stock.")
    else:
        reply=("There are:",len(final_list),"items in stock.")
        


class MyClient(discord.Client):
  
    async def on_ready(self):
        print('Logged in as', self.user.name,'with userID',self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
            if message.author.id == self.user.id:
                return
            if message.content.startswith('!status'):
                await message.reply('Howdy!', mention_author=True)

            if message.content.startswith('!stock'):
                html = requests.get(input_URL).content
                unicode_str = html.decode("utf8")
                encoded_str = unicode_str.encode("ascii", 'ignore')
                soup = BeautifulSoup(encoded_str, "html.parser")

                raw_list = []

                raw_content = soup.find_all("div",{"class":"item-cell"})
                

                for item in raw_content:
                    raw_list.append(str(item))

                final_list = []

                for element in raw_list:
                    if "OUT OF STOCK" not in element:
                        final_list.append(element)

                if len(final_list ) == 1:
                    reply=("There is only 1 item in stock.")
                elif len(final_list ) == 0:
                    reply=("There are no items in stock.")
                else:
                    reply=("There are:",len(final_list),"items in stock.")
                await message.reply("Give me a sec...")
                await message.reply(reply, mention_author=True)

            if message.content.startswith('!nostock'):
                html = requests.get(input_URL).content
                unicode_str = html.decode("utf8")
                encoded_str = unicode_str.encode("ascii", 'ignore')
                soup = BeautifulSoup(encoded_str, "html.parser")

                raw_list = []

                raw_content = soup.find_all("div",{"class":"item-cell"})
                

                for item in raw_content:
                    raw_list.append(str(item))

                final_list = []

                for element in raw_list:
                    if "OUT OF STOCK"  in element:
                        final_list.append(element)

                
                reply='There are: '+str(len(final_list))+' items out of stock.'
                await message.reply("Give me a sec...")
                await message.reply(reply, mention_author=True)


client = MyClient()
client.run(discord_key)
