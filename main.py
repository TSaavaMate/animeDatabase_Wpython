from animedatabase import AnimeDatabase

db = AnimeDatabase("nezuko")
while True:
    db.connect()
    db.create_table()
    choice = input("Choose an action: " + "\n"
                    "1.add anime" + "\n"
                    "2.view all anime" + "\n"
                    "3.filter animes by sport" + "\n"
                    "4.choose random anime to watch" + "\n"
                    "5.mark anime as seen" + "\n"
                    "6.delete anime" + "\n"
                    "7.Quit" + "\n")
    match choice:
        case "1":
            name = input(">>>Enter name:")
            sport = input(">>>Enter type of sport:")
            finished = input(">>>Is the anime finished? [Y/N]:")
            finished = 1 if finished == "Y" else 0
            rating = input(">>>Enter rating:")

            db.insert_row(name, sport, finished, rating)
        case "2":
            db.view_all()
        case "3":
            sport = input("Enter sport:")
            db.select_by_sport(sport)
        case "4":
            db.select_random()
        case "5":
            anime_id = int(input("Enter id of anime which u saw:"))
            db.mark_as_seen(anime_id)
        case "6":
            anime_id = int(input("Enter id of anime which u want to delete:"))
            db.delete_row(anime_id)
        case "7":
            db.disconnect()
            break
