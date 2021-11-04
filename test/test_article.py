import unittest
from unittest.mock import MagicMock
from app import Article

class TestArticle(unittest.TestCase):
    def setUp(self):
        self.test_db_articles = ['article_1', 'article_2', 'article_3']
        self.db_articles = Article()
        self.output = self.db_articles.get()
        self.output_not_found = self.db_articles.get(4) # a random index but that is not contained in the test_db_articles Array.
        self.test_error_message = {'error': 'not found'}

    def test_get_articles(self):
        self.assertCountEqual(self.output, self.test_db_articles)

    def test_get_articles_fail(self):
        test_db_articles = ['one', 2, {'id': 1}, 2]
        
        self.assertNotEqual(self.output, test_db_articles)

    def test_get_article(self):
        test_db_article = 'article_1'
        output = self.db_articles.get(0)

        self.assertEqual(output, test_db_article)

    def test_get_article_fail(self):
        test_db_article = 'article_1'

        self.assertNotEqual(self.output_not_found, test_db_article)
    
    def test_errorMessage(self):
        self.test_error_message = {'error': 'not found'}
        output = self.db_articles.errorMessage()

        self.assertEqual(output, self.test_error_message)

    def test_errorMessage_tobe_called(self):
        self.db_articles.errorMessage = MagicMock()
        self.db_articles.get(4) # article_id 4 doesn't exist
        self.db_articles.errorMessage.assert_called_once()

    def test_errorMessage_not_tobe_called(self):
        self.db_articles.errorMessage = MagicMock()
        self.db_articles.get(1) # article_id 1 does exist
        self.db_articles.errorMessage.assert_not_called()

if __name__ == '__main__':
    unittest.main()










# # 
# class FirstTestClass(unittest.TestCase):
#     def test_upper(self):
#         # Arrange
#         test_string = "test"
        
#         # Act
#         output = test_string.upper()
        
#         # Assert
#         self.assertEqual(output, 'TSEST')
        