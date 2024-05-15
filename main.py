from confluent_kafka import Producer, Consumer
from selenium import webdriver
import re

driver = webdriver.Chrome()
web_links ={}

file_path = r"C:\Users\User\Projects\web_link_extractor\data.txt"
def read_config():
  # reads the client configuration from client.properties
  # and returns it as a key-value map
  config = {}
  with open("client.properties") as fh:
    for line in fh:
      line = line.strip()
      if len(line) != 0 and line[0] != "#":
        parameter, value = line.strip().split('=', 1)
        config[parameter] = value.strip()
  return config

def read_data():
   # reads data from text file containing some useful links and returns only the links
  
    data = open(file_path, "r")
    input =""
    for x in data:
        input += x
        
    if re.search(r'(https?:\/\/(?:www\\.)?[ a-zA-Z0-9.\/\_]+)', input):
        p_data = re.findall(r'(https?:\/\/(?:www\\.)?[ a-zA-Z0-9.\/\_\(\)]+)', input)
        
    return p_data    
       

def main():
  # producer and consumer code here
    config = read_config()
    topic = "links11"
    
    # creates a new producer instance
    producer = Producer(config)

    # produces a sample message
    values = read_data()
    for i in range(len(values)):
        key = "link"
        value = values[i]
        producer.produce(topic, key=key, value=value)
        print(f"Produced message to topic {topic}: key = {key:12} value = {value:12}")
    
    # send any outstanding or buffered messages to the Kafka broker
    producer.flush()


    # sets the consumer group ID and offset  
    config["group.id"] = "python-group-1"
    config["auto.offset.reset"] = "earliest"

    # creates a new consumer and subscribes to your topic
    consumer = Consumer(config)
    consumer.subscribe([topic])
    try:
        while True:
        # consumer polls the topic and prints any incoming messages
            msg = consumer.poll(1.0)
            if msg is not None and msg.error() is None:
                key = msg.key().decode("utf-8")
                value = msg.value().decode("utf-8")
                print(f"Consumed message from topic {topic}: key = {key:12} value = {value:12}")
                driver.get(value)
                driver.implicitly_wait(20)
                urls_node = driver.execute_script("return document.querySelectorAll('#mw-content-text a')")
                
                urls = [urls_node[i].get_attribute('href') for i in range(10)]
                print('UUUUUUUUUUU', urls)
                web_links[value] = urls
                print(f"Consumed message from topic {topic}: key = {value} value = {urls}")
   
    except IndexError:
        print("We are getting only 10 liks per site")
    except KeyboardInterrupt:
        pass   
    finally:
        # closes the consumer connection
        consumer.close()

main()