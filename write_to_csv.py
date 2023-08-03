import csv


def write_to_csv(data):
    with open('data.csv', 'w') as f:
        write = csv.writer(f)
        write.writerow([
            'id',
            'sponsor',
            'start_date',
            'completion_date',
            'drug'
        ])
        write.writerows(data)
