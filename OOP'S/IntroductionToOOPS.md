**Object-Oriented Programming (OOP)** is a programming paradigm based on the concept of “**objects**,” which bundle both **data** and **behavior**.

Each object is an instance of a **class** (a blueprint or template).

| Concept        | Description                                                    | Example                              |
| -------------- | -------------------------------------------------------------- | ------------------------------------ |
| **Class**      | A blueprint to create objects. Defines attributes and methods. | `class Car { color, drive(); }`      |
| **Object**     | Instance of a class with its own state.                        | `Car myCar = new Car("Red");`        |
| **Attributes** | Variables that define the state of an object.                  | `name`, `balance`, `color`           |
| **Methods**    | Functions that define object behavior.                         | `deposit()`, `drive()`, `withdraw()` |

### OOP vs Procedural Programming

| Aspect                  | Procedural Programming        | Object-Oriented Programming          |
| ----------------------- | ----------------------------- | ------------------------------------ |
| **Approach**            | Step-by-step instructions     | Real-world modeling using objects    |
| **Data Handling**       | Global/shared access          | Encapsulated within objects          |
| **Reusability**         | Limited                       | High (via Inheritance, Polymorphism) |
| **Scalability**         | Difficult for large codebases | Highly scalable                      |
| **Modularity**          | Function-based                | Class and object-based               |
| **Real-world modeling** | Not intuitive                 | Closely mimics real-world            |

### Four Pillars of OOP

| Pillar            | Description                                                     | Example                           |
| ----------------- | --------------------------------------------------------------- | --------------------------------- |
| **Encapsulation** | Hides internal data and provides controlled access via methods. | `private balance; getBalance()`   |
| **Abstraction**   | Hides complexity and shows only essential features.             | `startCar()` hides engine details |
| **Inheritance**   | One class inherits properties/methods from another.             | `Car extends Vehicle`             |
| **Polymorphism**  | Same method works differently for different classes.            | `draw()` → Circle, Rectangle      |

### Benefits of OOP

1. **Modularity**: Code is divided into small classes.
2. **Reusability**: Inherited features reduce code duplication.
3. **Maintainability**: Easier to update/fix bugs in modular code.
4. **Scalability**: Easy to extend features.
5. **Security**: Encapsulation hides sensitive data.

### Use Cases of OOP

| Feature         | Use Case Example                                     |
| --------------- | ---------------------------------------------------- |
| **Modularity**  | Classes for `Account`, `Customer`, `Transaction`     |
| **Reusability** | `Vehicle` → `Car`, `Truck`, `Bike`                   |
| **Scalability** | Add `Loan` class to banking system                   |
| **Security**    | `private balance` only accessible via `getBalance()` |

### Real-Life Analogy: Banking System

| Element       | Real Example                            |
| ------------- | --------------------------------------- |
| **Class**     | `Account`, `Customer`, `Transaction`    |
| **Object**    | Raj's `Account`, John's `Transaction`   |
| **Attribute** | `name`, `balance`, `accountNumber`      |
| **Method**    | `deposit()`, `withdraw()`, `transfer()` |

### Why OOP is Better for Large-Scale Applications?

- **Separation of Concerns**: Each class handles one responsibility.
- **Code Reusability**: Build on existing code using inheritance.
- **Maintainability**: Easier to debug and modify small parts.
- **Security**: Access control with public/private.
- **Scalability**: Add features by creating new classes, not altering old ones.

### 🔹 Access Modifiers in OOP

| Modifier    | Access Level                               |
| ----------- | ------------------------------------------ |
| `public`    | Accessible from anywhere                   |
| `private`   | Accessible only within the class           |
| `protected` | Accessible within the class and subclasses |

### 🔹 Constructor

A special method used to initialize objects.

```java
class Car {
  Car(String color) {
    this.color = color;
  }
}

```

### 🔹 Static vs Instance

- **Static**: Belongs to the class. Shared across all objects.
- **Instance**: Unique to each object.

### Object Communication Flow

```
Class → Object → Method Call → Action

```

### Real-World Structure (Bank Example)

```
+------------------+
|     Account      |
+------------------+
| - balance        |
| - accountNumber  |
+------------------+
| + deposit()      |
| + withdraw()     |
+------------------+

```

## Functional Programming (FP) vs Object-Oriented Programming (OOP)

### What is Functional Programming?

**Functional Programming** is a programming paradigm where computation is treated as the **evaluation of mathematical functions** and avoids changing **state** or **mutating data**.

### Key Characteristics of Functional Programming:

| Feature                   | Description                                                  |
| ------------------------- | ------------------------------------------------------------ |
| **Pure Functions**        | No side effects. The output depends only on the input.       |
| **Immutability**          | Data does not change after it's created.                     |
| **First-Class Functions** | Functions are treated as values — they can be passed around. |
| **No Shared State**       | Functions do not rely on or alter any external state.        |
| **Declarative**           | Focuses on what to solve, not how.                           |

### Bank Example: Add Balance & Withdraw Money

Functional Programming Approach

```jsx
// Account is just a data object
const account = { name: "Raj", balance: 1000 };

// Pure function to deposit money
function deposit(account, amount) {
  return { ...account, balance: account.balance + amount };
}

// Pure function to withdraw money
function withdraw(account, amount) {
  if (account.balance >= amount) {
    return { ...account, balance: account.balance - amount };
  } else {
    throw new Error("Insufficient balance");
  }
}

// Usage
const updatedAccount = deposit(account, 500);
const finalAccount = withdraw(updatedAccount, 200);

 Every time you call a function, it returns a **new object** — no object is ever modified in place.
```

### OOP Approach

```python
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient balance")

# Usage
acc = Account("Raj", 1000)
acc.deposit(500)
acc.withdraw(200)

The account **state changes internally**, and behavior is bundled with data.
```

### Why OOP is Better for Real-World Systems like Banking

| Criteria                | Functional Programming                      | Object-Oriented Programming                           |
| ----------------------- | ------------------------------------------- | ----------------------------------------------------- |
| **Data + Behavior**     | Separated — functions don’t belong to data  | Bundled — data and methods in one object              |
| **State Management**    | Difficult — state must be passed every time | Easy — state is internal and managed                  |
| **Encapsulation**       | Not supported natively                      | Strongly supported via classes                        |
| **Security**            | Weak — no private data                      | Strong — access control (private, protected)          |
| **Real-world Modeling** | Harder — requires abstract separation       | Easy — mirrors real-world (e.g., `Account.deposit()`) |
| **Code Reusability**    | Functions reused but not extended           | Classes and methods easily reused and extended        |
| **Scalability**         | Becomes harder to manage with complex state | Scales well — modular and hierarchical                |

### Limitations of Functional Programming in Banking

- **No encapsulation**: Can't hide `balance`, increasing risk of misuse.
- **Immutability Overhead**: Every state change creates a new object → memory overhead.
- **Poor Real-World Mapping**: You don’t interact with real-world objects via pure functions, but via **actions performed on entities** (objects).
- **Too much state passing**: Every function needs to receive and return the full state, which becomes verbose.

### Why OOP Solves Real-World Problems Better

1. 👤 **Objects = Real Entities**: An `Account` class behaves like a real bank account.
2. 🔒 **Encapsulation**: Protects critical data like balance with access control.
3. 🔄 **Stateful Design**: Natural to track changes (deposits, withdrawals).
4. 🔁 **Polymorphism**: Can handle different account types with shared logic (`Savings`, `Current`, `LoanAccount`).
5. 🧱 **Modularity**: Add new features (e.g., transaction history, interest calculation) by extending classes.

| Aspect          | Functional Programming                          | Object-Oriented Programming                |
| --------------- | ----------------------------------------------- | ------------------------------------------ |
| Best For        | Small stateless utilities, data transformations | Real-world, complex, stateful applications |
| Memory Use      | Higher due to immutability                      | Lower as objects are updated in place      |
| Maintainability | Good for small systems                          | Great for large, evolving systems          |
| Example Domain  | Math functions, data pipelines                  | Banking systems, games, GUI apps, ERPs     |

Functional Programming is powerful in data-heavy, stateless domains like **data science**, **stream processing**, or **configuration systems**.

However, **banking systems**, **inventory management**, and other **business domains with real-world entities and states** are better modelled using **Object-Oriented Programming** because:

> OOP models the world as it is: objects with state and behaviour.

## Classes And Objects

### What is Class?(Logical Representation)

A Class is the logical representation or blueprint of a real-world entity.
It defines a set of attributes (data) and behaviors (methods) but does not occupy memory until instantiated.

- Defines structure and behavior but **not the data itself**.
- Acts as a **template** for creating objects.
- Can be reused to create multiple objects with similar characteristics.

```java
class Employee {
    String employeeName;
    double salary;

    void setName(String name) {
        employeeName = name;
    }

    void setSalary(double s) {
        salary = s;
    }

    double getSalary() {
        return salary;
    }
}
```

> This defines a **template** for creating employees. But it doesn't store any actual data until an object is created.

### What is Object ?(Physical Instance)

An Object is the physical instance of a class.
It holds actual data in memory and interacts with other parts of the program through methods.

- Created using the `new` keyword.
- Memory is **allocated in the heap**.
- Each object has its own **separate copy** of attributes.

```java
public class Main {
    public static void main(String[] args) {
        Employee obj1 = new Employee();
        Employee obj2 = new Employee();

        obj1.setName("Raj");
        obj1.setSalary(50000);

        obj2.setName("Rahul");
        obj2.setSalary(60000);

        System.out.println(obj1.getSalary()); // 50000.0
        System.out.println(obj2.getSalary()); // 60000.0
    }
}

```

> Two **separate employees** are created with their own **state**. `obj1` and `obj2` are independent.

### What are Attributes and Bhevaiour ?

| Term           | Definition                                        | Example                                   |
| -------------- | ------------------------------------------------- | ----------------------------------------- |
| **Attributes** | Data members of a class (state of an object)      | `employeeName`, `salary`                  |
| **Behaviors**  | Functions/methods that define how the object acts | `setName()`, `setSalary()`, `getSalary()` |

### How are objects created and destroyed in the memory?

### 1. Stack Memory

- Stores **method calls** and **local variables**, including **references** to objects.
- Fast but limited in size.
- When a method finishes execution, its **stack frame is destroyed**.

### 2. Heap Memory

- Stores **actual objects** and their **attributes**.
- Managed by the **Garbage Collector (GC)** in Java.
- Slower but much larger.

```java
Employee obj1 = new Employee();
```

| Memory Area | What Happens                                                        |
| ----------- | ------------------------------------------------------------------- |
| **Heap**    | `new Employee()` creates an object and stores its data here         |
| **Stack**   | `obj1` holds a **reference** (memory address) to the object in heap |

### Object Destruction: Garbage Collection in Java

- Objects are **automatically deleted** when no references to them exist.
- Java’s **Garbage Collector (GC)** periodically checks heap memory for unused objects and frees them.

Heap ⇒ System,Very large (if heap memory. runs out our system ran out of memory)

Stack ⇒ Runtime ,Limited

| Concept               | Explanation                                                 |
| --------------------- | ----------------------------------------------------------- |
| **Class**             | Logical blueprint (e.g., Employee)                          |
| **Object**            | Physical instance of a class with memory allocated          |
| **Attributes**        | Variables like `name`, `salary` stored in object            |
| **Behaviors**         | Methods like `setName()` or `getSalary()` define actions    |
| **Stack Memory**      | Stores method calls, local variables, and object references |
| **Heap Memory**       | Stores actual objects with attributes                       |
| **Garbage Collector** | Automatically removes unused objects from heap              |

## Attributes && Methods

### What are Attributes?

**Attributes** (also known as **fields** or **properties**) are variables that belong to a class. They define the **state** of an object — i.e., the data it holds.

- Describe the **characteristics** of an object.
- Each object has **its own copy** of the attributes.
- Typically declared as **private** to ensure **encapsulation**.
- Can be of any data type (e.g., `String`, `int`, `double`, etc.).

### Example Attributes in a `BankAccount` class:

- `name` (to store the account holder’s name)
- `balance` (to store account balance — should be private)

### What are Methods?

**Methods** are **functions** defined inside a class. They represent the **behavior** of the object — what the object can do or how it can interact with data (its own or external).

- Operate on attributes of the class.
- Often used to **get**, **modify**, or **process** data.
- Methods promote **controlled access** to private data.
- Improve **code modularity** and **reusability**.

### Example Methods in a `BankAccount` class:

- `getBalance()` — to view the balance
- `deposit(amount)` — to add funds
- `withdraw(amount)` — to subtract funds

```java
public class BankAccount {
    private String name;
    private double balance;

    // Constructor
    public BankAccount(String accountHolderName, double initialBalance) {
        name = accountHolderName;
        balance = initialBalance;
    }

    // Getter (read access)
    public double getBalance() {
        return balance;
    }

    // Setter (write access)
    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
        }
    }

    public void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
        }
    }

    public String getName() {
        return name;
    }

    public void setName(String newName) {
        name = newName;
    }
}
```

The reasons why too use methods instead of direct access

| Reason              | Explanation                                            |
| ------------------- | ------------------------------------------------------ |
| **Encapsulation**   | Prevents direct access to sensitive data like balance  |
| **Validation**      | Prevents invalid changes (e.g., negative deposit)      |
| **Maintainability** | Logic is centralized in methods, making updates easier |
| **Security**        | Hides internal implementation from the user            |

Best Practices When Using Attributes and Methods

| Practice                                  | Benefit                                        |
| ----------------------------------------- | ---------------------------------------------- |
| Declare sensitive attributes as `private` | Prevents unauthorized access                   |
| Provide `getter` and `setter` methods     | Allows controlled access to attributes         |
| Validate data in methods                  | Ensures only correct data is processed         |
| Avoid public attributes                   | Keeps your code modular, secure, and adaptable |

## Constructor

A **constructor** is a **special method** that gets called **automatically** when an object of a class is **created**. It’s mainly used to **initialize** the object's state (i.e., its variables/attributes).

## Key Characteristics

| Feature          | Description                                                 |
| ---------------- | ----------------------------------------------------------- |
| Name             | Same as the class (in C++/Java); `__init__` in Python       |
| Return Type      | No return type (not even `void`)                            |
| Called When?     | Automatically, at object creation                           |
| Default Behavior | If not written, a default constructor is used automatically |

## Purpose of a Constructor

1. **Object Initialisation**: Sets initial values for the object’s attributes.
2. **Code Reusability**: Same constructor logic is used every time a new object is created.
3. **Default Values**: Ensures the object starts with a valid default state.

---

## Types of Constructors

### 1. Non-Parameterized Constructor

A constructor that takes **no arguments**.

**Java:**

```java
class BankAccount {
    int balance;

    BankAccount() {
        balance = 0;
        System.out.println("Account created with default balance");
    }
}

```

**Python:**

```python
class BankAccount:
    def __init__(self):
        self.balance = 0
        print("Account created with default balance")

```

---

### 2. Parameterized Constructor

A constructor that takes **arguments** to assign values.

**Java:**

```java
class BankAccount {
    int balance;

    BankAccount(int initialBalance) {
        this.balance = initialBalance;
    }
}

```

**Python:**

```python
class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance

```

---

### 3. Copy Constructor

Used to **copy values** from another object of the same class.

**C++:**

```cpp
class BankAccount {
    int balance;
public:
    BankAccount(int b) { balance = b; }
    BankAccount(const BankAccount &acc) { balance = acc.balance; } // Copy constructor
};

```

**Java (manual copy constructor):**

```java
class BankAccount {
    int balance;

    BankAccount(BankAccount another) {
        this.balance = another.balance;
    }
}

```

**Python:**

```python
class BankAccount:
    def __init__(self, other=None):
        if other:
            self.balance = other.balance
        else:
            self.balance = 0

```

---

## Constructor Chaining (Java)

Chaining means calling one constructor from another to avoid duplicate code.

```java
class BankAccount {
    int balance;

    BankAccount() {
        this(100); // calling another constructor
    }

    BankAccount(int initialBalance) {
        this.balance = initialBalance;
    }
}

```

The `this()` call must be **first line** in the constructor.

---

## Constructor Overloading

When a class has **multiple constructors** with different **parameter lists**.

```java
class BankAccount {
    int balance;

    BankAccount() {
        this.balance = 0;
    }

    BankAccount(int initialBalance) {
        this.balance = initialBalance;
    }

    BankAccount(int deposit, int withdrawal) {
        this.balance = deposit - withdrawal;
    }
}

```

🟢 **Advantages:**

- Flexibility in object creation
- Cleaner and reusable code

---

## Real-World Example: Bank Account

### Use Case:

You're building a banking system that lets users:

- Create an account with zero or custom balance
- Duplicate an account (copy constructor)
- Use different constructors for different account types (savings, salary, etc.)

### Benefits of Constructors:

- Ensures every account starts with valid balance
- Easy to initialize different types of accounts
- Reduces code duplication with chaining and overloading

| Concept                 | Description                                         |
| ----------------------- | --------------------------------------------------- |
| Constructor             | Initializes objects during creation                 |
| Types                   | Non-parameterized, Parameterized, Copy              |
| Constructor Overloading | Same class, multiple constructors                   |
| Constructor Chaining    | One constructor calling another                     |
| Use-case                | Clean, reusable, and flexible object initialization |
