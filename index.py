import asyncio
from src.components.Scraping import scrape_website


def main():
    # Replace 'https://example.com' with the URL of the website you want to scrape
    url_to_scrape = 'https://www.linkedin.com/in/%F0%9D%90%92%F0%9D%90%A1%F0%9D%90%9A%F0%9D%90%B3%F0%9D%90%9A%F0%9D%90%9D-%F0%9D%90%82%F0%9D%90%A1%F0%9D%90%A8%F0%9D%90%A1%F0%9D%90%9A%F0%9D%90%A7-a382827/'
    # 'https://www.linkedin.com/in/muhammadtalha028989/'

    # Create a new event loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # Run the event loop to execute the scraping function
    loop.run_until_complete(scrape_website(url_to_scrape))

if __name__ == "__main__":
    main()





# def main():
#       # Create a new event loop
#   loop = asyncio.new_event_loop()
#   asyncio.set_event_loop(loop)
#   # Replace 'https://example.com' with the URL of the website you want to scrape
#   url_to_scrape = 'https://www.linkedin.com/in/muhammadtalha028989/'
#   website_scrape = scrape_website(url_to_scrape)
#   print(website_scrape)
#   asyncio.get_event_loop().run_until_complete(scrape_website(url_to_scrape))

# # Called the main function to execute the code
# main()