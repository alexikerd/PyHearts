Here are the current steps/plans that I believe are possible with pyhearts.

1.	Create the game in python.
		As of right now, I'm comfortable with ignoring passing cards and the rule of reaching 50/100 points.
		Eventually, however, this will need to be added.

2.	Generate stat trackers
		Some of the stats tracked will be cards passed and therefore unneccessary until later
		However, heart composition (percentage of points gained from hearts to total points gained) is important as well as which suit led that the queen of spades was played
		Another stat that is uneccesary would be the total points at the end of the game, but the points per round is useful

3.	Train an AI that can play the game efficiently
		At first, I want to optimize the game round by round as I can add additional layers of complexity later.
		I want to use deep reinforcement learning to develop a path of 13 choices in the cards to play with the penalty being the amount of points received at the end of a round
		No passing cards before the round starts, no worrying about getting a certain amound of points in order to hit 50/100
		However, I will include shooting the moon (I'm strongly considering playing around with this and seeing how the AI changes decision making based on the inclusion of shooting the moon as well as how long it takes to train)
		Essentially, I just want to optimize round by round gameplay and increase the complexity of the training each time we add features to the game and then to the stat tracker

4.	SQL Database
		I want the stat trackers to be uploading the information into the database (obviously) but after we've trained the AI to play round by round I would like to be able to play the AI and so we will need people to be able to log in and for the SQL database to compare our stats to the AI's
		Additionally, an ELO system will be developed using information obtained from the stat trackers.  This will go into effect after the AI has been trained and will take up its own SQL table.

5.	GUI
		We will need a website that allows people to log into the game and hopefully we can introduce a multiplayer option so it's not just one player vs three AI
		We can have leaderboard that ranks players based on ELO

6.	Balancing
		Eventually, if we are up to it, I would like to try to balance the game of hearts and see it's effect.
		I feel like the game is way too focused on the queen of spades and overall is much too simple without real in depth strategy.
		I'm curious to see how far this goes or if we even get this far but I expect this project to take up a lot of time.