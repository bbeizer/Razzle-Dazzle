# Razzle-Dazzle

This is a game I created. Each side has 4 pieces. All of the pieces move like knights in Chess, one of which contains a metal ball.
The piece with the ball is not able to move but it is able to pass the ball. That piece can pass the ball to other pieces that are
laterally or diagonally in range as long as the opponent's piece is not blocking the path. On a given turn, a player is able to move only one piece at a time, and is able to pass the ball to other pieces that are in line and not obstructed. The player must end their turn by pressing the key "n" to surrender their turn to the other player. The first player to get one of their piece with a ball on the opponents
back rank wins. To reset the game press the button "r".

# What you need to Download
  ´• pygame
  
   • vscode
   
   • to get the game to work, run the game with the play button on main.py

# Initial Setup

<img width="797" alt="Screen Shot 2022-11-27 at 1 53 47 PM" src="https://user-images.githubusercontent.com/89622436/204154385-bdd33197-7cb2-4f9d-8066-54a65440547d.png">

# White attempting to Move

<img width="795" alt="Screen Shot 2022-11-27 at 1 54 26 PM" src="https://user-images.githubusercontent.com/89622436/204154496-3ba66a06-13f8-4ef6-9565-ec5276c0cdfa.png">

# White attempting to Pass with the unhighlighted piece 

<img width="793" alt="Screen Shot 2022-11-27 at 2 07 49 PM" src="https://user-images.githubusercontent.com/89622436/204154934-2ce3f169-9b69-4e18-ba5a-04fb0571005f.png">

# White Winning

<img width="798" alt="Screen Shot 2022-11-27 at 1 56 21 PM" src="https://user-images.githubusercontent.com/89622436/204154727-610492f9-5931-498f-a192-0acc6aa0d385.png">

# Bugs/Future Improvement

Currently you can only play the game and make moves for each side on 1 computer. Ideally I would network the game in way where 2 clients are able to access the game on a remote server from their own devices. Each client would make moves which would alter the piece/ball configuration on the board on the server and the server would their relay the new board configuration onto the clients.
