import java.text.MessageFormat;

public class FormatString {
  public static void main(String[] args) {
    var language = "C#";
    var price = 24.99F;
    byte quotas = 20;

    var concatenation = "Course: " + language + " Programming Fundamentals \n" + "Price: $" + price + " \n" + "Quotas: "
        + quotas + " \n";

    var formatString = String.format("Course: %s Programming Fundamentals \nPrice: $%f \nQuotas: %d", language, price,
        quotas);

    var builder = new StringBuilder();
    builder.append("Course: ").append(language).append(" Programming Fundamentals \n").append("Price: $").append(price)
        .append(" \n").append("Quotas: ").append(quotas).append(" \n");
    var builderString = builder.toString();

    var messageFormat = MessageFormat.format("Course: {0} Programming Fundamentals \nPrice: ${1} \nQuotas: {2}",
        language, price, quotas);
  }
}