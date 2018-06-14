import requests
import sys
import argparse
import os

def main():
	
	# script parser
	parser = argparse.ArgumentParser()
	parser.add_argument('-Search', required = 'true', help = 'Search query')
	parser.add_argument('-File', required = 'true' ,help = 'Name of destination directory')
	args = parser.parse_args()

	#Bing API declaration
	Bing_URL = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"
	Bing_key = '90e220eba2cc4e54bf89929cf242665c'
	headers = {"Ocp-Apim-Subscription-Key": Bing_key }
	
	#Make API search request		
	parameters = {'q': args.Search, 'license':'All', 'imageType':'photo', 'count' : 250 , 'offset' : 0}
	response = requests.get( Bing_URL, headers = headers, params = parameters)
	search_results = response.json()
	number_results = search_results['totalEstimatedMatches']
	number_results = min( number_results, 250)
	
	print( '>> Found '+  str(number_results) +  ' results that matched \'' +  args.Search + '\'')
	
	#Create new directory if it doesn't already exist

	if not os.path.exists(args.File):
		print( '>> Creating Directory \'' + args.File + '\'\n')
		os.mkdir(args.File)

	#Save to file
	os.chdir(args.File)	
	file_number = 1

	#pull 50 images at a time until no more to pull
	print ('Fetching images')

	for offset in range( 0, number_results, 50 ):
		print( '>> Fetching more images... ')
		parameters["offset"] = offset
		response = requests.get(Bing_URL, headers=headers, params=parameters)
		search_results = response.json()
		
		#request image from URL & write to file
		for temp in search_results['value']:
			
			try :
				response = requests.get(temp['contentUrl'])	
				
			except:
				
				print('Cannot download image from \'' +  temp['contentUrl'])
				print('Skipping...\n')
				continue

			print('>> Fetching image ' + args.File+ str(file_number))		
			out_file = open( args.File + str(file_number) + '.jpeg', 'w')
			out_file.write(response.content)
			out_file.close()
			file_number += 1	
		
if __name__ == '__main__': main()

