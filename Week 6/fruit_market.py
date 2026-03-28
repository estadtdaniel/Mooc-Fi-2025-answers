# write your solution here
def read_fruits():
    with open("fruits.csv") as fruits:
        database = {}
        for line in fruits:
            value = line.split(";")
            fruit = value[0]
            price = float(value[1])
            database[fruit] = price
        return database

if __name__ == "__main__":
    read_fruits()