// Example 1:

class UPI : IUPI
{
    public bool Pay(float amount)
    {
        // logic
        return true;
    }
}

// abstraction
interface IUPI
{
    bool Pay(float amount);
}


class PhonePe
{
    public int Payment(float amount)
    {
        IUPI upiAbstraction;
        bool payStatus = upiAbstraction.Pay(amount);

        if (payStatus == true)
        {
            Console.WriteLine("Payment Done !");
        }
        else
        {
            Console.WriteLine("Payment Failed !");
        }
    }
}

// Example 2:
// abstraction
interface IUPI
{
    void Pay(float amount);
}

// PhonePe implements UPI
class PhonePe : IUPI
{
    public void Pay(float amount)
    {
        Console.WriteLine("Payment processing !!!!");
    }
}

class Program
{
    public static void main()
    {
        IUPI upiAbstraction;
        upiAbstraction = new PhonePe();
        upiAbstraction.Pay(500);
    }
}
