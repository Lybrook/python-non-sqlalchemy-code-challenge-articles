class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    def get_title(self):
        return self._title

    def set_title(self, new_title):
        if hasattr(self, "_title"):
            print("Title cannot be changed")
        elif isinstance(new_title, str) and 5 <= len(new_title) <= 50:
            self._title = new_title
        else:
            print("Title must be a string between 5 and 50 characters.")

    title = property(get_title, set_title)

    def get_author(self):
        return self._author

    def set_author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            print("Author must be an instance of Author.")

    author = property(get_author, set_author)

    def get_magazine(self):
        return self._magazine

    def set_magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        else:
            print("Magazine must be an instance of Magazine.")

    magazine = property(get_magazine, set_magazine)


class Author:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if hasattr(self, "_name"):
            print("Name cannot be changed")
        elif isinstance(new_name, str) and len(new_name) > 0:
            self._name = new_name
        else:
            print("Name must be a non-empty string.")

    name = property(get_name, set_name)

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        topic_areas = list({magazine.category for magazine in self.magazines()})
        return topic_areas if topic_areas else None


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
            self._name = new_name
        else:
            print("Name must be a string between 2 and 16 characters.")

    name = property(get_name, set_name)

    def get_category(self):
        return self._category

    def set_category(self, new_category):
        if isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category
        else:
            print("Category must be a non-empty string.")

    category = property(get_category, set_category)

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1
        contributing_authors = [author for author, count in author_counts.items() if count > 2]
        return contributing_authors if contributing_authors else None

