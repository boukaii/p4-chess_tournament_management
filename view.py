class ViewMenu:
    @classmethod
    def starting_menu(cls):
        print("Que voulez-vous faire ? ")
        choice = input("""
            Taper '1' Pour créer et commencer un nouveau tournoi ou reprendre un tournoi déja commencé
            Taper '2' Pour accéder aux rapports
            Taper '3' Pour quitter
            """)
        return choice


class ViewTournament:

    @classmethod
    def tournament_input(cls):
        name = input("Quel sera le nom du nouveau tournoi ?")
        place = input("A quel endroit ?")
        description = input("Description du tournoi :")
        while True:
            try:
                date = int(input("A quel date ? "))
                break
            except:
                print("Veuillez a entrer un nombre pour la date")
                pass
        while True:
            try:
                nb_tour = int(input("le nombre de tour est définie par défault sur 4, voulez-vous modifier ?"))
                break
            except:
                print("Veuillez a entrer un nombre pour définir le nb_tour")
                pass
        while True:
            try:
                nb_players = int(input("le nombre de joueurs est définie par défault sur 8, voulez-vous modifier ?"))
                break
            except:
                print("Veuillez a entrer un nombre pour définir le nb_players")
                pass
        return name, place, date, description, nb_tour, nb_players

    @classmethod
    def input_error(cls):
        print("\nInput error, veuillez entrer un choix valide.")

    @classmethod
    def type_tournament(cls):
        print()
        print("#" * 28 + " " + "Veuillez choisir un type d'échecs " + "#" * 28 + " ")
        print()
        print("tapez 1 pour le mode Bullet")
        print("tapez 2 pour le mode Blitz")
        print("tapez 3 pour le mode Speed")
        user_input = input()
        if user_input == "1":
            return "Bullet"
        elif user_input == "2":
            return "Blitz"
        elif user_input == "3":
            return "Speed"
        else:
            cls.input_error()
            cls.type_tournament()

    @classmethod
    def view_tournament_info(cls, tournament):
        print("#" * 28 + " " + "Résumer du tournoi " + "#" * 28 + " ")
        print("Name : {}".format(tournament.name))
        print("Place : {}".format(tournament.place))
        print("Date : {}".format(tournament.date))
        print("Description : {}".format(tournament.description))
        print("NB_tour : {}".format(tournament.nb_tour))
        print("NB_Player : {}".format(tournament.nb_players))


class ViewPlayers:

    @classmethod
    def player_info(cls):
        first_name = input(str("Nom du joueur ?"))
        last_name = input(str("Prénom du joueur ?"))
        date_birth = input("Age ?")
        gender = input(str("Genre ?"))
        return first_name, last_name, date_birth, gender

    @classmethod
    def view_players_info(cls, player):
        print("#" * 28 + " " + "Infos du joueur " + "#" * 28 + " ")
        print("First Name : {}".format(player.first_name))
        print("Last Name : {}".format(player.last_name))
        print("Gender : {}".format(player.gender))
        print("Date of birth : {}".format(player.date_birth))
        print()
        print()


class ViewResults:

    @classmethod
    def print_match(cls, match):
        print("#" * 28 + " " + "MATCH" + " " + "#" * 28 + " ")
        print("---------------------------")
        print(str(f"Player 1 : {match.player1}"))
        print(f"Player 2 : {match.player2}")

    @classmethod
    def score_match(cls, match):
        cls.print_match(match)
        print("Résultat du match : ")
        user_input = input(
            "Tapez 1 pour le joueur 1 | 2 pour joueur 2 | 3 pour un match nul : "
        )
        return user_input

    @staticmethod
    def input_error():
        print("\nInput error, veuillez entrer un choix valide.")

    @classmethod
    def view_round(cls, round_):
        print()
        print(round_)
        print()

    @classmethod
    def score_total(cls, match):
        print("Score total des joueurs du Match")
        print(str(f"Player 1 : {match.player1}, {match.score_player1}"))
        print(str(f"Player 2 : {match.player2}, {match.score_player2}"))


class ViewReports:

    @classmethod
    def report_menu(cls):
        print("Que voulez-vous faire ? ")
        choice = input("""
            Taper '1' Pour voir la liste de tout les joueurs trié par ordre alphabétique
            Taper '2' Pour voir la liste de tout les joueurs triée par score
            Taper '3' Pour voir la liste de tout les tournois
            """)
        return choice

    @staticmethod
    def display_player(list_player):
        for player in list_player:
            print(f"{player.last_name} {player.first_name} - {player.date_birth}"
                  f" - {player.gender} - Classement : {player.score}")
        print("Appuyer sur une touche pour revenir au menu rapport")
        input()

    @staticmethod
    def display_player_ranking(players_list):
        for player in players_list:
            print(f"Classement :{player.score} - {player.last_name}"
                  f" {player.first_name} - {player.date_birth} - {player.gender}")
        print("Appuyer sur une touche pour revenir au menu rapport")
        input()

    @staticmethod
    def display_tournament(tournaments):
        print("Infos sur les tournois")
        for tournament in tournaments:
            print(str(f"Voici les infos de tout les tournois : {tournament.name}, {tournament.place},"
                      f" {tournament.date}, {tournament.nb_tour}, {tournament.description},"
                      f" {tournament.nb_players}, {tournament.rounds}, {tournament.players}"))



