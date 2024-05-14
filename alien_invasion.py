import sys

import pygame

class AlienInvasion:
    #Класс для управления ресурсами и поведением игры.
    
    def _init_(self):
        #Инициализирует игру и создает игровые ресурсы.
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
    
    def run_game(self):
        #Запуск основного цикла игры.
        while True:
            #Отслеживание событий клавиатуры и мыши.
            for event in pygame.even.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #Отображение последнего прорисованного экрана.
            pygame.display.flip()

if _name_ == '_main_':
    #Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()