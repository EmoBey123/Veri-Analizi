import requests
response=requests.get('https://api.fbi.gov/wanted/v1/list')
r=response.json()
r=r["items"]
kisiler=[]
for veri in r:
  url=veri["files"][0]["url"]
  cinsiyet=veri["sex"]
  hair=veri["hair"]
  age=veri["age_range"]
  ulus=veri["nationality"]
  olay=veri["caution"]
  title=veri["title"]
  kisiler.append({
      "Başlık":title,
      "Cinsiyet":cinsiyet,
      "Yaş":age,
      "Saç":hair,
      "Ulus":ulus,
      "Url":url,
      "Olay":olay
  })
