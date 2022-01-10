def sort_alphanumeric_lst(an_list):
    sorted_list = sorted(
        an_list, 
        key=lambda x: \
            (int(x.partition(' ')[0]) \
                if x[0].isdigit() else float('inf'), x))
    print("Sorting <<<<<<<<<<<<<<< ", sorted_list)
    return sorted_list