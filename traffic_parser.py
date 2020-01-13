import csv, re, sys

if len(sys.argv) == 1:
    print('File to parse not specified.')
    sys.exit(1)

inputFile = sys.argv[1]

with open(inputFile + '_parsed.csv', mode='w', newline='') as trafico_parsed:
    csv_writer = csv.writer(trafico_parsed, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    with open(inputFile, mode='r') as traffic_file:
        csv_reader = csv.DictReader(traffic_file, delimiter=';')
        columns = ['devname', 'srcip', 'srcport', 'srcname', 'srcintf','devtype', 'osname', 'dstip', 'dstport', 'dstintf', 'service', 'policyid']

        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                print('Processing file, please wait...')
                
                # Header column
                csv_writer.writerow(columns)
                line_count +=1
            
            try:
                raw = row["raw"]
            except IndexError:
                print ("Raw column doesn't exist!")
                sys.exit(1)

            # Attributes to find
            rowValues = []

            for column in columns:
                columnValue = re.search(r'\b(\w*' + re.escape(column) + r'\S*)\b', raw)
                if columnValue is None:
                    columnValue = '0'
                rowValues.append(columnValue[0])
            
            # Write attributes row
            csv_writer.writerow(rowValues)
            
            line_count +=1

        print(f'Printed {line_count} lines.')