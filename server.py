from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():

    text_to_analyze = request.args.get('textToAnalyze', '')
   
    if not text_to_analyze.strip():
        return jsonify({"error": "Not valid text! Please try again!"}), 400

    result = emotion_detector(text_to_analyze)

    print(f"Result: {result}")
    
    if isinstance(result, dict):
        if result.get('dominant_emotion') is None:
            return jsonify({"error": "Text is not valid! Please try again!"}), 400 
        
        return jsonify(result)

    dominant_emotion = result.get('dominant_emotion')
    
    response = f"For the given statement, the system response is " 
    f"'anger': {result.get('anger')}, "
    f"'disgust': {result.get('disgust')}, "
    f"'fear': {result.get('fear')}, "
    f"'joy': {result.get('joy')} and "
    f"'sadness': {result.get('sadness')}. "
    f"The dominant emotion is {dominant_emotion}."
    return render_template('index.html', response=response, emotion_result=result)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)