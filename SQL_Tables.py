#This is where I set up each of the SQL tables
# (Leaderboard) The Leaderboard SQL table which lists all players who have ever played
		1. Player ID
		2. Player Username
		3. ELO
		4. Heart Composition
		5. Average Points per Game
		6. Favorite Suit to Pass
# (PlayerGBG) The Game by Game SQL table useful for generating player stats, it gets cleared after the game ends
		1. Player ID
		2. Points from Hearts
		3. Points from Queen
		4. # of Clubs passed
		5. # of Hearts passed
		6. # of Spades passed
		7. # of Diamonds passed
# (GameGBG) Another Game by Game SQL table that helps determine round by round game stats which will be used to generate a comprehensive game stats table
		1. Points Earned per Person
		2. # of Clubs passed
		3. # of Hearts passed
		4. # of Spades passed
		5. # of Diamonds passed
		6. Card Number that was Passed
		7. Suit that Drew out the Queen
		8. # of Remaining Card of Suit
		9. # of Rounds that Suit had been Led
		10. # of times holder of Queen Passes her
		11. # of times that Passer of Queen receives her
		12. # of times that Holder of Queen receives her
# (Analytics) Comprehensive Game Stats
		1. Average Points at End of Game
		2. Distribution of Suit of Cards Passed
		3. Average Size of Cards Passed
		4. Most Dangerous Time for Queen to be Played
		5. Strategy Involving the Queen 