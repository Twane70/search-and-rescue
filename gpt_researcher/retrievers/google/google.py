# googlesearch-python Retriever

# libraries
from googlesearch import search


class GoogleSearch:
    """
    Tavily API Retriever
    """
    def __init__(self, query):
        """
        Initializes the GoogleSearch object
        Args:
            query:
        """
        self.query = query

    def search(self, max_results=7, lang='en'):
        """
        Searches the query
        Returns:

        """
        """Useful for general internet search queries using the Google API."""
        print("Searching with query {0}...".format(self.query))

        search_results = []

        for source in search(self.query, lang=lang, num_results=max_results, advanced=True):
            if "youtube.com" in source.url:
                continue
            search_results.append({
                'title': source.title,
                'href': source.url,
                'body': source.description,
            })

        return search_results
