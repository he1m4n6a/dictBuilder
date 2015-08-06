# easyPass
>字典生成和字典整理工具


#####结构

    easyPass/
    ├── easyDirectory.py
    ├── frequency.py
    ├── judge.py
    ├── keyword.txt
    ├── main.py
    └── README.md

#####用法

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
  
  
#####例子

    python mian.py -m "verify"

生成验证码字典，默认4个字符，生成更多字符加入-n参数

    python main.py -f top500_user.txt -m "social" -o "output.txt"

生成辅助爆破字典，-o指定输出的文件名
    
    python main.py -f  keyword.txt -m "normal" -o "social_pass.txt"

迭代生成字符字典，-o指定输出的文件名，默认是output.txt
    
    python main.py -f keyword.txt -m "frequency" -n 100

筛选使用最频繁使用的密码,-n指定要筛选的个数
