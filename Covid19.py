import requests
import boto3
from lib.Settings import URL_COVID
import mysql.connector

if __name__ == "__main__":
    pass


class Covid:
    def start(self):
        print("Start getting stat ...")
        self.__get_data(URL_COVID)

    def __get_data(self, URL):
        covid = requests.get(URL_COVID)
        covid = covid.json()['Countries']
        self.__save_stat(covid)

    def __save_to_s3(self):
        bucketname = "str-s3-test"
        file_name = "covid.txt"
        s3 = boto3.client('s3')
        s3.upload_file(file_name, bucketname, file_name)

    def __save_stat(self, data):
        f = open("covid.txt", "w", encoding='utf-8')
        counter = 0
        while counter < 186:
            covid1 = data[counter]
            f.write("Country: \t" + covid1["Country"] +
                    "\nNew confirmed: \t" + str(covid1['NewConfirmed']) +
                    "\nNew confirmed: \t" + str(covid1['NewConfirmed']) +
                    "\nTotal confirmed:" + str(covid1['TotalConfirmed']) +
                    "\nNew deaths: \t" + str(covid1['NewDeaths']) +
                    "\nTotal deaths: \t" + str(covid1['TotalDeaths']) +
                    "\nNew recovered: \t" + str(covid1['NewRecovered']) +
                    "\nDate: \t\t" + covid1['Date'][0: 10] +
                    " " + covid1['Date'][-9: -1] + "\n\n"
                    )
            counter += 1
        f.close()
        self.__save_to_s3()


# def get_date_from_api(URL):
#     covid = requests.get(URL_COVID)
#     covid = covid.json()['Countries']
#     return covid


# def save_stat(covid):
#     f = open("curr.txt", "w", encoding='utf-8')

#     counter = 0
#     while counter < 186:
#         covid1 = covid[counter]
#         f.write("Country: \t" + covid1["Country"] +
#                 "\nNew confirmed: \t" + str(covid1['NewConfirmed']) +
#                 "\nNew confirmed: \t" + str(covid1['NewConfirmed']) +
#                 "\nTotal confirmed:" + str(covid1['TotalConfirmed']) +
#                 "\nNew deaths: \t" + str(covid1['NewDeaths']) +
#                 "\nTotal deaths: \t" + str(covid1['TotalDeaths']) +
#                 "\nNew recovered: \t" + str(covid1['NewRecovered']) +
#                 "\nDate: \t\t" + covid1['Date'][0: 10] +
#                 " " + covid1['Date'][-9: -1] + "\n\n"
#                 )
#         counter += 1

#     f.close()


# while counter < 186: +
#     covid1 = covid[counter]
#     print("Country: \t", covid1['Country'])
#     print("New confirmed: \t", covid1['NewConfirmed'])
#     print("Total confirmed:", covid1['TotalConfirmed'])
#     print("New deaths: \t", covid1['NewDeaths'])
#     print("Total deaths: \t", covid1['TotalDeaths'])
#     print("New recovered: \t", covid1['NewRecovered'])
#     print("Total recovered:", covid1['TotalRecovered'])
#     print("Date: \t\t", covid1['Date'][0: 10] +
#           " " + covid1['Date'][-9: -1], "\n")
#     counter += 1
