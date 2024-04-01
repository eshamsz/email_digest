import requests as r


api_key = "f5a112998480474da04d283496ddc2f0"
source = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=f5a112998480474da04d283496ddc2f0"


# pull data from source and create dictionary
pull = r.get(source)
content = pull.json()


# access article content
for article in content['articles']:
    print(article['title'])
    print(article['description'])
