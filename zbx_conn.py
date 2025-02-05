from zabbix_api import ZabbixAPI
import requests


# Настройки подключения
ZABBIX_SERVER = "http://10.207.1.39:8080"
USERNAME = "delme"
PASSWORD = "Q1q123456"
GRAPH_ID = "2900"  # 462
OUTPUT_FILE = "graph.png"
GRAPH_URL = f'{ZABBIX_SERVER}/chart2.php?graphid={GRAPH_ID}&width=900&height=200&context=host&filter_hostids[0]=10569'

# Создаем подключение к Zabbix API
zapi = ZabbixAPI(server=ZABBIX_SERVER)
zapi.login(USERNAME, PASSWORD)

print(zapi.api_version())

# Получаем информацию о графике
graph = zapi.graph.get({
    "output": "extend",
    "filter": {"graphid": GRAPH_ID}
})[0]

print(graph)

login_url = ZABBIX_SERVER + "/index.php"
login_data = {'autologin': '1', 'name': USERNAME, 'password': PASSWORD, 'enter': 'Sign in'}
# headers = {
#     'Content-Type': 'application/json',
# }

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0', 'Content-type' : 'application/x-www-form-urlencoded'}

session = requests.session()
login = session.post(login_url, params=login_data, headers=headers, verify=False)

if session.cookies['zbx_session']:
    graphreq = session.get(GRAPH_URL)
    with open(OUTPUT_FILE, 'wb') as file:
        file.write(graphreq.content)
