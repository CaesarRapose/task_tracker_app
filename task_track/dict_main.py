main_dict = {}
def add_to_dict(key, value):
    main_dict[key] = value
def get_from_dict(key):
    return main_dict.get(key, None)
def remove_from_dict(key):
    if key in main_dict:
        del main_dict[key]
def clear_dict():
    main_dict.clear()
def dict_size():
    return len(main_dict)
def dict_keys():
    return list(main_dict.keys())
def dict_values():
    return list(main_dict.values())
def dict_items():
    return list(main_dict.items())
def update_dict(new_dict):
    main_dict.update(new_dict)
def dict_exists(key):
    return key in main_dict
def dict_is_empty():
    return len(main_dict) == 0
def dict_get_all():
    return main_dict.copy()

