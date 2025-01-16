import requests
import json 


def emotion_detector(text_to_analyze): 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
        }
   

    obj = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    response = requests.post(url, headers=headers, json=obj)

    if response.status_code == 200:
        response_data = response.json()

        emotions = response_data.get('result', {}).get('emotion',{})
        

        result = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        return result
    else:
        return "Error: Unable to process request."

result = emotion_detector("I love this new technology!.")
print(result)


