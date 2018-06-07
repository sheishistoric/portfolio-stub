from dpla.api import DPLA
import os
my_api_key = os.getenv('6fe82fec460e727f153f50b9e6b28e07')
dpla_connection = DPLA(my_api_key)
result = dpla_connection.search('cats')
item = result.items[2]
print(item)
