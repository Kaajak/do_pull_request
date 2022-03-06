path = 'C:\\Users\\yer0nos\\Desktop\\Materiały z zajęć Testowanie - studia\\Zjazd 7 (05-06.03.2022) - Kamil Musiał\\kopia\\Zjazd 7 (05-06.03.2022) - Kamil Musiał\\dev\\pliki\\rolling_stones.txt'
with open (path, 'r') as file:
  content = file.readlines()
  content2 = file.read()

  # print (content)
  # print (content2)
# #funkcja usuwająca puste linie   "usun_puste"
# content_bez_pustych = usun_puste(content)
def usun_puste(content):
    content = str(content[0])
    x = content.replace(" ","")
    return x
    content_bez_pustych = usun_puste(content)
    print (content_bez_pustych)

  # content_bez_pustych = content2.strip('\n')
  # print (content_bez_pustych)
  # content_bez_pustych = file.read()

#
# # #funkcja licząca ilość wystapień litery "a"     "ile_a"
# # print('Litera "a" wystepuje ', ile_a(content),' razy'
  def ila_a(content):
    litera = "a"
    liczbawystapien = 0
    content = str(content[0])
    while liczbawystapien <= len(content):
      for litera in content:
        if content[liczbawystapien] == litera:
          liczbawystapien +=1
                return liczbawystapien





# #
# # #funkcja licząca ilość wystapień wskazanej litery     "ile"
# # print('Litera ' ,x, ' wystepuje ', ile(content, x),' razy'
# #
# # #funkcja biorąca "content" i zapisująca wszystkie linie w jednej liście     "razem"
# # content_razem = razem(content)
