#!/usr/bin/env python3
# coding: latin-1

#--> LIBRARIES
import requests
import json
import sys

#--> VARIABLES
##--> DEFINING THE API ENDPOINT
url = 'https://api.abuseipdb.com/api/v2/check' ###--> API END POINT
api_key = '<API_KEY_ABUSEIPDB_HERE>' ###--> API KEY
mxagedays = '90' ###--> Max Age In Days

#--> FUNCTIONS
##--> BANNER
def banner():
    print('''\033[1;30m
                                  .............
                          ..;,,;;....       ...,;,                   ...;;;;;,;;;....
                       .,,..                     .c.         ..;;::;;.;;,,;...   ....;,;;;,;.
                     ,;.                          c,..;,. .,,.,:;.          .;,.           ..;:,.
                   ;:.            .......;;,;;;;,;c.   ;;;..;:;.............   ;:              ;c;
                  ;:...........,;;;,;;;.....     :,,. .;, .::,;..           ..;c;.              ,l.
                .:cc;;;;.;;;,...                ;,.;.;;. .:;.   .............:c.;;              :c
                :,     .;,.     ...............;,...,;. .:.  .;.          ;cc:,;;.            .cc.
               ;;    .;,,;......              ;,..,;,..;:. ;;.         .;cc:,.. .,.         .:l,
              ,;..;;;;.                  .;,;ol;;:;,.;cc..,;.......,;:cl:;.      ,;       .:l,
    ... ..;;;;:;,:;.               .:ocoodxxxxdoldl:ll:;;,;;...;,::coc;  .;.    .;.     ;cc;
     ..,,;..;;cc;.            ...;cdd:dddxxdddcoxdcldoll,;;;;:c:coo:c.     ;; .;;.   .;l:.
     ...   ,c:c;         ..;;;,,cclllo:lddodolddlcooccc;;;,:;;.;c;.  ......;;;,.  .;cc,.
          ,:;;.       .;...;;. \033[0m\033[0;31m:o:\033[0m\033[1;30m,;:;cdd:;;;cl::lllll.  ..     ......   .;:,.;.;:l;.
                  ..;;,,;,.    .:;.::;odl,::;c;,\033[0m\033[0;31modooc.\033[0m\033[1;30m                .;;:;;, .:c:;,.
                 .,;,:;.    .\033[0m\033[0;31mccc\033[0m\033[1;30m;.;c:c:,:;;,c;c::;:;.    ..       ..;;;..,:;do;.  .;;
                ;;..;.   .;.\033[0m\033[0;31m;o;\033[0m\033[1;30m.:.;,:;,;,,\033[0m\033[0;31m,;::;\033[0m\033[1;30m::.....;,,..;.  .,::;.  ;clc;;,.    ;;
              .,,. .   .,.  .l:,,;,;:;;,..,.. .:,..::o;.;..;;;c:;.   .:c;     .;. ,:.
             ;;;      .,.     ;:;.:l;..        c,;:c;ll;;:cc:;.     .;;        .;:;.
            ::.      .,.        ,;;;.          ,lc:,co:coc:.       ,:,        ;:c.
          .:,.       ,,           ..           .;;c;,;cc...      .:l.      .;cc:.
         .:.        ;;.                         .;;.;c.         ;c;.    .;cc:,.
                   .;;                             ..          ,c;  .;;cc:,.
                   ,;.                                         ...;:c:,.
                   .                                        .;;cc:;.
                                                        ..;lc;l;.
                                                      .,:cc,.
 \033[0m''')
    print("\033[1;31m[---------------\t\t\t\t\t\t\t---------------]\n\n[*] Sentinel B1 - based abuseIPDB API - for find threat's ipAddress [*]\n\n## USAGE:\n\nSingle scan:\n\tpython3",sys.argv[0],"--single <IPAddress_Target>\nOR\n\tpython3",sys.argv[0],"-s <IPAddress_Target>\n\nList scan:\n\tpython3",sys.argv[0],"--list <List_Target.txt>\nOR\n\tpython3",sys.argv[0],"-l <List_Target.txt>\n\033[0m\n")
    exit(1)

##--> SINGLE SCAN
def singleScan():
    print("\033[44;1;37m[*] Checking threat...\033[0m")
    print('''\033[0;31m
                                             .
                      .....;;.             . .;;
                             .;;             .;c
                               .,.           ..c
                                .;,.          .:
                                  .;;         .;;.. ..,;
                 .;                 .,,        .,   .,;
                  .;.;;;.            .;;.     ..;,;..;
                        ...;;;,        .;,.     .;. .,,.
                 ;;;          .;;;;.     .;,.    .,...,;;
                  .,;;            ..;;;    .;;,   .;..;;. .
                     ...;;;,.         ...;    .;;;.;;;..;  . .
                           ....;;;,,.    ...;;   ...;,.;,,,c;;dl   ;  .
                      .,;.        ....;;;,  ...;,. ...:,.;.......,:cl::ll
                         .;;;;;;        ....... .;;.;..,,:c:;,,;.;,;:c:,;,co.
                            ;   .;;....;;.;;............;c:.;;:::c,..;,:,.....
                            .;.            .............,,,,............... ...
                             .;.     ;;;...  ... ...,;..;.;,,.. ;,....;......;..
                               .;;,;;       ..  . ...;;;;...;;;..,;..;;;......;.,
                                          .;...;...;;;..;;,;;;.,;.;:;..,,,;;..,..
                                            .,;...........;;;:;;:. .l;.;,....;..
                                                  ;.....  ...;...;;....... ...;.
                                                      .... .......  .  .,;   ;. ;
                                                       ;..    .         .;..    ..;
                                                      ... .....  ..    .  ...  ..
                                                            ;;.  . ..   .
                                                              .
\033[0m\n''')
    querystring = {'ipAddress': sys.argv[2],'maxAgeInDays': mxagedays}
    headers = {'Accept': 'application/json','Key': api_key}
    response = requests.request(method='GET', url=url, headers=headers, params=querystring)
    decodedResponse = json.loads(response.text)
    if decodedResponse['data']['totalReports'] != 0:
        try:
            print("\033[0;31m[!]\033[0m Threat \033[0;31mFOUND\033[0m -->",decodedResponse['data']['ipAddress'],"-->",decodedResponse['data']['countryCode'],"-->",decodedResponse['data']['domain'],"-->","\033[0;31m"+decodedResponse['data']['hostnames'][0]+"\033[0m","-->",decodedResponse['data']['isp'],"-->",decodedResponse['data']['usageType'],"-->",decodedResponse['data']['lastReportedAt'],"Total Reports -->",decodedResponse['data']['totalReports'])
        except:
            print("\033[0;31m[!]\033[0m Threat \033[0;31mFOUND\033[0m -->",decodedResponse['data']['ipAddress'],"-->",decodedResponse['data']['countryCode'],"-->",decodedResponse['data']['domain'],"-->",decodedResponse['data']['isp'],"-->",decodedResponse['data']['usageType'],"-->",decodedResponse['data']['lastReportedAt'],"Total Reports -->",decodedResponse['data']['totalReports'])
    else:
        try:
            print("\033[0;32m[*]\033[0m Threat \033[0;32mNOT FOUND\033[0m -->",decodedResponse['data']['ipAddress'],"-->",decodedResponse['data']['countryCode'],"-->",decodedResponse['data']['domain'],"-->","\033[0;32m"+decodedResponse['data']['hostnames'][0]+"\033[0m","-->",decodedResponse['data']['isp'],"-->",decodedResponse['data']['usageType'])
        except:
            print("\033[0;32m[*]\033[0m Threat \033[0;32mNOT FOUND\033[0m -->",decodedResponse['data']['ipAddress'],"-->",decodedResponse['data']['countryCode'],"-->",decodedResponse['data']['domain'],"-->",decodedResponse['data']['isp'],"-->",decodedResponse['data']['usageType'])
    exit(1)

##--> LIST SCAN
def listScan():
    outputLIST = []
    print("\033[44;1;37m[*] Searching threats...\033[0m")
    print('''\033[0;31m
                                             .
                      .....;;.             . .;;
                             .;;             .;c
                               .,.           ..c
                                .;,.          .:
                                  .;;         .;;.. ..,;
                 .;                 .,,        .,   .,;
                  .;.;;;.            .;;.     ..;,;..;
                        ...;;;,        .;,.     .;. .,,.
                 ;;;          .;;;;.     .;,.    .,...,;;
                  .,;;            ..;;;    .;;,   .;..;;. .
                     ...;;;,.         ...;    .;;;.;;;..;  . .
                           ....;;;,,.    ...;;   ...;,.;,,,c;;dl   ;  .
                      .,;.        ....;;;,  ...;,. ...:,.;.......,:cl::ll
                         .;;;;;;        ....... .;;.;..,,:c:;,,;.;,;:c:,;,co.
                            ;   .;;....;;.;;............;c:.;;:::c,..;,:,.....
                            .;.            .............,,,,............... ...
                             .;.     ;;;...  ... ...,;..;.;,,.. ;,....;......;..
                               .;;,;;       ..  . ...;;;;...;;;..,;..;;;......;.,
                                          .;...;...;;;..;;,;;;.,;.;:;..,,,;;..,..
                                            .,;...........;;;:;;:. .l;.;,....;..
                                                  ;.....  ...;...;;....... ...;.
                                                      .... .......  .  .,;   ;. ;
                                                       ;..    .         .;..    ..;
                                                      ... .....  ..    .  ...  ..
                                                            ;;.  . ..   .
                                                              .
\033[0m\n''')
    with open(str(sys.argv[2]), 'r') as fp:
        for line in fp.readlines():
            line = line.strip('\n')
            if line != '':
                querystring = {'ipAddress': str(line),'maxAgeInDays': mxagedays}
                headers = {'Accept': 'application/json','Key': api_key}
                response = requests.request(method='GET', url=url, headers=headers, params=querystring)
                decodedResponse = json.loads(response.text)
                if decodedResponse['data']['totalReports'] != 0:
                    try:
                        print("\033[0;31m[!]\033[0m Threat \033[0;31mFOUND\033[0m -->",decodedResponse['data']['ipAddress'],"-->",decodedResponse['data']['countryCode'],"-->",decodedResponse['data']['domain'],"-->","\033[0;31m"+decodedResponse['data']['hostnames'][0]+"\033[0m","-->",decodedResponse['data']['isp'],"-->",decodedResponse['data']['usageType'],"-->",decodedResponse['data']['lastReportedAt'],"Total Reports -->",decodedResponse['data']['totalReports'])
                    except:
                        print("\033[0;31m[!]\033[0m Threat \033[0;31mFOUND\033[0m -->",decodedResponse['data']['ipAddress'],"-->",decodedResponse['data']['countryCode'],"-->",decodedResponse['data']['domain'],"-->",decodedResponse['data']['isp'],"-->",decodedResponse['data']['usageType'],"-->",decodedResponse['data']['lastReportedAt'],"Total Reports -->",decodedResponse['data']['totalReports'])
                    outputLIST.append(decodedResponse['data']['ipAddress'])
                else:
                    try:
                        print("\033[0;32m[*]\033[0m Threat \033[0;32mNOT FOUND\033[0m -->",decodedResponse['data']['ipAddress'],"-->",decodedResponse['data']['countryCode'],"-->",decodedResponse['data']['domain'],"-->","\033[0;32m"+decodedResponse['data']['hostnames'][0]+"\033[0m","-->",decodedResponse['data']['isp'],"-->",decodedResponse['data']['usageType'])
                    except:
                        print("\033[0;32m[*]\033[0m Threat \033[0;32mNOT FOUND\033[0m -->",decodedResponse['data']['ipAddress'],"-->",decodedResponse['data']['countryCode'],"-->",decodedResponse['data']['domain'],"-->",decodedResponse['data']['isp'],"-->",decodedResponse['data']['usageType'])
        print("\n\n\033[41;1;37m:( ! THREAT'S FOUND!  ):\033[0m\n")
        for n in range(len(outputLIST)):
            print(outputLIST[n])

        exit(1)

#--> MAIN
##--> CHECK ARGS
if len(sys.argv) != 3:
    banner()
    exit(1)

##--> DEFINING TYPE SCAN
if sys.argv[1] == "--list" or sys.argv[1] == "-l": ###--> FOR SCAN WITH IP ADDRESS LIST
    if '.txt' in sys.argv[2]:
        listScan()
        exit(1)
    else:
        banner()
elif sys.argv[1] == "--single" or sys.argv[1] == "-s": ###--> FOR SCAN WITH SINGLE IP ADDRESS
    if '.' in str(sys.argv[2]):
        singleScan()
        exit(1)
    else:
        banner()
else:
    banner()
    exit(1)