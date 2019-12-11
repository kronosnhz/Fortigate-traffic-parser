import csv, re, sys

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
                csv_writer.writerow(['srcip', 'srcport', 'dstip', 'dstport', 'service'])
                line_count +=1
            raw = row["raw"]

            dstip = re.search(r'\b(\w*dstip\S*)\b', raw)
            if dstip is None:
                dstip = '0'

            dstport = re.search(r'\b(\w*dstport\S*)\b', raw)
            if dstport is None:
                dstport = '0'

            srcip = re.search(r'\b(\w*srcip\S*)\b', raw)
            if srcip is None:
                srcip = '0'
            
            srcport = re.search(r'\b(\w*srcport\S*)\b', raw)
            if srcport is None:
                srcport = '0'
            
            service = re.search(r'\b(\w*service\S*)\B', raw)
            if service is None:
                service = '0'
            
            csv_writer.writerow([srcip[0], srcport[0], dstip[0], dstport[0], service[0]])
            
            line_count +=1

        print(f'Printed {line_count} lines.')