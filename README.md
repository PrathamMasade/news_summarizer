This repository consists of all the python files necessary to create a news summarizer.
1) the news_scrape.py file takes an already existing excel sheet, summarizes the content from a BBC news article and breaks it into the following columns:
     -title
     -summary
     -date
     -source
     -url
   I used google Gemini API to summarize the content.
2) The update.py file takes the excel sheet creates a new column which categorizes the news article into sports, politics, entertainment etc. 
3) The views.py contains the API views to handle the required GET requests for retiving the news data in JSON format and searching news by the categories.
4) "newssummarizer" is the django project which contains the ursl.py,settings.py etc. and "news" is the app containing views.py, news_scrape.py, update.py etc. to build the news summarizer. 
     
