# Object Oreinted Programing OOP

## Classes and functions

### MOBILE 
    DATA (attributes)  - model, brand, price, battery capacity, RAM, storage, networkProvider
    BEHAVIOUR (methods/function) - makeCall(), sendMessage(), charge(), playGame()

    makeCall(networkProvider) -> FUNCTION
    {
        airtel -> DATA
        joi -> DATA
    }


## 4 principles/pillars of OOPS

 1. Encapsulation
 2. Abstraction
 3. Inheritance
 4. Polymorphism 
 

# Encapsulation - 
    Data hide [amazon app customer can not change the amount of a product but seller can]
    access control - 
                PUBLIC
                PRIVATE 
                PROTECTED

    public class SamsungS25
    {
        // class variables
        float price;
        int ram;
        int storage;
        string networkProvider;

        // PUBLIC METHOD
        public bool makeCall(networkProvider)
        {
            if(networkProvider != '')
            {
                return true;
            }
            return false;
        }

        // PRIVATE METHOD
        private savePhotos(storage)
        {
            if(storage > 1)
            {
                return true;
            }
            return false;
        }
    }

    public class iPhone13
    {
        // class variables
        float price;
        int ram;
        int storage;
        string networkProvider;

        SamsungS25.makeCall(networkProvider);
        SamsungS25.savePhotos(storage); // ERROR !!

    }


# Abstraction