import pygame
from pygame.locals import *
from ChessBoard import ChessBoard

redColor   = pygame.Color(255,0,0)
greenColor = pygame.Color(0,255,0)
blueColor  = pygame.Color(0,0,255)
whiteColor = pygame.Color(255,255,255)
grayColor  = pygame.Color(180,180,180)
blackColor = pygame.Color(0,0,0)

BoardPixel = ( 20 + 8*60 + 20, 20 + 8*60 + 20)

class Problem(object):
    def __init__(self, fen):
        self.fen = fen
        self.surface = pygame.display.get_surface()
        self.chess = ChessBoard()
        self.chess.setFEN(fen)
        self.pieces = []

    def update(self):
        x = y = 0
        for (i,l) in enumerate(self.chess._board):
            for (j,piece) in enumerate(l):
                # location (j,i), draw piece
                x = 20 + (j*60) + 5
                y = 20 + (i*60) + 5

                if piece != '.':
                    cp = ChessPiece(piece, [x,y])
                    self.pieces.append(cp)

        for p in self.pieces:
            p.draw()
    
    def getTurn(self):
        if self.chess.getTurn() == 0:
            return "White"
        else:
            return "Black"

class ChessPiece(pygame.sprite.Sprite):
    def __init__(self, piece, loc):
        super(ChessPiece, self).__init__()
        self.pchr = piece
        if piece == 'r': pieceImage = pygame.image.load("img/r.png")
        if piece == 'n': pieceImage = pygame.image.load("img/n.png")
        if piece == 'b': pieceImage = pygame.image.load("img/b.png")
        if piece == 'q': pieceImage = pygame.image.load("img/q.png")
        if piece == 'k': pieceImage = pygame.image.load("img/k.png")
        if piece == 'p': pieceImage = pygame.image.load("img/p.png")
        if piece == 'R': pieceImage = pygame.image.load("img/wr.png")
        if piece == 'N': pieceImage = pygame.image.load("img/wn.png")
        if piece == 'B': pieceImage = pygame.image.load("img/wb.png")
        if piece == 'Q': pieceImage = pygame.image.load("img/wq.png")
        if piece == 'K': pieceImage = pygame.image.load("img/wk.png")
        if piece == 'P': pieceImage = pygame.image.load("img/wp.png")
        self.image = pieceImage
        self.image.set_colorkey( self.image.get_at((0,0)) )
        self.topleft = loc
        print self.topleft

    def draw(self):
        surface = pygame.display.get_surface()
        surface.blit( self.image.convert(), self.topleft )

    def __str__(self):
        return self.pchr

class RawBoardDrawing(object):
    def __init__(self):
        self.surface = pygame.display.get_surface()
        
    def update(self):
        for i in range(0,9):
            for j in range(0,9):
                rectColor = whiteColor
                if 1 == (i+j)%2:
                    rectColor = grayColor
                if i==8 or j==8:
                    rectColor = blackColor
                pygame.draw.rect(self.surface, rectColor, 
                                 ( 20+i*60, 20+j*60, 20+(i+1)*60, 20+(j+1)*60))
                    
        pygame.draw.rect(self.surface, blackColor, (0,0, 520,20))
        pygame.draw.rect(self.surface, blackColor, (0,0, 20,520))
        pygame.draw.rect(self.surface, blackColor, (520,520, 500,0))
        pygame.draw.rect(self.surface, blackColor, (520,520, 0,500))

