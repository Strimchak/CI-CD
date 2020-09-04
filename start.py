import requests
import boto3

URL_PB_API = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"


def get_date_from_api(URL):
    req = requests.get(URL)
    data = req.json()
    return data


def show_currency(currencies):
    f = open("curr.txt", "a")
    for x in currencies:
        f.write('{0:<5} {1:<3} {2:<2} {3:<4} {4:<10} {5:<4}{6:<0}'.format(
            x["ccy"], "-", x["base_ccy"], " ", x["buy"], x["sale"], "\n"))
    f.close()


def show_buckets():
    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket.name)
        print("---")
        for item in bucket.objects.all():
            print("\t%s" % item.key)


def upload_file_in_bucket():
    s3 = boto3.resource('s3')
    s3.meta.client.upload_file('curr.txt', 'str-s3-test', 'curr.txt')


def delete_file_from_bucket():
    s3 = boto3.resource('s3')
    s3.Object('str-s3-test', 'curr.txt').delete()


currencies = get_date_from_api(URL_PB_API)

show_currency(currencies)


upload_file_in_bucket()

# delete_file_from_bucket()
# show_buckets()
