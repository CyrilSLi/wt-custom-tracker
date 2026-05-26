import requests as r
routes = r.get("https://winnipegtransit.com/api/v2/routes").json()
routes_list = ",".join([route["id"] for route in routes])
print('{ queries: "' + routes_list + '".split(",").map((el) => ({route: el})) }')