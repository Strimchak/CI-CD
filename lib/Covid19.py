import requests
import boto3
from lib.Settings import URL_COVID, HOSTNAME, USER, PASSWORD
import mysql.connector

if __name__ == "__main__":
    pass


class Covid:

    def __init__(self):
        self.db = mysql.connector.connect(
            host=HOSTNAME,
            user=USER,
            password=PASSWORD
        )
        print(self.db)

    def start(self):
        self.__get_data(URL_COVID)

    def __get_data(self, URL):
        responce = requests.get(URL_COVID)
        covid = responce.json()
        self.__save_stat(covid)
        self.__save_data(covid)

    def __save_to_s3(self):
        bucketname = "str-s3-test"
        file_name = "covid.txt"
        s3 = boto3.client('s3')
        s3.upload_file(file_name, bucketname, file_name)

    def __save_stat(self, data):
        f = open("covid.txt", "w", encoding='utf-8')
        for country in data['Countries']:
            f.write("Country: \t" + country["Country"] +
                    "\nNew confirmed: \t" + str(country['NewConfirmed']) +
                    "\nNew confirmed: \t" + str(country['NewConfirmed']) +
                    "\nTotal confirmed:" + str(country['TotalConfirmed']) +
                    "\nNew deaths: \t" + str(country['NewDeaths']) +
                    "\nTotal deaths: \t" + str(country['TotalDeaths']) +
                    "\nNew recovered: \t" + str(country['NewRecovered']) +
                    "\nDate: \t\t" + country['Date'][0: 10] +
                    " " + country['Date'][-9: -1] + "\n\n"
                    )
        f.close()
        self.__save_to_s3()

    def __save_data(self, covid):
        cursor = self.db.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS covid19")
        cursor.execute('USE covid19')
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS covid19_table (Id INT AUTO_INCREMENT PRIMARY KEY, Country VARCHAR(255), CountryCode VARCHAR(255),  Slug VARCHAR(255), NewConfirmed INT(10), TotalConfirmed INT(10), NewDeaths INT(10), TotalDeaths INT(10), NewRecovered INT(10), TotalRecovered INT(10), Date DATETIME)")
        covid = covid['Countries']
        counter = 0
        length = len(covid)
        while counter < length:
            covid1 = covid[counter]
            for x in covid1:
                if x == "Country":
                    country = covid1.get(x)
                elif x == "CountryCode":
                    countrycode = covid1.get(x)
                elif x == "Slug":
                    slug = covid1.get(x)
                elif x == "NewConfirmed":
                    newconfirmer = covid1.get(x)
                elif x == "TotalConfirmed":
                    totalconfirmed = covid1.get(x)
                elif x == "NewDeaths":
                    newdeaths = covid1.get(x)
                elif x == "TotalDeaths":
                    totaldeaths = covid1.get(x)
                elif x == "NewRecovered":
                    newrecovered = covid1.get(x)
                elif x == "TotalRecovered":
                    totalrecovered = covid1.get(x)
                elif x == "Date":
                    date = covid1.get(x)
                    datetime = (date[0: 10] + " " + date[-9: -1])
            sql = "INSERT IGNORE INTO covid19_table (Country, CountryCode, Slug, NewConfirmed, TotalConfirmed, NewDeaths, TotalDeaths, NewRecovered, TotalRecovered, Date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (country, countrycode, slug, newconfirmer, totalconfirmed,
                   newdeaths, totaldeaths, newrecovered, totalrecovered, datetime)
            cursor.execute(sql, val)
            self.db.commit()
            counter += 1
        print("Information added")

        # while counter < length:
        #     covid1 = covid[counter]
        #     for x in covid1:
        #         if x == "CountryCode":
        #             countrycode = covid1.get(x)
        #         elif x == "NewConfirmed":
        #             newconfirmer = covid1.get(x)
        #         elif x == "TotalConfirmed":
        #             totalconfirmed = covid1.get(x)
        #         elif x == "NewDeaths":
        #             newdeaths = covid1.get(x)
        #         elif x == "TotalDeaths":
        #             totaldeaths = covid1.get(x)
        #         elif x == "NewRecovered":
        #             newrecovered = covid1.get(x)
        #         elif x == "TotalRecovered":
        #             totalrecovered = covid1.get(x)
        #         elif x == "Date":
        #             date = covid1.get(x)
        #             datetime = (date[0: 10] + " " + date[-9: -1])
        #     mycursor.execute("UPDATE countries SET  NewConfirmed='" + newconfirmer + "', TotalConfirmed='" + totalconfirmed + "', NewDeaths='" + newdeaths + "', TotalDeaths='" + totaldeaths + "', NewRecovered='" + newrecovered + "', TotalRecovered='" + totalrecovered + "', Date='" +
        #                     date + "' WHERE CountryCode='" + countrycode + "'")
        #     self.db.commit()
        #     counter += 1
