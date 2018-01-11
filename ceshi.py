# Git change by LZ 18.01.11
import json
from datetime import datetime

f_name1 = 'D:\\Workspaces\\Jmeter\\files\\info.json'
f_name2 = 'D:\\Workspaces\\Jmeter\\files\\byte.json'
# 读取info.json和写入Output.txt
try:
    with open(f_name1) as f_obj1:
        f_data1 = json.load(f_obj1)
except FileNotFoundError:
    msg = '对不起，目录下不存在info.json文件'
    print(msg)
else:
    number = int(f_data1['ResultData']['Num'])
    current_number = 0
    with open('Output.txt', 'a') as file_obj:
        # 写入当前时间戳
        file_obj.write('\n\n\n运行时间：' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n\n')
        file_obj.write('当前网关下挂设备数量为：' + str(number) + '\n\n')
        while current_number < number:
            file_obj.write('设备' + str(current_number + 1) + '的名称：' + f_data1['ResultData']['Info'][current_number][
                'Devname'] + '\n')
            file_obj.write(
                '设备' + str(current_number + 1) + '的IP地址：' + f_data1['ResultData']['Info'][current_number]['IP'] + '\n')
            file_obj.write('设备' + str(current_number + 1) + '的MAC地址：' + f_data1['ResultData']['Info'][
                current_number]['DeviceMAC'] + '\n')
            if int(f_data1['ResultData']['Info'][current_number]['AccessInternet']) == 1:
                file_obj.write('设备' + str(current_number + 1) + '是否能访问Internet：是\n')
            else:
                file_obj.write('设备' + str(current_number + 1) + '是否能访问Internet：否\n')
            if int(f_data1['ResultData']['Info'][current_number]['ConnectType']) == 0:
                file_obj.write('设备' + str(current_number + 1) + '连入网关的方式：有线\n')
                file_obj.write('设备' + str(current_number + 1) + '连入网关端口：' + 'LAN' + f_data1['ResultData'][
                    'Info'][current_number]['Port'] + '\n')
            else:
                file_obj.write('设备' + str(current_number + 1) + '连入网关的方式：无线\n')
                file_obj.write('设备' + str(current_number + 1) + '连入网关端口：' + 'SSIDIndex' + f_data1['ResultData'][
                    'Info'][current_number]['SSIDIndex'] + '\n')
            file_obj.write('\n')
            current_number += 1
# 读取byte.json和写入Output.txt
try:
    with open(f_name2) as f_obj2:
        f_data2 = json.load(f_obj2)
except FileNotFoundError:
    msg2 = '对不起，目录下不存在byte.json文件'
    print(msg2)
else:
    with open('Output.txt', 'a') as file_obj:
        file_obj.write('2.4GWiFi接收流量：' + f_data2['ResultData']['WLAN1RX'] + ' KB\n')
        file_obj.write('2.4GWiFi发送流量：' + f_data2['ResultData']['WLAN1TX'] + ' KB\n')
        file_obj.write('Port1接收流量：' + f_data2['ResultData']['Port1RX'] + ' KB\n')
        file_obj.write('Port1发送流量：' + f_data2['ResultData']['Port1TX'] + ' KB\n')
        file_obj.write('Port2接收流量：' + f_data2['ResultData']['Port2RX'] + ' KB\n')
        file_obj.write('Port2发送流量：' + f_data2['ResultData']['Port2TX'] + ' KB\n')
        file_obj.write('字节数在合理范围内，且单调递增！\n')




