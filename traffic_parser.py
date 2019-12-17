import csv, re, sys

if len(sys.argv) == 1:
    print('File to parse not specified.')
    sys.exit(1)

inputFile = sys.argv[1]

with open(inputFile + '_parsed.csv', mode='w', newline='') as trafico_parsed:
    csv_writer = csv.writer(trafico_parsed, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    with open(inputFile, mode='r') as traffic_file:
        csv_reader = csv.DictReader(traffic_file, delimiter=';')
        
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                print('Processing file, please wait...')
                
                # Header column
                csv_writer.writerow(['srcip', 'srcport', 'srcname', 'srcintf','devtype', 'osname', 'dstip', 'dstport', 'dstintf', 'service', 'policyid'])
                line_count +=1
            
            try:
                raw = row["raw"]
            except IndexError:
                print ("Raw column doesn't exist!")
                sys.exit(1)

            # Attributes to find
            srcip = re.search(r'\b(\w*srcip\S*)\b', raw)
            if srcip is None:
                srcip = '0'
            
            srcport = re.search(r'\b(\w*srcport\S*)\b', raw)
            if srcport is None:
                srcport = '0'

            srcname = re.search(r'\b(\w*srcname\S*)\b', raw)
            if srcname is None:
                srcname = '0'

            srcintf = re.search(r'\b(\w*srcintf\S*)\b', raw)
            if srcintf is None:
                srcintf = '0'

            devtype = re.search(r'\b(\w*devtype\S*)\b', raw)
            if devtype is None:
                devtype = '0'
            
            osname = re.search(r'\b(\w*osname\S*)\b', raw)
            if osname is None:
                osname = '0'

            dstip = re.search(r'\b(\w*dstip\S*)\b', raw)
            if dstip is None:
                dstip = '0'

            dstport = re.search(r'\b(\w*dstport\S*)\b', raw)
            if dstport is None:
                dstport = '0'

            dstintf = re.search(r'\b(\w*dstintf\S*)\b', raw)
            if dstintf is None:
                dstintf = '0'
            
            service = re.search(r'\b(\w*service\S*)\B', raw)
            if service is None:
                service = '0'

            policyid = re.search(r'\b(\w*policyid\S*)\B', raw)
            if policyid is None:
                policyid = '0'
            
            # Write attributes row
            csv_writer.writerow([srcip[0], srcport[0], srcname[0], srcintf[0], devtype[0], osname[0], dstip[0], dstport[0], dstintf[0], service[0], policyid[0]])
            
            line_count +=1

        print(f'Printed {line_count} lines.')