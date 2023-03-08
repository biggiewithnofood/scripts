#imported os Module For Security 
import os, telebot, requests, json
disabled = "false"
admin = 208030263
theme = "neko"
ntheme = "neko"
users = []
#howmany = 8

# Getting Bot Token From Secrets
BOT_TOKEN = os.environ.get('5795521591:AAHmc06R4vrR5jlXeDztxVTe5Y156O-SpZ8')

# Creating Telebot Object
bot = telebot.TeleBot('5877333666:AAFl0T-K9fKOdJDtIuBaNPRVCxuQlyNMY1Q')
#botleak = telebot.TeleBot('6199332686:AAFnSjVp45siKu3ZjpBEjgSNjNd0pIaYWVw')

# Get a list of all the users who have interacted with your

          


# Whenever Starting Bot

@bot.message_handler(commands=['hello'])
def send_hello(message):
  tableurl = []

  def add_url(table, url):
    if url in table:
      print("Error! URL already exists in table.")
      senddd2()
    else:
      #txt = [urll]
      tableurl.append(url)
      bot.send_photo(message.chat.id, url)
      print("URL added to table.")

  def senddd2():
    import requests
    try:
      url = f'https://api.waifu.pics/sfw/{theme}'
      response = requests.get(url)
      da = response.text
      imge = json.loads(da)
      urrl = imge['url']
      add_url(tableurl, urrl)
      print(urrl)
     # bot.send_photo(message.chat.id, urrl)

    except Exception as e:
         print(e)
         return senddd2()
    print("")

    
  def senddd():
    text = message.text.split(maxsplit=1)[1]
    textddd = int(text)
    #hoho = textddd
    #lolxdlol = text 
    for i in range(textddd):
      try:
        import requests
        url = f'https://api.waifu.pics/sfw/{theme}'
        response = requests.get(url)
        da = response.text
        imge = json.loads(da)
        urrl = imge['url']
        add_url(tableurl, urrl)
        print(urrl)
        #bot.send_photo(message.chat.id, urrl)

          #url = 'https://api.waifu.pics/sfw/waifu'
          #response = requests.get(url)
          #da = response.text
         #imge = json.loads(da)
         #urrl = imge['url']
         #print(urrl)
          #b0t.send_photo(message.chat.id, urrl)
          #time.sleep(0.2)
          #print("")
      except Exception as e:
        print(e)
        senddd2()
        #return senddd2()
      
      #time.sleep(0.2)
  senddd()

@bot.message_handler(commands=['nhello'])
def send_nhello(message):
  #photo = 1
  tableurl = []

  def add_url(table, url):
    if url in table:
      print("Error! URL already exists in table.")
      senddd2()
    else:
      #global photo
      #txt = [urll]
      tableurl.append(url)
      #bot.send_message(message.chat.id, f"Фото #{photo}")
      bot.send_photo(message.chat.id, url)
      
      print("URL added to table.")

  
  
  def senddd2():
    #global tableurl
    import requests
    try:
      url = f'https://api.waifu.pics/nsfw/{ntheme}'
      response = requests.get(url)
      da = response.text
      imge = json.loads(da)
      urrl = imge['url']
      add_url(tableurl, urrl)
      print(urrl)
      #bot.send_photo(message.chat.id, urrl)
      

    except Exception as e:
         print(e)
         return senddd2()
    print("")

    
  def senddd():
    #global tableurl
    text = message.text.split(maxsplit=1)[1]
    textddd = int(text)
    
    
    
    
    #hoho = textddd
    #lolxdlol = text /
    for i in range(textddd):
      try:
        import requests
        url = f'https://api.waifu.pics/nsfw/{ntheme}'
        response = requests.get(url)
        da = response.text
        imge = json.loads(da)
        urrl = imge['url']
        add_url(tableurl, urrl)
        print(urrl)
        #bot.send_photo(message.chat.id, urrl)
        #generated = generated + 1

        #url = 'https://api.waifu.pics/nsfw/waifu'
        #response = requests.get(url)
       # da = response.text
        #imge = json.loads(da)
       # urrl = imge['url']
     #   print(urrl)
        #bot.send_photo(message.chat.id, urrl)
        #time.sleep(0.2)
        #print("")
      except Exception as e:
        print(e)
        senddd2()
        #return senddd2()
      
      #time.sleep(0.2)
  senddd()

bot.infinity_polling()
