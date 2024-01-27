def even_odd_filter(**kwargs):
    for (num_type, nums) in kwargs.items():
        if num_type == "even":
            kwargs[num_type] = [x for x in nums if x % 2 == 0]
        else:
            kwargs[num_type] = [x for x in nums if x % 2 == 1]

    sorted_dict = dict(sorted(kwargs.items(), key=lambda d: -len(d[1])))
    return sorted_dict
