# Python Mastery: The Definitive Reference & Knowledge Base

Welcome to **MASTER**, the definitive, exhaustive, and structured knowledge base designed to bridge fundamentals, advanced Python internals, system design patterns, and engineering best practices.

This repository merges, restructures, and massively expands upon foundational curriculum with comprehensive notes, real-world executable code demonstrations, and core technical interview questions.

---

## Table of Contents & Study Tracker

| # | Topic | Description | Status | Link |
|---|-------|-------------|:------:|------|
| 01 | **Basics** | Variables, Data Types, Operators, Type Casting, I/O, Conditionals, Loops, Strings, Lists, Tuples, Sets, Dictionaries, Comprehensions | `Not Started` | [01_Basics](./01_Basics/) |
| 02 | **Functions** | Declarations, `*args`/`**kwargs`, LEGB Scope, Closures, Lambdas, Decorators, Recursion | `Not Started` | [02_Functions](./02_Functions/) |
| 03 | **Modules & Packages** | Imports, `__init__.py`, Custom Packages, `pip`, Standard Library Deep Dive (`os`, `sys`, `collections`, `itertools`, etc.) | `Not Started` | [03_Modules_and_Packages](./03_Modules_and_Packages/) |
| 04 | **OOP** | Classes & Objects, Methods (`self`, `@classmethod`, `@staticmethod`), Inheritance, Polymorphism, Abstraction, Dunder Methods, Composition | `Not Started` | [04_OOP](./04_OOP/) |
| 05 | **Exception Handling** | `try`/`except`/`else`/`finally`, Custom Exceptions, Chaining, Stack Traces, Clean Error Architecture | `Not Started` | [05_Exception_Handling](./05_Exception_Handling/) |
| 06 | **File Handling** | Text & Binary Streams, `with` Statement Internals, CSV, JSON, `pathlib` vs `os.path`, Large File Streaming | `Not Started` | [06_File_Handling](./06_File_Handling/) |
| 07 | **DSA Fundamentals** | Arrays, Strings, Linear/Binary Search, Bubble/Merge/Quick Sort, Two-Pointer, Sliding Window | `Not Started` | [07_DSA_Fundamentals](./07_DSA_Fundamentals/) |
| 08 | **Time Complexity & Big-O** | Asymptotic Analysis, $O(1)$ to $O(2^n)$, Space Complexity, Amortized Analysis, Profiling Real Functions | `Not Started` | [08_Time_Complexity_and_Big_O](./08_Time_Complexity_and_Big_O/) |
| 09 | **Python Memory Management** | Reference Counting, Cyclic GC, `gc` module, `sys.getrefcount`, Object Identity (`id()`, `is` vs `==`), Shallow vs Deep Copy | `Not Started` | [09_Python_Memory_Management](./09_Python_Memory_Management/) |
| 10 | **Context Managers** | `with` Statement Mechanics, `__enter__` & `__exit__`, `@contextmanager`, Resource Safety, Timing, Error Suppression | `Not Started` | [10_Context_Managers](./10_Context_Managers/) |
| 11 | **Iterators & Generators** | Iterator Protocol (`__iter__`/`__next__`), `yield` & Generator Functions, Generator Expressions, Pipelines, `itertools` Deep Dive | `Not Started` | [11_Iterators_and_Generators](./11_Iterators_and_Generators/) |
| 12 | **Testing** | `unittest`, `pytest`, Fixtures, Parameterized Tests, Assertions, Mocking with `unittest.mock`, TDD Workflows | `Not Started` | [12_Testing](./12_Testing/) |
| 13 | **Regular Expressions** | `re` Engine, Metacharacters, Greedy vs Lazy Quantifiers, Capturing Groups, Lookahead/Lookbehind, Real-world Validation | `Not Started` | [13_Regular_Expressions](./13_Regular_Expressions/) |
| 14 | **Type Hints & Typing** | Static Typing, PEP 484, `Optional`, `Union`, Generics (`TypeVar`), `Protocol`, `TypedDict`, Runtime Type Verification | `Not Started` | [14_Type_Hints](./14_Type_Hints/) |
| 15 | **Virtual Environments & Packaging** | `venv`, Dependency Management, `requirements.txt`, Modern Packaging with `pyproject.toml`, Wheels, `pip` Architecture | `Not Started` | [15_Virtual_Environments_and_Packaging](./15_Virtual_Environments_and_Packaging/) |
| 16 | **Data Structures from Scratch** | Pure Python Implementations: Singly/Doubly Linked List, Stack, Queue, Hash Map, Binary Search Tree, Graph | `Not Started` | [16_Data_Structures_from_Scratch](./16_Data_Structures_from_Scratch/) |
| 17 | **Concurrency** | Threads vs Processes vs Asyncio, Global Interpreter Lock (GIL), ThreadPoolExecutor, ProcessPoolExecutor, Event Loop | `Not Started` | [17_Concurrency](./17_Concurrency/) |
| 18 | **Databases with Python** | DB-API 2.0, `sqlite3`, Connection Pools, Parameterized Queries, Transaction Management (ACID), Intro to SQLAlchemy ORM | `Not Started` | [18_Databases_with_Python](./18_Databases_with_Python/) |
| 19 | **Git & GitHub for Real Projects** | Git Plumbing vs Porcelain, Branching Strategies, Interactive Rebase, Conflict Resolution, Semantic Commits, PRs, Open Source | `Not Started` | [19_Git_and_GitHub](./19_Git_and_GitHub/) |
| 20 | **Intro to Flask** | WSGI Architecture, Routing, Request/Response Lifecycle, Jinja2 Templates, DB Integration, Blueprints & Factory Pattern | `Not Started` | [20_Intro_to_Flask](./20_Intro_to_Flask/) |

---

## Directory Architecture

Every topic folder follows an identical, rigorous three-part structure:

```text
MASTER/
├── XX_Topic_Name/
│   ├── notes.md                 # In-depth structured bullet-point theoretical notes
│   ├── examples/                # 5 runnable Python files demonstrating 5 distinct angles
│   │   ├── 01_basic_usage.py
│   │   ├── 02_edge_cases.py
│   │   ├── 03_real_world_use_case.py
│   │   ├── 04_common_mistakes_and_fixes.py
│   │   └── 05_advanced_idiomatic.py
│   └── interview_questions.md   # 5-8 high-yield interview questions with model answers
```

---

## How to Use This Knowledge Base

1. **Active Revision**: Check off each subtopic in [`progress_tracker.md`](./progress_tracker.md) as you master it.
2. **Read Notes**: Review `notes.md` to understand foundational theory, under-the-hood CPython mechanics, and pitfalls.
3. **Execute & Experiment**: Run every script inside `examples/`. Modify parameters and observe behavior.
4. **Mock Interview**: Attempt answering each prompt in `interview_questions.md` before reading the model answers.
