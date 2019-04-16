# -*- coding: utf-8 -*-

# 12306 账号
USER_ACCOUNTS = [
    # 目前已支持仅查询，不下单，屏蔽掉下面的账号即可
    {
        'key': 0,  # 如使用多个账号 key 不能重复
        'user_name': '15861816753',
        'password': 'wdd19961011'
    },
    # {
    #     'key': 'wangwu',
    #     'user_name': 'wangwu@qq.com',
    #     'password': 'wangwu'
    # }
]

# 查询间隔(指每一个任务中每一个日期的间隔 / 单位秒)
# 默认取间隔/2 到 间隔之间的随机数 如设置为 1 间隔则为 0.5 ~ 1 之间的随机数
# 接受字典形式 格式:    {'min': 0.5, 'max': 1}
QUERY_INTERVAL = 1

# 用户心跳检测间隔 格式同上
USER_HEARTBEAT_INTERVAL = 120

# 多线程查询
QUERY_JOB_THREAD_ENABLED = 1  # 是否开启多线程查询，开启后第个任务会单独分配线程处理

# 打码平台账号
# 目前只支持免费打码接口 和 若快打码，注册地址：http://www.ruokuai.com/login
AUTO_CODE_PLATFORM = 'free'  # 免费填写 free 若快 ruokuai  # 免费打码无法保证持续可用，如失效请手动切换
AUTO_CODE_ACCOUNT = {  # 使用 free 可用省略
    'user': 'your user name',
    'pwd': 'your password'
}

# 语音验证码
# 没找到比较好用的，现在用的这个是阿里云 API 市场上的，基本满足要求，价格也便宜
# 购买成功后到控制台找到  APPCODE 放在下面就可以了
# 地址：易源 https://market.aliyun.com/products/57126001/cmapi019902.html
# 2019-01-18 更新
# 增加新的服务商 鼎信 https://market.aliyun.com/products/56928004/cmapi026600.html?spm=5176.2020520132.101.2.e27e7218KQttQS
NOTIFICATION_BY_VOICE_CODE = 1  # 开启语音通知
NOTIFICATION_VOICE_CODE_TYPE = 'dingxin'  # 语音验证码服务商  可用项 dingxin  yiyuan
NOTIFICATION_API_APP_CODE = 'your app code'
NOTIFICATION_VOICE_CODE_PHONE = 'your phone'  # 接受通知的手机号

# 钉钉通知
# 使用说明   https://open-doc.dingtalk.com/docs/doc.htm?treeId=257&articleId=105735&docType=1
DINGTALK_ENABLED = 0
DINGTALK_WEBHOOK = 'https://oapi.dingtalk.com/robot/send?access_token=your token'

# Telegram消息推送
# 目前共有两个Bot：
#   1：https://t.me/notificationme_bot
#   2：https://t.me/RE_Link_Push_bot
# 任选一个Bot，关注获取URL链接，如果没有回复则发送给Bot这条信息: /start
# 将获取的URL填入下面对应位置
# 注意：因为以上Bot都由他人公益提供，无法保证随时可用，如以上Bot都无法使用，请使用其他消息推送方式
# Bot1来源：https://github.com/Fndroid/tg_push_bot
# Bot2来源：https://szc.me/post/2.html
TELEGRAM_ENABLED = 0
TELEGRAM_BOT_API_URL = 'https://tgbot.lbyczf.com/sendMessage/:your_token'

# ServerChan 和 PushBear 微信消息推送
# 使用说明
# ServerChan     http://sc.ftqq.com
# PushBear       http://pushbear.ftqq.com
SERVERCHAN_ENABLED = 0
SERVERCHAN_KEY = ''
PUSHBEAR_ENABLED = 0
PUSHBEAR_KEY = ''

# Bark 推送到ios设备
# 参考 https://www.v2ex.com/t/467407
BARK_ENABLED = 0
BARK_PUSH_URL = 'https://api.day.app/:your_token'

# 输出日志到文件
OUT_PUT_LOG_TO_FILE_ENABLED = 0
OUT_PUT_LOG_TO_FILE_PATH = 'runtime/12306.log'  # 日志目录

# 分布式集群配置
CLUSTER_ENABLED = 0  # 集群状态
NODE_IS_MASTER = 1  # 是否是主节点 同时只能启用 1 个主节点
NODE_SLAVE_CAN_BE_MASTER = 1  # 主节点宕机后，子节点是否可以自动提升为主节点(建议打开)
NODE_NAME = 'master'  # 节点名称，不能重复
REDIS_HOST = 'localhost'  # Redis  host
REDIS_PORT = '6379'  # Redis  port
REDIS_PASSWORD = ''  # Redis  密码 没有可以留空

# 邮箱配置
EMAIL_ENABLED = 0  # 是否开启邮件通知
EMAIL_SENDER = 'sender@example.com'  # 邮件发送者
EMAIL_RECEIVER = 'receiver@example.com'  # 邮件接受者 # 可以多个 [email1@gmail.com, email2@gmail.com]
EMAIL_SERVER_HOST = 'localhost'  # 邮件服务 host
EMAIL_SERVER_USER = ''  # 邮件服务登录用户名
EMAIL_SERVER_PASSWORD = ''  # 邮件服务登录密码

# Web 管理
WEB_ENABLE = 1  # 是否打开 Web 管理
WEB_USER = {  # 登录信息
    'username': 'admin',
    'password': 'password'
}
WEB_PORT = 8008  # 监听端口

# 是否开启 CDN 查询
CDN_ENABLED = 0
CDN_CHECK_TIME_OUT = 1 # 检测单个 cdn 是否可用超时时间

# 查询任务
QUERY_JOBS = [
    {
        # 'job_name':  'bj -> sz',  # 任务名称，不填默认会以车站名命名，不可重复
        'account_key': 0,  # 将会使用指定账号下单
        'left_dates': [  # 出发日期 :Array
            "2019-01-25",
            "2019-01-26",
        ],
        'stations': {  # 车站 支持多个车站同时查询  :Dict or :List
            'left': '北京',
            'arrive': '深圳',
        },
        #  # 多个车站示例  (建议添加多个，有时多买几站成功率会高一点)
        # 'stations': [{
        #     'left': '北京',
        #     'arrive': '深圳',
        # },{  # 多个车站示例
        #     'left': '北京',
        #     'arrive': '广州',
        # }],
        'members': [  # 乘客姓名，会根据当前账号自动识别乘客类型 购买儿童票 设置两个相同的姓名即可，程序会自动识别 如  ['张三', '张三']
            "张三",
            "王五",
            # 7,  # 支持通过序号确定唯一乘客，序号查看可通过  python main.py -t 登录成功之后在 runtime/user/ 下找到对应的 用户名_passengers.json 文件，找到对应的 code 填入
        ],
        'allow_less_member': 0,  # 是否允许余票不足时提交部分乘客
        'seats': [  # 筛选座位  有先后顺序 :Array
            # 可用值: 特等座, 商务座, 一等座, 二等座, 软卧, 硬卧, 动卧, 软座, 硬座, 无座
            '硬卧',
            '硬座'
        ],
        'train_numbers': [  # 筛选车次 可以为空，为空则所有车次都可以提交 如 [] 注意大小写需要保持一致
            "K356",
            "K1172",
            "K4184"
        ],
        'except_train_numbers': [  # 筛选车次，排除车次  train_numbers 和 except_train_numbers 不可同时存在
        ],
        'period': {  # 筛选时间
            'from': '00:00',
            'to': '24:00'
        }

    },
    # {
    #     'job_name':  'cd -> gz',  # 任务名称，不填默认会以车站名命名，不可重复
    #     'account_key': 0,  # 将会使用指定账号下单
    #     'left_dates': [
    #         "2019-01-27",
    #         "2019-01-28"
    #     ],
    #     'stations': {
    #         'left': '成都',
    #         'arrive': '广州',
    #     },
    #     'members': [
    #         "小王",
    #     ],
    #     'allow_less_member': 0,
    #     'seats': [
    #         '硬卧',
    #     ],
    #     'train_numbers': []
    # }
]
