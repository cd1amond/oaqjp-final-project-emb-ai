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

    # init some local vars to hold the scores and answer
    anger_score = None
    disgust_score = None
    fear_score = None
    joy_score = None
    sadness_score = None
    dominant_emotion = None

    try:
        # Make a POST request to the API with the payload and headers
        response = requests.post(url, json=myobj, headers=header, timeout=100)

        if response.status_code == 200:
            # Parse the response from the API
            formatted_response = json.loads(response.text)
            # Access the first item in the emotionPredictions list
            emotion_data = formatted_response['emotionPredictions'][0]['emotion']
            # Extract individual emotion scores
            anger_score = emotion_data['anger']
            disgust_score = emotion_data['disgust']
            fear_score = emotion_data['fear']
            joy_score = emotion_data['joy']
            sadness_score = emotion_data['sadness']
            # Determine the dominant emotion
            emotions = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score
            }
            dominant_emotion = max(emotions, key=emotions.get)
        else:
            dominant_emotion = 'unknown'
    except Exception as e:
        print(f"Error: {e}")
        dominant_emotion = 'unknown'

    return {'anger': anger_score, 
        'disgust': disgust_score, 
        'fear': fear_score, 
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion}
    