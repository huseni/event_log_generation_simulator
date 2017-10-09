#!/usr/bin/env
###############################################################################
###############################################################################
import time
from time import gmtime, strftime
from random import randrange, uniform

current_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())


def write_file(file_name=None):
    a = randrange(10, 250)
    b = randrange(20, 250)
    c = randrange(30, 250)
    d = randrange(40, 250)
    e = randrange(50, 250)
    f = randrange(60, 250)
    g = randrange(70, 250)
    h = randrange(80, 250)
    i = randrange(90, 250)
    j = randrange(20, 255)
    k = randrange(55, 200)
    l = randrange(105, 250)
    m = randrange(87, 100)
    n = randrange(98, 230)


    DEV2 = "ccmmm"
    DEV4 = "nnmmm"
    DEV3 = "mqttttt"
    DEV1 = "ocscom"
    DEV5 = "mobiledesktop"

    event_code2 = "CMG-002"
    event_code4 = "NMMD-002"
    event_code3 = "MQTT-002"
    event_code1 = "OCUC-002"
    event_code5 = "DDEVICE-002"


    IP1 = """ %s.%s.%s.%s """ % (n, e, d, h)
    IP2 = """ %s.%s.%s.%s """ % (a, c, l, k)
    IP3 = """ %s.%s.%s.%s """ % (d, b, g, f)
    IP4 = """ %s.%s.%s.%s """ % (f, k, n, d)
    IP5 = """ %s.%s.%s.%s """ % (c, m, i, b)

    MSG2 = "CMG was able to convert the request from tcp to http successfully"
    MSG4 = "NMMD has successfully sent out an email for the VHR successfully"
    MSG3 = "MQTT broker was able to publish the message successfully"
    MSG1 = "OCUC is successfully received the response"
    MSG5 = "DDEVICE device has received the response successfully"


    # randrange gives you an integral value
    int_random1 = randrange(0, 10)
    int_random2 = randrange(0, 20)
    int_random3 = randrange(0, 40)
    int_random4 = randrange(0, 60)
    int_random5 = randrange(0, 80)
	
    # uniform gives you a floating-point value
    float_random1 = uniform(0, 20)
    float_random2 = uniform(0, 40)
    float_random3 = uniform(0, 60)
    float_random4 = uniform(0, 80)
    float_random5 = uniform(0, 100)



    fd = open(file_name, 'a')
    current_time1 = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    str1 = """ %s%s%s %s %s %s %s """ % (DEV1, IP1, current_time1, event_code1, int_random1, float_random3, MSG1)
    fd.write(str1 + '\n')
    fd.close()
    time.sleep(9)

    fd = open(file_name, 'a')
    current_time2 = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    str2 = """ %s%s%s %s %s %s %s """ % (DEV2, IP2, current_time2, event_code2, int_random4, float_random4, MSG2)
    fd.write(str2 + '\n')
    fd.close()
    time.sleep(16)

    fd = open(file_name, 'a')
    current_time3 = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    str3 = """ %s%s%s %s %s %s %s """ % (DEV3, IP3, current_time3, event_code3, int_random1, float_random3, MSG3)
    fd.write(str3 + '\n')
    fd.close()
    time.sleep(12)

    fd = open(file_name, 'a')
    current_time4 = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    str4 = """ %s%s%s %s %s %s %s """ % (DEV4, IP4, current_time4, event_code4, int_random3, float_random1, MSG4)
    fd.write(str4 + '\n')
    fd.close()
    time.sleep(15)

    fd = open(file_name, 'a')
    current_time5 = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    str5 = """ %s%s%s %s %s %s %s """ % (DEV5, IP5, current_time5, event_code5, int_random2, float_random1, MSG5)
    fd.write(str5 + '\n')
    fd.close()
    time.sleep(11)


print(write_file('system.log'))

