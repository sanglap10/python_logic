// This example demonstrates abstraction using C# interfaces and classes.
// Abstraction allows us to define generic operations (like payment) without specifying the exact implementation.
// Different payment apps (PhonePe, GooglePay) implement the same payment interface in their own way.

public interface IUPI
{
    // Declares the payment operation, but does not specify how it works.
    void Pay(float amount);
}

// PhonePe provides its own implementation of the Pay method.
public class PhonePe : IUPI
{
    public void Pay(float amount)
    {
        Console.WriteLine($"Processing payment of {amount} via PhonePe...");
        Console.WriteLine("Payment successful!");
    }
}

// GooglePay also implements the Pay method differently.
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
        // Using abstraction: we interact with the payment system via the IUPI interface,
        // allowing us to switch between payment providers easily.
        IUPI upiAbstraction;

        upiAbstraction = new PhonePe();
        upiAbstraction.Pay(500);

        upiAbstraction = new GooglePay();
        upiAbstraction.Pay(1000);
    }
}
