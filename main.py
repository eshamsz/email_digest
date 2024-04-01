import requests as r
from send_email import send_email

api_key = "f5a112998480474da04d283496ddc2f0"
source = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=f5a112998480474da04d283496ddc2f0"


# pull data from source and create dictionary
pull = r.get(source)
content = pull.json()


# access article content
body = ""
for article in content['articles']:
    # get preview of article content
    # cutoff_index = article['content'].find("...Click")
    # content_preview = article['content'][:cutoff_index].strip()
    
    # concatenate title and url
    if article['title'] is not None:
        body = body + article['title'] + "\n" + "Click here for more: " + article['url'] + 2*"\n"

body = body.encode("utf-8")
send_email(body, "saleemesha04@gmail.com")
