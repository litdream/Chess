#!/usr/bin/env python

import os
import sys
import pygame
import random
from getopt import gnu_getopt
from pygame.locals import *
from GameGraphic import *
from ChessBoard import ChessBoard

USAGE = '''\
USAGE: %s [options] [QUIZ_NUMBER]

options:
  -h, --help            Help screen
  -p, --pract-chess     Practical Chess Quiz
  -c, --chess-com       Chess.com quiz
  -b, --bril-chkmate    1001 Brilliant way to Checkmate
  -w, --winning-sac     1001 Winning Sacrifice

*if QUIZ_NUMBER is not provided, quiz will be randomly selected.

'''

class QuestionSet(object):
    def __init__(self, idx, qno=None):
        self.idx = idx
        self.qno = qno
        self.parser = None
        if   idx == 0:  self.parser = PractChessParser()
        elif idx == 1:  self.parser = ChessComParser()
        elif idx == 2:  self.parser = BrilChkmateParser()
        elif idx == 3:  self.parser = WinningSacParser()
        
    def getQuiz(self, qno=None):
        if qno: 
            self.qno = qno
            if type(self.parser) is PractChessParser:
                self.qno = int(self.qno)
        return self.parser.getQuiz(self.qno)

    def getFen(self, qno=None):
        q = self.getQuiz(qno)
        return q.fen

class PractChessRec(object):
    def __init__(self, buf):
        self.num = int(buf[0])
        self.fen = buf[1]
        self.title = buf[2]
        self.text = buf[3]

class ChessComRec(object):
    def __init__(self, buf):
        self.num = buf[0]
        self.fen = buf[1]
        self.title = buf[2]
        self.text = buf[3]

class PractChessParser(object):
    def __init__(self):
        self.filename = 'practical-chess-exercises.dat'
        self.rec = PractChessRec
        self._load_quiz()
        
    def _load_quiz(self):
        self.questions = []
        with open(self.filename) as fh:
            buf = []
            for l in fh:
                l = l.strip()
                if len(l):  
                    buf.append(l)
                else:
                    if buf: self.questions.append( self.rec(buf))
                    buf = []
            if buf:
                self.questions.append(self.rec(buf))

    def getQuiz(self, qno):
        rtn = None
        if qno:
            for q in self.questions:
                if q.num == qno:
                    rtn = q
                    break
        else:
            random.shuffle(self.questions)
            rtn = self.questions[0]

        if not rtn:
            print "Problem(", qno, ") not found."
            sys.exit(1)
        return rtn


class ChessComParser(PractChessParser):
    def __init__(self):
        self.filename = 'chess-com-quiz.dat'
        self.rec = ChessComRec
        self._load_quiz()
        

class BrilChkmateParser(object):
    pass

class WinningSacParser(object):
    pass



def usage():
    print USAGE % sys.argv[0]
    
def main():
    sa = 'hpc'
    la = ('help', 'pract-chess', 'chess-com' )
    o,arg = gnu_getopt(sys.argv[1:], sa, la)

    quizset = ('pract', 'chesscom', 'bril', 'winning')
    bookidx = None
    for k,v in o:
        if   k in ('-h', '--help'):  usage(); sys.exit(0)
        elif k in ('-p', '--pract-chess'): bookidx = 0
        elif k in ('-c', '--chess-com'):  bookidx = 1
        elif k in ('-b', '--bril-chkmate'): bookidx = 2
        elif k in ('-w', '--winning-sac'): bookidx = 3
    
    qnum = None
    try:
        qnum = arg[0]
    except IndexError:
        pass

    questionSet = QuestionSet(bookidx)
    
    #Copy of prt-exercise.  
    # TODO: Refactor as display

    pygame.init()
    quiz = questionSet.getQuiz(qnum)
    fen = quiz.fen
    print "\n%s\n" % fen

    problem = Problem(fen)

    fpsClock = pygame.time.Clock()
    background = pygame.image.load("img/chess-board.png")
    screen = pygame.display.set_mode( BoardPixel )
    pygame.display.set_caption("(" + str(quiz.num) + ") " + problem.getTurn() + " To Move")
    screen.blit(background.convert(), background.get_rect() )

    while True:
        problem.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == KEYUP or event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)

        fpsClock.tick(10)
        pygame.display.update()


if __name__ == '__main__':
    main()
