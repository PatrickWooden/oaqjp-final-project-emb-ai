from emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_anger(self):
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result, "anger")
    def test_joy(self):
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result, "joy")
    def test_disgust(self):
        result = emotion_detector("I feeel disgusted just hearing about this")
        self.assertEqual(result, "disgust")
    def test_sadness(self):
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result, "sadness")
    def test_fear(self):
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result, "fear")
    
unittest.main()