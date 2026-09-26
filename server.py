"""
Flask application server for the Emotion Detection web app.
Handles routing for the home page and the emotion analysis API endpoint.
"""
from flask import Flask,  render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("__main__")

@app.route('/')
def view():
    """
    Renders the main application interface (index.html) when users 
    visit the root URL.
    
    Returns:
        str: Rendered HTML template of the home page.
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector_route():
    """
    Retrieves the text from the request query arguments, passes it to the 
    emotion_detector function, and formats the resulting scores into a 
    human-readable system response string. Handles blank or invalid entries.
    
    Returns:
        str: A formatted string displaying individual emotion scores and 
             the dominant emotion, or an error message if the input was invalid.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    emotion = emotion_detector(text_to_analyze)
    if emotion['dominant_emotion'] is None :
        system_response = "Invalid text! Please try again!."
        return system_response
    system_response = (
        f"For the given statement, the system response is "
        f"'anger': {emotion['anger']}, "
        f"'disgust': {emotion['disgust']}, "
        f"'fear': {emotion['fear']}, "
        f"'joy': {emotion['joy']}, and "
        f"'sadness': {emotion['sadness']}. "
        f"The dominant emotion is {emotion['dominant_emotion']}"
    )
    return system_response

if __name__ == "__main__":
    app.run(host = 'localhost' , port = 5000)
