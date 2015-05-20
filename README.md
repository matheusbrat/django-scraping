# django-scraping

Current endpoints for example

URL: https://djangoscraping.herokuapp.com
GET - List others existent endpoints

URL: https://djangoscraping.herokuapp.com/outlets/
GET - List outlets 
    Params for filtering: name, description, url
POST - Create outlet
    Params for creation: name, url, description

URL: https://djangoscraping.herokuapp.com/outlets/ID
GET - Retrieve specific outlet 
DElETE - Remove specific outlet (cascade)  
PUT - Update specific outlet


URL: https://djangoscraping.herokuapp.com/writers/
GET - List writers
    Params for filtering: name, twitter, profile
POST - Create writer
    Params for creation: name, twitter, profile

URL: https://djangoscraping.herokuapp.com/writers/ID
GET - Retrieve specific writer
DElETE - Remove specific writer
PUT - Update specific writer

URL: https://djangoscraping.herokuapp.com/articles/
GET - List articles
    Params for filtering: title, url, content, publication_date, writers_name, writers_twitter, writers_profile, outlet_name

URL: https://djangoscraping.herokuapp.com/articles/ID 
GET - Retrieve specific article