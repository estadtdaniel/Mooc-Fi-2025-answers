# Write your solution here

def find_movies(database: list, search_term: str):
    new_database = []
    
    for item in database:
        if item["name"].lower().find(search_term) >= 0:
            new_database.append(item)
    return(new_database)
            

            

if __name__ == "__main__":
    database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
    {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
    {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101},
    {'name': 'Jaws', 'director': 'Steven Spielberg', 'year': 1975, 'runtime': 124}]

    my_movies = find_movies(database, "ja")
    print(my_movies)