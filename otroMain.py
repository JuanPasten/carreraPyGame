import pygame, sys
import random

class Runner():
    __customes = ("turtle2", "prawn", "moray", "octopus")
    
    def __init__(self, x=0, y=0):        
        ixCustome = random.randint(0, 3)
        
        self.custome = pygame.image.load("images/{}.png".format(self.__customes[ixCustome]))
        self.position = [x, y]
        self.name = ""
        
    def avanzar(self):
        self.position[0] += random.randint(1, 6)        

class Game():    
    runners = []
    __posY = (160, 200, 240, 280)
    __names = ("Speedy", "Lucera", "Alonso", "Torcuata")
    __startLine = -5
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        self.__background = pygame.image.load("images/pista.jpg")
        pygame.display.set_caption("Carrera de bichos")
        
        for i in range(4):
            theRunner = Runner(self.__startLine, self.__posY[i])
            theRunner.name = self.__names[i]
            self.runners.append(theRunner)
        
        # Runner(self.__starLine, 240) + self.runners.append(firstRunner)
        #La linea de abajo es equivalente a la línea de arriba
        #runners.append(Runner(self._starLine, 240))
    
    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                    
            for activeRunner in self.runners:
                activeRunner.avanzar()
                if activeRunner.position[0] >= self.__finishLine:
                    print("{} ha ganado".format(activeRunner.name))
                    gameOver = True
                          
            self.__screen.blit(self.__background, (0,0))
            
            for runner in self.runners:
                self.__screen.blit(runner.custome, runner.position)                
            
            pygame.display.flip()
            
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()
    
    def close(self):
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    pygame.font.init()
    game.competir()
    
    
#El bucle for runner in self.__runners es equivalente a las cuatro líneas de aquí abajo
#self.__screen.blit(self.runners[0].custome, self.runners[0].position)
#self.__screen.blit(self.runners[0].custome, self.runners[0].position)
#self.__screen.blit(self.runners[0].custome, self.runners[0].position)
#self.__screen.blit(self.runners[0].custome, self.runners[0].position)