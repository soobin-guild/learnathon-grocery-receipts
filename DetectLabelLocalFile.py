# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3

def find_items_in_array(itemarray,itemstofind):
    items = []

    for item in itemarray:
        if item in itemstofind:
            items.append(item)

    return items


def find_groceries(items):
    #find major grocery items
    itemstofind = ["EGGS","MILK","CHEESE","CHN","GND B","NY","PORK","ONION","SSG","BROCCOLI","BUNS","POTATOES"]
    groceries = find_items_in_array(items,itemstofind)
    return groceries


def detect_text_file(photo):
      client = boto3.client('rekognition')

      with open(photo, 'rb') as image:
        response = client.detect_text(Image={'Bytes': image.read()})

      items = [text['DetectedText'] for text in response['TextDetections']]
      
      return items


def main():
    photo = input("Enter image file name: ")

    grocerylist = find_groceries(detect_text_file(photo))
    
    if not grocerylist :
        print("no grocery found on the receipt :( ")
    else :
        print("GROCERIES FOUND: ")
        print(*grocerylist, sep=',\n')


if __name__ == "__main__":
    main()
