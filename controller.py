from model import Tournament, Match, Round, Player
from view import ViewMenu, ViewPlayers, ViewTournament, ViewResults, ViewReports
from utils import load_current_tournament


class TournamentManagement:

    def __init__(self):
        self.tournament = None

    test = ViewTournament
    test1 = ViewPlayers
    test2 = ViewResults
    test3 = Tournament
    test4 = Round
    test5 = ViewReports

    def start_tournament(self):
        current_tournament = load_current_tournament()
        if not current_tournament:
            name, place, date, description, nb_tour, nb_players = self.test.tournament_input()
            self.tournament = Tournament(name=name, place=place, date=date, description=description, nb_tour=nb_tour, nb_players=nb_players)
            self.test.view_tournament_info(self.tournament)
            self.start_type_tournament()
            self.tournament.save()
        else:
            self.tournament = current_tournament
        self.create_players()
        self.create_rounds()
        self.tournament.save(as_current=False)

    def start_type_tournament(self):
        self.test.type_tournament()

    def create_players(self):
        print("#" * 28 + " " + "Renseignements sur les joueurs " + "#" * 28 + " ")
        for i in range(self.tournament.nb_players - len(self.tournament.players)):
            first_name, last_name, date_birth, gender = self.test1.player_info()
            player = Player(first_name=first_name, last_name=last_name, date_birth=date_birth, gender=gender)
            self.tournament.add_player(player)
            self.test1.view_players_info(player)
            self.tournament.save()

    def create_rounds(self):
        # Création des 4 Round
        for i in range(self.tournament.nb_tour - len(self.tournament.rounds)):
            round_ = Round("round #" + str(i + 1))
            self.tournament.add_round(round_)
            print(round_.name)
        # Divise notre liste de joueur par deux et on trie notre liste de joueur par rang(range définie a 0)
            list_player = sorted(self.tournament.players, key=lambda x: x.score, reverse=True)
            matchs = list()
            for ia in range(0, len(list_player), 2):
                player1 = list_player[ia]
                player2 = list_player[ia + 1]
                match = ([player1, 0], [player2, 0])
                matchs.append(match)
                print("*" * 30)
                print(match)
                round_.add_match(Match(player1, player2))
                print("*" * 100)

            for match in round_.matchs:
                print(match)
                user_input = self.test5(match)
                self.save_score(match, user_input)
                self.tournament.save()

    def test5(self, match):
        user_input = self.test2.score_match(match)
        while user_input not in ["1", "2", "3"]:
            user_input = self.test2.score_match(match)
        return user_input

    def save_score(self, match, user_input):
        if user_input == "1":
            match.score_player1 = 1
            match.player1.score += 1
        elif user_input == "2":
            match.score_player2 = 1
            match.player2.score += 1
        else:
            match.score_player1 = 0.5
            match.player1.score += 0.5
            match.score_player2 = 0.5
            match.player2.score += 0.5


class MenuManagement:
    tournament1 = TournamentManagement()
    test = ViewTournament
    test1 = ViewReports

    def main_menu(self):
        choice = 1
        print("#" * 28 + " " + "Bienvenue" + " " + "#" * 28)
        while choice != 0:
            choice = int(ViewMenu.starting_menu())
            if choice == 1:
                self.tournament1.start_tournament()
            elif choice == 2:
                self.tournament1.start_tournament()
            elif choice == 3:
                pass



# input("\nAppuyer sur n'importe quel touche pour revenir au menu:")