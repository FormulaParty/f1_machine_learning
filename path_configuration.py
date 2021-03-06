import os
import datetime


class Path(object):

    Database = 'Database/'
    GrandPrix = 'GrandPrix/'
    Config = 'Config/'
    Season = 'Season/'

    def __init__(self):
        if not os.path.exists(self.Database + self.GrandPrix):
            os.makedirs(self.Database + self.GrandPrix)
        if not os.path.exists(self.Database + self.Config):
            os.makedirs(self.Database + self.Config)
        if not os.path.exists(self.Database + self.Season):
            os.makedirs(self.Database + self.Season)

    def grandprix_folder_path(self, year, name):
        Path = self.Database + self.GrandPrix + str(year) + '/' + str(year) + '_' + name
        if not os.path.exists(Path):
            os.makedirs(Path)
        return Path

    def grandprix_path(self, year, name, content):
        Path = self.grandprix_folder_path(year, name)
        Path = Path + '/' + str(year) + '_' + name + '-' + content + '.csv'
        return Path

    def standings_path(self, year):
        return self.Database + self.GrandPrix + str(year) + '/' + 'CurrentDriverStandings.csv'

    def gp_multiplerace_path(self, year, date, name, content, race_id):
        Path = self.grandprix_folder_path(year, date, name)
        Path = Path + '/' + date + '_' + name + '-' + 'Race' + str(race_id) + '-' + content + '.csv'
        return Path

    def config_path(self, name):
        Path = self.Database + self.Config + name + '.csv'
        return Path

    def season_path(self, name):
        Path = self.Database + self.Season + name + '.csv'
        return Path

    def get_grandprix_path(self):
        return self.Database + self.GrandPrix

    def get_config_path(self):
        return self.Database + self.Config

    def get_season_path(self):
        return self.Database + self.Season
