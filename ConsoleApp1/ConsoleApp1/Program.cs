
Console.WriteLine("калькулятор");

Console.WriteLine("введите перое число:");
string firstInput = Console.ReadLine();
double firstNumber = Convert.ToDouble (firstInput);

Console.WriteLine("введите второе число:");
string SecondInput = Console.ReadLine();
double SeconNumber = Convert.ToDouble (SecondInput);


Console.WriteLine("Введите действие:");
string TnirdInput = Console.ReadLine();

double result = 0;
if (TnirdInput == ("*")

    result = firstNumber + SeconNumber;

if (TnirdInput == "*") 


if (firstNumber > SeconNumber)

    result = firstNumber - SeconNumber;

else

    result = SeconNumber - firstNumber;

Console.WriteLine( "Результат действия:");
Console.WriteLine (result); 
