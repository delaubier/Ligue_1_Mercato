import os
import requests
import tweepy
from bs4 import BeautifulSoup
import urllib.request
from PIL import Image
import io

# Chargement des variables d'environnement (.env)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    if os.path.exists(".env"):
        with open(".env", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    os.environ.setdefault(k.strip(), v.strip())

a=1
d=0
T=True
while T:
    headers = {'User-Agent':
               'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

    page = "https://www.transfermarkt.fr/ligue-1/letztetransfers/wettbewerb/FR1/plus/1"
    page2 = "https://www.transfermarkt.fr/ligue-1/letztetransfers/wettbewerb/FR1/galerie/1"
    pageTree = requests.get(page, headers=headers)
    pageTree2 = requests.get(page2, headers=headers)
    pageSoup = BeautifulSoup(pageTree.content, 'html.parser')
    pageSoup2 = BeautifulSoup(pageTree2.content, 'html.parser')

    Players = pageSoup.find_all("a", {"class": "spielprofil_tooltip"})

    Players[0].text

    Values = pageSoup.find_all("td", {"class": "rechts hauptlink"})

    Values[0].text

    De = pageSoup.find_all("a", {"class": "vereinprofil_tooltip"})

    De[0].text

    Vers = pageSoup.find_all("a", {"class": "vereinprofil_tooltip"})

    Vers[0].text

    Age = pageSoup.find_all("td", {"class": "zentriert"})

    Poste = pageSoup.find_all("td", {"class": False})

    Poste[0].text

    Nationalite = pageSoup.find_all("td", {"class": "zentriert"})

    Ligue = pageSoup.find_all("td", {"title": False})
    Ligue[0].text

    Images = pageSoup2.find_all("div", {"class": "galerie-bild-container"})

    Lien = pageSoup.find_all("td", {"class": "hauptlink"})

    PlayersList = []
    ValuesList = []
    DeList = []
    VersList = []
    AgeList = []
    PosteList = []
    ImageList = []
    NationaliteList = []
    LigueList = []
    ImgList = []
    LienList = []

    for i in range(0, 25):
        PlayersList.append(Players[i].text)
        ValuesList.append(Values[i].text)
        DeList.append(De[i].text)
        VersList.append(Vers[3].text)
        AgeList.append(Age[1].text)
    PosteList.append(Poste[12].text)
    LigueList.append(Ligue[23].text)

    for Nat in Nationalite:
        # The find() function will find the first image whose class is "flaggenrahmen" and has a title
        Image_Pays = Nat.find("img", {"class": "flaggenrahmen"}, {"title": True})
        # The country_image variable will be a structure with all the image information,
        # one of them is the title that contains the name of the country of the flag image
        if (Image_Pays != None):  # We will test if we have found any matches than add them
            NationaliteList.append(Image_Pays['title'])

    for Img in Images:
        # The find() function will find the first image whose class is "flaggenrahmen" and has a title
        Image_Joueur = Img.find("img", {"class": "galerie-bild"})
        # The country_image variable will be a structure with all the image information,
        # one of them is the title that contains the name of the country of the flag image
        if (Image_Joueur != None):  # We will test if we have found any matches than add them
            ImgList.append(Image_Joueur['src'])
    for L in Lien:
        # The find() function will find the first image whose class is "flaggenrahmen" and has a title
        Lien_Joueur = L.find("a", {"class": "spielprofil_tooltip"})
        # The country_image variable will be a structure with all the image information,
        # one of them is the title that contains the name of the country of the flag image
        if (Lien_Joueur != None):  # We will test if we have found any matches than add them
            LienList.append(Lien_Joueur['href'])
    LienComplet = "https://www.transfermarkt.fr" + LienList[0]

    page3 = LienComplet
    pageTree3 = requests.get(page3, headers=headers)
    pageSoup3 = BeautifulSoup(pageTree3.content, 'html.parser')

    Contrat = pageSoup3.find_all("td", {"class": "zentriert"})

    ContratList = []
    for i in range(0, 25):
        ContratList.append(Contrat[i].text)

    consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
    consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
    access_token = os.getenv("TWITTER_ACCESS_TOKEN")
    access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    urllib.request.urlretrieve(ImgList[0], "test.jpg")

    imgn = Image.open("test.jpg")

    b = io.BytesIO()

    imgn.save(b, "PNG")
    b.seek(0)
    fp = io.BufferedReader(b)

    media = api.media_upload('test.png', file=fp)

    API = tweepy.API(auth)



    if a==1 or d != PlayersList[0]:
        if NationaliteList[0] == "France":
            if ValuesList[0] == "Prêt":
                api.update_status(media_ids=[media.media_id], status="\U0001F534 OFFICIEL \U0001F534 \n\n" + "\U0001F1F9\U0001F1F7 " + PlayersList[1] + " (" + PosteList[0] + " " + "de " + AgeList[0] + " ans)" + " est prêté à/au " + VersList[3] + " (" + LigueList[0] + ") jusqu'au " + ContratList[1] + " en provenance de/du "+ DeList[1] + " !\n\n\U000027A1 https://www.transfermarkt.fr" + LienList[0])
                print("Tweet envoyé !")
            elif ValuesList[0] == "?":
                api.update_status(status = "\U0001F534 OFFICIEL \U0001F534 \n\n" + "\U0001F1F9\U0001F1F7 " + PlayersList[1] + " (" + PosteList[0] + " " + "de " + AgeList[0] + " ans)" + " est transféré à " + VersList[3] + " (" +LigueList[0] + ")" + " en provenance de " + DeList[1] + " pour un montant inconnu !\n\n\U000027A1 https://www.transfermarkt.fr" + LienList[0])
                print("Tweet envoyé !")
            elif ValuesList[0] == "Transfert libre":
                api.update_status(status = "\U0001F534 OFFICIEL \U0001F534 \n\n" + "\U0001F1F9\U0001F1F7 " + PlayersList[1] + " (" + PosteList[0] + " " + "de " + AgeList[0] + " ans)" + " est transféré à " + VersList[3] + " (" +LigueList[0] + ")" + " en provenance de " + DeList[1] + " pour un montant inconnu !\n\n\U000027A1 https://www.transfermarkt.fr" + LienList[0])
                print("Tweet envoyé !")
            elif ValuesList[0] == "-":
                api.update_status(status = "\U0001F534 OFFICIEL \U0001F534 \n\n" + "\U0001F1F9\U0001F1F7 " + PlayersList[1] + " (" + PosteList[0] + " " + "de " + AgeList[0] + " ans)" + " est transféré à " + VersList[3] + " (" +LigueList[0] + ")" + " en provenance de " + DeList[1] + " pour un montant inconnu !\n\n\U000027A1 https://www.transfermarkt.fr" + LienList[0])
                print("Tweet envoyé !")
            elif ValuesList[0] == "Fin du prêt":
                api.update_status(status = "\U0001F534 OFFICIEL \U0001F534 \n\n" + "\U0001F1F9\U0001F1F7 " + PlayersList[1] + " (" + PosteList[0] + " " + "de " + AgeList[0] + " ans)" + " est transféré à " + VersList[3] + " (" +LigueList[0] + ")" + " en provenance de " + DeList[1] + " pour un montant inconnu !\n\n\U000027A1 https://www.transfermarkt.fr" + LienList[0])
                print("Tweet envoyé !")
            else :
                api.update_status(status="\U0001F534 OFFICIEL \U0001F534 \n\n" + "\U0001F1F9\U0001F1F7 " + PlayersList[1] + " (" + PosteList[0] + " " + "de " + AgeList[0] + " ans)" + " est transféré à " + VersList[3] + " (" + LigueList[0] + ")" + " en provenance de " + DeList[1] + " pour " + ValuesList + " !\n\n\U000027A1 https://www.transfermarkt.fr" + LienList[0])
                print("Tweet envoyé !")
        elif NationaliteList[0] == "Turquie":
            if ValuesList[0] == "Prêt":
                api.update_status(media_ids=[media.media_id],status="\U0001F534 OFFICIEL \U0001F534 \n\n" + "\U0001F1F9\U0001F1F7 " + PlayersList[1] + " (" + PosteList[0] + " " + "de " + AgeList[0] + " ans)" + " est prêté à/au " + VersList[3] + " (" + LigueList[0] + ") jusqu'au " + ContratList[1] + " en provenance de/du " + DeList[1] + " !\n\n\U000027A1 https://www.transfermarkt.fr" + LienList[0])
                print("Tweet envoyé !")
            elif ValuesList[0] == "?":
                api.update_status(
                    status="\U0001F534 OFFICIEL \U0001F534 \n\n" + "\U0001F1F9\U0001F1F7 " + PlayersList[1] + " (" +
                           PosteList[0] + " " + "de " + AgeList[0] + " ans)" + " est transféré à " + VersList[3] + " (" +
                           LigueList[0] + ")" + " en provenance de " + DeList[
                               1] + " pour un montant inconnu !\n\n\U000027A1 https://www.transfermarkt.fr" + LienList[0])
                print("Tweet envoyé !")
            elif ValuesList[0] == "Transfert libre":
                api.update_status(
                    status="\U0001F534 OFFICIEL \U0001F534 \n\n" + "\U0001F1F9\U0001F1F7 " + PlayersList[1] + " (" +
                           PosteList[0] + " " + "de " + AgeList[0] + " ans)" + " est transféré à " + VersList[3] + " (" +
                           LigueList[0] + ")" + " en provenance de " + DeList[
                               1] + " pour un montant inconnu !\n\n\U000027A1 https://www.transfermarkt.fr" + LienList[0])
                print("Tweet envoyé !")
            elif ValuesList[0] == "-":
                api.update_status(
                    status="\U0001F534 OFFICIEL \U0001F534 \n\n" + "\U0001F1F9\U0001F1F7 " + PlayersList[1] + " (" +
                           PosteList[0] + " " + "de " + AgeList[0] + " ans)" + " est transféré à " + VersList[3] + " (" +
                           LigueList[0] + ")" + " en provenance de " + DeList[
                               1] + " pour un montant inconnu !\n\n\U000027A1 https://www.transfermarkt.fr" + LienList[0])
                print("Tweet envoyé !")
            elif ValuesList[0] == "Fin du prêt":
                api.update_status(
                    status="\U0001F534 OFFICIEL \U0001F534 \n\n" + "\U0001F1F9\U0001F1F7 " + PlayersList[1] + " (" +
                           PosteList[0] + " " + "de " + AgeList[0] + " ans)" + " est transféré à " + VersList[3] + " (" +
                           LigueList[0] + ")" + " en provenance de " + DeList[
                               1] + " pour un montant inconnu !\n\n\U000027A1 https://www.transfermarkt.fr" + LienList[0])
                print("Tweet envoyé !")
            else:
                api.update_status(status="\U0001F534 OFFICIEL \U0001F534 \n\n" + "\U0001F1F9\U0001F1F7 " + PlayersList[1] + " (" + PosteList[0] + " " + "de " + AgeList[0] + " ans)" + " est transféré à " + VersList[3] + " (" + LigueList[0] + ")" + " en provenance de " + DeList[1] + " pour " + ValuesList + " !\n\n\U000027A1 https://www.transfermarkt.fr" + LienList[0])
                print("Tweet envoyé !")
        else:
            if ValuesList[0] == "Prêt":
                api.update_status(media_ids=[media.media_id], status="\U0001F534 OFFICIEL \U0001F534 \n\n" + PlayersList[1] + " (" + PosteList[0] + " " + "de " + AgeList[0] + " ans)" + " est prêté à/au " + VersList[3] + " (" + LigueList[0] + ") jusqu'au " + ContratList[1] + " en provenance de/du "+ DeList[1] + " !\n\n\U000027A1 https://www.transfermarkt.fr" + LienList[0])
                print("Tweet envoyé !")
            elif ValuesList[0] == "?":
                api.update_status(status = "\U0001F534 OFFICIEL \U0001F534 \n\n" + PlayersList[1] + " (" + PosteList[0] + " " + "de " + AgeList[0] + " ans)" + " est transféré à " + VersList[3] + " (" +LigueList[0] + ")" + " en provenance de " + DeList[1] + " pour un montant inconnu !\n\n\U000027A1 https://www.transfermarkt.fr" + LienList[0])
                print("Tweet envoyé !")
            elif ValuesList[0] == "Transfert libre":
                api.update_status(status = "\U0001F534 OFFICIEL \U0001F534 \n\n" + PlayersList[1] + " (" + PosteList[0] + " " + "de " + AgeList[0] + " ans)" + " est transféré à " + VersList[3] + " (" +LigueList[0] + ")" + " en provenance de " + DeList[1] + " pour un montant inconnu !\n\n\U000027A1 https://www.transfermarkt.fr" + LienList[0])
                print("Tweet envoyé !")
            elif ValuesList[0] == "-":
                api.update_status(status = "\U0001F534 OFFICIEL \U0001F534 \n\n" + PlayersList[1] + " (" + PosteList[0] + " " + "de " + AgeList[0] + " ans)" + " est transféré à " + VersList[3] + " (" +LigueList[0] + ")" + " en provenance de " + DeList[1] + " pour un montant inconnu !\n\n\U000027A1 https://www.transfermarkt.fr" + LienList[0])
                print("Tweet envoyé !")
            elif ValuesList[0] == "Fin du prêt":
                api.update_status(status = "\U0001F534 OFFICIEL \U0001F534 \n\n" + PlayersList[1] + " (" + PosteList[0] + " " + "de " + AgeList[0] + " ans)" + " est transféré à " + VersList[3] + " (" +LigueList[0] + ")" + " en provenance de " + DeList[1] + " pour un montant inconnu !\n\n\U000027A1 https://www.transfermarkt.fr" + LienList[0])
                print("Tweet envoyé !")
            else :
                api.update_status(status="\U0001F534 OFFICIEL \U0001F534 \n\n" + PlayersList[1] + " (" + PosteList[0] + " " + "de " + AgeList[0] + " ans)" + " est transféré à " + VersList[3] + " (" + LigueList[0] + ")" + " en provenance de " + DeList[1] + " pour " + ValuesList + " !\n\n\U000027A1 https://www.transfermarkt.fr" + LienList[0])
                print("Tweet envoyé !")
        d=PlayersList[0]

    a=0