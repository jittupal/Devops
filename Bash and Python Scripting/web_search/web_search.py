import sys
import webbrowser

def google_search(query):
    search_query = f"{query} site:greenhouse.com OR site:lever.com OR site:lever.in after:2025"
    
    encoded_query = search_query.replace(" ", "+")
    
    url = f"https://www.google.com/search?q={encoded_query}"
    
    webbrowser.open(url)
 
    
if len(sys.argv) > 1:
    search_item = ' '.join(sys.argv[1:])
    google_search(search_item)
else:
    print("Please provide a search query")