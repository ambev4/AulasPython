# from datetime import datetime

# data_str = '2024-12-22 15:49:00'
# data_fmt = '%d-%m-%Y %H:%M'

# # data = datetime.strptime(data_str, data_fmt)

# print(data_str)


# ------------------------------------------------------------------------
from datetime import datetime

data_str_data = '2022/04/20 07:49:23'
data_str_data = '20/04/2022'
data_str_fmt = '%d/%m/%Y'
# from pytz import timezone

# data = datetime(2022, 4, 20, 7, 49, 23)
data = datetime.strptime(data_str_data, data_str_fmt)
print(data)
data = datetime.now()
print(data.timestamp())  # Isso está na base de dados
print(datetime.fromtimestamp(data.timestamp()))
# data_str_data = '2022/04/20 07:49:23'
# data_str_data = '20/04/2022'
# data_str_fmt = '%d/%m/%Y'

# data = datetime(2022, 4, 20, 7, 49, 23, tzinfo=timezone('Asia/Tokyo'))
# data = datetime.strptime(data_str_data, data_str_fmt)

print(type(data))