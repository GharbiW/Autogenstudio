import requests
from typing import List, Tuple, Optional

# Define the structure of a search result entry
ResponseEntry = Tuple[str, str, str]

# Configuration variables for the web search function
CONFIG = {
    "api_provider": "google",  # or "bing"
    "result_count": 3,
    # For Google Search enter these values
    "google_api_key": "YOUR_GOOGLE_API_KEY",  # Replace with your actual Google API key
    "google_search_engine_id": "YOUR_GOOGLE_SEARCH_ENGINE_ID",  # Replace with your actual Google Custom Search Engine ID
    # Or Bing Search enter these values
    "bing_api_key": "YOUR_BING_API_KEY"  # Replace with your actual Bing API key
}

class WebSearch:
    """
    A class that encapsulates the functionality to perform web searches using
    Google Custom Search API or Bing Search API based on the provided configuration.
    """

    def __init__(self, config: dict):
        """
        Initializes the WebSearch class with the provided configuration.

        Parameters:
        - config (dict): A dictionary containing configuration settings.
        """
        self.config = config

    def search_query(self, query: str) -> Optional[List[ResponseEntry]]:
        """
        Performs a web search based on the query and configuration.

        Parameters:
        - query (str): The search query string.

        Returns:
        - A list of ResponseEntry tuples containing the title, URL, and snippet of each result.
        """
        api_provider = self.config.get("api_provider", "google")
        result_count = int(self.config.get("result_count", 3))
        try:
            if api_provider == "google":
                return self._search_google(query, cnt=result_count)
            elif api_provider == "bing":
                return self._search_bing(query, cnt=result_count)
        except ValueError as e:
            print(f"ValueError occurred: {e}")
        except UnicodeDecodeError as e:
            print(f"UnicodeDecodeError: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error occurred: {e}")
        return None

    def _search_google(self, query: str, cnt: int) -> Optional[List[ResponseEntry]]:
        """
        Performs a Google search and processes the results.
        Parameters:
        - query (str): The search query string.
        - cnt (int): The number of search results to return.

        Returns:
        - A list of ResponseEntry tuples containing the title, URL, and snippet of each Google search result.
        """
        api_key = self.config.get("google_api_key")
        search_engine_id = self.config.get("google_search_engine_id")
        if not api_key or not search_engine_id:
            print("Google API key or Search Engine ID is missing!")
            return None

        url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}&q={query}"
        if cnt > 0:
            url += f"&num={cnt}"

        response = requests.get(url)
        
        # Handling the potential encoding issue
        response.encoding = 'utf-8'  # Set encoding to utf-8 explicitly
        try:
            if response.status_code == 200:
                result_list: List[ResponseEntry] = []
                # We explicitly handle possible non-UTF-8 characters by ignoring or replacing them
                content = response.content.decode('utf-8', errors='replace')  # Use 'replace' or 'ignore'
                result_json = response.json()
                for item in result_json.get("items", []):
                    result_list.append((item["title"], item["link"], item["snippet"]))
                return result_list
            else:
                print(f"Error with Google Custom Search API: {response.status_code} - {response.text}")
                return None
        except UnicodeDecodeError as e:
            print(f"UnicodeDecodeError during Google response processing: {e}")
            return None

    def _search_bing(self, query: str, cnt: int) -> Optional[List[ResponseEntry]]:
        """
        Performs a Bing search and processes the results.

        Parameters:
        - query (str): The search query string.
        - cnt (int): The number of search results to return.

        Returns:
        - A list of ResponseEntry tuples containing the name, URL, and snippet of each Bing search result.
        """
        api_key = self.config.get("bing_api_key")
        if not api_key:
            print("Bing API key is missing!")
            return None

        url = f"https://api.bing.microsoft.com/v7.0/search?q={query}"
        if cnt > 0:
            url += f"&count={cnt}"

        headers = {"Ocp-Apim-Subscription-Key": api_key}
        response = requests.get(url, headers=headers)
        
        # Handling the potential encoding issue
        response.encoding = 'utf-8'  # Set encoding to utf-8 explicitly
        try:
            if response.status_code == 200:
                result_list: List[ResponseEntry] = []
                # We explicitly handle possible non-UTF-8 characters by ignoring or replacing them
                content = response.content.decode('utf-8', errors='replace')  # Use 'replace' or 'ignore'
                result_json = response.json()
                for item in result_json.get("webPages", {}).get("value", []):
                    result_list.append((item["name"], item["url"], item["snippet"]))
                return result_list
            else:
                print(f"Error with Bing Search API: {response.status_code} - {response.text}")
                return None
        except UnicodeDecodeError as e:
            print(f"UnicodeDecodeError during Bing response processing: {e}")
            return None

# Example usage
# Instantiate the WebSearch class with the CONFIG dictionary
search = WebSearch(CONFIG)

# Perform a search query
query = "Example Query"
results = search.search_query(query)

# Display the search results if available
if results is not None:
    for title, link, snippet in results:
        print(f"Title: {title}\nLink: {link}\nSnippet: {snippet}\n")
else:
    print("No results found.")
