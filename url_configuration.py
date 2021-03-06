import datetime


class Url_builder(object):
    Ergast = "https://ergast.com/api/f1/"
    F1_1 = "https://livetiming.formula1.com/static/"
    F1_2 = "_Race/SPFeed.json"

    def f1_url(self, year, date, gp_name):
        url = self.F1_1 + str(year) + "/" + str(date) + "_" + gp_name + "/" + str(date) + self.F1_2

        return url

    def url_season(self, year=None):

        # all seasons in list format
        def all_seasons():
            current_year = datetime.datetime.today().year
            url_list = []

            year = 1970
            while year <= current_year:
                url = self.Ergast + str(year) + ".json?limit=1000"
                url_list.append(url)
                year = year + 1

            return url_list

        # specific season
        def season(year):
            url = self.Ergast + str(year) + ".json?limit=1000"
            url = [url]

            return url

        # specific season on a list
        def season_list(year_list):
            url_list = []

            for year in year_list:
                url_list.append(self.Ergast + str(year) + ".json?limit=1000")

            return url_list

        # selector
        if year is None:
            return all_seasons()
        if type(year) is int:
            return season(year)
        if type(year) is list:
            return season_list(year)
        else:
            print('ERROR ON URL CONFIGURATION')

    def url_status(self):
        return self.Ergast + 'status.json?limit=1000'

    def url_driver(self, round, year):
        return self.Ergast + str(year) + '/' + str(round) + '/' + 'drivers.json?limit=1000'

    def url_constructor(self, round, year):
        return self.Ergast + str(year) + '/' + str(round) + '/' + 'constructors.json?limit=1000'

    def url_pitstops_time(self, round, year):
        return self.Ergast + str(year) + '/' + str(round) + '/' + 'pitstops.json?limit=1000'

    def url_results(self, round, year):
        return self.Ergast + str(year) + '/' + str(round) + '/' + 'results.json?limit=1000'

    def url_lapbylap(self, round, year):
        return self.Ergast + str(year) + '/' + str(round) + '/' + 'laps/', '.json?limit=1000'

    def url_driver_standings(self, round, year):
        return self.Ergast + str(year) + '/' + str(round) + '/' + 'driverStandings.json?limit=1000'

    def url_status(self, round, year):
        return self.Ergast + str(year) + '/' + str(round) + '/' + 'status.json?limit=1000'
