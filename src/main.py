import pygame 
import sys
from a_pass import APass
from const import *
from game import Game 
from square import Square
from move import Move

class Main:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Razzle Dazzle')
        self.game = Game()
        
    def mainloop(self):
        
        game = self.game
        screen = self.screen
        board = self.game.board
        dragger = self.game.dragger
        
        while True:
            # show methods
            game.show_bg(screen)
            game.show_moves(screen)
            game.show_pieces(screen)
            game.show_ball(screen)
            #game.show_passes(screen)
            
            if dragger.dragging:
                dragger.update_blit(screen)


            for event in pygame.event.get():

                # click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE
                    #checks if square has piece
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        if piece.has_ball() == False:
                            board.calc_moves(piece, clicked_row, clicked_col)
                            dragger.save_initial(event.pos)
                            dragger.drag_piece(piece)
                        else:
                            board.calc_passes(piece, clicked_row, clicked_col)
                        #show methods
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        game.show_ball(screen)
                        #game.show_passes(screen)
                # mouse motion 
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        #show methods
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        game.show_ball(screen)
                        #game.show_passes(screen)
                        dragger.update_blit(screen)
                # click release
                elif event.type == pygame.MOUSEBUTTONUP:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        release_row = dragger.mouseY // SQSIZE
                        release_col = dragger.mouseX // SQSIZE
                        #create possible move / pass
                        initial = Square(dragger.initial_row, dragger.initial_col)
                        final = Square(release_row, release_col)
                        move = Move(initial, final)
                        a_pass = APass(initial, final)
                        if board.valid_move(dragger.piece, move):
                            board.move(dragger.piece, move)
                            # show methods
                            game.show_bg(screen)
                            game.show_pieces(screen)
                            game.show_ball(screen)
                            #game.show_passes(screen)
                            # dont need to show moves because we do that in other methods 
                            # also this is the method that released a piece
                        if board.valid_pass(dragger.piece, a_pass):
                            board.pass_ball(dragger.piece, a_pass)
                            # show methods
                            game.show_bg(screen)
                            game.show_pieces(screen)
                            game.show_ball(screen)
                            #game.show_passes(screen)
                            # dont need to show moves because we do that in other methods 
                            # also this is the method that released a piece

                        dragger.undrag_piece()
                # exit the application
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()


main = Main()
main.mainloop()
