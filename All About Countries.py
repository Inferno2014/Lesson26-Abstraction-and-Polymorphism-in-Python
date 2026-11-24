class India():
    def capital(self):
        print('The capital of India is: Delhi')
    def language(self):
        print('The language(s) used in India are: Hindi and Tamil')
    def type_country(self):
        print('Type of country India is: Democracy')
class Japan():
    def capital(self):
            print('The capital of Japan is: Tokyo')
    def language(self):
        print('The language(s) used in Japan are: Japanese')
    def type_country(self):
        print('Type of country Japan is: Parliamentary Constitutional Monarcy')
i = India()
j = Japan()
countries = [i,j]
for k in countries:
     k.capital()
     k.language()
     k.type_country()