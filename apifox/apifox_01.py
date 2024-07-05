import http.client

conn = http.client.HTTPSConnection("www.baidu.com")
payload = ''
headers = {
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
   'Accept': '*/*',
   'Host': 'www.baidu.com',
   'Connection': 'keep-alive',
   'Cookie': 'BAIDUID=F5F63D99C2C9BEA338C6A013A5ABE9F9:FG=1; BIDUPSID=F5F63D99C2C9BEA3F442DFA940B015B4; PSTM=1720144642; BDSVRTM=3; BD_HOME=1'
}
conn.request("GET", "/", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))