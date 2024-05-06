
import requests
import os


def get_news(country, api_key='890603a55bfa47048e4490069ebee18c'):
  url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
  r = requests.get(url)
  content = r.json()
  articles = content['articles']
  results = []
  for article in articles:
    results.append(f"TITLE\n'{article['title']}, '\nDESCRIPTION\n', {article['description']}")
    for i, e in enumerate(results[0]):
        if e == ',':
            results[0] = results[0][:i] + results[0][i+1:]
    printed_result = '\n\n'.join(results)

  return printed_result

print(get_news(country='us'))

