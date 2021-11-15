import pandas as pd 
def listToString(l):
    listToStr = ' '.join([str(elem) for elem in l])
    return listToStr

df = pd.read_csv('goodreads_books.csv')
df = df[['id','title','cover_link','author','rating_count','average_rating','date_published','publisher','genre_and_votes','isbn13']]

df_Genre = list(df['genre_and_votes'])
df.dropna(axis=0,inplace=True)
df = df.head(1000)

df_genre = list(df['genre_and_votes'])
for i in range(0,len(df_genre)):
    dummy = df_genre[i]
    split_list = dummy.split(',')[0]
    genre = listToString(split_list.split()[:-1])
    df_genre[i] = genre

df['genre_and_votes'] = df_genre
df.columns = ['BookId','Title','CoverLink','Author','RatingCount','Rating','PublishingDate','Publisher','Genre','ISBN']


#df.to_csv('Books.csv')