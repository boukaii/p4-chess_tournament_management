from model import Tournament, Match, Round, Player
from view import ViewMenu, ViewPlayers, ViewTournament, ViewResults, ViewReports
from utils import load_current_tournament, load_tournaments, load_players


class TournamentManagement:

    def __init__(self):
        self.tournament = None

    view_tournament_global = ViewTournament
    view_players_global = ViewPlayers
    view_results_global = ViewResults
    view_reports_global = ViewReports

    def start_tournament(self):
        current_tournament = load_current_tournament()
        if not current_tournament:
            name, place, date, description, nb_tour, nb_players = self.view_tournament_global.tournament_input()
            self.tournament = Tournament(name=name, place=place, date=date,
                                         description=description, nb_tour=nb_tour, nb_players=nb_players)
            self.view_tournament_global.view_tournament_info(self.tournament)
            self.start_type_tournament()
            self.tournament.save()
        else:
            self.tournament = current_tournament
        self.create_players()
        self.create_rounds()
        self.tournament.save(as_current=False)

    def start_type_tournament(self):
        self.view_tournament_global.type_tournament()

    def create_players(self):
        print("#" * 28 + " " + "Renseignements sur les joueurs " + "#" * 28 + " ")
        for i in range(self.tournament.nb_players - len(self.tournament.players)):
            first_name, last_name, date_birth, gender = self.view_players_global.player_info()
            player = Player(first_name=first_name, last_name=last_name, date_birth=date_birth, gender=gender)
            self.tournament.add_player(player)
            self.view_players_global.view_players_info(player)
            self.tournament.save()

    def create_rounds(self):
        # Création des 4 Round
        for i in range(self.tournament.nb_tour - len(self.tournament.rounds)):
            round_ = Round("round #" + str(i + 1))
            self.tournament.add_round(round_)
            self.view_results_global.view_round(round_.name)
        # Divise notre liste de joueur par deux et on trie notre liste de joueur par rang(range définie a 0)
            list_player = sorted(self.tournament.players, key=lambda x: x.score, reverse=True)
            matchs = list()
            for ia in range(0, len(list_player), 2):
                player1 = list_player[ia]
                player2 = list_player[ia + 1]
                match = ([player1, 0], [player2, 0])
                matchs.append(match)
                round_.add_match(Match(player1, player2))
            for match in round_.matchs:
                user_input = self.result_score(match)
                self.choice_result(match, user_input)
                self.view_results_global.score_total(match)
                self.tournament.save()

    def result_score(self, match):
        user_input = self.view_results_global.score_match(match)
        while user_input not in ["1", "2", "3"]:
            user_input = self.view_results_global.score_match(match)
        return user_input

    def choice_result(self, match, user_input):
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


class Report:
    view_reports_global = ViewReports

    def menu_report(self):
        choice = 1
        print("#" * 28 + " " + "Bienvenue dans le menu des rapports " + " " + "#" * 28)
        while choice != 0:
            choice = int(ViewReports.report_menu())
            # choix 1 pour afficher les joueurs par ordre alphabétique
            if choice == 1:
                self.report_player_name()
            # choix 2 pour afficher les joueurs par classement
            elif choice == 2:
                self.report_player_score()
            # choix 2 pour afficher les joueurs par classement
            elif choice == 3:
                self.report_tournament()

    def report_player_name(self):
        players = load_players()
        players.sort(key=lambda x: x.last_name)
        self.view_reports_global.display_player(players)

    def report_player_score(self):
        players = load_players()
        players.sort(key=lambda x: x.score)
        self.view_reports_global.display_player_ranking(players)

    def report_tournament(self):
        tournaments = load_tournaments()
        self.view_reports_global.display_tournament(tournaments)


class MenuManagement:
    tournament = TournamentManagement()
    report_menu = Report()

    def main_menu(self):
        choice = 1
        print("#" * 28 + " " + "Bienvenue" + " " + "#" * 28)
        while choice != 0:
            choice = int(ViewMenu.starting_menu())
            if choice == 1:
                self.tournament.start_tournament()
            elif choice == 2:
                self.tournament.start_tournament()
            elif choice == 3:
                self.report_menu.menu_report()
            else:
                exit()
