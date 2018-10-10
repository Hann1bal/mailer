# coding=utf-8
import json
import random
import xlrd, xlwt
import requests

domains = ["fake.com", "sock.com", "rom.com", "tail.com", "tail.kz", "bahoo.com"]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l","m", "n","o","0", "l", "1", "2", "3", "4", "5", "6", "7", "8", "9",
           "10"]
genders = ["F", "M"]


def get_one_random_domain(domains):
    return domains[random.randint(0, len(domains) - 1)]


def get_one_random_name(letters):
    email_name = ""
    for i in range(7):
        email_name = email_name + letters[random.randint(0, 25)]
    return email_name


def get_one_random_names(letters):
    email_name = letters[random.randint(0, 11)].upper()
    for i in range(7):
        email_name = email_name + letters[random.randint(0, 15)]
    return email_name

def get_one_random_password(letters):
    email_name = letters[random.randint(0, 11)].upper()
    for i in range(7):
        email_name = email_name + letters[random.randint(0, 25)]
    return email_name


def get_one_gender(genders):
    return genders[random.randint(0, len(genders) - 1)]


def generate_random_emails():
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Test')
    for i in range(0, 100000):
        one_name = str(get_one_random_name(letters))
        one_domain = str(get_one_random_domain(domains))
        fname = str(get_one_random_names(letters))
        gname = str(get_one_random_names(letters))
        gender = str(get_one_gender(genders))
        mail = one_name + "@" + one_domain
        print(mail)
        ws.write(i, 0, mail)
        ws.write(i, 1, str(get_one_random_names(letters)) + str(i))
        ws.write(i, 2, gender)
        ws.write(i, 3, fname)
        ws.write(i, 4, gname)
    wb.save('xl_rec.xls')


def main():
    generate_random_emails()



def testin_reg():
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Test')
    rb = xlrd.open_workbook('xl_rec.xlsx', formatting_info=True)
    sheet = rb.sheet_by_index(0)
    for rownum in range(sheet.nrows):
        username = sheet.cell(rowx=rownum, colx=0).value
        password = sheet.cell(rowx=rownum, colx=1).value
        gender = sheet.cell(rowx=rownum, colx=2).value
        family_name = sheet.cell(rowx=rownum, colx=3).value
        given_name = sheet.cell(rowx=rownum, colx=4).value
        response_data = {}
        data = {
            "username": username,
            "password": password,
            # "given_name": given_name,
            # "family_name": family_name,
            # "middle_name": "",
            # "gender": gender
        }
        # data["csrfmiddlewaretoken"] = request.COOKIES['csrftoken']
        headers = {'content-type': 'application/json', "Accept": "text/plain",
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'}
        r = requests.post(url='http://******',
                          data=json.dumps(data, skipkeys=False), headers=headers)

        response_data['result'] = "Good"
        response_data['message'] = str(r._content)
        ws.write(rownum, 0, username)
        ws.write(rownum, 1, rownum)
        if json.loads(r.content)["status"] == 200 or json.loads(r.content)["status"] == "200":
            code = "PASSED"
            ws.write(rownum, 3, code)
            ws.write(rownum, 2, json.loads(r._content)["token"])
            ws.write(rownum, 4, json.loads(r._content)["status"])
        else:
            code = "Failed"
            ws.write(rownum, 2, json.loads(r._content)["token"])
            ws.write(rownum, 3, code)
            ws.write(rownum, 4,json.loads(r._content)["status"])
        print rownum
    wb.save('xl_r2ec_login.xlsx')
    print json.dumps({"status":"DONE"})
main()
