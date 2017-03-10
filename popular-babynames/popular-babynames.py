from scraper.scraper import get_baby_names_by_range
from scraper.save_results import get_collection, save_results

def main(args):
    """ Main Function """
    collection = get_collection('localhost', 27017, 'baby_names', 'names')
    save_results(collection, get_baby_names_by_range(1880, 2017))

if __name__=="__main__":
    main(None)
