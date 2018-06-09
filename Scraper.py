import requests
import sys
import argparse
#import tqdm
import os
import os.path

def main():
	
	# script parser
	parser = argparse.ArgumentParser()
	parser.add_argument('-Search', required = 'true', help = 'Search term')
	parser.add_argument('-File', required = 'true' ,help = 'Name of output file')
	args = parser.parse_args()

	#Bing API declaration
	Bing_URL = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"
	Bing_key = 'a5b720e54ce94803a38959afda2115d7'
	headers = {"Ocp-Apim-Subscription-Key": Bing_key }
	params = {'q': args.Search, 'license':'public', 'imageType':'photo', 'count' : 250 , 'offset' : 0}

	#Make API request		
	response = requests.get( Bing_URL, headers = headers, params = params)
	search_results = response.json()
	
	
	if search_results['totalEstimatedMatches'] > 250:
		number_results = 250
	else:
		number_results = search_results['totalEstimatedMatches']

	print( '>> Found '+  str(number_results) +  ' results that matched \'' +  args.Search + '\'')
	
	if not os.path.exists(args.File):
		print( '>> Creating Directory \'' + args.File + '\'')
		os.mkdir(args.File)
		os.chdir(args.File)	
	else:
		print('>> Directory \'' + args.File + '\' already exists')
		sys.exit()


	#Save to file
	filename = args.File
	file_number = 1
	for offset in range( 0, number_results, 50 ):
		out_file = open( filename + str(file_number), 'w')
		print( '>> Fetching images... ')
		params["offset"] = offset
		search = requests.get(Bing_URL, headers=headers, params=params)
		search.raise_for_status()
		results = search.json()
		
		for temp in results['value']:
			print('>> Fetching image ' +  str(file_number))
			out_file = open( args.File + str(file_number) + '.jpeg', 'w')
			r = requests.get(temp['contentUrl'])
			out_file.write(r.content)
			out_file.close()
			file_number += 1	
		
if __name__ == '__main__': main()

