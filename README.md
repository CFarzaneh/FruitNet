# FruitNet
A groundbreaking convolutional neural network


Scraper.py

1. Requires two arguments "-Search" and "-File". Search is the string that searches Bing's query and -File specifies the name of the directory in which the found images will be saved in
2. Saves files as -File + counter +.jpeg
3. If the directory already exists, the scraper will override any files that match the name of the file
4. If the directory doesn't exist, the scraper will create a new directory in the same directory that the program is stored in
5. If no items are found, the program will throw an error (That I have yet to catch and handle)


The Following example searches Bing for images of Ferraris and saves them into a folder called Italian_cars

Example:
	python Scraper.py -Search Ferrari -File Italian_Cars

File_Directory
|
|
|-------Italian_cars
|	|
|	|----Ferrari1.jpeg
|	|----Ferrari2.jpeg
	|----Ferrari3.jpeg
