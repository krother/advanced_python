# How to structure classes, modules and packages?

## How to structure a bigger program?

### OOP
* Design Patterns
* facade
* encapsulation of your interface: web gui cli
* refactoring

### Advantages of Object-oriented Programming

-   Encapsulation: data and code stick together
-   Code reuse: inherit and dont write all anew
-   Maintenance: errors are easier to find/less frequent
-   Structure: additional level of grouping things
-   consistency: People are used to think in objects (programmers too)
-   Polymorphism: similar objects do different things
-   Objects are good dimension for Unit testing
-   Disadvantages:

    -   Code is a little longer (for doing small tasks)
    -   Code is a little slower (when there are many instances)

### What Exceptions to catch

-   File operations
-   web operations
-   big function calls
-   database operations
-   NEVER CATCH everything


### Web
* Flask, Django
*

#### quality
A program that looks good from the outside (e.g. a shiny GUI or web interface) and has produced scientific results may seem flawless from a supervisors perspective. It may still be entirely rotten from the inside.

#### bugs piling up in legacy code
What to do with all bugs? I mean: that there was a see of bugs and small features to implement all around and it felt like runing in mad circles. One thing you touch causes three next problems 1 week of work for something that was planned for one day, and the pile of 'easy fixes' is pilling ...


#### nested loops

- What is the depth of the most nested loop / if statement?


