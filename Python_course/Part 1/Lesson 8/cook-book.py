with open("recipes.txt", encoding="utf-8") as f:
    cook_book = {}
    line = f.readline()
    while line:
        name_dish = line.strip()
        count_ingredients = int(f.readline().strip())
        ingredient_list = []
        for _ in range(count_ingredients):
            ingredient_name, quantity, measure = f.readline().strip().split(' | ')
            ingredient_dict = {}
            ingredient_dict['ingridient_name'] = ingredient_name
            ingredient_dict['quantity'] = int(quantity)
            ingredient_dict['measure'] = measure
            ingredient_list.append(ingredient_dict)
        cook_book[name_dish] = ingredient_list
        f.readline()
        line = f.readline()

print(cook_book)


def get_shop_list_by_dishes(list_of_dishes, person_count):
    recipes = cook_book
    shop_dict = {}
    for key, value in recipes.items():
        if key in list_of_dishes:
            for product_dict in value:
                dict_of_m_and_q = {}
                name = product_dict['ingridient_name']
                measure = product_dict['measure']
                quantity = product_dict['quantity']
                dict_of_m_and_q['measure'] = measure
                dict_of_m_and_q['quantity'] = int(quantity) * person_count
                shop_dict[name] = dict_of_m_and_q

    print(shop_dict)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
