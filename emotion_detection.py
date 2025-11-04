'''
 This is the main module of the Emotion Detection.
'''
import json
import requests

def emotion_detector(text_to_analyse):
    '''
    This is the emotion_detector method.
    '''
    # Define the URL for the emotion detector API
    url = \
'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header, timeout=100)

    # Parse the response from the API
    formatted_response = json.loads(response.text)

    return formatted_response
    