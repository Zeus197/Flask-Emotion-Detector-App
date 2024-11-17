from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionAnalyzer(unittest.TestCase):
    def test_emotion_detector(self):

        #test case for joy
        test_joy = emotion_detector('I am glad this happened')
        self.assertEqual(test_joy["dominant_emotion"],"joy")

        #test case for anger
        test_anger = emotion_detector('I am really mad about this')
        self.assertEqual(test_anger["dominant_emotion"],"anger")

        #test case for anger
        test_disgust = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(test_disgust["dominant_emotion"],"disgust")

        #test case for anger
        test_sadness = emotion_detector('I am so sad about this')
        self.assertEqual(test_sadness["dominant_emotion"],"sadness")

        #test case for anger
        test_fear = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(test_fear["dominant_emotion"],"fear")
unittest.main()