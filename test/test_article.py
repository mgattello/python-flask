import unittest
from unittest.mock import MagicMock, Mock
from app import Article

class TestArticle(unittest.TestCase):
    def setUp(self):
        self.output_expected = ['article_1', 'article_2', 'article_3']
        self.setup_articles = self.setupArticle(self.output_expected)
        self.setup_empty_articles = self.setupArticle()
        self.test_error_message = {'error': 'not found'}
    
    def setupArticle(self, db = []):
        articles = Article(db)
        return articles

    def test_get(self):
        output = self.setup_articles.get()

        self.assertCountEqual(output, self.output_expected)
    
    def test_get_all_articles(self):
        self.setup_empty_articles.getAll = MagicMock()

        self.setup_empty_articles.get()

        self.setup_empty_articles.getAll.assert_called_once_with([])

    def test_get_all_articles_length_major_10(self):
        # articles length > 10
        limit_articles_number = 10
        articles = ['test', 'test', 'test', 412, 12, 12, 1, {}, [], 'test', 'test', 'test']
        setup_article = self.setupArticle(articles)

        get_all_result = setup_article.getAll(articles)
        result_length = len(get_all_result)
        
        self.assertEqual(result_length, limit_articles_number)

    def test_get_all_articles_length_minor_10(self):
        setup_article = self.setupArticle(self.output_expected)
        articles_length = len(self.output_expected)
        
        get_all_result = setup_article.getAll(self.output_expected)
        result_length = len(get_all_result)
        
        self.assertEqual(result_length, articles_length)

    def test_get_article_by_id(self):
        test_article = 'article_1'
        result = self.setupArticle(self.output_expected)
        expected_article = result.get(0)

        self.assertEqual(test_article, expected_article)

    def test_errormessage(self):
        expected = self.test_error_message
        output = self.setup_empty_articles.errorMessage()

        self.assertEqual(output, expected)

    def test_errormessage_tobe_called(self):
        self.setup_empty_articles.errorMessage = MagicMock()
        articles = self.setup_empty_articles.get()
        outside_articles_length = len(articles) + 1

        self.setup_empty_articles.get(outside_articles_length)

        self.setup_empty_articles.errorMessage.assert_called_once()

    def test_errormessage_not_tobe_called(self):
        self.setup_articles.errorMessage = MagicMock()

        self.setup_articles.get(1)
        
        self.setup_articles.errorMessage.assert_not_called()

if __name__ == '__main__':
    unittest.main()