### Simplification
- Tiles have open doors in each direction
- Events cannot move players
- Game ends when haunt begins
- no dropping or trading cards
Hard code special tiles/events?

### Process

1. get current board state
2. send board state to agent
3. agent sends its next legal desired action
4. resolve that action
5. flip new tile and place it, update board state
6. move agent and resolve tile, update board state
7. if no card drawn, repeat 1-6 until speed reaches 0
8. resolve drawn cards
9. resolve end-of-turn actions
10. move to next player and repeat 1-9 until haunt is rolled
11. calculate haunt roller and calculate final metrics


### Metrics
- Tiles players explored
- Tiles players traveled
- Stats gained
- Items drawn
- Haunt revealer
- Traitor