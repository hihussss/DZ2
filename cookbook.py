def parse(file):
    discr_bludo = []
    with open(file, encoding = "utf-8") as f:
        data = f.read()
    data_1 = data.split("\n")
    for count,value in enumerate(data_1):
        if value.isdigit():
            discr_bludo.append(data_1[count-1])
            del data_1[count-1]
    for i, k in enumerate(data_1):
        if k.isdigit():
            del data_1[i]        
    stroka = ",".join(data_1)
    new_stroka = stroka.strip().split(",,")
    cook_book1 = dict(zip(discr_bludo,new_stroka))
    cook_book = {}
    for bludo,val in cook_book1.items():
        new_list = val.strip().split(",")
        for va in new_list:
            va = va.split("|")
            ingredient_name,quantity,measure = va
            if bludo in cook_book:
                cook_book[bludo] += [{"ingredient_name":ingredient_name.strip(),"quantity":quantity.strip(),"measure":measure.strip()}]
            else:
                cook_book[bludo] = [{"ingredient_name":ingredient_name.strip(),"quantity":quantity.strip(),"measure":measure.strip()}]
   
    return cook_book

print(parse("data.txt"))


def get_shop_list_by_dishes(dishes, person_count):
    gostis = {}
    tovars = []
    for dish in dishes:
        tovar = parse("data.txt")[dish]
        tovars.extend(tovar)
    for v in tovars:
        gostis[v["ingredient_name"]]={"measure":v["measure"],"quantity":int(v["quantity"])*person_count}
        
        
    return print(gostis)


get_shop_list_by_dishes(["Омлет","Вок"], 3)

def copy_book(text1,text2):
    with open(text1, encoding = "utf-8") as f1:
         data1 = f1.readlines()
    with open(text1, encoding = "utf-8") as f12:     
         data1_text = f12.read()
    with open(text2, encoding = "utf-8") as f2:
         data2 = f2.readlines()
    with open(text2, encoding = "utf-8") as f22:     
         data2_text = f22.read() 
    if len(data1) > len(data2):
         with open("3.txt", "w", encoding = "utf-8") as f3:
            f3.write(f"{text2}\n{len(data2)}\n{data2_text}\n")
         with open("3.txt", "a", encoding = "utf-8") as f3:
            f3.write(f"{text1}\n{len(data1)}\n{data1_text}")   
    elif len(data1) < len(data2):
         with open("3.txt", "w", encoding = "utf-8") as f3:
            f3.write(f"{text1}\n{len(data1)}\n{data1_text}\n") 
         with open("3.txt", "a", encoding = "utf-8") as f3:
            f3.write(f"{text2}\n{len(data2)}\n{data2_text}")
    else:
        print("Строки равны")
    with open("3.txt", encoding = "utf-8") as f3:
        itog_text = f3.read()
    return itog_text

print(copy_book("1.txt","2.txt"))