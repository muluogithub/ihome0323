import os


# 应用目录
BASE_DIR=os.path.join(os.path.dirname(__file__))
# 应用的基本配置
settings={
    'static_path':os.path.join(BASE_DIR,'static'),
    'template_path':os.path.join(BASE_DIR,'templates'),
    'cookie_secret':'7VZajlmLRhmYYAVoo0f5DquUFRCCwEzGrwiBOew9kPM=',
    'xsrf_token':True,
    'debug':True,
}


# sql数据库配置
mysql_config={
    'host': '127.0.0.1',
    'user': 'root',
    'password': '123456',
    'database': 'ihome'
}

# redis
redis_config={
    'host':'127.0.0.1',
    'port':6379
}

# 日志文件目录
log_file=os.path.join(BASE_DIR,'logs/log.txt')
log_level='debug'

# 密码加密
passwd_hash_key="ihome"