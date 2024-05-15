########## Web_Link_Extractor  ########
A Simple Producer/Consumer Web Link Extractor
1. The producer receives a list of URLs it can be from file, command line etc; I have used some dummy data from wikipedia and extracted the urls only from that data(saved as a text file).

2. The consumer reads the queue and consumes the content produced from producer extracts hyperlinks into a list. This list is output (file or command
line) against each parsed URL. The code in this repo is giving the List in CMd prompt as output but we can choose to generate thi list into a file if needed.

3. I have enhanced the consumer to open up the url's consumed and extract some relevant hypelinks available on that page( restricted the count to 10 as an example) and display this as dictionary.
4. This can fther be extended as to save this data to a database.

####### I have used Apahe kafka using confluent in my project #######
Firstly, we need to set up our kafka and get our IDE ready to run our project. This could be done using https://developer.confluent.io . The site demonstartes pretty straight forward explanation to go ahead and run a basic producer and cosumer on ur IDE.

########### coomands used to run producer and consumer concurrently #########
python main.py -- This command would run the producer first printing producer data and then folloed by the consumer data in the same terminal. 

If the Confluent CLI was set up then we can run producer and consumer in 2 different terminals to see results at the same time using :
confluent kafka topic produce links11 --- here links11 is the topic that we r using for running a producer.
confluent kafka topic consume --from-beginning links --- consumer.

