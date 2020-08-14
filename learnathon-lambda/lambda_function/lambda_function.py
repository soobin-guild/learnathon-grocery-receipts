import json
import boto3

def find_groceries(items):
      #find major grocery items: steak, beef, pork, chicken?
      groceries = []

      if "EGG" in items:
            groceries.append("Eggs")
      if "MILK" in items:
            groceries.append("Milk")
      if "CHEESE" in items:
            groceries.append("Cheese")


      if "CHN" in items:
            groceries.append("Chicken")
      if "GND B" in items:
            groceries.append("Ground Beef")
      if "STEAK" in items:
            groceries.append("Steak")
      if "PORK" in items:
            groceries.append("Pork")


      if "ONION" in items:
            groceries.append("Onion")

      return groceries

def detect_text_file(imagebinary):
      client = boto3.client('rekognition')

      response = client.detect_text(Image={'Bytes':imagebinary})

      items = [text['DetectedText'] for text in response['TextDetections']]
      
      return items


def lambda_handler(event, context):
      grocery_items = find_groceries(detect_text_file(event.get('image')))
      return{
            'statusCode' : 200,
            'headers': {
                  'Access-Control-Allow-Headers': 'Content-Type',
                  'Access-Control-Allow-Origin': '*',
                  'Access-Control-Allow-Methods': 'GET'
            },
            'body' : json.dumps(grocery_items)
      }