import pygame 
import sys
from a_pass import APass
from const import *
from game import Game
from piece import Piece 
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
        did_win = False
        while True:
            # show methods
            game.show_bg(screen)
            
            # show passes or moves depending on what the dragger has
            if dragger.piece != None:
                game.show_moves(screen)
            else:
                game.show_passes(screen)
            
            game.show_pieces(screen)
            game.show_ball(screen)
            game.show_win(screen, game.current_player, did_win)
            
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
                                    game.show_bg(screen)
                                    game.show_moves(screen)
                                    game.show_pieces(screen)
                                    game.show_ball(screen)
                                    game.show_win(screen, game.current_player, did_win)
                            # move the ball
                            else:
                                ball = piece.ball
                                board.calc_passes(piece, clicked_row, clicked_col)
                                dragger.save_initial(event.pos)
                                dragger.drag_ball(ball)
                                # show methods 
                                game.show_bg(screen)
                                game.show_passes(screen)
                                game.show_pieces(screen)
                                game.show_ball(screen)
                                game.show_win(screen, game.current_player, did_win)
                # mouse motion 
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        #show methods
                        game.show_bg(screen)

                        if dragger.piece != None:
                            game.show_moves(screen)
                        else:
                            game.show_passes(screen)

                        game.show_pieces(screen)
                        game.show_ball(screen)
                        game.show_win(screen, game.current_player, did_win)
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
                                game.show_bg(screen)
                                game.show_pieces(screen)
                                game.show_ball(screen)
                                game.show_win(screen, game.current_player, did_win)
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
                                game.show_bg(screen)
                                game.show_pieces(screen)
                                game.show_ball(screen)
                                game.show_win(screen, game.current_player, did_win)
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
main.mainloop()
