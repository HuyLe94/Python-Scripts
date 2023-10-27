# Python-Scripts
These scripts purposes are for helping me finding the perfect pokemon with specific moveset for specific scenario. Rather than going through bulbapedia and search for each move on each pokemons which there ares thousands of each, this will save significant amount of time.
output folder contain all moves text files and each files will contain the pokedex number and the name of the pokemons that can learn that move.
AllMovesLink.py will scrape all the moves from bulbapedia with their name and full html link of that move, then save it to a text files, MovesAndLinks.txt is the result.
LinkAndList.py will go through MovesAndLinks.txt and save the data to a text file for each moves and their link, result is the output folder.
moveSet.py is a script to search for a list of Pokemon that can learn the move(s) that you want and give you the result, just need to manually add the moves in file_basenames[] list, not case sensitive.
MoveSetEXE.py is a better version of moveSet.py, it have a GUI for you to enter in the move you want and it will autocomplete the name for you if it match any of the moves in files, remember to change the directory in the code or you can simply browse to the folder in the GUI, noted that the browse directory will not be save so it's better to change it in the code.
WebScraper(specificSkills).py is not needed for anything but if you must know, it function the same as LinkAndList.py but very slow since you have to input each link per run/file, where LinkAndList.py will automatically take the data from a text and run once for each lines.
