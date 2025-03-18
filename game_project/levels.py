import pygame
import os
import csv


class LevelData:

    def __init__(self):
        self.level_data = self.load_level_data()

    def load_level_data(self):
        game_stages = []
        for stage in os.listdir("levels"):
            level_data = [[] for _ in range(27)]
            with open(f"levels/{stage}", newline="") as csv_file:
                reader = csv.reader(csv_file, delimiter=",")
                for i, row in enumerate(reader):
                    for j, tile in enumerate(row):
                        level_data[i].append(int(tile))
            
            game_stages.append(level_data)

        return game_stages

    def save_level_data(self, level_data):
        number = len(level_data)
        for i in range(number):
            num = i + 1 if len(str(i + 1)) > 1 else "0" + str(i + 1)
            with open(f"levels/battle_city_level_{str(num)}.csv", "w", newline="") as csv_file:
                writer = csv.writer(csv_file, delimiter=",")
                for row in level_data[i]:
                    writer.writerow(row)
        
        return
    