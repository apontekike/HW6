import argparse as arg
from pathlib import Path
import json
from .newsapi import fetch_latest_news

def find_path(fname):
    return Path(__file__).parent.parent / fname

def load_file(fname):
    return json.load(open(find_path(fname),"r"))

def main():

    parser = arg.ArgumentParser()

    parser.add_argument("-k","--key_api", required=True,help="api key to access data")
    parser.add_argument("-b","--days_to_lookback", default =None,help="from the date it will retrive the articles")
    parser.add_argument("-i","--input", required=True,help="input file")
    parser.add_argument("-o","--output", required=True,help="output directory")
    args = parser.parse_args()

    names = load_file(args.input)

    if args.key_api[-3:] == "txt":
        api_key = open(find_path(args.key_api),"r").read()
    else:
        api_key = args.key_api

    if args.days_to_lookback != None:
        for k,v in names.items():
            with open(args.output + "/" + k + ".json","w") as file:
                data = fetch_latest_news(api_key,v,args.days_to_lookback)
                articles = {k:data}
                file.write(str(articles))
    else:
        for k,v in names.items():
            with open(args.output + "/" + k + ".json","w") as file:
                data = data = fetch_latest_news(api_key,v)
                articles = {k:data}
                file.write(str(articles))
            
if "__main__" == __name__:
    main()