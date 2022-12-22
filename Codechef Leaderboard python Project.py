from bs4 import BeautifulSoup
from tabulate import tabulate
import requests
import pandas as pd
class users:
    def __init__(self,name,username,web,rating):
        self.name=name
        self.web=web
        self.rating=rating
        self.username=username
    def printuser(self):
        print("Name:",self.name,"\nUser Name:",self.username,"\nWeb:",self.web,"\nRating:",self.rating)

def rate(user):
    return int(user.rating)

def getlist():
    ratinglist=[]
    print("\n\tCode Chef Leader Board")
    print("\n-----------MENU----------")
    print("1 Displaying the live Rating of all the class members")
    print("2 Creating a Leaderboard table of your friends")
    choice=int(input("Enter your choice : "))
    if choice==1:
        print("Getting Data...")
        f=open('username.txt','r')
        usernames=f.read().split()
        for username in usernames:
            web='https://www.codechef.com/users/'+username
            code=requests.get(web).text
            soup=BeautifulSoup(code,'lxml')
            if(soup.find('div',class_='rating-number')):
                rating=soup.find('div',class_='rating-number').text.split()[0].replace('?i','')
                name=soup.find('div',class_='user-details-container plr10').h1.text
                ratinglist.append(users(name,username,web,rating))
        f.close()
    elif choice==2:
        usernames = [i for i in input("Enter the usernames with spaces : ").split()] 
        print("Getting Data...")
        for username in usernames:
            web='https://www.codechef.com/users/'+username
            code=requests.get(web).text
            soup=BeautifulSoup(code,'lxml')
            if(soup.find('div',class_='rating-number')):
                rating=soup.find('div',class_='rating-number').text.split()[0].replace('?i','')
                name=soup.find('div',class_='user-details-container plr10').h1.text
                ratinglist.append(users(name,username,web,rating))           
    return ratinglist

ratinglist=getlist()
ratinglist.sort(key=rate,reverse=True)
names=[]
ratings=[]
webs=[]
usernames=[]
for i in ratinglist:
    names.append(i.name)
    ratings.append(i.rating)
    webs.append(i.web)
    usernames.append(i.username)
dic={"Name":names,"Ratings":ratings,"Webs":webs,"Usernames":usernames}
df=pd.DataFrame(dic)
print(tabulate(df, headers = 'keys', tablefmt = 'rst'))