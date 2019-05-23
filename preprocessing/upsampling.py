import csv

INPUT_FILE = ''
OUTPUT_FILE = ''

def upsampling(input_file, output_file, ratio_upsampling=1):

    # Create a file with equal number of tweets for each label
    #    input_file: path to file
    #    output_file: path to the output file
    #    ratio_upsampling: ratio of each minority classes vs majority one. 1 mean there will be as much of each class than there is for the majority class.
    i = 0
    counts = {}
    dict_data_by_label = {}
    # GET LABEL LIST AND GET DATA PER LABEL
    with open(input_file, 'r', newline='') as csvinfile:
        csv_reader = csv.reader(csvinfile, delimiter=',', quotechar='"')
        for row in csv_reader:
            counts[row[0].split()[0]] = counts.get(row[0].split()[0], 0) + 1
            if not row[0].split()[0] in dict_data_by_label:
                dict_data_by_label[row[0].split()[0]] = [row[0]]
            else:
                dict_data_by_label[row[0].split()[0]].append(row[0])
            i = i + 1
            if i % 10000 == 0:
                print("read" + str(i))
    # FIND MAJORITY CLASS
    majority_class = ""
    count_majority_class = 0
    for item in dict_data_by_label:
        if len(dict_data_by_label[item]) > count_majority_class:
            majority_class = item
            count_majority_class = len(dict_data_by_label[item])

            # UPSAMPLE MINORITY CLASS
    data_upsampled = []
    for item in dict_data_by_label:
        data_upsampled.extend(dict_data_by_label[item])
        if item != majority_class:
            items_added = 0
            items_to_add = count_majority_class - len(dict_data_by_label[item])
            while items_added < items_to_add:
                data_upsampled.extend(
                    dict_data_by_label[item][:max(0, min(items_to_add - items_added, len(dict_data_by_label[item])))])
                items_added = items_added + max(0, min(items_to_add - items_added, len(dict_data_by_label[item])))
    # WRITE ALL
    i = 0

    with open(output_file, 'w') as txtoutfile:
        for row in data_upsampled:
            txtoutfile.write(row + '\n')
            i = i + 1
            if i % 10000 == 0:
                print("writer" + str(i))

    upsampling('tweets.train', 'uptweets.train')