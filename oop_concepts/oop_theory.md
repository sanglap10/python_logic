# Object-Oriented Programming (OOP)

## Overview
Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects," which can contain data (attributes) and behavior (methods).

### Example: Mobile Phone
#### Attributes (Data):
- Model
- Brand
- Price
- Battery Capacity
- RAM
- Storage
- Network Provider

#### Behavior (Methods/Functions):
- `makeCall()`
- `sendMessage()`
- `charge()`
- `playGame()`

#### Example Method:
```java
// Function to demonstrate making a call
makeCall(networkProvider) {
    if (networkProvider === 'airtel') {
        // Airtel specific behavior
    } else if (networkProvider === 'jio') {
        // Jio specific behavior
    }
}
```

---

## Four Pillars of OOP
1. **Encapsulation**
   - Hiding internal details and exposing only necessary functionalities.
2. **Abstraction**
   - Hiding implementation details and showing only essential features.
3. **Inheritance**
   - Reusing and extending features of an existing class.
4. **Polymorphism**
   - Designing objects to share behaviors, allowing one interface to be used for a general class of actions.

---

## Encapsulation
Encapsulation ensures that sensitive data is hidden from users and can only be accessed through specific methods. It uses **access control modifiers**:
- **Public**: Accessible from anywhere.
- **Private**: Accessible only within the class.
- **Protected**: Accessible within the class and its subclasses.

### Example: Encapsulation in a Mobile Class
```java
public class SamsungS25 {
    // Class variables (attributes)
    private float price;
    private int ram;
    private int storage;
    private String networkProvider;

    // Public method (behavior)
    public boolean makeCall(String networkProvider) {
        if (networkProvider != null && !networkProvider.isEmpty()) {
            return true;
        }
        return false;
    }

    // Private method
    private boolean savePhotos(int storage) {
        if (storage > 1) {
            return true;
        }
        return false;
    }
}
```

### Example: Encapsulation Access Error
```java
public class iPhone13 {
    public void exampleUsage() {
        SamsungS25 samsung = new SamsungS25();
        samsung.makeCall("Jio"); // Allowed
        samsung.savePhotos(5);   // ERROR: savePhotos is private and cannot be accessed
    }
}
```

**Key Takeaway**: Encapsulation protects data and ensures controlled access through public methods.

---

## Abstraction
Abstraction focuses on exposing only the essential features of an object while hiding the implementation details. For example, a "Mobile" class might expose methods like `makeCall()` and `sendMessage(...)` but hide how these methods actually work.

### Example: Abstraction using C# Interface

```csharp
// This example demonstrates abstraction using interfaces and classes.
// Abstraction allows us to define generic operations (like payment) without specifying the exact implementation.
// Different payment apps (PhonePe, GooglePay) implement the same payment interface in their own way.

public interface IUPI
{
    void Pay(float amount);
}

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

---

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

---
