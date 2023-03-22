var language = "C#";
var price = 24.99F;
byte quotas = 20;

var concatenation = "Course: " + language + " Programming Fundamentals \n" + "Price: $" + price + " \n" + "Quotas: " + quotas + " \n";

var interpolation = $"Course: {language} Programming Fundamentals \nPrice: ${price} \nQuotas: {quotas}";

var format = string.Format("Course: {0} Programming Fundamentals \nPrice: ${1} \nQuotas: {2}", language, price, quotas);

var literalString = @"
Course: C# Programming Fundamentals 
Price: $24.99 
Quotas: 20 

";