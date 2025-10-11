## Inheritance

Inheritance is a way to create a new class that reuses, extends, or modifies the features of an existing class. The new class is called a "child" or "subclass," and the existing class is known as a "parent" or "superclass." This helps avoid code duplication and makes programs easier to maintain.

### Example: Phone Inheritance

Suppose you have a generic "Phone" class with basic features. You can create a new class, like "SmartPhone," that inherits from "Phone" and adds extra features.

#### C# Example

```csharp
// Parent class
public class Phone
{
    public string Brand;
    public void MakeCall(string number)
    {
        Console.WriteLine($"Calling {number} from {Brand} phone.");
    }
}

// Child class
public class SmartPhone : Phone
{
    public void BrowseInternet()
    {
        Console.WriteLine("Browsing internet...");
    }
}

// Usage
SmartPhone myPhone = new SmartPhone();
myPhone.Brand = "Samsung";
myPhone.MakeCall("1234567890"); // Inherited from Phone class
myPhone.BrowseInternet();       // Defined in SmartPhone class
```

#### Java Example

```java
// Parent class
class Phone {
    String brand;
    void makeCall(String number) {
        System.out.println("Calling " + number + " from " + brand + " phone.");
    }
}

// Child class
class SmartPhone extends Phone {
    void browseInternet() {
        System.out.println("Browsing internet...");
    }
}

// Usage
SmartPhone myPhone = new SmartPhone();
myPhone.brand = "Samsung";
myPhone.makeCall("1234567890"); // Inherited from Phone class
myPhone.browseInternet();       // Defined in SmartPhone class
```

**Key Takeaway**: Inheritance lets you build new classes on top of existing ones, saving time and reducing code repetition.
