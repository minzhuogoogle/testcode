pagehtml = open('index.nginx-debian.html', 'w')
pagehtml.write('<!DOCTYPE html>\n')
pagehtml.write('<html>\n')
pagehtml.write('<head>\n')
pagehtml.write('<title>Welcome to IoT Portal!</title>\n')
pagehtml.write('</head>\n')
pagehtml.write('<body>\n')
pagehtml.write('<h1>Welcome to IoT Certification Portal!</h1>\n')

pagehtml.write('<table>\n')
#iot-certification, Chromebox, teemo, Linux-4.4.141-14563-g78fd9f781aae-x86_64-with-Ubuntu-16.04-xenial, x86_64, #1 SMP PREEMPT Thu Sep 6 02:37:58 PDT 2018, 4.4.141-14563-g78fd9f781aae, 62, 2018-09-22 06:00:00+00:00
# column headers
pagehtml.write("<th>\n")
pagehtml.write("<td>Project</td>\n")
pagehtml.write("<td>Registry</td>\n")
pagehtml.write("<td>Device</td>\n")
pagehtml.write("<td>System</td>\n")
pagehtml.write("<td>Machine</td>\n")
pagehtml.write("<td>Plaform</td>\n")
pagehtml.write("<td>Version</td>\n")
pagehtml.write("<td>Count</td>\n")
pagehtml.write("<td>Time</td>\n")
pagehtml.write("</th>\n")


infile = open("msg.device.csv","r")

for line in infile:
    row = line.split(",")
    project = row[0]
    registry = row [1]
    device = row[2]
    system = row[3]
    machine = row[4]
    platform = row[5]
    version = row[6]
    count = row[7]
    time = row[8]

    pagehtml.write("<tr>\n")
    pagehtml.write("<td>%s</td>\n" % project)
    pagehtml.write("<td>%s</td>\n" % registry)
    pagehtml.write("<td>%s</td>\n" % device)
    pagehtml.write("<td>%s</td>\n" % system)
    pagehtml.write("<td>%s</td>\n" % machine)
    pagehtml.write("<td>%s</td>\n" % platform)
    pagehtml.write("<td>%s</td>\n" % version)
    pagehtml.write("<td>%s</td>\n" % count)
    pagehtml.write("<td>%s</td>\n" % time)
    pagehtml.write("</tr>\n")

# end the table
pagehtml.write("</table>\n")

