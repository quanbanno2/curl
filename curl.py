import subprocess
import sys

url_list = sys.argv[-1]  # 得到文件变量


def get_cost(url):
    cmd_list = ['curl', '-o', '/dev/null', '-s', '-w', '%{time_total}\n']
    cmd_list.append(url)  # 拼接指令
    out = subprocess.Popen(cmd_list, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)  # 执行拼接的指令
    stdout, stderr = out.communicate()

    cost = float(stdout) * 1000
    return cost


# 循环打印
with open(url_list) as f:
    for url in f.read().split("\n"):
        if url:
            print("%s %s" % (url, get_cost(url)))
