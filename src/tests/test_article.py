import unittest
from unittest import mock
from unittest.mock import MagicMock
from src.app import Article

class TestArticle(unittest.TestCase):
    def setUp(self):
        self.output_expected = ['article_1', 'article_2', 'article_3']
        self.setup_articles = self.setupArticle(self.output_expected)
        self.setup_empty_articles = self.setupArticle()
        self.test_error_message = {'error': 'not found'}
    
    def setupArticle(self, db = []):
        articles = Article(db)
        return articles

    def mockSQLAlchemyDBMethods(self):
        articles = self.setup_articles

        articles._query = MagicMock()
        articles._commit = MagicMock()
        articles.delete = MagicMock()
        articles.post = MagicMock()
        articles.serialised = MagicMock()
        
        return articles
    
    def mockArticleMethods(self):
        articles = self.setup_articles

        articles.read = MagicMock()
        articles.create = MagicMock()
        articles.cancel = MagicMock()
        articles.errorMessage = MagicMock()

        return articles
    
    def test_read(self):
        output = self.setup_articles.read()
        print(output)

    def test_query_to_be_called_with_read(self):
        articles = Article(self.output_expected)
        articles._query = MagicMock()
        articles.read()

        articles._query.assert_called_once()
    
    def test_query_not_to_spill_methods(self):
        mockedClass = self.mockSQLAlchemyDBMethods()
        
        mockedClass.read()
        
        mockedClass._commit.assert_not_called()
        mockedClass.post.assert_not_called()
        mockedClass.delete.assert_not_called()

    def test_post_not_to_spill_methods(self):
        mockedClass = self.mockSQLAlchemyDBMethods()

        mockedClass.post()

        mockedClass._query.assert_not_called()
        mockedClass.delete.assert_not_called()

    def test_delete_not_to_spill_methods(self):
        mockedClass = self.mockSQLAlchemyDBMethods()
        
        mockedClass.delete()

        mockedClass._query.assert_not_called()
        mockedClass.post.assert_not_called()

    def test_serialised_not_to_spill_methods(self):
        mockedClass = self.mockSQLAlchemyDBMethods()

        mockedClass.serialised('TestModel', 'TestSchema')

        mockedClass._query.assert_not_called()
        mockedClass._commit.assert_not_called()
        mockedClass.post.assert_not_called()
        mockedClass.delete.assert_not_called()

    def test_post_to_be_called_with_create(self):
        mockedClass = self.mockSQLAlchemyDBMethods()

        mockedClass.create('TestTitle', 'TestBody')

        mockedClass.post.assert_called_once()

    def test_delete_to_be_called_with_cancel(self):
        mockedClass = self.mockSQLAlchemyDBMethods()

        mockedClass.cancel('TestQuery')

        mockedClass.delete.assert_called_once()
    
    def test_read__not_to_spill_methods(self):
        mockedClass = self.mockArticleMethods()

        mockedClass.read()

        mockedClass.read.assert_called_once()
        mockedClass.create.assert_not_called()
        mockedClass.cancel.assert_not_called()
        mockedClass.errorMessage.assert_not_called()

    def test_create__not_to_spill_methods(self):
        mockedClass = self.mockArticleMethods()

        mockedClass.create()

        mockedClass.read.assert_not_called()
        mockedClass.create.assert_called_once()
        mockedClass.cancel.assert_not_called()
        mockedClass.errorMessage.assert_not_called()

    def test_cancel__not_to_spill_methods(self):
        mockedClass = self.mockArticleMethods()

        mockedClass.cancel()

        mockedClass.read.assert_not_called()
        mockedClass.create.assert_not_called()
        mockedClass.cancel.assert_called_once()
        mockedClass.errorMessage.assert_not_called()

    def test_errorMessage__not_to_spill_methods(self):
        mockedClass = self.mockArticleMethods()

        mockedClass.errorMessage()

        mockedClass.read.assert_not_called()
        mockedClass.create.assert_not_called()
        mockedClass.cancel.assert_not_called()
        mockedClass.errorMessage.assert_called_once()

if __name__ == '__main__':
    unittest.main()