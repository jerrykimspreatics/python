class Country:
    def __init__(self, name):
        self.name = name
        # self.population = "인구"
        # self.capital = "수도"

    def show(self):
        print("국가 클래스의 메서드입니다.")

class Korea(Country):
    def __init__(self, name, population):
        super().__init__(name)
        self.population = population

    def country_info(self):
        print(f'국가 이름: {self.name}, 인구: {self.population}')

korea = Korea('대한민국', 50000000)
korea.show()
korea.country_info()

