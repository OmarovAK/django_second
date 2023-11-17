from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },

}


def list_dishes(request):
    my_dict = {
        'title': 'Список блюд',
        'dishes': DATA,
    }
    return render(request, 'calculator/dishes.html', my_dict)


def detail_dish(request, name_dish):
    local_dict = DATA[name_dish].copy()
    num_dish = int(request.GET.get('num_dish', 1))
    new_dict = {}
    while len(local_dict) != 0:
        key_value = list(local_dict.popitem())
        new_dict[key_value[0].replace(",", "").capitalize()] = round(key_value[1] * num_dish, 3)

    my_dict = {
        'title': name_dish,
        'dish_detail': new_dict,
        'count_dish': num_dish,
        }
    return render(request, 'calculator/dish_calc.html', my_dict)


def main_page(request):
    my_dict = {
        'title': 'Главная страница'
    }
    return render(request, 'calculator/index.html', my_dict)


