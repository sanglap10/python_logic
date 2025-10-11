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
```

**Key Takeaway**: Abstraction hides complex logic and allows programmers to work with simplified interfaces.

---

## Inheritance
Inheritance allows a **child class (subclass)** to acquire properties and behaviors from a **parent class (superclass)**.  
It helps in:
- **Code reusability** — eliminating duplicate code.  
- **Extensibility** — enhancing or modifying existing functionality.  
- **Maintainability** — improving code structure and readability.

---

### Example: Vehicle → Car & Motorcycle (Hierarchical Inheritance)

#### C# Example
```csharp
// Parent class (Base)
public class Vehicle
{
    public void Start()
    {
        Console.WriteLine("Vehicle is starting...");
    }

    public void Stop()
    {
        Console.WriteLine("Vehicle has stopped.");
    }
}

// Child class 1
public class Car : Vehicle
{
    public void PlayMusic()
    {
        Console.WriteLine("Playing music inside the car...");
    }
}

// Child class 2
public class Motorcycle : Vehicle
{
    public void KickStart()
    {
        Console.WriteLine("Motorcycle started with a kick start...");
    }
}

// Usage
public class Program
{
    public static void Main()
    {
        Car car = new Car();
        car.Start();
        car.PlayMusic();
        car.Stop();

        Console.WriteLine("-------------------");

        Motorcycle bike = new Motorcycle();
        bike.Start();
        bike.KickStart();
        bike.Stop();
    }
}
```

#### Java Example
```java
// Parent class (Base)
class Vehicle {
    void start() {
        System.out.println("Vehicle is starting...");
    }

    void stop() {
        System.out.println("Vehicle has stopped.");
    }
}

// Child class 1
class Car extends Vehicle {
    void playMusic() {
        System.out.println("Playing music inside the car...");
    }
}

// Child class 2
class Motorcycle extends Vehicle {
    void kickStart() {
        System.out.println("Motorcycle started with a kick start...");
    }
}

// Usage
public class Main {
    public static void main(String[] args) {
        Car car = new Car();
        car.start();
        car.playMusic();
        car.stop();

        System.out.println("-------------------");

        Motorcycle bike = new Motorcycle();
        bike.start();
        bike.kickStart();
        bike.stop();
    }
}
```

**Key Takeaway**:  
Inheritance enables code reuse and hierarchical structure, allowing multiple subclasses to share a common base class.

---

## Polymorphism

**Polymorphism** means **"many forms"** — it allows the **same method name** to behave **differently** depending on which object is calling it.

A parent class defines a method, and child classes can **override** it to provide their own specific behavior.

---

### Example: Vehicle → Car → Motorcycle

#### C# Example
```csharp
// Parent class
public class Vehicle
{
    public virtual void Start()
    {
        Console.WriteLine("Vehicle is starting...");
    }
}

// Child class 1
public class Car : Vehicle
{
    public override void Start()
    {
        Console.WriteLine("Car is starting with key ignition...");
    }
}

// Child class 2
public class Motorcycle : Vehicle
{
    public override void Start()
    {
        Console.WriteLine("Motorcycle is starting with a self start button...");
    }
}

// Usage
public class Program
{
    public static void Main()
    {
        Vehicle myCar = new Car();
        Vehicle myBike = new Motorcycle();

        myCar.Start();   // Calls Car's version
        myBike.Start();  // Calls Motorcycle's version
    }
}
```

#### Java Example
```java
// Parent class
class Vehicle {
    void start() {
        System.out.println("Vehicle is starting...");
    }
}

// Child class 1
class Car extends Vehicle {
    @Override
    void start() {
        System.out.println("Car is starting with key ignition...");
    }
}

// Child class 2
class Motorcycle extends Vehicle {
    @Override
    void start() {
        System.out.println("Motorcycle is starting with a self start button...");
    }
}

// Usage
public class Main {
    public static void main(String[] args) {
        Vehicle myCar = new Car();
        Vehicle myBike = new Motorcycle();

        myCar.start();   // Calls Car's version
        myBike.start();  // Calls Motorcycle's version
    }
}
```

**Key Takeaway**:  
Polymorphism allows methods to take on different forms based on the object that calls them, making code flexible, reusable, and extensible.

---
