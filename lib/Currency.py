import requests
from boto3.session import Session
import boto3
from lib.Settings import FILENAME, URL

if __name__ == "__main__":
    pass

class Currency:
    def start(self):
        print("Start getting currencies ...")
        self.__get_data(URL)
    
    def __get_data(self,URL):
        responce = requests.get(URL)
        data = responce.json()
        print("data => ", data)
        print("Try to save file")
        self.__save_to_currency_file(data)
        print("Try to show data")
        self.__show_currencies(data)


    def __save_to_s3(self):
        # bucketname = input("Enter bucket name to upload > ")
        bucketname = "currency-u"
        # file_name = input("Enter file name to upload > ")
        file_name = "currency.txt"
        s3 = boto3.client('s3')
        s3.upload_file(file_name, bucketname, file_name)

    def __save_to_currency_file(self, data):
        with open(FILENAME, "w") as file:
            for item in data:
                file.write(item["ccy"] + " " + item["base_ccy"] +
                        " " + item["buy"] + " " + item["sale"] + "\n")
        self.__save_to_s3()

    def __show_currencies(self, currency):
        print("Inside show_Ccurrency")
        for item in currency:
            print(item["ccy"] + " " + item["base_ccy"] +
                " " + item["buy"] + " | " + item["sale"])







# import requests
# import boto3
# import time

# URL_PB_API = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"


# def get_date_from_api(URL):
#     req = requests.get(URL)
#     data = req.json()
#     return data


# def show_currency(currencies):
#     f = open("curr.txt", "w")
#     for x in currencies:
#         f.write('{0:<5} {1:<3} {2:<2} {3:<4} {4:<10} {5:<4}{6:<0}'.format(
#             x["ccy"], "-", x["base_ccy"], " ", x["buy"], x["sale"], "\n"))
#     f.close()


# def show_buckets():
#     s3 = boto3.resource('s3')
#     for bucket in s3.buckets.all():
#         print(bucket.name)
#         print("---")
#         for item in bucket.objects.all():
#             print("\t%s" % item.key)


# def upload_file_in_bucket():
#     s3 = boto3.resource('s3')
#     s3.meta.client.upload_file('curr.txt', 'str-s3-test', 'curr.txt')


# def delete_file_from_bucket():
#     s3 = boto3.resource('s3')
#     s3.Object('str-s3-test', 'curr.txt').delete()

# counter =0
# while True:
#     counter+=1
#     print("Sending a ", counter, "time")
#     currencies = get_date_from_api(URL_PB_API)
#     show_currency(currencies)
#     upload_file_in_bucket()
#     time.sleep(300)

# delete_file_from_bucket()
# show_buckets()