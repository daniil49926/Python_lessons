site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def output_site(struct, count=0):
    for i_key, i_val in struct.items():
        if type(i_val) == dict:
            print(("\t" * count), f"'{i_key}':", "{")
            output_site(i_val, count+1)
        else:
            print(("\t" * count), f"'{i_key}': '{i_val}'")


def change_template(struct, list_site):
    for name in list_site:
        print(f"Сайт для {name}")
        struct["html"]["head"]["title"] = f"Куплю/продам {name} недорого"
        struct["html"]["body"]["h2"] = f"У нас самая низкая цена на {name}"
        output_site(struct)


num_site = int(input("Введите кол-во сайтов: "))
list_prod = []
for i in range(num_site):
    name_prod = input("Введите название продукта для нового сайта: ")
    list_prod.append(name_prod)
    change_template(site, list_prod)

# зачёт! 🚀
