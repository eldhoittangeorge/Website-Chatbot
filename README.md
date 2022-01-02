# Website-Chatbot
A chatbot for finding information from website easier

## Abstract
Chatbot is a system that gives appropriate answers to questions expressed in natural languages such as English. A chatbot can help you in finding information efficiently. Generally speaking, we use search engines to search for relevant documents when we look for some information on the Web. However, because they show you documents, you must read the documents and decide whether they contain the information you need. A chatbot can provide a better solution in this scenario.

We propose a ROBERTa based model for creating a chatbot. The proposed system can be added to any website in the form of a chatbot. The users can ask questions about the website and the chatbot can provide useful or related information. The model will be trained using the website content. The model can be deployed in a web server and the website can communicate with the model using an API.

## Requirements
- pandas
- numpy
- pytorch
- scrapy
- transformers
- farm-haystack

## Usage
### 1. Web Crawler
The current crawler is created to crawl the mgmits.ac.in website. To run the spider execute the following commands.
```
cd /SiteCrawler
scrapy crawl MitsSpider
```
The site data will be stored in Website-Chatbot/Site Data/

### 2. Context Evaluation Model 
Run the notebook Website-Chatbot/Models/Context Evaluation Model/Model 2.ipynb <br/>The current implementation doesn't use crawled website data for answering question. The data used is game of thrones wiki data.


### 3. Non Context Model 
Run the notebook Website-Chatbot/Models/Non Context Model/Model.ipynb
