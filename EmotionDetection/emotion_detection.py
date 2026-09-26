import requests,json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    in_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = in_json , headers = header )

    if response.status_code == '400':
        result = {
        'anger' : None,
        'disgust' : None,
        'fear' : None,
        'joy' : None,
        'sadness' : None,
        'dominant_emotion' : None
        }
        return result

    format_res = json.loads(response.text)
    emotions = format_res['emotionPredictions'][0]['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    dominant = max(emotions , key = emotions.get)

    result = {
        'anger' : anger_score,
        'disgust' : disgust_score,
        'fear' : fear_score,
        'joy' : joy_score,
        'sadness' : sadness_score,
        'dominant_emotion' : dominant
    }
    return result