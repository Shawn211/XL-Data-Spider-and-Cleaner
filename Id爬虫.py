# -*- coding: cp936 -*-
# coding = utf-8

import re
import requests
import os
import json
import time


def main():
    authorization = input('---------------------\n请输入新鲜的Authorization：')
    batch = input('---------------------\n本次新企业开发批次为：')

    path = 'E:\新企业开发\第' + batch + '批需要开发的企业'
    companies = get_companies_name(path)
    print(f'本批次共{len(companies)}家')

    companies_info = []
    headers = {'Authorization': authorization}
    print('---------------------\n正在收集数据...')
    for company in companies:
        company_id = get_company_id(company, headers)
        companies_info.append([company, company_id])

    save(companies_info, batch)


def get_companies_name(path):
    companies = []
    temporary = dict()

    files = os.listdir(path)
    for file in files:
        num = re.search(r'^(\d+)', file).group(1)
        temporary[int(num)] = file

    with open('CompaniesName.txt', 'w') as f:
        f.write('')

    temporary_nums = sorted(list(temporary))
    for num in temporary_nums:
        with open('CompaniesName.txt', 'a+') as f:
            f.write(re.search(r'(.*)\.', temporary[num]).group(1) + '\n')
        company = re.search(r'\d+(.*?)[(（\-.AB23]', temporary[num]).group(1)
        print(company)
        companies.append(company)
    return companies


def get_company_id(company, headers):
    url = 'http://a.***********.com/api/backend/company/all/info?name='
    url = url + company
    text = requests.get(url, headers=headers).text

    json_text = json.loads(text)
    if json_text['total'] == 1:
        company_id = json_text['rows'][0]['_id']
        return company_id
    else:
        for row in json_text['rows']:
            if row['name'] == company:
                company_id = row['_id']
                return company_id


def save(companies, batch):
    file = 'results.txt'

    text = ''
    for company in companies:
        text += f'\n\'{company[1]}\': [\'app.excel_process.new_{batch}.\', ],  # {company[0]}'

    with open(file, 'w') as f:
        f.write(text)
    print('\n数据已保存！See you next time~')
    time.sleep(1.5)


if __name__ == '__main__':
    main()
