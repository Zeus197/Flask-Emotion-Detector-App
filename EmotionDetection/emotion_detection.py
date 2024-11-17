import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_obj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=my_obj, headers=header)
    if response.status_code == 400:
        return {'anger': None,'disgust': None,'fear': None,'joy': None,'sadness': None,'dominant_emotion': None}
        
    formatted_response = json.loads(response.text)
    anger_score = formatted_response["emotionPredictions"][0]["emotion"]["anger"]
    disgust_score = formatted_response["emotionPredictions"][0]["emotion"]["disgust"]
    fear_score = formatted_response["emotionPredictions"][0]["emotion"]["fear"]
    joy_score = formatted_response["emotionPredictions"][0]["emotion"]["joy"]
    sadness_score = formatted_response["emotionPredictions"][0]["emotion"]["sadness"]

    if(anger_score > disgust_score and anger_score > fear_score and anger_score > joy_score and anger_score > sadness_score):
       dominant_emotion =   "anger"
    elif(disgust_score > anger_score and disgust_score > fear_score and disgust_score > joy_score and disgust_score > sadness_score):
       dominant_emotion = "disgust"
    elif(fear_score > anger_score and fear_score > disgust_score and fear_score > joy_score and fear_score > sadness_score):
       dominant_emotion = "fear"
    elif(joy_score > anger_score and joy_score > disgust_score and joy_score > fear_score and joy_score > sadness_score):
       dominant_emotion = "joy"
    elif(sadness_score > anger_score and sadness_score > disgust_score and sadness_score > fear_score and sadness_score > joy_score):
       dominant_emotion = "sadness"
    return {'anger': anger_score,'disgust': disgust_score,'fear': fear_score,'joy': joy_score,'sadness': sadness_score,'dominant_emotion': dominant_emotion}

