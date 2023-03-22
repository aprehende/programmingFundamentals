language = "C#"
price = 24.99
quotas = 20

concatenation = "Course: " + language + " Programming Fundamentals \n" + "Price: $" + str(price) + " \n" + "Quotas: " + str(quotas) + " \n"

stringFormat = "Course: {2} Programming Fundamentals \nPrice: ${1} \nQuotas: {0}".format(language, price, quotas)

stringFormat2 = "Course: {pepito} Programming Fundamentals \nPrice: ${price} \nQuotas: {quotas}".format(pepito = language, price = price, quotas = quotas)

stringFormat3 = "Course: {} Programming Fundamentals \nPrice: ${} \nQuotas: {}".format(language, price, quotas)

interpolation = f"Course: {language} Programming Fundamentals \nPrice: ${price} \nQuotas: {quotas}"

stringFormat% = "Course: %s Programming Fundamentals \nPrice: $%d \nQuotas: %d"%(language, price, quotas)