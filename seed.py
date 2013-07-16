import model
import csv

def load_users(session):
    with open ('seed_data/u.user','rb') as f:
        filename_users = csv.reader(f, delimiter='|')
        for user_row in filename_users:
            new_user_row = User(id=user_row[0],age=user_row[1],gender=user_row[2], profession=user_row[3], zipcode=user_row[4])
            session.add(new_user_row)
        session.commit()   
    #print filename_users

def load_movies(session):
    # use u.item
    pass

def load_ratings(session):
    # use u.data
    pass

def main(session):
    # You'll call each of the load_* functions with the session as an argument
    #load_users(session)
    pass

if __name__ == "__main__":
    s= model.connect()
    main(s)
