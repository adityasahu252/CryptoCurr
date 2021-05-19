from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse
import requests,time,schedule
from bs4 import BeautifulSoup
from .models import Currency_Details
# REST  FRAMEWORK IMPORTS 
from .serializers import CryptoSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin




def get_htmlcontent():
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content=session.get(f'https://in.finance.yahoo.com/cryptocurrencies').text
    return html_content



def home():
    print("update.....")
    data = get_htmlcontent()
    # print(data)
    soup = BeautifulSoup(data, 'html.parser') #data-reactid="89"
    namelist=[89,121,153,185,217,249,281,313,345,377]
    pricelist=[92,124,156,188,220,252,284,316,348,380]
    changelist=[94,126,158,190,222,254,286,318,350,382]
    percent_changelist=[96,128,160,192,224,256,288,320,352,384]
    
    for (n,p,c,s) in zip(namelist,pricelist,changelist,percent_changelist):
       
        curr_name=soup.find('td',attrs={'data-reactid':n}).text
        t = Currency_Details.objects.get(name=curr_name)
        # print(t.change)
        
        
        #  name=  soup.find('td',attrs={'data-reactid':n}).text   
        #  price=soup.find('span',attrs={'data-reactid':p}).text 
        #  change=soup.find('span',attrs={'data-reactid':c}).text 
        #  percent_change=soup.find('span',attrs={'data-reactid':s}).text
        #  cryptodata=Currency_Details(name=name,price=price,change=change,percent_change=percent_change)
        #  cryptodata.save()

         
        # t.name=  soup.find('td',attrs={'data-reactid':n}).text 
        t.price=soup.find('span',attrs={'data-reactid':p}).text 
        t.change=soup.find('span',attrs={'data-reactid':c}).text 
        t.percent_change=soup.find('span',attrs={'data-reactid':s}).text
        cryptodata=Currency_Details(name=t.name,price=t.price,change=t.change,percent_change=t.percent_change)
        cryptodata.save()
        # print(name,price,change,percent_change)

    # name1=soup.find('span',attrs={'data-reactid':'124'}).text 
    # print(name1)
    return HttpResponse(requests,"hello")
    

def script_run(request):
    schedule.every(5).seconds.do(home)

    while 1:
        schedule.run_pending()
        time.sleep(1)
    return HttpResponse("connected")


#rest framework code start here
def landin(request):
    return render(request,'index.html')


class CurrencyList(GenericAPIView,ListModelMixin):
    queryset=Currency_Details.objects.all()
    serializer_class=CryptoSerializer

    def get(self,request,*args,**kwargs):
        return self.list(self,request,*args,**kwargs)
  



    
