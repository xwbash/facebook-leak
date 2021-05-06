def mainProgram(direct, link):
    liste = []
    with open(direct,'r',encoding='utf-8') as file:   
        for line in file:      
            for word in line.split(","): 
                liste.append(word)     
                if(word == link):
                    boyutu = len(liste)
                    if(liste[boyutu-7] == "male"):
                        liste[boyutu-7] = "erkek"
                    else:
                        liste[boyutu-7] = "kadın"
                    print("ID: "+liste[boyutu-13]+"\n"+"Telefon Numarasi: "+liste[boyutu-12]+"\n"+"İsim: "+liste[boyutu-11]+"\n"+"Soyisim: "+liste[boyutu-10]+"\n"+"Email: "+liste[boyutu-9]+"\n"+"Doğum Günü: "+ liste[boyutu-8] +"\n"+ "Cinsiyeti: " +liste[boyutu-7])
                    break
print("coded by xwbash.")
direct = input("Dizini giriniz.: ")
link = input("Facebook Linki.: ")
mainProgram(direct,link)

