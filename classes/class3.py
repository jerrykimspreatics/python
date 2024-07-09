# 클래스 변수와 인스턴스 변수
class Movie:
    count = 0

    def __init__(self, title, audience):
        self.title = title
        self.audience = audience
        Movie.count += 1

movie1 = Movie('기생충', 1000)
movie2 = Movie('범죄도시4', 1000)

# print(movie1.count)
# print(movie2.count)
print(Movie.count)
