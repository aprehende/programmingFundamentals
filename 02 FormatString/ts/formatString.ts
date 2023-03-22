const language = "C#";
const price = 24.99;
const quotas = 20;

const concatenation =
  "Course: " +
  language +
  " Programming Fundamentals \n" +
  "Price: $" +
  price +
  " \n" +
  "Quotas: " +
  quotas +
  " \n";

const interpolation = `Course: ${language} Programming Fundamentals \nPrice: $${price} \nQuotas: ${quotas}`;
