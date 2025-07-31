Java, a compiled language, offers platform independence and thread safety.

- **The Java Virtual Machine (JVM)**
- The JVM is a program that converts byte code to machine code**. Its key functions include:**
- **Loading** Java bytecode (.class files)
- **Verifying** the bytecode for safety
- **Executing** the bytecode using either interpretation or Just-In-Time (JIT) compilation
- **Managing memory**, including garbage collection
- **Providing security and isolation** for running programs

## **What is a Virtual Machine?**

A **Virtual Machine (VM)** is a software-based emulation of a physical computer. It simulates hardware to run operating systems and applications as if they were running on a real machine.

**Key Features of a Virtual Machine:**

- **Hardware Abstraction**: The VM acts like a real computer with CPU, memory, storage, etc.
- **Isolation**: Each VM is separated from the host system and other VMs.
- **Portability**: VMs can be moved and run on different hardware.
- **Use Cases**: Running multiple OS’s, server virtualization, sandboxing, and software testing.

**Examples:**

- **JVM**: A **language-level virtual machine** (specific to Java).
- **VirtualBox, VMware, and Hyper-V: System-level virtual machines**.

### **Java Virtual Machine (JVM) Components – Explained in Detail**

**1. Class Loader Subsystem**

Responsible for loading .class files into memory.

📌 **Phases:**

- **Loading**
  - **Bootstrap ClassLoader**: Loads core Java classes (java.lang._, java.util._) from rt.jar.
  - **Extension ClassLoader**: Loads classes from the ext directory.
  - **Application ClassLoader**: Loads classes from the classpath (.class files of your application).
- **Linking**
  - **Verify**: Checks bytecode validity.
  - **Prepare**: Allocates memory for static variables.
  - **Resolve**: Replaces symbolic references with direct memory references.
- **Initialization**
  - Executes static initializers and blocks.

**2. Runtime Data Areas**

This is where JVM stores all data during program execution:

**a. Method Area**

- Stores class structures like metadata, method code, static variables.
- Shared across all threads.

**b. Heap**

- Stores objects and instance variables.
- Managed by the **Garbage Collector**.
- Shared across all threads.

**c. Java Stack**

- One stack per thread.
- Contains frames for method invocations.
- Each frame has:
  - Local variables
  - Operand stack
  - Return address

**d. Program Counter (PC) Register**

- Each thread has its own PC register.
- Holds the address of the current executing instruction.
- Crucial for **multithreading**.

**e. Native Method Stack**

- Stores information about native (non-Java) method invocations.
- Works with **JNI (Java Native Interface)**.

**3.  Execution Engine**

This executes bytecode that has been loaded into memory.

**Components:**

- **Interpreter**:
  - Reads and executes bytecode instructions line-by-line.
  - Slower due to repeated parsing.
- **JIT (Just-In-Time) Compiler**:
  - Converts frequently executed bytecode into native machine code at runtime.
  - Improves performance significantly.
  - Works **after Interpreter**, on "hot spots".
- **Garbage Collector**:
  - Frees memory by removing unreachable objects.
  - Works in the **heap memory**.

**4.  Native Method Interface (JNI)**

- Allows Java to call native applications (written in C/C++).
- Enables platform-specific features not provided by Java.
- Communicates with the **Native Method Stack** and **Native Method Library**.

**How Everything Is Linked**

1. **Class is loaded** via the Class Loader Subsystem.
2. **Metadata and static variables** go into the **Method Area**.
3. **Objects are created** in the **Heap**.
4. Each **Thread** gets:
   - A **Java Stack** for method calls.
   - A **PC Register** to track current instruction.
   - A **Native Stack** for native method calls.
5. The **Execution Engine**:
   - Starts with the **Interpreter**.
   - Later, **JIT compiler** kicks in to optimize.
   - **Garbage Collector** manages the heap.
6. For native method calls, **JNI** bridges to **native libraries**.

## **Java Basics**

In Java everything is classes and Objects

A running program is called a process

Classes are the template from which object is created. All the objects are stored in the Heap.

Every thread which is a worker. Where the code is running, has its own stack which keeps getting emptied from time to time

1 byte = 8 bits

The maximum value for a 32-bit signed integer is  (2^31 )−1, which equals **2,147,483,647**.

```java
import java.util.Scanner;
public class InputExample {
	public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);
	System.out.print("Enter your name: ");
	String name = scanner.nextLine();
	System.out.print("Enter your age: ");
	int age = scanner.nextInt();
	System.out.print("Enter your GPA: ");
	double gpa = scanner.nextDouble();
	System.out.print("Enter your grade: ");
	char grade = scanner.next().charAt(0);
	System.out.println("\n--- User Info ---");
	System.out.println("Name: " + name);
	System.out.println("Age: " + age);
	System.out.println("GPA: " + gpa);
	System.out.println("Grade: " + grade);
	scanner.close(); // Optional but good practice
	}
	}
```

Always **close the scanner** when done (scanner.close()).

If you mix nextLine() with nextInt() or nextDouble(), be careful of leftover newline characters. Let me know if you want help handling that edge case!

For big numbers we have long

We also have wrappers in java like Integer,String,List etc

Optinal is used to handle nullptr

```java
Optional<Integer> optional = Optional.ofNullable(marks.get("rahul"));
if(optional.isPresent()){
	System.out.println("Marks of rahul: " + optional.get());
	}
else {
	System.out.println("Rahul not found in the map");
	}
```

# **Java Collection Framework**

- Java Collection Framework is a set of classes and interfaces that implements commonly reusable data structure. It is similar to the Standard Template Library (STL) in C++
- In Java, collections can store custom objects, allowing you to define your own classes and use them within collections such as List, Set, and Map. Let’s take a simple class Person as an

example:

```java
class Person {
	String name;
	int age;
	Person(String name, int age) {
		this.name = name;
		this.age = age;
	}
	@Override
	public String toString() {
		return name + “ (“ + age + “)”;
		}
	}
```

- Now, you can store instances of this Person class in a collection like an ArrayList

`List<Person> people = new ArrayList<>();`

`people.add(new Person("John", 30));`

`people.add(new Person("Alice", 25));`

`System.out.println(people);`

# **Collections**

A List is an ordered collection that allows duplicate elements. It provides positional access and is commonly used in scenarios where order matters.

## List

### **i. ArrayList**

- An ArrayList is a resizable array implementation of the List interface. It offers fast random access but slower insertions and deletions as elements need to be shifted

`List<String> arrayList = new ArrayList<>();`

`arrayList.add("Apple");`

`arrayList.add("Banana");`

`System.out.println(arrayList);`

### **ii. LinkedList**

- LinkedList is a doubly linked list implementation of the List interface. It provides fast insertions and deletions but slower random access compared to ArrayList.

`List<String> linkedList = new LinkedList<>();`

`linkedList.add("Cat");`

`linkedList.add("Dog");`

`System.out.println(linkedList); // Output: [Cat, Dog]`

### **iii. Stack**

- Stack is a subclass of Vector that implements a last-in, first-out (LIFO) stack of elements. It provides typical stack operations like push() and pop().

`Stack<Integer> stack = new Stack<>();`

`stack.push(1);`

`stack.push(2);`

`System.out.println(stack.pop()); // Output: 2`

### **iv. Vector**

- Vector is similar to ArrayList but is synchronized, meaning it is thread-safe for multi-threaded environments.

`Vector<String> vector = new Vector<>();`

`vector.add("Red");`

`vector.add("Blue");`

`System.out.println(vector); // Output: [Red, Blue]`

## **Set**

A Set is a collection that does not allow duplicate elements. It is useful when you need to store unique elements.

### **i. HashSet**

- HashSet is an implementation of the Set interface that uses a hash table for storage. It provides constant time performance for basic operations like add and remove.

`Set<String> hashSet = new HashSet<>();`

`hashSet.add("One");`

`hashSet.add("Two");`

`System.out.println(hashSet); // Output: [One, Two]`

### **ii. TreeSet**

- TreeSet is an implementation of the Set interface that stores elements in a sorted order using a red-black tree. The elements are sorted based on their natural ordering or a custom comparator.

## **Queue**

A Queue is a collection that follows the first-in, first-out (FIFO) principle. It is commonly used in scenarios where elements are processed in the order they are added.

### **ArrayQueue**

- Java doesn’t have a direct ArrayQueue, but you can implement a queue using an ArrayList. Alternatively, you can use LinkedList as a queue.

```java
import java.util.ArrayList;

public class ArrayListQueue<T> {

    private ArrayList<T> list = new ArrayList<>();

    // Enqueue
    public void enqueue(T item) {
        list.add(item);
    }

    // Dequeue
    public T dequeue() {
        if (list.isEmpty()) {
            return null;
        }
        return list.remove(0); // O(n) because of shifting elements
    }

    // Peek
    public T peek() {
        if (list.isEmpty()) {
            return null;
        }
        return list.get(0);
    }

    // Check if the queue is empty
    public boolean isEmpty() {
        return list.isEmpty();
    }

    // Get the size of the queue
    public int size() {
        return list.size();
    }
}

```

### **LinkedList (as Queue)**

- LinkedList can be used as a queue since it implements both the List and Queue interfaces

`Queue<String> queue = new LinkedList<>();`

`queue.add("First");`

`queue.add("Second");`

`System.out.println(queue.poll()); // Output: First`

### **PriorityQueue**

- PriorityQueue is a queue that orders elements according to their natural ordering or a custom comparator. Elements with higher priority are processed first.

`PriorityQueue<Integer> priorityQueue = new PriorityQueue<>();`

`priorityQueue.add(10);`

`priorityQueue.add(5);`

`System.out.println(priorityQueue.poll()); // Output: 5`

## **Map**

A Map is a collection that maps keys to values. It does not allow duplicate keys, but multiple keys can map to the same value.

### **HashMap**

- HashMap is an implementation of the Map interface that uses a hash table for storage. It allows null keys and values.

`Map<String, Integer> hashMap = new HashMap<>();`

`hashMap.put("Apple", 10);`

`hashMap.put("Banana", 20);`

`System.out.println(hashMap); // Output: {Apple=10, Banana=20}`

### **TreeMap**

- TreeMap is a red-black tree-based implementation of the Map interface. It stores entries in sorted order based on keys.

`Map<String, Integer> treeMap = new TreeMap<>();`

`treeMap.put("Orange", 5);`

`treeMap.put("Mango", 15);`

`System.out.println(treeMap); // Output: {Mango=15, Orange=5}`

## **Iterator**

- An Iterator allows you to traverse through a collection. ListIterator is a special type of iterator for List collections.

### **List Iterator**

- ListIterator allows bidirectional traversal of a list, i.e., both forward and backward.

```java
List<String> list = new ArrayList<>();
list.add("One");
list.add("Two");
ListIterator<String> iterator = list.listIterator();
while (iterator.hasNext()) {
	System.out.println(iterator.next());
	}
```

## **Custom Comparator**

- A Comparator allows you to define custom sorting logic for collections. You can use it to sort objects based on specific attributes.

```java
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;

// Sorting a list of people by age
Collections.sort(people, new Comparator<Person>() {
    @Override
    public int compare(Person p1, Person p2) {
        return p1.age - p2.age;
    }
});

// Task class with priority and name
class Task {
    int priority;
    String name;

    Task(int priority, String name) {
        this.priority = priority;
        this.name = name; // Fixed: was `this,name = name;`
    }

    @Override
    public String toString() {
        return name + " (Priority: " + priority + ")";
    }
}

public class CustomPriorityQueue {

    public static void main(String[] args) {
        // Custom comparator: lower number = higher priority
        Comparator<Task> taskComparator = (t1, t2) -> Integer.compare(t1.priority, t2.priority);

        PriorityQueue<Task> taskQueue = new PriorityQueue<>(taskComparator);

        taskQueue.offer(new Task(3, "Do homework"));
        taskQueue.offer(new Task(1, "Fix urgent bug"));
        taskQueue.offer(new Task(2, "Email professor"));

        // Process tasks by priority
        while (!taskQueue.isEmpty()) {
            System.out.println(taskQueue.poll());
        }
    }
}

```
