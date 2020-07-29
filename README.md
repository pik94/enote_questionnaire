## Question 1
*What is a difference between a list and a set?*

**The list** is a special structure in Python that can store any other elements 
and supports indexing like C array

The Python's **set** is a special data structure similar to mathematical sets.

Differences between the list and the set:
1. The list supports indexing, while the set not, i.e. complexity of extracting
a cell of the list is *O(1)* (if we know its index), an element of the set 
is *O(n)* where n is a number of elements of the set.
2. The list can store any elements, whereas the set can include only hashable ones. 
For example, we can put the list into the list but not the set into the set. 
However, it's possible to store a frozen set in the set.
3. The set uses the hash table so elements are stored in random way.


## Question 2
*What ways of achieving concurrency do you know? What are the limitations 
of those ways?*

In Python we can use three ways to achieve concurrency:
1. Multi-processing
2. Multi-threading
3. Asynchrony

#### Multi-processing
In this case we create system process that is one of processes of OS.
Processes are completely independent, i.e. they have their own CPU resources, 
memory etc.

Advantages:
1. Concurrency in case of multi-cores systems.
2. OS cares about management of resources.
3. Applicable for both CPU and IO-bound tasks.

Disadvantages:
1. Require extra resources.
2. It's challenging when communication between processes.

#### Multi-threading
Use threads for achieving of concurrency.

Advantages:
1. Applicable for IO-bound tasks, for example, requests to extra sources.
2. Require less resources than processes.
3. Different threads can share memory.

Disadvantages:
1. Python threads are not real ones because of GIL. At one time it's executed 
only one thread.
2. Not applicable for CPU-bound tasks.
3. It's challenging to manage share memory. For example, deadlocks.
4. A python interpreter switches threads (by default, each 5 ms) which is 
not efficient.


#### Asynchrony
Another way in achieving of concurrency. In this case we use only one thread 
switching a context of execution.

Advantages:
1. Applicable for IO-bound tasks, for example, requests to extra sources.
2. Lighter than processes.
3. We switch the context of execution when we need, not relying on 
the interpreter as in case of threads.
4. Use only one thread quite efficiently.

Disadvantages:
1. Not applicable for CPU-bound tasks.
2. It's challenging to write async code.


## Question 3
*What is the worst case time complexity of a quick sort?*

The worst case of a quick sort is when an array is sorted vice versa than we need. 
In this case the complexity is *O(n^2)* where n is a number of array's elements.


## Question 4
*What is an eigenvalue and an eigenvector?*

Let *V* is a vector space under a field *K*, *A*: *V* -> *V* is a linear operator.

A number **a** from the field *K* is an eigenvalue of the operator A if there is 
a vector **v** from *V* not equaled **0** called a eigenvector and there is 
an equality: *A*(**v**) = **av**

## Question 5
*For a given linked list containing the first 100 numbers of the sequence: 0, 1,
1, 2, 3, 5, 8, 13, ..., 218922995834555169026, provide a solution that returns 
a linked list in the following order:*
*218922995834555169026, ..., 13, 8, 5, 3, 2, 1, 1, 0. Please do not rely on 
standard packages for queues.*

Please, find a code in this repository in `task_5.py` script. I just realised 
a linked list with a basic methods that you can find in source code. To run it,
just type next in the terminal:
1. Create a virtual environment and activate it:
    ```shell script
    python3.7 -m venv venv && source ./venv/bin/activate
    ```

2. Run a script:
    ```shell script
    python task_5.py
    ```
   If you want to change a number of Fibonacci, add and argument `-n <number>`.
 