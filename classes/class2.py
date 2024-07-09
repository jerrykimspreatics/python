
class Movie:
    # 생성자
    # def __init__(self):
    #     print("Movie 클래스입니다.")

    # 매개 변수가 있는 생성자
    def __init__(self, title, audience):
        self.title = title
        self.audience = audience

    # getter, setter
    def get_title(self):
        return self.title

    def get_audience(self):
        return self.audience

# movie = Movie()
movie1 = Movie("기생충", 1000)
movie2 = Movie("범죄도시4", 800)
# print(movie1.title, movie1.audience)
# print(movie2.title, movie2.audience)
print(movie1.get_title(), movie1.get_audience())
print(movie2.get_title(), movie2.get_audience())
