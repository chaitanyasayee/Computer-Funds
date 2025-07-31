## Encapsulation (Data Hiding)

**Definition**:

Encapsulation is a **core principle of Object-Oriented Programming (OOP)**. It refers to **binding data and the functions that manipulate that data into a single unit**, typically a class, and **restricting direct access** to some of the object's components.

### Why Is It Called _Data Hiding_?

Encapsulation is often referred to as **data hiding** because:

- Internal details (like variables) are **kept private**.
- Access is provided through **public methods** (getters/setters).
- This restricts **unauthorized or accidental modification** of internal state.

### Key Concepts

- **Private Fields**: Only accessible within the class.
- **Public Methods**: Controlled access to read or modify private data.
- **Getter/Setter Methods**: Used to access or update the private fields with logic or validation.

### Benefits of Encapsulation

| Feature                | Description                                                         |
| ---------------------- | ------------------------------------------------------------------- |
| **Data Security**      | Prevents unauthorized access/modification of internal data.         |
| **Maintainability**    | Changes to internal implementation won't affect outside code.       |
| **Modularity**         | Keeps code organized; each class handles its own data and behavior. |
| **Easier Debugging**   | Centralized control makes errors easier to trace and fix.           |
| **Reduced Complexity** | Only essential behavior is exposed; internal details are hidden.    |

Think of a **vending machine**:

- The **internal logic** (how it stores snacks, accepts coins) is hidden.
- You interact using a **simple interface**: press buttons and insert coins.
- You can't reach inside to grab the snacks — that's encapsulation.

---

### Code Example

### Python

```python
class BankAccount:
    def __init__(self, name, balance):
        self.__accountHolderName = name    # Private field
        self.__balance = balance           # Private field

    def get_balance(self):
        return self.__balance              # Getter

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount       # Setter with validation
        else:
            print("Invalid deposit amount")

```

### Java

```java
public class BankAccount {
    private String accountHolderName;
    private double balance;

    public double getBalance() {
        return balance;
    }

    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
        }
    }
}

```

---

### Key Takeaways

- **Encapsulation** = Data + Methods bundled together + Controlled Access.
- Promotes **data protection, code modularity, and maintainability**.
- It’s implemented using:
  - `private` access modifier for variables.
  - `public` methods to get or set values (with validation).

The statement **"Encapsulation can only be achieved in classes with constructors"** is **not entirely accurate**. Let's clarify:

### **What is True:**

- **Encapsulation requires classes** (or structures in some languages) that **bundle data and methods**.
- You often **use constructors** to initialize data, especially in OOP languages like Java, C++, and Python.

### **What is NOT True:**

- **Encapsulation does NOT require a constructor to exist.**
- A class **can still encapsulate data without a constructor** by using default values or later assignment.

### **What is Required for Encapsulation:**

1. **Private data (fields or attributes)** – Hidden from direct access outside the class.
2. **Public methods (getters/setters)** – Controlled access to private data.

A constructor is **optional**, not mandatory.

### Example (Python – No constructor used):

```python
class BankAccount:
    __balance = 0  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

```

Even without a constructor (`__init__`), this is encapsulation:

- Data (`__balance`) is hidden.
- Access is controlled via `deposit()` and `get_balance()`.

---

### Example (Java – Encapsulation without using constructor):

```java
public class BankAccount {
    private int balance; // private data

    public void deposit(int amount) {
        if (amount > 0) balance += amount;
    }

    public int getBalance() {
        return balance;
    }
}

```

Again, no constructor used here. You can still achieve encapsulation.

---

> Encapsulation is about restricting direct access and exposing controlled methods.
>
> A constructor is just a tool for initializing data, not a requirement for encapsulation.

## What are Access Modifiers (also called Access Specifiers)?

Access modifiers are **keywords** used in object-oriented programming to **control the visibility** of classes, methods, and variables. They determine **which parts of the code can access specific members** (variables, methods, classes).

**Think of access modifiers as door locks**:

- A **public door** is open to everyone.
- A **private door** can only be opened from inside the house.
- A **protected door** is for family members (and close relatives).
- A **default door** (no label) is only for people inside the building.

## Purpose of Access Modifiers

| Purpose                       | Explanation                                            |
| ----------------------------- | ------------------------------------------------------ |
| **Encapsulation**             | Restrict direct access to sensitive data.              |
| **Controlled Access**         | Specify who can access what.                           |
| **Modularity**                | Break code into secure components.                     |
| **Flexibility & Maintenance** | Allow safe data sharing via methods (getters/setters). |

---

## Types of Access Modifiers

Most OOP languages (Java, C++, Python with conventions) provide the following access levels:

### 1. **Public**

- **Accessible** from anywhere (same class, same package/module, different package/module).
- Used when you want methods or data to be **globally visible**.

### 🔧 Syntax

```java
public int number;

```

### Key Points:

- No restrictions.
- Best for utility methods or constants.

### Real-world analogy:

> A public park — anyone can enter.

---

### 2. **Private**

- **Accessible only within the same class**.
- Not accessible in other classes, even if in the same package/module.
- Used to protect sensitive data.

### 🔧 Syntax

```java
private double balance;

```

### Key Points:

- Promotes encapsulation.
- Data is accessed via public getter/setter methods.

### Real-world analogy:

> A private diary — only you can read it.

### Can we create a private class?

- In **Java**: Only **inner/nested classes** can be marked `private`.
- In **C++**: You cannot mark a class as `private`, but you can restrict member access.
- In **Python**: No strict enforcement — use `_` or `__` to indicate "private".

---

### 3. **Protected**

- **Accessible within the same package** and **by subclasses in other packages**.
- Commonly used for inheritance.

### Syntax

```java
protected String type;

```

### Key Points:

- Allows subclass access, even across packages.
- Not accessible to unrelated external classes.

### Real-world analogy:

> A family heirloom — shared only with children/grandchildren.

---

### 4. **Default (Package-Private in Java)**

- When **no access modifier is specified**, the member is only accessible **within the same package**.

### Syntax

```java
String message; // no modifier → default/package-private

```

### Key Points:

- Accessible to all classes in the same package.
- Not accessible outside the package.

### Real-world analogy:

> Office break room — accessible only to company employees (same building).

---

## Comparison Table

| Access Modifier | Class | Same Package | Subclass (Other Package) | Other World (Global) |
| --------------- | ----- | ------------ | ------------------------ | -------------------- |
| **Public**      | ✅    | ✅           | ✅                       | ✅                   |
| **Protected**   | ✅    | ✅           | ✅                       | ❌                   |
| **Default**     | ✅    | ✅           | ❌                       | ❌                   |
| **Private**     | ✅    | ❌           | ❌                       | ❌                   |

### Java

- Fully supports all four access levels.
- Only **nested classes** can be private.
- Package-private is default.

### C++

- Uses `public`, `private`, and `protected`.
- No default/package-private access modifier.
- Members are `private` by default in classes.

### Python

- No built-in access control keywords.
- Uses **naming conventions**:
  - `_var`: protected
  - `__var`: private (name mangling)
- Still **accessible**, but discouraged from being used externally.

---

## Recap: Purpose of Each Modifier

| Modifier      | Purpose                    |
| ------------- | -------------------------- |
| **public**    | Universal access           |
| **private**   | Hide internals             |
| **protected** | Inheritance-focused access |
| **default**   | Same-package interaction   |

---

> Encapsulation is best achieved when data is `private`, and access is provided through **public/protected methods** — this enforces clean interfaces and internal integrity.

# Inheritance

## What is Inheritance?

Inheritance allows a class (child/subclass) to **reuse properties and behaviors** (fields and methods) of another class (parent/superclass). It promotes **code reuse**, **polymorphism**, and **hierarchical classification** in object-oriented programming (OOP).

---

## Syntax Comparison

| Concept           | Java                             | C++                              | Python                                               |
| ----------------- | -------------------------------- | -------------------------------- | ---------------------------------------------------- |
| Class declaration | `class A {}`                     | `class A {}`                     | `class A:`                                           |
| Inheritance       | `class B extends A {}`           | `class B : public A {}`          | `class B(A):`                                        |
| Access Specifier  | `public`, `protected`, `private` | `public`, `protected`, `private` | All members public by default (private via `_`/`__`) |

---

### Java

```java
class Animal {
    void sound() {
        System.out.println("Animal sound");
    }
}

class Dog extends Animal {
    void sound() {
        System.out.println("Dog barks");
    }
}

```

### C++

```cpp
class Animal {
public:
    void sound() {
        cout << "Animal sound" << endl;
    }
};

class Dog : public Animal {
public:
    void sound() {
        cout << "Dog barks" << endl;
    }
};

```

### Python

```python
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

```

---

## Types of Inheritance

### 1. Single Inheritance

```java
class A {}
class B extends A {}

```

```cpp
class A {};
class B : public A {};

```

```python
class A: pass
class B(A): pass

```

### 2. Multilevel Inheritance

```java
class A {}
class B extends A {}
class C extends B {}

```

```cpp
class A {};
class B : public A {};
class C : public B {};

```

```python
class A: pass
class B(A): pass
class C(B): pass

```

### 3. Hierarchical Inheritance

```java
class A {}
class B extends A {}
class C extends A {}

```

```cpp
class A {};
class B : public A {};
class C : public A {};

```

```python
class A: pass
class B(A): pass
class C(A): pass

```

### 4. Multiple Inheritance

- **Java**: ❌ Not supported with classes (allowed using **interfaces**)
- **C++**: ✅ Fully supported
- **Python**: ✅ Fully supported

---

## Multiple Inheritance Example

### C++

```cpp
class A { public: void show() { cout << "A"; } };
class B { public: void display() { cout << "B"; } };
class C : public A, public B {};

```

### Python

```python
class A:
    def show(self): print("A")
class B:
    def display(self): print("B")
class C(A, B): pass

```

### Java (Using Interface)

```java
interface A {
    void show();
}
interface B {
    void display();
}
class C implements A, B {
    public void show() { System.out.println("A"); }
    public void display() { System.out.println("B"); }
}

```

---

## Diamond Problem

Occurs in **C++** and **Python** when multiple inheritance creates ambiguity from a common base class.

### Solution:

- **C++**: Use `virtual` inheritance
- **Python**: Uses **MRO (Method Resolution Order)**
- **Java**: Avoided by disallowing multiple class inheritance

---

## Access Specifiers in Inheritance

| Access Level | Java                       | C++                        | Python                 |
| ------------ | -------------------------- | -------------------------- | ---------------------- |
| Public       | Accessible everywhere      | Accessible everywhere      | Default access         |
| Protected    | Accessible in subclass     | Accessible in subclass     | By convention: `_var`  |
| Private      | Not accessible in subclass | Not accessible in subclass | By convention: `__var` |

---

## Method Overriding vs Overloading

| Feature             | Overloading                        | Overriding                           |
| ------------------- | ---------------------------------- | ------------------------------------ |
| Definition          | Same method name, different params | Subclass redefines superclass method |
| Inheritance Needed? | No                                 | Yes                                  |
| Params              | Must differ                        | Must be same                         |
| Java/C++            | ✅ Supported                       | ✅ Supported                         |
| Python              | ❌ Not supported directly          | ✅ Supported                         |

## super / base() / super()

| Language | Keyword   | Purpose                            |
| -------- | --------- | ---------------------------------- |
| Java     | `super`   | Access parent methods/constructors |
| C++      | `Base::`  | Call base class members            |
| Python   | `super()` | Call parent class methods          |

---

## Constructor Behavior

| Language | Inheritance Constructor Behavior                              |
| -------- | ------------------------------------------------------------- |
| Java     | Subclass constructor **must call** parent using `super()`     |
| C++      | Base class constructor called automatically, unless specified |
| Python   | Explicit call to `super().__init__()` needed                  |

---

## Private Members

| Language | Can child access private members directly?  |
| -------- | ------------------------------------------- |
| Java     | ❌ (access via getter/setter)               |
| C++      | ❌ (use friend function or protected)       |
| Python   | ❌ (name mangling or protected by `_`/`__`) |

---

## Advantages of Inheritance

- Reduces code duplication
- Promotes reusability
- Improves maintainability
- Enables polymorphism
- Models real-world relationships

---

## Real-Life Examples

| Parent Class | Child Classes               |
| ------------ | --------------------------- |
| Vehicle      | Car, Bike, Truck            |
| Employee     | Developer, Manager          |
| Animal       | Mammal, Reptile → Dog, Cat  |
| Shape        | Circle, Rectangle, Triangle |

- Inheritance allows code reuse and logical hierarchy.
- Java avoids multiple inheritance via classes (uses interfaces).
- Python and C++ allow full multiple inheritance but must handle ambiguity carefully.
- Use method overriding to customize parent behavior.
- Use `super` or `base` to invoke parent members explicitly.

Here are **key points on inheritance** that are most frequently asked in interviews, especially related to **access modifiers**, **overriding**, and the **`super` keyword**, with concise explanations and examples across **Java, C++, and Python**:

## Access Modifiers and Inheritance

### Java

| Modifier    | Same Class | Subclass (same pkg) | Subclass (other pkg) | Other Classes |
| ----------- | ---------- | ------------------- | -------------------- | ------------- |
| `private`   | ✅         | ❌                  | ❌                   | ❌            |
| `default`   | ✅         | ✅                  | ❌                   | ❌            |
| `protected` | ✅         | ✅                  | ✅                   | ❌            |
| `public`    | ✅         | ✅                  | ✅                   | ✅            |

### C++

- `private` members: **Not accessible** in derived class.
- `protected` members: **Accessible** in derived class.
- `public` members: **Accessible** everywhere.

### Python

- No strict access control.
  - `_protected`: Convention for internal use (can be accessed by subclasses).
  - `__private`: Name mangled, avoid access from subclass.
  - Everything is technically public but can be accessed by convention.

## Method Overriding (Polymorphism)

- **Definition**: Subclass provides its own implementation of a method already defined in the superclass.
- **Rules**:
  - Same method name and parameters.
  - Return type must be compatible.
  - Access modifier cannot be more restrictive than in superclass.
  - Use `@Override` annotation in Java for safety.

### Java Example:

```java
class Animal {
    void sound() {
        System.out.println("Generic animal sound");
    }
}
class Dog extends Animal {
    @Override
    void sound() {
        System.out.println("Dog barks");
    }
}

```

### C++ Example:

```cpp
class Animal {
public:
    virtual void sound() {
        cout << "Generic animal sound";
    }
};

class Dog : public Animal {
public:
    void sound() override {
        cout << "Dog barks";
    }
};

```

### Python Example:

```python
class Animal:
    def sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

```

---

## `super` Keyword

### Purpose:

- Call the **parent class's method or constructor**.
- Useful when overriding and you still want to use the base implementation.

### Java:

```java
class Animal {
    void sound() {
        System.out.println("Animal sound");
    }
}

class Dog extends Animal {
    void sound() {
        super.sound(); // Call parent method
        System.out.println("Dog barks");
    }
}

```

### C++:

```cpp
class Animal {
public:
    void sound() {
        cout << "Animal sound";
    }
};

class Dog : public Animal {
public:
    void sound() {
        Animal::sound(); // Call base class method
        cout << "Dog barks";
    }
};

```

### Python:

```python
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")

```

---

## Quick Interview Checklist

| Concept               | Key Point                                                                               |
| --------------------- | --------------------------------------------------------------------------------------- |
| **Inheritance**       | Reuse code from base class. Java uses `extends`, C++ uses `: public`, Python uses `()`  |
| **Overriding**        | Same method name, signature. Subclass redefines parent method.                          |
| **Access Modifiers**  | Control visibility. Java: private/protected/public; C++: similar; Python: by convention |
| **super keyword**     | Access parent class method/constructor. Used when overriding.                           |
| **Constructor Chain** | In Java & C++, parent constructor called first. Python uses `super().__init__()`        |

### What is Polymorphism?

**Polymorphism** (from Greek: "many forms") allows one interface (method or object) to behave differently in different scenarios. It's a fundamental principle of Object-Oriented Programming (OOP).

## **Types of Polymorphism**

| Type                      | Also Called     | Resolved At  | Achieved By        |
| ------------------------- | --------------- | ------------ | ------------------ |
| Compile-time Polymorphism | Static Binding  | Compile Time | Method Overloading |
| Run-time Polymorphism     | Dynamic Binding | Runtime      | Method Overriding  |

## **Compile-time vs Runtime Polymorphism**

| Feature                     | Compile-time Polymorphism             | Runtime Polymorphism            |
| --------------------------- | ------------------------------------- | ------------------------------- |
| Achieved By                 | Method Overloading                    | Method Overriding               |
| Binding Time                | Compile Time                          | Runtime                         |
| Inheritance Required?       | ❌ No                                 | ✅ Yes                          |
| Return Type Differentiation | ❌ Not Allowed                        | ✅ Must match or be covariant   |
| Overload vs Override        | Overload: same name, different params | Override: same name + signature |

### **. Compile-Time Polymorphism (Static Polymorphism)**

**Definition:** Method call is resolved at compile time based on method signature.

### ✅ Achieved via:

- **Method Overloading** (same method name with different parameter list)
- **Operator Overloading** (C++ only)

### 🔸 Key Points:

- Faster execution (early binding).
- Improves readability.
- Return type **cannot** be the only difference.
- Supported in: ✅ C++, ✅ Java, ⚠️ Python (limited).

### 🔸 Example:

**Java**

```java
java
CopyEdit
class Math {
    int add(int a, int b) { return a + b; }
    double add(double a, double b) { return a + b; }
}

```

**C++**

```cpp
cpp
CopyEdit
class Math {
public:
    int add(int a, int b) { return a + b; }
    double add(double a, double b) { return a + b; }
};

```

**Python** *(Limited - uses default args or `*args`)\*

```python
python
CopyEdit
class Math:
    def add(self, a, b=0):  # No true overloading
        return a + b

```

---

### **Run-Time Polymorphism (Dynamic Polymorphism)**

**Definition:** Method call is resolved at **runtime** using **object type**, not reference type.

### Achieved via:

- **Method Overriding** (Subclasses provide specific implementation)

### 🔸 Key Points:

- Slower execution (late binding).
- Dynamic dispatch occurs at runtime.
- Based on object’s actual class, not reference class.
- Supported in: ✅ Java, ✅ C++, ✅ Python

### 🔸 Example:

**Java**

```java
java
CopyEdit
class Animal {
    void speak() { System.out.println("Animal sound"); }
}
class Dog extends Animal {
    void speak() { System.out.println("Dog barks"); }
}
Animal obj = new Dog();  // Output: Dog barks

```

**C++**

```cpp
cpp
CopyEdit
class Animal {
public:
    virtual void speak() { cout << "Animal sound"; }
};
class Dog : public Animal {
public:
    void speak() override { cout << "Dog barks"; }
};
Animal* a = new Dog(); // Output: Dog barks

```

**Python**

```python
python
CopyEdit
class Animal:
    def speak(self): print("Animal sound")
class Dog(Animal):
    def speak(self): print("Dog barks")
a = Dog()  # Output: Dog barks

```

## Can Return Type Differentiate Overloading?

**No** — Return type alone cannot differentiate method overloads.

```java
java
CopyEdit
// Invalid Overloading
int add(int a, int b) {}
double add(int a, int b) {} // Compile error!

```

---

## Can You Override a Static Method?

🚫 **No** — Static methods are bound at **compile-time**.

### What Happens Instead?

- If a static method is **re-declared** in subclass, it **hides** the parent’s static method — this is **method hiding**, **not overriding**.

```java
java
CopyEdit
class A {
    static void show() { System.out.println("Parent"); }
}
class B extends A {
    static void show() { System.out.println("Child"); }
}
A obj = new B();
obj.show(); // Output: Parent (not Child)

```

---

## How to Trigger a Static Method from a Child Class?

Use:

- `ChildClass.methodName();` — ✅ Works.
- Using object reference is allowed but not recommended.

```java
java
CopyEdit
class A {
    static void display() { System.out.println("Parent"); }
}
class B extends A {
    static void display() { System.out.println("Child"); }
}
B.display();  // Output: Child

```

---

## Key Concepts for Interviews

### Access Modifiers

| Modifier  | Same Class | Same Package | Subclass      | Outside |
| --------- | ---------- | ------------ | ------------- | ------- |
| private   | ✅         | ❌           | ❌            | ❌      |
| default   | ✅         | ✅           | ✅ (same pkg) | ❌      |
| protected | ✅         | ✅           | ✅            | ❌      |
| public    | ✅         | ✅           | ✅            | ✅      |

### Method Overriding Rules

- Same method name and parameters.
- Subclass method must not reduce visibility.
- Final methods cannot be overridden.
- Constructors can't be overridden.

### `super` Keyword

Used to:

1. Access parent class method.
2. Access parent constructor.

```java
java
CopyEdit
class Parent {
    void show() { System.out.println("Parent"); }
}
class Child extends Parent {
    void show() {
        super.show();  // Access parent method
        System.out.println("Child");
    }
}

```

## **Java Compilation to Execution Process**

### 🔄 Steps:

1. **Write** Java source code → `.java`
2. **Compile** using `javac` → `.class` file (bytecode)
3. **JVM executes** `.class` file via:
   - Classloader (loads class files)
   - Bytecode Verifier (security check)
   - **Interpreter** (line-by-line execution)
   - **JIT Compiler** (improves performance by converting bytecode to native code at runtime)

---

## **Java Virtual Machine (JVM) Components**

| Component             | Role                                               |
| --------------------- | -------------------------------------------------- |
| **Classloader**       | Loads `.class` files into memory                   |
| **Bytecode Verifier** | Checks for illegal code (e.g., stack overflows)    |
| **Interpreter**       | Executes bytecode line-by-line                     |
| **JIT Compiler**      | Converts bytecode into native code for performance |
| **Garbage Collector** | Frees memory used by unreachable objects           |

---

## **Bytecode and Platform Independence**

- **.class file** → Contains **bytecode**
- Bytecode is **not machine code**.
- It is executed by the **JVM**, which varies per OS.
- This makes Java **platform-independent**.

---

## Quick Facts for Interviews

| Concept                   | Key Point                                   |
| ------------------------- | ------------------------------------------- |
| Polymorphism              | Many forms (overloading/overriding)         |
| Overloading Return Type   | ❌ Cannot differ only by return type        |
| Method Overriding         | ✅ Requires inheritance, same signature     |
| Static Methods            | ❌ Cannot be overridden, only hidden        |
| Compile-Time Polymorphism | ✅ Method overloading                       |
| Runtime Polymorphism      | ✅ Method overriding, dynamic binding       |
| javac                     | Compiles `.java` → `.class` (bytecode)      |
| JVM                       | Runs bytecode using interpreter + JIT       |
| .class                    | Output of compiler, contains bytecode       |
| JIT                       | Converts bytecode to native code at runtime |
| Bytecode                  | Platform-independent; executed by JVM       |
| Classloader               | Loads classes into memory                   |
