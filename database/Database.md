## The Database

The Database will serve as the MDP for the Drama Manager. It will help inform decisions and ensure the DM can properly guide players toward optimal goals.

### Structure
The database will be a graph database, with board states as members of the graphs, and agent/DM actions as transitions between states. Each node will have several additional attributes, such as the expected untility of that path, the maximum utility of the path, and tracked metrics for player satisfaction.

### Process

As players take actions, they are added into the tree, branching off from existing nodes into new directions. Eventually this tree/graph structure will contain thousands of possible paths that players can take, each leading toward optimal or suboptimal results for their style of play. The DM can navigate these paths and find key places the utility of that path was determined, and take action to ensure that utility is achieved. 