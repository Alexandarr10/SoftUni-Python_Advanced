def sorting_cheeses(**kwargs):
    sorted_dict = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result = ""
    for name, quantities in sorted_dict:
           result += f"{name}\n"
           sorted_quantities = sorted(quantities, reverse=True)

    return sorted_dict


print(
    sorting_cheeses(
        Parmesan = [102, 120],
        Camembert = [100, 100, 105, 500, 430],
        Mozzarella = [50, 125],
    )
)


