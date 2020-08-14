# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3


def detect_text_local_file(photo):
    client = boto3.client('rekognition')

    with open(photo, 'rb') as image:
        response = client.detect_text(Image={'Bytes': image.read()})

    print('Detected Texts in '+photo)
    for text in response['TextDetections']:
        print(text['DetectedText'] + ' : ' + str(text['Confidence']))

    return len(response['TextDetections'])


def detect_labels_local_file(photo):

    client = boto3.client('rekognition')

    with open(photo, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})

    print('Detected labels in ' + photo)
    for label in response['Labels']:
        print(label['Name'] + ' : ' + str(label['Confidence']))

    return len(response['Labels'])


def main():
    photo = 'photo.jpg'

    label_count = detect_labels_local_file(photo)
    print("Labels detected: " + str(label_count))

    print("---")

    text_count = detect_text_local_file(photo)
    print("Texts detected: " + str(text_count))


if __name__ == "__main__":
    main()
