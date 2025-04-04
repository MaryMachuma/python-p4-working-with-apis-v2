# file: lib/open_library_api.py
import requests
import json

class Search:
    def get_search_results(self):
        """Retrieve raw search results from the Open Library API for a hardcoded book title.

        Returns:
            bytes: The raw response content from the API.
        """
        search_term = "the lord of the rings"
        search_term_formatted = search_term.replace(" ", "+")
        fields = ["title", "author_name"]
        fields_formatted = ",".join(fields)
        limit = 1

        url = (
            f"https://openlibrary.org/search.json?"
            f"title={search_term_formatted}&fields={fields_formatted}&limit={limit}"
        )

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.content
        except requests.RequestException as e:
            print(f"Error fetching search results: {e}")
            return b""

    def get_search_results_json(self):
        """Retrieve JSON search results from the Open Library API for a hardcoded book title.

        Returns:
            dict: The parsed JSON response from the API, or an empty dict if the request fails.
        """
        search_term = "the lord of the rings"
        search_term_formatted = search_term.replace(" ", "+")
        fields = ["title", "author_name"]
        fields_formatted = ",".join(fields)
        limit = 1

        url = (
            f"https://openlibrary.org/search.json?"
            f"title={search_term_formatted}&fields={fields_formatted}&limit={limit}"
        )
        print(url)

        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except (requests.RequestException, ValueError) as e:
            print(f"Error fetching or parsing JSON search results: {e}")
            return {}

    def get_user_search_results(self, search_term):
        """Retrieve and format search results from the Open Library API for a user-provided book title.

        Args:
            search_term (str): The book title to search for.

        Returns:
            str: A formatted string with the book's title and author, or an error message if the request fails.
        """
        search_term_formatted = search_term.replace(" ", "+")
        fields = ["title", "author_name"]
        fields_formatted = ",".join(fields)
        limit = 1

        url = (
            f"https://openlibrary.org/search.json?"
            f"title={search_term_formatted}&fields={fields_formatted}&limit={limit}"
        )

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            # Check if the response contains results
            if not data.get("docs") or len(data["docs"]) == 0:
                return "No results found for this search term."

            # Extract title and author
            book = data["docs"][0]
            title = book.get("title", "Unknown Title")
            author = book.get("author_name", ["Unknown Author"])[0]
            return f"Title: {title}\nAuthor: {author}"
        except (requests.RequestException, ValueError, KeyError) as e:
            return f"Error fetching or parsing search results: {e}"

# For manual testing
if __name__ == "__main__":
    # Test get_search_results
    # results = Search().get_search_results()
    # print(results)

    # Test get_search_results_json
    # results_json = Search().get_search_results_json()
    # print(json.dumps(results_json, indent=1))

    # Test get_user_search_results with user input
    search_term = input("Enter a book title: ")
    result = Search().get_user_search_results(search_term)
    print("Search Result:\n")
    print(result)