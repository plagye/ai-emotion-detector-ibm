import unittest
from EmotionDetection.emotion_detection import emotion_detector

class EmotionDetectionTest(unittest.TestCase):
    
    def test_joy(self):
        joy = emotion_detector('I am glad this happened')
        self.assertEqual(joy['dominant_emotion'], 'joy')

    def test_anger(self):
        anger = emotion_detector('I am really mad about this')
        self.assertEqual(anger['dominant_emotion'], 'anger')

    def test_disgust(self):
        disgust = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(disgust['dominant_emotion'], 'disgust')

    def test_sadness(self):
        sadness = emotion_detector('I am so sad about this')
        self.assertEqual(sadness['dominant_emotion'], 'sadness')

    def test_fear(self):
        fear = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(fear['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()

