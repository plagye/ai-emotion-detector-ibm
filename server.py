"""
This module is the server of emotion detection app
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_detection():
    """
    Main function for detecting emotions
    """
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is None:
        return 'Invalid text! Please try again!'
    return f"""For the given statement, the system response is anger: {anger}, disgust:
    {disgust}, fear: {fear}, joy: {joy}, sadness: {sadness}. 
    The dominant emotion is {dominant_emotion}."""

@app.route('/')
def index():
    """
    This function displays the index page
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
