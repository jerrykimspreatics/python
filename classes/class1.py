
class Movie:
    # field
    name = ''

    #method
    def print_msg(self, msg):
        print(msg)

movie1 = Movie()
movie1.name = "Jerry"
print(movie1.name)
movie1.print_msg("반갑습니다.")

movie2 = Movie();
movie2.name = "John"
print(movie1.name)
movie1.print_msg("감사해요~")