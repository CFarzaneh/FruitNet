# FruitNet
A groundbreaking convolutional neural network that will classify fruit images.
Supports predicitons on the following fruit:
	- Red Apples
	- Bananas
	- Pineapples
	- Green Grapes
	- Oranges

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
|	|----Ferrari3.jpeg



	train.py

To train the model, run:
	 python3 train.py

** Make sure that you have a folder called dataset in the same directory that contains folders of the 5 fruits, each with png images of the fruits. After training, the model will be saved as fruitnet.model.**



	classify.py


Once the model has been saved, you are now ready to predict your images. It is important that your test images are independent of the images used to create the model. test the model, make sure the fruitnet.model file exists and run:

	python3 classify.py


Once the program is ready to accept an image, it will prompt you to insert a path to an image of any format. A simple drag & drop can be used to quickly retrieve the images absolute path. 

Once the image has been processed by our predictor, a window will display the imported image along with a message displaying the prediction and it's percentage of accuracy.

