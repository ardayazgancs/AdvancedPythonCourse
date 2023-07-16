from news import NewsFeed

import yagmail
import pandas
import datetime

df = pandas.read_excel('people.xlsx', nrows=3)

today = datetime.datetime.now().strftime('%Y-%m-%d')
yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')

email = yagmail.SMTP(user='...', password='...')
for index, row in df.iterrows():
    news_feed = NewsFeed(interest=row['interest'], from_date=yesterday, to_date=today)
    email.send(to=row['email'],
               subject=f"Your {row['interest']} news for today!",
               contents=f"Hi {row['name']},\n See what's on about {row['interest']} today.\n {news_feed.get()}\nArda")
