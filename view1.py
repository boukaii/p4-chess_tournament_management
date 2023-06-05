class ViewMenu:

    @classmethod
    def starting_menu(cls):
        print("Que voulez-vous faire ? ")
        choice = input("""
            Taper '1' Pour créer et commencer un nouveau tournoi
            Taper '2' Pour reprendre le tournoi
            Taper '3' Pour accéder aux rapports
            Taper '4' Pour quitter
            """)
        return choice


class ViewTournament:

    @classmethod
    def tournament_input(cls):
        name = input("Quel sera le nom du nouveau tournoi ?")
        place = input("A quel endroit ?")
        date = input("A quel date ? ")
        nb_tour = int(input("le nombre de tour est définie par défault sur 4, voulez-vous modifier ?"))
        nb_players = int(input("le nombre de joueurs est définie par défault sur 8, voulez-vous modifier ?"))
        description = input("Description du tournoi :")
        return name, place, date, description, nb_tour, nb_players

    @classmethod
    def type_tournament(cls):
        print()
        print("#" * 28 + " " + "Veuillez choisir un type d'échecs " + "#" * 28 + " ")
        print()
        print("tapez 1 pour le mode Bullet")
        print("tapez 2 pour le mode Blitz")
        print("tapez 3 pour le mode Speed")
        return int(input("Quel mode avez-vous choisi ?"))

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

    # def display_player_ranking(self, players_list):
    #     for player in players_list:
    #         print(f"Classement :{player.score} - {player.last_name}"
    #               f" {player.first_name} - {player.date_birth} - {player.gender}")
    #     print("Appuyer sur une touche pour revenir au menu rapport")
    #     input()
    #
    # def display_tournament(self, tournament):
    #     print("--------------------------------------------------\n")
    #     print("Tapez le tournoi:\n")
    #     for tournament in tournaments:
    #         print(f"{tournament}\n")
    #
