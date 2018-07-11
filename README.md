# dictBuilder
>字典生成和字典整理工具，生成基于姓名关联的字典、爆破字典等，后渗透阶段方便对数据进行筛选、整理。


# 结构

    dictBuilder/
    ├── easyDirectory.py
    ├── frequency.py
    ├── judge.py
    ├── keyword.txt
    ├── main.py
    └── README.md

# 用法

Usage: main.py [options]

Options:

    -h, --help            show this help message and exit   
    -f FILE, --file=FILE  input file
    -m [normal|verify|frequency], --mode=[normal|verify|frequency]
                        select mode,default=normal
    -c CSV, --csv=CSV     set input file as csv format
    -o FILE, --output=FILE
                        output dirctory file
    -n NUM, --num=NUM     input number
  
  
# 例子

1. 生成验证码字典，默认4个字符，生成更多字符加入-n参数
    python mian.py -m "verify"

2. 根据输入的字符串生成4位验证码字典，生成更多字符加入-n参数
    python mian.py -m "verify" -s "abcdefghijklmnopqrstuvwxyz0123456789"

3. 生成辅助爆破字典，-o指定输出的文件名
    python main.py -f top500_user.txt -m "social" -o "output.txt"

4. 迭代生成字符字典，-o指定输出的文件名，默认是output.txt
    python main.py -f keyword.txt -m "normal" -o "output.txt"

5. 筛选使用最频繁使用的密码,-n指定要筛选的个数
    python main.py -f keyword.txt -m "frequency" -n 100


