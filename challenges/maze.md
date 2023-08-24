
# Graph Traversal

**🎯 Find your way out of the maze.**

    maze = """
    ############
    #     # ##S#
    ### #      #
    ### ###### #
    ###   # ## #
    # ## ## ## #
    #    #     #
    #X##########""".strip().split('\n')

    x, y = (10, 1)
    target = (1, 7)

Write a function that will walk the maze (the graph) until the exit (`X`) is reached.

## Hints

You can proceed according to the **graph traversal algorithm**:

1. create a stack of the nodes to visit
2. create a stack of already visited nodes
3. take the next node from the stack
4. check whether the node is the exit, if yes, finish
5. if the node is a wall, continue to 3.
6. add the neighbours of the node to the nodes to visit

Try out what changes when you replace the stack by a queue.

*Translated with [www.DeepL.com](www.DeepL.com/Translator)*
