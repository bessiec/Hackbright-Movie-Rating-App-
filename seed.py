import model 
import csv
import datetime

def load_users(session):
    with open ('seed_data/u.user','rb') as f:
        filename_users = csv.reader(f, delimiter='|')
        for user_row in filename_users:
            new_user_row = model.User(id=user_row[0],age=user_row[1],gender=user_row[2], profession=user_row[3], zipcode=user_row[4])
            session.add(new_user_row)
        session.commit()   

def load_movies(session):
    with open ('seed_data/u.item', 'rb') as f:
        filename_movies = csv.reader(f, delimiter = '|') 
        for movies_row in filename_movies:
            title = movies_row[1]
            title = title.decode("latin-1")
            title = title.rstrip(title[-6:])
            date = movies_row[2]
            if date=="":
                continue
            else: 
                date = datetime.datetime.strptime(date,'%d-%b-%Y')
            new_movies_row = model.Movies(id=movies_row[0], name=title, released_at=date, imdb_url=movies_row[4])
            session.add(new_movies_row)
        session.commit()

def load_ratings(session):
    with open ('seed_data/u.data','rb') as f:
        filename_data = csv.reader(f, delimiter='\t')
        for data_row in filename_data:
            new_data_row = model.Ratings(movie_id=data_row[0], user_id=data_row[1], rating=data_row[2])
            session.add(new_data_row)
        session.commit()

def main(session):
    load_users(session)
    load_movies(session)
    load_ratings(session)

if __name__ == "__main__":
    s= model.connect()
    main(s)
