from six.moves import urllib
from six.moves.urllib import parse as urlparse
import json

class Client(object):

  def __init__(self):
    self.base_params = {}
    self.log = []
    
    self.load_config()
    
  def load_config(self):
    with open("config.txt", "r") as f:
      line = f.readline()
      parts = urlparse.urlparse(line)
      query = urlparse.parse_qs(parts[4])
      for key, value in query.items():
        self.base_params[key] = value[0]
        
    
  def make_request(self, path, params):
    protocol = "https"
    host = "hk4e-api-os.mihoyo.com"    
        
    # merge params with base parameters
    params.update(self.base_params)       
    query = urlparse.urlencode(params)    
    
    url_parts = [protocol, host, path, '', query, '']    
    url = urlparse.urlunparse(url_parts)
    
    return urllib.request.urlopen(url).read()
    
  def get_gacha_log(self, gacha_id):
    page = 1
    path = "/event/gacha_info/api/getGachaLog"
    has_next = True
    while has_next:    
      params = {      
        'auth_appid'  : 'webview_gacha',
        'init_type'   : gacha_id,
        'gacha_type' : gacha_id,
        'page' : page,
        'size': 20,
      }
    
      resp = json.loads(self.make_request(path, params))
      code = resp["retcode"]
      message = resp["message"]
      data = resp["data"]      
      self.parse_gacha_log(data)
      
      print(page)
      # result set has a limit of 20 so we need to check if there's more data
      has_next = len(data["list"]) == int(data["size"])
      page += 1
    
  def parse_gacha_log(self, data):
    item_list = data["list"]
    for item in item_list:
      self.log.append(item)      
    
  def get_event_gacha(self):
    self.get_gacha_log(301)
  
  def get_perm_gacha(self):
    self.get_gacha_log(200)
    
  def get_weapon_gacha(self):
    self.get_gacha_log(302)
    
  def get_novice_gacha(self):
    self.get_gacha_log(100)
     
    
  def export_log(self):
    with open("log.txt", "w") as f:
      f.write("Banner,Type,Date,Name\n")
      for item in self.log:
        gacha_type = item["gacha_type"]
        item_type = item["item_type"]
        rank = item["rank_type"]
        name = item["name"]
        time = item["time"]
        
        f.write("%s,%s,%s,%s\n" %(gacha_type, item_type, time, name))
      
  def run(self):
    self.get_event_gacha()   
    self.get_weapon_gacha()    
    self.get_perm_gacha()
    self.get_novice_gacha()
    self.export_log()
    
    
if __name__ == "__main__":
  c = Client()
  c.run()