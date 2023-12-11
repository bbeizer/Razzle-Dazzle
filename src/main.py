from tkinter import N
import pygame 
import sys
import pickle
from a_pass import APass
from const import *
from game import Game
from piece import Piece 
from square import Square
from move import Move
from client import Network
from render import Render


class Main:
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Razzle Dazzle')
        self.game = Game()
        self.board = self.game.board
        self.renderer = Render()

    def menu_screen(self):
        run = True
        game = self.game
        screen = self.screen
        while run == True:
            game.show_menu(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.board = Main.connect()
                    run = False
                    main.mainloop()

    def connect():
        global n 
        n = Network()
        return n.board
    
    def mainloop(self):
        game = self.game
        renderer = self.renderer
        screen = self.screen
        board = self.game.board
        dragger = self.game.dragger
        did_win = False
        while True:
            # show methods
            renderer.show_bg(screen, game)
            
            # show passes or moves depending on what the dragger has
            if dragger.piece != None:
                renderer.show_moves(screen, game)
            else:
                renderer.show_passes(screen, game)
            renderer.show_pieces(screen, game)
            renderer.show_ball(screen, game)
            renderer.show_win(screen, game.current_player,did_win, game)
            
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
                        #if its the correct players turn
                        if piece.color == game.current_player:
                            # if piece doesn't have ball, move the piece
                            if piece.has_ball() == False:
                                if board.move_made == True and piece.moved == True or board.move_made == False and piece.moved == False:
                                    board.calc_moves(piece, clicked_row, clicked_col)
                                    dragger.save_initial(event.pos)
                                    dragger.drag_piece(piece)
                                    #show methods
                                    renderer.show_bg(screen, game)
                                    renderer.show_moves(screen, game)
                                    renderer.show_pieces(screen, game)
                                    renderer.show_ball(screen, game)
                                    renderer.show_win(screen, game.current_player,did_win, game)
                            # move the ball
                            else:
                                ball = piece.ball
                                board.calc_passes(piece, clicked_row, clicked_col)
                                dragger.save_initial(event.pos)
                                dragger.drag_ball(ball)
                                # show methods 
                                renderer.show_bg(screen, game)
                                renderer.show_moves(screen, game)
                                renderer.show_pieces(screen, game)
                                renderer.show_ball(screen, game)
                                renderer.show_win(screen, game.current_player,did_win, game)
                # mouse motion 
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        #show methods
                        renderer.show_bg(screen, game)

                        if dragger.piece != None:
                            renderer.show_moves(screen, game)
                        else:
                            renderer.show_passes(screen, game)
                            renderer.show_pieces(screen, game)
                            renderer.show_ball(screen, game)
                            renderer.show_win(screen, game.current_player,did_win, game)
                        dragger.update_blit(screen)
                # click release
                elif event.type == pygame.MOUSEBUTTONUP:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        release_row = dragger.mouseY // SQSIZE
                        release_col = dragger.mouseX // SQSIZE
                        #create possible move / pass squares
                        initial = Square(dragger.initial_row, dragger.initial_col)
                        final = Square(release_row, release_col)
                        # if the dragger has a piece execute the if
                        if dragger.piece != None:
                            move = Move(initial, final)
                            if board.valid_move(dragger.piece, move):
                                board.move(dragger.piece, move)
                                #plays move sound
                                game.play_sound(True)
                                # if a piece moves, the balls potential passes needs to be reset
                                # show methods
                                renderer.show_bg(screen, game)
                                renderer.show_pieces(screen, game)
                                renderer.show_ball(screen, game)
                                renderer.show_win(screen, game.current_player,did_win, game)
                            #game.show_passes(screen)
                            # dont need to show moves because we do that in other methods 
                        # if the dragger has a ball
                        else:
                            a_pass = APass(initial, final)
                            piece = initial.piece
                            if board.valid_pass(dragger.ball, a_pass):
                                board.pass_ball(a_pass)
                                # plays pass sound 
                                game.play_sound(False)
                                if final.row == 0 and game.current_player == 'White' or final.row == 7 and game.current_player == 'Black':
                                    did_win = True
                                # show methods
                                renderer.show_bg(screen, game)
                                renderer.show_pieces(screen, game)
                                renderer.show_ball(screen, game)
                                renderer.show_win(screen, game.current_player,did_win, game)
                            # dont need to show moves or passes because this is release the mouse
                            # also this is the method that released a piece

                        dragger.undrag_piece()
                        dragger.undrag_ball()
                    
                # key press
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game.reset()
                        did_win = False
                        game = self.game
                        board = self.game.board
                        dragger = self.game.dragger
                    elif event.key == pygame.K_n:
                        if did_win == False:
                            board.move_made = False
                            Piece.set_initial_squares()
                            game.next_turn()
        

                # exit the application
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()


main = Main()
main.menu_screen()
