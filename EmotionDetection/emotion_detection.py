import requests
import json

def emotion_detector(text_to_analyze): 
    if not text_to_analyze:
        return{
            'anger': None,
            'joy': None,
            'fear': None,
            'disgust': None,
            'sadness': None,
            'dominant_emotion': None
            }
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    obj = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    try:

        response = requests.post(url, headers=headers, json=obj)

        if response.status_code == 200:
        
            response_data = response.json()
            emotions = response_data.get('emotionPredictions', [{}])[0].get('emotion', {})
            
            anger_score = emotions.get('anger', 0)
            disgust_score = emotions.get('disgust', 0)
            fear_score = emotions.get('fear', 0)
            joy_score = emotions.get('joy', 0)
            sadness_score = emotions.get('sadness', 0)

        
            possible_emotions = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score
            }

            dominant_emotion = max(possible_emotions, key=possible_emotions.get, default=None)
            possible_emotions['dominant_emotion'] = dominant_emotion

            if dominant_emotion is None:
                return{"error": "Text is not valid! Please try again!"}

            return possible_emotions
        else:
            return {"error": f"Error: Received status code {response.status_code}, Message: {response.text}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}