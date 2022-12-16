#3 Класс "Темы"

class Themes():
    def init(self, themes)
        self.themes = list()

    def add_theme(self, themes, value):
        self.themes = list()
        value = str(input())
        self.themes.append(value)

    def shift_one(self, themes):
        self.themes = themes[1:] + themes[:1]

    def reverse_order(self, themes):
        self.themes = themes.reversed()

    def get_themes(self, themes):
        print(self.themes)

    def get_first(self, themes):
        self.themes = themes[0]

    def main():
        teh = Themes(['IOLO', 'JKHS', 'dwqdq', 'dwqfwefr'])
        teh.add_theme('324235')
        teh.shift_one()
        teh.reverse_order()
        teh.get_first()


main()