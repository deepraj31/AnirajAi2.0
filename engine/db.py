import sqlite3

conn = sqlite3.connect('Aniraj.db')
cursor = conn.cursor()

websites = [
    {"name": "Google", "url": "https://www.google.com"},
    {"name": "Facebook", "url": "https://www.facebook.com"},
    {"name": "YouTube", "url": "https://www.youtube.com"},
    {"name": "Amazon", "url": "https://www.amazon.com"},
    {"name": "Reddit", "url": "https://www.reddit.com"},
    {"name": "Wikipedia", "url": "https://www.wikipedia.org"},
    {"name": "Twitter", "url": "https://www.twitter.com"},
    {"name": "Instagram", "url": "https://www.instagram.com"},
    {"name": "Netflix", "url": "https://www.netflix.com"},
    {"name": "LinkedIn", "url": "https://www.linkedin.com"},
    {"name": "Microsoft", "url": "https://www.microsoft.com"},
    {"name": "Apple", "url": "https://www.apple.com"},
    {"name": "Chat GPT", "url": "chat.openai.com"},
    {"name": "GitHub", "url": "https://www.github.com"},
    {"name": "Stack Overflow", "url": "https://www.stackoverflow.com"},
    {"name": "Gmail", "url": "https://www.gmail.com"},
    {"name": "Yahoo", "url": "https://www.yahoo.com"},
    {"name": "Bing", "url": "https://www.bing.com"},
    {"name": "Spotify", "url": "https://www.spotify.com"},
    {"name": "Twitch", "url": "https://www.twitch.tv"},
    {"name": "eBay", "url": "https://www.ebay.com"},
    {"name": "CNN", "url": "https://www.cnn.com"},
    {"name": "BBC", "url": "https://www.bbc.com"},
    {"name": "NY Times", "url": "https://www.nytimes.com"},
    {"name": "Weather", "url": "https://www.weather.com"},
    {"name": "Wikipedia", "url": "https://www.wikipedia.org"},
    {"name": "MSN", "url": "https://www.msn.com"},
    {"name": "Forbes", "url": "https://www.forbes.com"},
    {"name": "CNET", "url": "https://www.cnet.com"},
    {"name": "Pinterest", "url": "https://www.pinterest.com"},
    {"name": "Adobe", "url": "https://www.adobe.com"}
]

# websites = [{'name': website['name'].lower(), 'url': website['url']} for website in websites]

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)


# query = "INSERT INTO sys_command VALUES (null,'ms word', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE')"
# cursor.execute(query)
# conn.commit()


# query = "DELETE FROM sys_command WHERE ID = "
# cursor.execute(query)
# conn.commit()



query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)




# for website in websites:
#     cursor.execute('INSERT INTO web_command (name, url) VALUES (?, ?)', (website['name'], website['url']))

# # Commit changes and close connection
# conn.commit()







query = "INSERT INTO web_command VALUES (null,'whatsapp web', 'https://web.whatsapp.com/')"
cursor.execute(query)
conn.commit()




# query = "DELETE FROM web_command WHERE ID = "
# cursor.execute(query)
# conn.commit()
