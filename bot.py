import discord
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from auth import bot_token

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def sentiment_scores(sentence):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)

    print(f"\nSentence: {sentence}")

    print(f"Sentiment Scores: {sentiment_dict}")
    
    if sentiment_dict['compound'] >= 0.05:
        return "Overall Sentiment: Positive"

    elif sentiment_dict['compound'] <= -0.05:
        return "Overall Sentiment: Negative"
    else:
        return "Overall Sentiment: Neutral"

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    output = sentiment_scores(message.content)
    await message.channel.send(output)

client.run(bot_token)