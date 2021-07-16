import requests
from bs4 import BeautifulSoup



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0',
    'TE': 'Trailers',
}



class animelek:
    def __init__(self,mainlink,one_ep=False,start=1,end=2):
        self.mainlink=mainlink
        self.one_ep=one_ep
        self.start=start
        self.end=end
    def get_servers(self,link):
        rs=requests.get(link,headers=headers)
        soup=BeautifulSoup(rs.text,'html.parser')
        servers={}
        #
        widj=soup.find(attrs={'class':'deatils-page'})
        servers_html=widj.find(attrs={'id':'episode-servers'}).find_all('li')
        #
        for server_html in servers_html:
            servers[server_html.find('a').text]=server_html.find('a').get('data-ep-url')
        return servers
    def get_all_eps_links(self):
        mainlink=self.mainlink
        res=requests.get(mainlink,headers=headers)
        eps=[]
        sp=BeautifulSoup(res.text,'html.parser')
        eps_html=sp.find(attrs={'id':'DivEpisodesList'})
        eps_html=eps_html.find_all('div',{'class':'episodes-card'})
        for index,ep_html in enumerate(eps_html):
            ep={}
            ep_a=ep_html.find(attrs={'class':'episodes-card-title'}).find('a')
            ep_num=index+1
            ep_link,ep_name=ep_a.get('href'),ep_a.text
            ep['num']=ep_num
            ep['name']=ep_name
            ep['link']=ep_link
            eps.append(ep)
        return eps
    def get4sharediframe_download(self,iframesrc):
        r1=requests.get(iframesrc,headers=headers)
        sp1=BeautifulSoup(r1.text,'html.parser')
        link=sp1.find('video').find('source').get('src')
        return link

    def get_one_ep(self,num):
        all_eps=self.get_all_eps_links()
        ep=all_eps[num-1]
        ep_servers=self.get_servers(ep['link'])
        for serv in ep_servers:
            if '4shared' in serv:
                fourshared=ep_servers[serv]
                break
        return self.get4sharediframe_download(fourshared),ep['name']
    def start(self):
        if self.one_ep==False:
            pass
        else:
            
            pass
            
        
