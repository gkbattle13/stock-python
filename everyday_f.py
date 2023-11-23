# -*- coding: utf-8 -*-

# 获取基础数据
import inspect
import os
import sys
import time
from akShare_data import americastockdata
from config import configuration

# 获取当前文件路径
current_path = inspect.getfile(inspect.currentframe())
file_abs_path = os.path.abspath(current_path)
# 划分目录，比如a/b/c划分后变为a/b和c
list_path = os.path.split(file_abs_path)
print("添加包路径为：" + list_path[0])
sys.path.append(list_path[0])


def run():
    print(sys.path)
    # TODO 处理需要处理的数据
    time_start = time.time()

    needDate = time.strftime("%Y%m%d", time.localtime())
    engine, logger = configuration.sql_tuShare_log('config.ini')
    us_stock_basic_data = americastockdata.AmericaStockBasicData(engine, logger)

    # base_t(engine, pro, logger)
    # market_t(engine, pro, logger, needDate)
    # reference_t(engine, pro, logger, needDate)
    # financial_statements_t(engine, pro, logger, needDate)

    # us_stock.article_epu_index()
    # us_stock.weibo_index()
    # us_stock.baidu()
    # us_stock.google()

    # 获取美股名单
    # us_stock.get_us_stock_name()
    # 获取美股知名数据
    # us_stock.stock_us_famous_spot_em()

    # us_stock.get_stock_us_daily()

    # 多线程获取美股数据
    us_stock_basic_data.get_stock_us_daily_thread()
    time_end = time.time()
    logger.info("f-clock 运行完成共用时：" + str(time_end - time_start) + 's')


run()
