from google.cloud.bigquery import Dataset
import json


device = open('device.list.csv', 'w')
deviceinfo = open('device.info.csv', 'w')
msgdevice = open('msg.device.csv', 'w')
client = bigquery.Client()

dataset_ref = client.dataset('iotpubdata')

device_query = 'select devicename from iotpubdata.iotpubmessages group by devicename'

device_query_job = client.query(device_query)  # API request
device_rows = device_query_job.result()

for each_device in device_rows:
    print each_device.devicename
    device.write(each_device.devicename)
    device.write('\n')
    device_detail_query = 'select project, registry, devicename, machine, platform, system, processor, version, release from iotpubdata.iotpubmessages  where devicename = "{}" group by project, registry, devicename, machine, platform, system, processor, version, release'.format(each_device.devicename)
    device_detail_query_job = client.query(device_detail_query)  # API request
    device_detail_rows = device_detail_query_job.result()
    for each_row in device_detail_rows:
        print each_row.project, each_row.registry, each_row.devicename, each_row.machine, each_row.platform, each_row.system, each_row.processor, each_row.version, each_row.release
        deviceinfo.write('{}, {}, {}, {}, {}, {}, {}, {}, {}'.format(each_row.project, each_row.registry, each_row.devicename, each_row.machine, each_row.platform, each_row.system, each_row.processor, each_row.version, each_row.release))
        deviceinfo.write('\n')
    msg_detail_query = 'select * from (select project, registry, devicename, platform, machine,  version, release, count(devicename) AS COUNT, TIMESTAMP_TRUNC(timestamp, HOUR) AS TIME from iotpubdata.iotpubmessages GROUP by TIMESTAMP_TRUNC(timestamp,HOUR), devicename, platform, machine, version, release, project, registry) where devicename = "{}"      ORDER by TIME DESC'.format(each_device.devicename)
    msg_device_query_job = client.query(msg_detail_query)
    msg_device_rows = msg_device_query_job.result()
    for msg_device in msg_device_rows:
        print msg_device.project, msg_device.registry, msg_device.devicename, msg_device.platform, msg_device.machine,  msg_device.version, msg_device.release, msg_device.COUNT, msg_device.TIME
        msgdevice.write('{}, {}, {}, {}, {}, {}, {}, {}, {}'.format(msg_device.project, msg_device.registry, msg_device.devicename, msg_device.platform, msg_device.machine,  msg_device.version, msg_device.release, msg_device.COUNT, msg_device.TIME))
        msgdevice.write('\n')

