# Introduction:
近日，thinkphp团队发布了版本更新，其中修复了一处远程代码执行漏洞，可直接getshell，影响范围：v5.x < 5.1.31，<= 5.0.23
# Dependencies:
pip install -r requirements.txt
# Usage:
```
python thinkphp_rce_poc.py -h
usage: thinkphp rce poc [options]

The thinkphp rce test

optional arguments:
  -h, --help            show this help message and exit
  -m BULKFILE, --multiple BULKFILE
                        scan multiple targets given in a textual file
  -o OUTFILE, --output OUTFILE
                        output file name,default is url.txt

```
# Screenshot:
![avatar](https://github.com/heroanswer/thinkphp_rce_poc/blob/master/screenshot.png)
