class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if hasattr(self, '_title'):
            return ValueError("Title can't be changed after creation")
        

        if isinstance (title, str) and (5<= len(title) <=50):
            self._title = title
        else:
            return ValueError("Title must be a string between 5 and 50 characters")
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            return TypeError("Author must be a string")
        
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            return TypeError("Magazine must be a string")
    
class Author:
    all = []

    def __init__(self, name):
     self.name = name
     if not isinstance(name, str) and len(name.strip()) == 0:
        return ValueError("Author name must be a non-empty string")
     Author.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, New_name):
           if not isinstance(New_name, str) or not New_name:
            return ValueError(" Error:  name must be a non-empty string")
           if hasattr(self, "_name"):
               return TypeError("Error: name can not be changed.")
           self._name = New_name

        
   
    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return list(set(article.magazine.category for article in self.articles()))  or None

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
            self._name = new_name
        
            return ValueError("Magazine name must be a string between 2 and 16 characters")
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and 2 <= len(new_category) <= 16:
            self._category = new_category
        else:
            return ValueError("Magazine category must be a string between 2 and 16 characters")

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):

        titles=list(article.title for article in self.articles())
        return titles if titles else None
    
    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        contributing_authors= [author for author, count in author_counts.items() if count > 2 ]
        return contributing_authors if contributing_authors else None
        author1 = Author("John Doe")
author2 = Author("Jane Smith")

magazine1 = Magazine("Tech Today", "Technology")
magazine2 = Magazine("Health Weekly", "Health")

article1 = author1.add_article(magazine1, "The Future of AI")
article2 = author1.add_article(magazine1, "Quantum Computing Basics")
article3 = author2.add_article(magazine2, "Healthy Living Tips")
article4 = author1.add_article(magazine2, "Nutrition Myths Debunked")

print(f"Articles by {author1.name}: {[article.title for article in author1.articles()]}")
print(f"Articles by {author2.name}: {[article.title for article in author2.articles()]}")
print(f"Magazines by {author1.name}: {[magazine.name for magazine in author1.magazines()]}")
print(f"Contributors to {magazine1.name}: {[author.name for author in magazine1.contributors()]}")
print(f"Titles in {magazine2.name}: {magazine2.article_titles()}")
