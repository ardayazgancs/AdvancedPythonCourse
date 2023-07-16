from news import NewsFeed

import yagmail
import pandas

df = pandas.read_excel('people.xlsx', nrows=3)

email = yagmail.SMTP(user='...', password='...')
for index, row in df.iterrows():
    news_feed = NewsFeed(interest=row['interest'], from_date='2020-11-14', to_date='2020-11-15')
    email.send(to=row['email'],
               subject=f"Your {row['interest']} news for today!",
               contents=f"Hi {row['name']},\n See what's on about {row['interest']} today.\n {news_feed.get()}\nArda")
