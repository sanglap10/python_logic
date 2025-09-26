// Abstraction using interface
public interface IUPI
{
    void Pay(float amount);
}

// PhonePe implements UPI abstraction
public class PhonePe : IUPI
{
    public void Pay(float amount)
    {
        Console.WriteLine($"Processing payment of {amount} via PhonePe...");
        Console.WriteLine("Payment successful!");
    }
}

public class GooglePay : IUPI
{
    public void Pay(float amount)
    {
        Console.WriteLine($"Processing payment of {amount} via GooglePay...");
        Console.WriteLine("Payment successful!");
    }
}

public class Program
{
    public static void Main()
    {
        IUPI upiAbstraction;

        upiAbstraction = new PhonePe();
        upiAbstraction.Pay(500);

        upiAbstraction = new GooglePay();
        upiAbstraction.Pay(1000);
    }
}