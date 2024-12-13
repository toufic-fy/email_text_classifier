from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from typing import Union, Any

class VectorizerFactory:
    """Factory class to create vectorizers based on configuration."""
    _vectorizers = {
        "tfidf": TfidfVectorizer,
        "bow": CountVectorizer,
    }
    @staticmethod
    def get_vectorizer(vectorizer_type: str, **kwargs) -> Union[TfidfVectorizer, CountVectorizer]:
        """Retrieve the specified vectorizer class."""
        
        vectorizer_cls = VectorizerFactory._vectorizers.get(vectorizer_type.lower())
        if not vectorizer_cls:
            raise ValueError(f"Unsupported vectorizer type: {vectorizer_type}")
        
        return vectorizer_cls(**kwargs)