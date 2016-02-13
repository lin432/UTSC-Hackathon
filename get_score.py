badger_data = open("badgerdata.csv", "r")

def get_score(company_data):
    '''(str) -> float
    '''
    company_data = company_data.split(',')
    product = company_data[0]
    company_name = company_data[-1]
    company_name.split()
    if type(company_name) == list:
        company_name = company_name[0]
    company_name.strip('.')
    company_name = company_name.upper()
    
    score = 'Not Found'
    
    for next_line in badger_data:
        if next_line.startswith(company_name[0]):
            if company_name in next_line:
                next_line = next_line.strip('\n')
                score = next_line.split(',')
                score.append(product)

    return score
